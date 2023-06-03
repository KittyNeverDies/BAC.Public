import os
import time

from subprocess import check_output
from bucket.utils import clean_path, prepare_strings, kill_proc, is_launched


def protect(target, original_strings):
    launched = True
    while launched:
        launched = is_launched(target)
        time.sleep(5)
        out = check_output(f"listdlls {target}", shell=True)
        new_strings = prepare_strings(out)
        if original_strings != len(new_strings):
            print("BAC | Injection detected! Closing app...")
            kill_proc(target)
            exit()


def launch_protect(args):
    target = clean_path(args.apppath)
    with open(args.logspath) as f:
        original_strings = f.read()
    if not is_launched(target):
        os.popen(args.apppath)
        time.sleep(5)
    protect(target, original_strings)
