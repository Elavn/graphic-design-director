#!/usr/bin/env python3
"""Mechanical image gate: dimensions + approximate large-red-area detection.
Requires Pillow; intentionally avoids claiming automatic design or brand fidelity.
"""
import argparse
import json
from pathlib import Path
from PIL import Image

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('image',type=Path)
parser.add_argument('--width',type=int,required=True)
parser.add_argument('--height',type=int,required=True)
parser.add_argument('--max-saturated-red-share',type=float,default=None,help='Max fraction of highly saturated red pixels; red photorealistic objects may require human review')
parser.add_argument('--json',type=Path,default=None,help='Write machine-readable report')
args=parser.parse_args()
if not (0<= (args.max_saturated_red_share if args.max_saturated_red_share is not None else 0) <= 1):
    parser.error('share must be between 0 and 1')
im=Image.open(args.image).convert('RGB')
w,h=im.size
# Sample <= ~200k points for speed and bounded memory.
step=max(1,int(((w*h)/200000)**.5))
pixels=[im.getpixel((x,y)) for y in range(0,h,step) for x in range(0,w,step)]
# A broad highly saturated red classifier, not a full brand token checker.
red=sum(r>=150 and r>g*1.45 and r>b*1.4 and g<150 for r,g,b in pixels)/max(1,len(pixels))
issues=[]
if (w,h)!=(args.width,args.height):issues.append(f'size {w}x{h} != {args.width}x{args.height}')
if args.max_saturated_red_share is not None and red>args.max_saturated_red_share:issues.append(f'red area share {red:.1%} > {args.max_saturated_red_share:.1%}')
report={'file':str(args.image),'actual_pixels':{'width':w,'height':h},'target_pixels':{'width':args.width,'height':args.height},'aspect_ratio':round(w/h,6),'saturated_red_share_estimate':round(red,6),'result':'FAIL' if issues else 'PASS','issues':issues,'limitations':'Does not prove palette role, logo, typography or layout fidelity; inspect visually.'}
print(json.dumps(report,indent=2))
if args.json:args.json.write_text(json.dumps(report,indent=2)+'\n')
raise SystemExit(bool(issues))
