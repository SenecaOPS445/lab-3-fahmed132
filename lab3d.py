#!/usr/bin/env python3
# Author ID: Fahmed132

import subprocess

def free_space():
    p = subprocess.Popen("df -h | grep '/$' | awk '{print $4}'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout,_= p.communicate()
    free_space_str = stdout.decode('utf-8').strip()
    return free_space_str

if __name__ == "__main__":
    print(free_space())
