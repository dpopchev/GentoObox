#!/usr/bin/env python

import datetime
import re
import sys

day = datetime.date.today().day

RE = re.compile(r'\b%d\b' % day)

for line in sys.stdin.readlines():
  print(line[:22] + RE.sub(r'${color red}%d$color' % day, line[22:42]) + line[42:])
