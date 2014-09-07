tykwol
======
tykwol.py is a wake-on-lan magic packet sender written in python and scapy. I wrote it
because I couldn't find any WOL tools that allows the user to specify interface
on a multi homed box, when broadcasting the WOL magic packet. This script takes a
mac address and an interface as arguments, and sends the magic packet out the
specified interface to wake the machine with the specified mac. It is an extension
of the WOL example in the Scapy documentation.

This script requires:
- Python - http://www.python.org/ - /usr/ports/lang/python26 on FreeBSD
- Scapy - http://www.secdev.org/projects/scapy/ - /usr/ports/net/scapy on FreeBSD

The latest version can be found at https://github.com/tykling/tykwol
