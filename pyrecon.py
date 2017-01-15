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
    '/proc/cmdline'
    #'/etc/shadow',
    '/etc/group',
    #'/etc/sudoers',
]

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

# List directories

treeFile = open(args.directory + '/dirwalk', 'w+')
for root, dirs, filenames in os.walk('/home/'):
    for name in filenames:
        treeFile.write('\n')
        treeFile.write(os.path.join(root, name))
    for name in dirs:
        treeFile.write('\n')
        treeFile.write(os.path.join(root, name))
