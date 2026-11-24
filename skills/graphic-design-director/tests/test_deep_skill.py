from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = {
    'references/deep/creative-strategy.md',
    'references/deep/art-direction-atlas.md',
    'references/deep/typographic-craft.md',
    'references/deep/composition-architecture.md',
    'references/deep/color-direction.md',
    'references/deep/identity-and-logos.md',
    'references/deep/imagery-and-materials.md',
    'references/deep/medium-playbooks.md',
    'references/deep/reference-intelligence.md',
    'references/deep/critique-and-revision.md',
    'references/deep/decision-examples.md',
    'evals/deep-regression-cases.md',
}

class DeepSkillTests(unittest.TestCase):
    def test_deep_modules_present(self):
        for name in REQUIRED:
            with self.subTest(name=name):
                self.assertTrue((ROOT/name).is_file())
                self.assertGreater(len((ROOT/name).read_text().split()), 250)

    def test_skill_routes_to_deep_modules(self):
        skill=(ROOT/'SKILL.md').read_text()
        for name in REQUIRED:
            if not name.startswith('evals/'):
                with self.subTest(name=name):
                    self.assertIn(name,skill)

    def test_local_only_no_provider_scripts(self):
        self.assertFalse((ROOT/'scripts/adapters').exists())
        self.assertFalse((ROOT/'scripts/orchestrator.py').exists())
        self.assertFalse((ROOT/'PIPELINE-PHASE3.md').exists())
        self.assertFalse((ROOT/'PIPELINE-PHASE2.md').exists())

    def test_links_in_markdown_resolve(self):
        for file in ROOT.rglob('*.md'):
            data=file.read_text()
            for link in re.findall(r'(?<!!)\[[^]]+\]\(([^)]+)\)', data):
                target=link.split('#', 1)[0]
                if not target or '://' in target or target.startswith('mailto:'):
                    continue
                with self.subTest(file=file,link=link):
                    self.assertTrue((file.parent / target).exists())

    def test_no_client_asset_bundled(self):
        names=[str(p.relative_to(ROOT)).lower() for p in ROOT.rglob('*') if p.is_file()]
        self.assertFalse(any('pickam' in p for p in names))

if __name__=='__main__':
    unittest.main()
