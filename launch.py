import argparse
from bucket import launch


def parse_args():
    args = argparse.ArgumentParser(
        prog='',
        description='Detecting DLL injection into application',
        epilog='Please be accurate with arguments!',
    )
    args.add_argument("apppath")
    args.add_argument("logspath")
    args.add_argument("--protect", help="Protects selected application",
                      default="Protect",
                      action="store_true", required=False)
    gotten_args = args.parse_args()
    return gotten_args


if __name__ == '__main__':
    launch(parse_args())


