import os
import time

from subprocess import check_output
from bucket.utils import clean_path, prepare_strings, kill_proc


def get_logs(args):
    target = clean_path(args.apppath)
    os.popen(args.apppath)
    print("BAC | Launched app, waiting 5 seconds before making log.")
    time.sleep(5)
    out = check_output(f"listdlls {target}", shell=True)
    strings_list = prepare_strings(out)
    file = open(args.logspath, "w")
    file.write(str(len(strings_list)))
    file.close()
    kill_proc(target)
    exit()
