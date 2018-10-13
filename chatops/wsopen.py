#!/usr/bin/python

import sys
import pushbullet
from pushbullet import Pushbullet

webSite = sys.argv[1]

pb = Pushbullet('<token>')

push = pb.push_link("Your site", webSite , device=pb.devices[1])

print "Website has opened check your Chrome!"
#print pb.devices[1]
#print(pb.devices)
