# JAVA-MONITORING
Python script for monitoring 

Important: Java's environnement variables status only refreshes when command line is closed and re-opened.

This is currently intended for windows.

Process:

1- Check if Java is installed

2- Install/Update/ChangeTo desired Java version (Or do nothing)

3- Send Email to give a status report 
```
Usage:

Get necessary python packages: pip install -r requirements.txt

usage: monitor_java.py [-h] [j_version] [sender_email] [receiver_email]

positional arguments:
  j_version       desired java version (default:8)(eg: 8,10,11,12,13,14,15)
  sender_email    sender email (default:talonpythonchallenge@gmail.com)
  receiver_email  receiver email (default:yuchenmichaelchu@gmail.com)

optional arguments:
  -h, --help      show this help message and exit
```
Does not support JAVA 9 and 10 (MSI packages not available + deprecated versions)
