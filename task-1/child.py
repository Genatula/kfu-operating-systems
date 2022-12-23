#!/usr/bin/python3 
# -*- coding: utf-8 -*-

import sys
import os
import random
import time

s = int(sys.argv[1])
pid = os.getpid()
ppid = os.getppid()

print('Child[{0}]: I have been started. My PID is {1}. My PPID is {2}'.format(pid, pid, ppid))

time.sleep(s)

print('Child[{0}]: I am going to terminate now. My PID is {1}. My PPID is {2}'.format(pid, pid, ppid))

os._exit(1 if random.randint(1, 10) > 5 else 0)
