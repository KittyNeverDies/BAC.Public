import psutil


def is_launched(target) -> bool:
    for targets in psutil.process_iter():
        if targets.name() == target:
            return True
    return False
