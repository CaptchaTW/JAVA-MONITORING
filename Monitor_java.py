import subprocess
import re
import os
import requests
import wget

java_is_installed = True


def check_java():
    global java_is_installed
    try:
        version = subprocess.check_output(['java', '-version'], stderr=subprocess.STDOUT)
        decoded_version = version.decode("utf-8")
        version_number = re.search(r'\"(\d+\.\d+).*\"', decoded_version).groups()[0]
        print(version_number)
    except FileNotFoundError:
        java_is_installed = False
        print("Java is not installed on the system")
    print("check_java_test")


def install_java():
    url = 'https://api.adoptopenjdk.net/v3/installer/latest/8/ga/windows/x64/jdk/hotspot/normal/adoptopenjdk'
    filename = wget.download(url)
    print(filename)
    os.system('msiexec /i '+ filename + ' INSTALLLEVEL=1 /passive')


def monitor_java():
    check_java()
    install_java()
    #check_java()

monitor_java()
