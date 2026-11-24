#!/usr/bin/env python3
"""Install the portable skill for major Agent Skills CLIs; Python 3 standard library."""
import argparse
import datetime
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parent.parent
NAME = 'graphic-design-director'
TARGETS = {
    'claude': ('.claude/skills', '.claude/skills'),
    'codex': ('.agents/skills', '.agents/skills'),
    'gemini': ('.gemini/skills', '.gemini/skills'),
    'cursor': ('.cursor/skills', '.cursor/skills'),
    'opencode': ('.opencode/skills', '.config/opencode/skills'),
}

def main():
    p=argparse.ArgumentParser(description='Install Graphic Design Director into Agent Skills directories')
    p.add_argument('--target',choices=[*TARGETS,'all'],required=True)
    p.add_argument('--scope',choices=['project','user'],default='project')
    p.add_argument('--project',type=Path,default=Path.cwd())
    p.add_argument('--dry-run',action='store_true')
    p.add_argument('--force',action='store_true',help='Back up existing install before replacing')
    a=p.parse_args()
    assert (ROOT/'SKILL.md').exists(), 'SKILL.md missing'
    names=list(TARGETS) if a.target=='all' else [a.target]
    destinations=[]
    for name in names:
        proj,user=TARGETS[name]
        base=(a.project.expanduser().resolve()/proj) if a.scope=='project' else Path.home()/user
        dst=base/NAME
        if dst.resolve()==ROOT: p.error('Cannot install skill over itself')
        destinations.append((name,dst))
    if not a.dry_run and not a.force:
        existing=[str(d) for _,d in destinations if d.exists()]
        if existing: p.error('Already installed; use --force to back up and replace: '+', '.join(existing))
    for name,dst in destinations:
        print(f'{name}: {dst}')
        if a.dry_run: continue
        dst.parent.mkdir(parents=True,exist_ok=True)
        if dst.exists():
            stamp=datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
            backup=dst.with_name(dst.name+'.backup-'+stamp)
            if backup.exists(): p.error('Backup exists already: '+str(backup))
            dst.rename(backup)
            print('  backed up to: '+str(backup))
        shutil.copytree(ROOT,dst,ignore=shutil.ignore_patterns('.git','__pycache__','*.pyc','*.local.jsonl','*.private.*'))
        print('  installed; reload agent session when necessary')
    if a.target=='all': print('Warning: check for duplicate skill IDs, as some agents read other agents\' directories.')

if __name__=='__main__': main()
