#!/usr/bin/env python3
"""Check representative flat-color regions in an output image using Pillow.

Example:
  python scripts/check_palette_regions.py design.png \
      --region 390,690,430,719=#0E4B38 \
      --region 475,690,526,719=#C4EE3A

Only sample intentionally flat regions away from edges and text. Do not use
for photos, gradients, shadows, textured backgrounds or logo verification.
"""
import argparse
import json
import math
from pathlib import Path
from PIL import Image

def parse(s):
    try:
        coords,color=s.split('=',1)
        rect=tuple(int(v) for v in coords.split(','))
        if len(rect)!=4 or not (rect[0]<rect[2] and rect[1]<rect[3]): raise ValueError()
        if not (len(color)==7 and color.startswith('#')): raise ValueError()
        rgb=tuple(int(color[i:i+2],16) for i in (1,3,5))
        return rect,color.upper(),rgb
    except Exception:
        raise argparse.ArgumentTypeError('Use x0,y0,x1,y1=#RRGGBB')

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('image')
    p.add_argument('--region',action='append',required=True,type=parse)
    p.add_argument('--max-channel-error',type=int,default=2)
    args=p.parse_args()
    if not 0<=args.max_channel_error<=255: p.error('--max-channel-error must be 0-255')
    im=Image.open(args.image).convert('RGB')
    allpass=True; result=[]
    for rect,expect_hex,expect in args.region:
        if not (0<=rect[0]<rect[2]<=im.width and 0<=rect[1]<rect[3]<=im.height):
            p.error(f'region {rect} outside image dimensions {im.size}')
        cropped=im.crop(rect)
        region=list(cropped.get_flattened_data() if hasattr(cropped,"get_flattened_data") else cropped.getdata())
        # Median robust to a few isolated antialias edge pixels.
        median=tuple(sorted(px[i] for px in region)[len(region)//2] for i in range(3))
        err=max(abs(median[i]-expect[i]) for i in range(3))
        passed=err<=args.max_channel_error
        allpass &= passed
        result.append({'rect':rect,'expected':expect_hex,'observed_median':'#'+''.join(f'{x:02X}' for x in median),'max_channel_error':err,'status':'PASS' if passed else 'FAIL'})
    print(json.dumps({'image':str(args.image),'dimensions':im.size,'swatches':result,'result':'PASS' if allpass else 'FAIL'},indent=2))
    return 0 if allpass else 1

if __name__=='__main__':raise SystemExit(main())
