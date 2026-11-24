from pathlib import Path
import hashlib,json,subprocess,sys,tempfile,unittest
from PIL import Image

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from review_gate import validate

class V071RegressionTests(unittest.TestCase):
    def test_three_revision_knowledge_files(self):
        for p in ['references/deep/concept-legibility.md','references/deep/photo-material-fidelity.md','references/deep/wordmark-construction.md']:
            self.assertTrue((ROOT/p).is_file());self.assertGreater(len((ROOT/p).read_text().split()),170)
    def test_skill_routes_to_new_knowledge(self):
        s=(ROOT/'SKILL.md').read_text()
        for p in ['references/deep/concept-legibility.md','references/deep/photo-material-fidelity.md','references/deep/wordmark-construction.md','evals/v071-targeted-regressions.md']:
            self.assertIn(p,s)
    def test_technical_pass_stops_before_creative_approval(self):
        with tempfile.TemporaryDirectory() as td:
            b=Path(td);Image.new('RGB',(120,140),'white').save(b/'render.png')
            r=validate({'output':'render.png','expected_dimensions':[120,140],'locked_assets':[]},b)
            self.assertEqual(r['status'],'TECHNICAL_PASS_REVIEW_REQUIRED')
            self.assertEqual(r['creative_approval'],'NOT_AUTOMATED')
    def test_wrong_resolution_fails(self):
        with tempfile.TemporaryDirectory() as td:
            b=Path(td);Image.new('RGB',(120,140),'white').save(b/'render.png')
            r=validate({'output':'render.png','expected_dimensions':[100,140],'locked_assets':[]},b)
            self.assertEqual(r['status'],'BLOCKED')
    def test_approved_asset_integrity(self):
        with tempfile.TemporaryDirectory() as td:
            b=Path(td);Image.new('RGB',(30,40),'white').save(b/'render.png')
            (b/'logo.svg').write_text('<svg/>')
            digest=hashlib.sha256((b/'logo.svg').read_bytes()).hexdigest()
            m={'output':'render.png','expected_dimensions':[30,40],'locked_assets':[{'path':'logo.svg','sha256':digest}]}
            self.assertEqual(validate(m,b)['status'],'TECHNICAL_PASS_REVIEW_REQUIRED')
            (b/'logo.svg').write_text('<svg>changed</svg>')
            self.assertEqual(validate(m,b)['status'],'BLOCKED')
    def test_path_escape_fails(self):
        with tempfile.TemporaryDirectory() as td:
            b=Path(td)
            r=validate({'output':'../other-file.png','expected_dimensions':[100,100]},b)
            self.assertEqual(r['status'],'BLOCKED')
    def test_no_external_provider_dependencies(self):
        self.assertFalse((ROOT/'scripts/adapters').exists())
        self.assertFalse((ROOT/'scripts/orchestrator.py').exists())
        self.assertFalse((ROOT/'PIPELINE-PHASE3.md').exists())
    def test_no_unwarranted_automatic_numeric_scores(self):
        s=(ROOT/'evals/v071-targeted-regressions.md').read_text()
        self.assertIn('Never automatically award an originality score',s)

if __name__=='__main__': unittest.main()
