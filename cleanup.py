#!/usr/bin/python
# Module:   cleanup.py
# Purpose:  remove test files
# Date:     N/A
# Notes:    
# 1)  Test python code, cleanup test files and example data
#
import subprocess

print "Cleaning up test files"
subprocess.call('rm -f *.bin', shell=True)
subprocess.call('rm -f *.css', shell=True)
subprocess.call('rm -f *.dat', shell=True)
subprocess.call('rm -f *.db', shell=True)
subprocess.call('rm -f *.gif', shell=True)
subprocess.call('rm -f *.gdbm', shell=True)
subprocess.call('rm -f *.json', shell=True)
subprocess.call('rm -f *.log', shell=True)
subprocess.call('rm -f *.png', shell=True)
subprocess.call('rm -f *.pyc', shell=True)
subprocess.call('rm -f *.sdb', shell=True)
subprocess.call('rm -f *.sql', shell=True)
subprocess.call('rm -f *.sqlite', shell=True)
subprocess.call('rm -f *.tar', shell=True)
subprocess.call('rm -f *.tgz', shell=True)
subprocess.call('rm -f *.txt', shell=True)
subprocess.call('rm -f *.wav', shell=True)
subprocess.call('rm -f *.zip', shell=True)
subprocess.call('rm -f test/moretests/*', shell=True)
subprocess.call('rmdir test/moretests', shell=True)
subprocess.call('rm -f test/*', shell=True)
subprocess.call('rm -f README.html', shell=True)
