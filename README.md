# pyrecon
A post exploitation enumeration tool for linux/unix devices that have Python 2.\* installed with nothing other than default libraries and using no native bash commands.

This tool is part of a project to learn python as well as linux OS enumeration.

Development Status: Ongoing 1/16/2017

* To-Do Features
** Build archive/auto exfil capability
** File/Log Cleanup on Exit + Autodelete if connection breaks
** Debian vs. RHEL filesystems
** root vs. \* user checks
** Add following capabilities

'mount | column -t',
sticky bit files
'/usr/bin/find / -perm -g=s -o -perm -4000 ! type l -maxdepth 3 -exec ls -ld {} \; 2>/dev/null',
world directories
'/usr/bin/find / -perm 222 -type d 2>/dev/null',
world writeable files
'/usr/bin/find / -perm 0777 -type f 2>/dev/null'
'/usr/bin/find / -user $(whoami) 2>/dev/null',
'/usr/bin/w',
'/usr/bin/'last',
