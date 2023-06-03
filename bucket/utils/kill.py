import psutil


def kill_proc(target) -> None:
    for targets in psutil.process_iter():
        if targets.name() == target:
            targets.kill()

