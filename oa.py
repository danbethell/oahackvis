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
        doc = xml.dom.minidom.parseString(result)
        return doc
    return result

def termCount(term,person=None,debates=True,comments=True,hansard=True):
    '''
    Return count of records where term was found.
    Not the same as the total frequency of term for th record.
    '''
    result = ''
    count = []
    parms = {"search":term}
    if person:
        parms.update({"person":person})
    if hansard:
        result = request( "getHansard", parms)
        dom = xml.parseString(result)
        count += dom.getElementsByTagName("match")
    if debates:
        parms.update({"type":"representatives"})
        result = request( "getDebates", parms)
        dom = xml.parseString(result)
        count += dom.getElementsByTagName("match")
        parms.update({"type":"senate"})
        result = request( "getDebates", parms)
        dom = xml.parseString(result)
        count += dom.getElementsByTagName("match")
    if comments:
        result = request( "getComments", parms)
        dom = xml.parseString(result)
        count += dom.getElementsByTagName("match")
    return len(count)


if __name__ == '__main__':
    for term in ['transport','economy','promiscuity','broadband','alcohol','crowdsourcing']:
        print '%s total %s' % (term, termCount(term))
        print '%s debates %s' % (term, termCount(term, comments=False, hansard=False))
        print '%s hansard %s' % (term, termCount(term, debates=False, comments=False))
        print '%s comments %s' % (term, termCount(term, hansard=False, debates=True))

