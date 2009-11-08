import urllib2
import key

request_root = "http://www.openaustralia.org/api/"

# request some information
def request( function, params={}, dom=False):
    global api_key, request_root
    plist = ['key=%s' % key.api_key,'output=xml']
    for key in params.keys():
        plist.append('%s=%s' % (key,params[key]))
    request = "%s%s?%s" % ( request_root, function, '&'.join(plist) )
    response = urllib2.urlopen( request )
    result = response.read()
    if dom:
        doc = dom.parseString(result)
        return doc
    return result
