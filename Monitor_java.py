import subprocess
import re
import os
import requests
import wget

java_is_installed = True
os_system = "windows"
architecture = "x64"
image_type = 'jdk'
java_version = '8'
JVM = 'hotspot'
vendor = 'adoptopenjdk'


# Check for java version, also in the same time checks for if java exists
def check_java_version():
    global java_is_installed
    try:
        version_number = get_version_number()
        print("Install Java version: ", version_number)
    except FileNotFoundError:
        java_is_installed = False
        print("Java is not installed on the system")


# Check if java is installed, if it is not install the version in the argument
def check_java_exist(custom_version):
    global java_is_installed
    if not java_is_installed:
        install_java(custom_version)
        java_is_installed = True


# Update existing java version to desired version
def update_java(custom_version):
    if java_is_installed:
        if check_java_argument_version(custom_version):
            print("Java version is already at desired version")
        else:
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
    return version == version_number


def install_java(custom_version):
    url = 'https://api.adoptopenjdk.net/v3/installer/latest/' + custom_version + '/ga/' + os_system + '/' + architecture \
          + '/' + image_type + '/' + JVM + '/normal/' + vendor
    filename = wget.download(url)
    print("Downloaded", filename)
    os.system('msiexec /i ' + filename + ' INSTALLLEVEL=2 /passive')
    print("Installed:", filename)


def send_status_email():
    print("test")


def monitor_java():
    check_java_version()
    install_java(java_version)
    update_java(java_version)


monitor_java()
