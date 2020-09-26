import subprocess
import re
import os


def check_java():
    try:
        version = subprocess.check_output(['java', '-version'], stderr=subprocess.STDOUT)
        version = version.decode("utf-8")
        print(re.search(r'\"(\d+\.\d+).*\"', version).groups()[0])
    except FileNotFoundError:

        print("Java is not installed on the system")

    print("check_java_test")


def monitor_java():
    check_java()


monitor_java()