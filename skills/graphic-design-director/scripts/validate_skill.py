#!/usr/bin/env python3
"""Validate skill metadata and local Markdown references; Python 3 stdlib-only."""
from pathlib import Path
import re
import sys

ROOT=Path(__file__).resolve().parent.parent
f=ROOT/'SKILL.md'
errors=[]
if not f.exists(): errors.append('Missing SKILL.md')
else:
    text=f.read_text(encoding='utf8')
    fm=re.match(r'\A---\s*\n(.*?)\n---\s*\n',text,re.S)
    if not fm: errors.append('Missing frontmatter')
    else:
        fields=dict(re.findall(r'^([\w-]+):\s*(.+)$',fm.group(1),re.M))
        if fields.get('name')!=ROOT.name: errors.append('name must match enclosing directory')
        if not fields.get('description'): errors.append('description must be non-empty')
        if len(fields.get('name',''))>64: errors.append('name exceeds 64 characters')
    for label,link in re.findall(r'\[([^]]+)\]\(([^)]+)\)',text):
        if link.startswith(('http:','https:','#','mailto:')):continue
        if not (ROOT/link.split('#')[0]).exists():errors.append('Broken link: '+label+' -> '+link)
for name in ['README.md','VERSION','CHANGELOG.md','references/visual-reference-studies.md',
             'references/concept-engine.md','references/model-and-cli-portability.md',
             'references/critique-learning-protocol.md','evals/reference-image-cases.md',
             'prompts/portable-activation.md']:
    if not (ROOT/name).is_file():errors.append('Missing '+name)
print('Skill',ROOT.name,'v'+(ROOT/'VERSION').read_text().strip(),'-',len(list(ROOT.rglob('*'))),'entries')
for e in errors:print('ERROR:',e)
print('PASS' if not errors else 'FAIL')
sys.exit(bool(errors))

