#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import os
import random

n = int(sys.argv[1])
ppid = os.getpid()

for i in range(n):
    pid = os.fork()
    if pid != 0:
        print('Parent[{0}]: I ran children process with PID {1}'.format(ppid, pid))
        terminated_pid, exit_status = os.wait()
        exit_status = os.waitstatus_to_exitcode(exit_status)
        print('Parent[{0}]: Child process with PID {1} terminated. Exit status: {2}'.format(ppid, terminated_pid, exit_status))
        if exit_status != 0:
            pid = os.fork()
            if pid != 0:
                print('Parent[{0}]: I ran children process with PID {1}'.format(ppid, pid))
                terminated_pid, exit_status = os.wait()
                exit_status = os.waitstatus_to_exitcode(exit_status)
                print('Parent[{0}]: Child process with PID {1} terminated. Exit status: {2}'.format(ppid, terminated_pid, exit_status))
            else:
                os.execl('./child.py', './child.py', str(random.randint(5, 10)))
    else:
        os.execl('./child.py', './child.py', str(random.randint(5, 10)))
        
