"""Contract and preflight regression tests: python -m unittest discover -s tests -v"""
import json
from pathlib import Path
import importlib.util
import io
from contextlib import redirect_stdout, redirect_stderr
from types import SimpleNamespace
import tempfile
import unittest

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
CLI = ROOT / 'scripts' / 'pipeline.py'
_spec = importlib.util.spec_from_file_location('gdd_pipeline', CLI)
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)

def run(*args):
    out, err = io.StringIO(), io.StringIO()
    with redirect_stdout(out), redirect_stderr(err):
        result = _module.main(list(map(str,args)))
    return SimpleNamespace(returncode=result, stdout=out.getvalue(), stderr=err.getvalue())

def read(path):
    return json.loads(path.read_text(encoding='utf-8'))

def write(path, d):
    path.write_text(json.dumps(d, indent=2)+'\n', encoding='utf-8')

class PipelineTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.project = self.base / 'alpha'
        result = run('init', '--project', self.project, '--id', 'alpha', '--mode', 'CREATE', '--medium', 'social poster')
        self.assertEqual(result.returncode, 0, result.stderr)

    def ready(self):
        doc = read(self.project/'project.json')
        doc['brief']['summary'] = 'Announce a public creative event'
        doc['brief']['key_message'] = 'The event is opening'
        doc['output'].update({'format':'PNG','width_px':1080,'height_px':1350})
        write(self.project/'project.json', doc)

    def test_v031_reference_core_is_untouched(self):
        import hashlib
        baseline = read(ROOT / 'baselines' / 'v0.3.1-manifest.json')
        reference_files = {name: sha for name, sha in baseline['files_sha256'].items() if name.startswith('references/')}
        self.assertEqual(len(reference_files),23)
        for name, sha in reference_files.items():
            h=hashlib.sha256((ROOT/name).read_bytes()).hexdigest()
            self.assertEqual(h,sha,name)

    def test_approved_asset_subdirectory_symlink_escape_blocked(self):
        self.ready()
        outside=self.base/'outside'; outside.mkdir()
        approved=self.project/'approved-assets'
        approved.rmdir()
        try:
            approved.symlink_to(outside, target_is_directory=True)
        except (OSError, NotImplementedError):
            self.skipTest('OS does not allow creating symlinks')
        src=self.base/'source.svg';src.write_text('<svg/>')
        result=run('register-asset','--project',self.project,'--id','logo-a','--file',src,'--kind','logo')
        self.assertEqual(result.returncode,2)
        self.assertFalse((outside/'logo-a.svg').exists())

    def test_schemas_are_valid_draft_2020_12(self):
        for p in (ROOT/'schemas').glob('*.schema.json'):
            Draft202012Validator.check_schema(read(p))

    def test_preflight_qa_report_is_schema_valid(self):
        self.ready()
        self.assertEqual(run('preflight','--project',self.project).returncode,0)
        validator=_module.schema_validator('qa-report')
        validator.validate(read(self.project/'reports'/'preflight.json'))

    def test_init_validates_but_not_ready(self):
        self.assertEqual(run('validate','--project',self.project).returncode,0)
        preflight = run('preflight','--project',self.project)
        self.assertEqual(preflight.returncode,1)
        self.assertEqual(read(self.project/'reports'/'preflight.json')['status'],'BLOCKED')

    def test_ready_brief(self):
        self.ready()
        preflight=run('preflight','--project',self.project)
        self.assertEqual(preflight.returncode,0,preflight.stdout)
        self.assertEqual(read(self.project/'reports'/'preflight.json')['status'],'READY_FOR_CREATIVE')

    def test_reinit_refuses_overwrite(self):
        self.assertEqual(run('init','--project',self.project,'--id','alpha').returncode,2)
        self.assertTrue((self.project/'project.json').exists())

    def test_reference_required_for_adapt(self):
        self.ready()
        doc=read(self.project/'project.json')
        doc['mode']='ADAPT'
        write(self.project/'project.json',doc)
        self.assertEqual(run('preflight','--project',self.project).returncode,1)

    def test_register_lock_and_detect_tampering(self):
        self.ready()
        src=self.base/'source.svg'
        src.write_text('<svg/>',encoding='utf8')
        res=run('register-asset','--project',self.project,'--id','logo-a','--file',src,'--kind','logo','--approved')
        self.assertEqual(res.returncode,0,res.stderr)
        manifest=read(self.project/'assets.json')
        self.assertTrue(manifest['assets'][0]['approved'])
        self.assertEqual(len(manifest['assets'][0]['sha256']),64)
        self.assertEqual(run('preflight','--project',self.project).returncode,0)
        (self.project/'approved-assets'/'logo-a.svg').write_text('<svg>changed</svg>',encoding='utf8')
        self.assertEqual(run('preflight','--project',self.project).returncode,1)
        self.assertIn('asset.integrity',[c['id'] for c in read(self.project/'reports'/'preflight.json')['checks']])

    def test_cannot_register_duplicate_asset(self):
        src=self.base/'a.png'; src.write_bytes(b'not-a-real-png')
        a=['register-asset','--project',self.project,'--id','test-asset','--file',src,'--kind','photo']
        self.assertEqual(run(*a).returncode,0)
        self.assertEqual(run(*a).returncode,2)

    def test_path_traversal_blocked(self):
        self.ready()
        m=read(self.project/'assets.json')
        m['assets']=[{'id':'bad-asset','path':'../secret.png','sha256':'0'*64,'kind':'other','approved':False,'reuse':'style-only','source_name':'secret.png','notes':''}]
        write(self.project/'assets.json',m)
        self.assertEqual(run('preflight','--project',self.project).returncode,1)
        self.assertIn('asset.path',[c['id'] for c in read(self.project/'reports'/'preflight.json')['checks']])

    def test_duplicate_ids_block(self):
        self.ready()
        ledger=read(self.project/'constraints.json')
        c={'id':'one-constraint','level':'HARD','kind':'copy','statement':'Exact text','source':'user','verification':'AUTOMATIC','status':'ACTIVE'}
        ledger['constraints']=[c,c.copy()]
        write(self.project/'constraints.json',ledger)
        self.assertEqual(run('preflight','--project',self.project).returncode,1)

    def test_manual_check_holds_review_status(self):
        self.ready()
        ledger=read(self.project/'constraints.json')
        ledger['constraints'].append({'id':'geometry','level':'HARD','kind':'layout','statement':'Match illustration perspective','source':'user','verification':'MANUAL','status':'ACTIVE'})
        write(self.project/'constraints.json',ledger)
        self.assertEqual(run('preflight','--project',self.project).returncode,0)
        self.assertEqual(read(self.project/'reports'/'preflight.json')['status'],'REVIEW_REQUIRED')

    def test_other_project_isolation(self):
        self.ready()
        doc=read(self.project/'assets.json')
        doc['project_id']='other'
        write(self.project/'assets.json',doc)
        self.assertEqual(run('validate','--project',self.project).returncode,1)
        self.assertIn('project.isolation',[c['id'] for c in read_report(self.project,via_preflight=True)['checks']])

    def test_schema_failure(self):
        self.ready()
        doc=read(self.project/'project.json')
        doc['mode']='ANYTHING'
        write(self.project/'project.json',doc)
        res=run('validate','--project',self.project)
        self.assertEqual(res.returncode,1)
        self.assertIn('schema.project.json',res.stdout)

    def test_references_must_be_registered(self):
        self.ready()
        doc=read(self.project/'project.json')
        doc['reference_asset_ids']=['missing-reference']
        write(self.project/'project.json',doc)
        self.assertEqual(run('preflight','--project',self.project).returncode,1)

    def test_render_direction_must_be_known(self):
        self.ready()
        doc=read(self.project/'render-request.json')
        doc['direction_id']='missing-direction'
        write(self.project/'render-request.json',doc)
        self.assertEqual(run('preflight','--project',self.project).returncode,1)


def read_report(project,via_preflight=False):
    if via_preflight:
        run('preflight','--project',project)
    return read(project/'reports'/'preflight.json')

if __name__ == '__main__':
    unittest.main()
