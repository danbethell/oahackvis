#!/usr/bin/env python
import urllib2
import xml.dom.minidom as xml
import oa, lexi

# get representatives
result = oa.request( "getRepresentatives" )
dom = xml.parseString(result)
representatives = dom.getElementsByTagName("match")

# print some results
print "Num Representatives: %d" % len(representatives)

# exercise term counting.
print lexi.termCount("promiscuity")
print lexi.termCount("affair")
print lexi.termCount("web")
print lexi.termCount("broadband")
