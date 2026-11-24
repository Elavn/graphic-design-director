#!/usr/bin/env python3
"""Graphic Design Director local evidence gate: NEVER a creative auto-approval."""
import argparse,hashlib,json,sys
from pathlib import Path
try:
    from PIL import Image
except ImportError:
    Image=None

def file_hash(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def validate(manifest,base):
    failures=[];checked=[]
    expected=manifest.get('expected_dimensions')
    if not isinstance(expected,list) or len(expected)!=2 or not all(isinstance(x,int) and x>0 for x in expected):
        failures.append('expected_dimensions must be [positive_int,positive_int]')
    output=manifest.get('output')
    if not isinstance(output,str) or not output:failures.append('output path required')
    else:
        p=(base/output).resolve()
        if not p.is_relative_to(base.resolve()): failures.append('output escapes project root')
        elif not p.is_file():failures.append('missing output')
        else:
            checked.append({'output_sha256':file_hash(p)})
            if Image is None:failures.append('Pillow unavailable: cannot verify raster size')
            else:
                try:
                    with Image.open(p) as image:
                        dims=list(image.size)
                    checked.append({'measured_dimensions':dims})
                    if isinstance(expected,list) and dims!=expected:failures.append('incorrect output dimensions')
                except Exception as exc:failures.append(f'unreadable raster file: {exc}')
    for a in manifest.get('locked_assets',[]):
        rel=a.get('path','');sha=a.get('sha256','')
        p=(base/rel).resolve()
        if not rel or not p.is_relative_to(base.resolve()) or not p.is_file():
            failures.append(f'missing or unsafe locked asset: {rel}')
        elif file_hash(p)!=sha:failures.append(f'locked asset modified: {rel}')
        else:checked.append({'locked_asset_sha256':sha,'path':rel})
    # IMPORTANT: semantic fidelity and actual creative quality cannot be established here.
    return {'hard_checks':'FAIL' if failures else 'PASS',
            'status':'BLOCKED' if failures else 'TECHNICAL_PASS_REVIEW_REQUIRED',
            'failures':failures,'verified':checked,
            'creative_approval':'NOT_AUTOMATED',
            'manual_review_required':['concept comprehension','typography and crop','photo medium and source-UI text','wordmark distinctiveness and rights']}

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--manifest',required=True)
    ap.add_argument('--report')
    ns=ap.parse_args();m=Path(ns.manifest).resolve();r=validate(json.loads(m.read_text()),m.parent)
    data=json.dumps(r,indent=2)
    if ns.report:Path(ns.report).write_text(data)
    print(data)
    return 2 if r['hard_checks']=='FAIL' else 0
if __name__=='__main__':sys.exit(main())
