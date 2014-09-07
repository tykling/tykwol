#!/usr/local/bin/python
import sys
from scapy.all import *

#check number of arguments
if len(sys.argv) != 3:
  sys.exit("Usage: " + sys.argv[0] + " em0 1234567890ab    - where em0 is the interface and 1234567890ab is the mac address to wake up.")

#set variables
ifc = sys.argv[1]
hexmac = sys.argv[2]

#remove colon from the mac
hexmac = hexmac.replace(":", "")

#remove dot from the mac (thanks cisco)
hexmac = hexmac.replace(".", "")

#remove dashes from the mac (thanks microsoft)
hexmac = hexmac.replace("-", "")

#check length of the supplied mac address
if len(hexmac) != 12:
  sys.exit("Mac address must be 12 digits - allowed seperators are colon (:) dash (-) and dot (.)!")

#decode the hex mac address to ascii
mac = hexmac.decode("hex")

#define the FF byte (the magic packet needs six FF bytes as padding in the beginning of the packet)
eff = '\xff'

#the main procedure
def main():
        #build and send the magic packet
        sendp(Ether(dst='ff:ff:ff:ff:ff:ff') /IP(dst='255.255.255.255') /UDP(dport=9) /Raw(eff*6 + mac*16),iface=ifc)
        #a little output to the user
        print "Sent magic packet to", hexmac, "on interface", ifc

#call the main procedure
main()
