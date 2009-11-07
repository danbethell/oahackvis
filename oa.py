import urllib2

api_key = "BQZw3gBCok7mGHLW9kB5t65S"
request_root = "http://www.openaustralia.org/api/"

# request some information
def request( function, params={}):
    global api_key, request_root
    plist = ['key=%s' % api_key,'output=xml']
    for key in params.keys():
        plist.append('%s=%s' % (key,params[key]))
    request = "%s%s?%s" % ( request_root, function, '&'.join(plist) )
    response = urllib2.urlopen( request )
    result = response.read()
    return result
