import subprocess
import re
import os
import requests
import wget
import sys
import argparse
import platform
java_is_installed = True  # tracks if java was already installed on the computer

parser = argparse.ArgumentParser()
parser.add_argument("j_version", type=int, nargs='?', default=8, help="desired java version")
args = parser.parse_args()

# Parameters for getting JDK
if os.name == 'nt':
    os_system = "windows"
else:
    sys.exit("Please run this on windows")

architecture = "x" + str(re.search(r"^\d+", platform.architecture()[0]).group(0))
image_type = 'jdk'
java_version = str(args.j_version)
JVM = 'hotspot'
vendor = 'adoptopenjdk'
java_available_releases = []


# Check for java version, also in the same time checks for if java exists
def check_java_version():
    global java_is_installed
    try:
        version_number = get_version_number()
        print("Java version: ", version_number)
    except FileNotFoundError:
        java_is_installed = False
        print("Java is not installed on the system")


# Check if java is installed, if it is not install the version in the argument
def check_java_exist(custom_version):
    global java_is_installed
    if not java_is_installed:
        install_java(custom_version)


# Update existing java version to desired version
def update_java(custom_version):
    if java_is_installed:
        if check_java_argument_version(custom_version):
            print("Java version is already at desired version")
        else:
            print("Updating Java to version: ", custom_version)
            install_java(java_version)


# Returns the current java version number
def get_version_number():
    version = subprocess.check_output(['java', '-version'], stderr=subprocess.STDOUT)
    decoded_version = version.decode("utf-8")
    version_number = re.search(r'\"(\d+\.\d+).*\"', decoded_version).groups()[0]
    return version_number


# Check if the current java version is the desired version
def check_java_argument_version(version):
    version_number = get_version_number()
    return version == version_number[-1]


def install_java(custom_version):
    url = 'https://api.adoptopenjdk.net/v3/installer/latest/' + custom_version + '/ga/' + os_system + '/' + architecture \
          + '/' + image_type + '/' + JVM + '/normal/' + vendor
    filename = wget.download(url)
    print("\nDownloaded: ", filename)
    os.system('msiexec /i ' + filename + ' INSTALLLEVEL=2 /passive')
    print("Installed:", filename)
    if os.path.exists(filename):
        os.remove(filename)


def send_status_email():
    print("test")


# Look for available Java versions
def get_available_versions():
    global java_available_releases
    headers = {
        'accept': 'application/json',
    }
    response = requests.get('https://api.adoptopenjdk.net/v3/info/available_releases', headers=headers)
    available_releases = response.json()
    java_available_releases = available_releases['available_releases']


# Check if user specified version exists
def check_version_exists():
    if int(java_version) in java_available_releases:
        print("Specified Java version is available")
    else:
        sys.exit("Java version specified is not available")


def monitor_java():
    get_available_versions()
    check_version_exists()
   # check_java_version()
   # check_java_exist(java_version)
   # update_java(java_version)

monitor_java()
