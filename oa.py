import urllib2
import key

request_root = "http://www.openaustralia.org/api/"

# request some information
def request( function, params={}, dom=False):
    plist = ['key=%s' % key.getAPIKey(),'output=xml']
    for k in params.keys():
        plist.append('%s=%s' % (k,params[k]))
    request = "%s%s?%s" % ( request_root, function, '&'.join(plist) )
    response = urllib2.urlopen( request )
    result = response.read()
    if dom:
        doc = dom.parseString(result)
        return doc
    return result
