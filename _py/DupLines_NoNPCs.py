#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import json
import os
import sys

err = os.EX_OK

if len(sys.argv) < 2:
    sys.exit(os.EX_NOINPUT)

with open(sys.argv[1]) as f:
    oD = json.load(f)

oJ = dict()
for k, vl in oD.items():
    NoNPCs = True
    for v in vl:
        if "actor_name.csv::Npc_" in v:
            NoNPCs = False
    if NoNPCs:
        oJ[k] = vl

print(json.dumps(oJ, sort_keys=True))

sys.exit(err)
