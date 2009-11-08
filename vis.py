#!/usr/bin/env python
import urllib2
import xml.dom.minidom as xml
import oa, lexi

# get representatives
result = oa.request( "getRepresentatives" )
dom = xml.parseString(result)
representatives = dom.getElementsByTagName("match")
print "Num Representatives: %d" % len(representatives)
for rep in representatives:
    print rep

# get a representative's id
result = oa.request( "getRepresentatives", {"search":"Kevin%20Rudd"} )
print result
dom = xml.parseString(result)
elem = dom.getElementsByTagName("person_id").item(0)
#for child in elem.childNodes:
    #if child.nodeType == xml.TEXT_NODE:
        #id = child.data
        #break
#print id

# exercise term counting.
for term in ["promiscuity","affair","web","broadband"]:
    print 'Term %s: %d' % (term,lexi.termCount(term))
    print "Term %s in %s: %d" % (term, "hansards", lexi.termCount(term, debates=False, comments=False))
