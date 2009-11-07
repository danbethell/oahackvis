#!/usr/bin/env python
import urllib2
import xml.dom.minidom as xml

api_key = "BQZw3gBCok7mGHLW9kB5t65S"
request_root = "http://www.openaustralia.org/api/"

# request some information
def request( function ):
    global api_key, request_root
    request = "%s%s?key=%s&output=xml" % ( request_root, function, api_key )
    response = urllib2.urlopen( request )
    result = response.read()
    return result

# get representatives
result = request( "getRepresentatives" )
dom = xml.parseString(result)
representatives = dom.getElementsByTagName("match")

# print some results
print "Num Representatives: %d" % len(representatives)
