import os
from bucket.modes import launch_protect, get_logs


def launch(args):
    print("__________               __           __       _____  _________  \n"
          "\______   \__ __   ____ |  | __ _____/  |_    /  _  \ \_   ___ \ \n"
          " |    |  _/  |  \_/ ___\|  |/ // __ \   __\  /  /_\  \/    \  \/ \n"
          " |    |   \  |  /\  \___|    <\  ___/|  |   /    |    \     \____\n"
          " |______  /____/  \___  >__|_ \\___  >__|   \____|__  /\______  /\n"
          "        \/            \/     \/    \/               \/        \/ \n")
    if args.apppath or not args.logspath or not os.path.isfile(args.apppath):
        print("BAC | Protecting / Logging application required!")
        return
    if args.protect:
        if not args.logspath or not os.path.isfile(args.logspath):
            print("BAC | For protecting, logs file required!")
        launch_protect(args)
    elif not args.protect:
        get_logs(args)
