#!/usr/bin/env python
import urllib2
import xml.dom.minidom as xml
import oa

# get representatives
result = oa.request( "getRepresentatives" )
dom = xml.parseString(result)
representatives = dom.getElementsByTagName("match")
print "Num Representatives: %d" % len(representatives)

# exercise term counting.
for term in ["promiscuity","affair","web","broadband"]:
    print 'Term %s: %d' % (term,oa.termCount(term))
    print "Term %s in %s: %d" % (term, "hansards", oa.termCount(term, debates=False, comments=False))

