#!/usr/bin/env python3
"""Opt-in feedback record; writes ignored JSONL, does not edit skill or train a model."""
import argparse
import json
from datetime import datetime,timezone
from pathlib import Path
import secrets

ROOT=Path(__file__).resolve().parent.parent
CATEGORIES=['concept','typography','layout','realism','color','copy','culture','accessibility','production','other']

def main():
    p=argparse.ArgumentParser(description='Log private design critique')
    p.add_argument('--brief',default='')
    p.add_argument('--critique',required=True)
    p.add_argument('--category',choices=CATEGORIES,required=True)
    p.add_argument('--severity',choices=['blocker','major','minor','preference'],default='major')
    p.add_argument('--cause',default='')
    p.add_argument('--rule',default='')
    a=p.parse_args()
    record={'id':'obs-'+secrets.token_hex(4),'timestamp':datetime.now(timezone.utc).isoformat(),
            'brief_id':a.brief,'critique':a.critique,'category':a.category,'severity':a.severity,
            'suspected_cause':a.cause,'proposed_rule':a.rule,'approved':False,'status':'observed',
            'test_id':None,'skill_version':(ROOT/'VERSION').read_text().strip()}
    dst=ROOT/'feedback'/'observations.local.jsonl'
    dst.parent.mkdir(parents=True,exist_ok=True)
    with dst.open('a',encoding='utf8') as out: out.write(json.dumps(record,ensure_ascii=False)+'\n')
    print('Recorded '+record['id']+' in '+str(dst)+' (no model or instruction changes made)')

if __name__=='__main__': main()
