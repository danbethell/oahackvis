#!/usr/bin/env python
import urllib2
import xml.dom
import xml.dom.minidom as xml
import oa, lexi

# get representatives
result = oa.request( "getRepresentatives" )
dom = xml.parseString(result)
representatives = dom.getElementsByTagName("match")
print "Num Representatives: %d" % len(representatives)

# exercise term counting.
for term in ["promiscuity","affair","web","broadband"]:
    print 'Term %s: %d' % (term,lexi.termCount(term))
    print "Term %s in %s: %d" % (term, "hansards", lexi.termCount(term, debates=False, comments=False))
