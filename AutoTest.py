# coding=utf-8
# --author='fangfang'

import os
import sys

from flask_script import Manager

from auto.app import create_app

if sys.platform.startswith("linux") or sys.platform.startswith("darwin"):
    os.environ["PATH"] = os.environ["PATH"] + ":" + os.getcwd() + "/driver"
else:
    os.environ["PATH"] = os.environ["PATH"] + ";" + os.getcwd() + "/driver"


app = create_app('development')   # development, production
manager = Manager(app)


if __name__ == '__main__':

    # check_version()

    # load_all_task(app)

    manager.run()

