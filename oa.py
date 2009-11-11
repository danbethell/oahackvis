import urllib2
import xml.dom.minidom as xml

api_key = "YOUR_OPEN_AUSTRALIA_API_KEY_HERE"
request_root = "http://www.openaustralia.org/api/"

def getAPIKey():
    '''
    Returns the API key
    '''
    global api_key
    return api_key

def getRequestRoot():
    '''
    Returns the OpenAustralia api http root
    '''
    global request_root
    return request_root

def request( function, params={}):
    '''
    Make a call to the OpenAustralia API
    Returns a string of xml suitable for parsing to minidom
    '''
    plist = ['key=%s' % getAPIKey(),'output=xml']
    for k in params.keys():
        plist.append('%s=%s' % (k,params[k]))
    request = "%s%s?%s" % ( getRequestRoot(), function, '&'.join(plist) )
    response = urllib2.urlopen( request )
    result = response.read()
    return result

def getText( rep, key ):
    '''
    Gets some text from a dom element
    '''
    element = rep.getElementsByTagName( key )[0]
    nodelist = element.childNodes
    result = ""
    for node in nodelist:
        if node.nodeType == node.TEXT_NODE:
            result = result + node.data
    return result

def getRepresentatives():
    '''
    Return the representatives as a list of dictionaries
    '''
    result = request( "getRepresentatives" )
    dom = xml.parseString(result)
    representatives = dom.getElementsByTagName("match")

    # format xml representatives into a list of 'rep' dictionaries
    reps = []
    for r in representatives:
        rep = {}
        rep['member_id'] = getText(r, "person_id")
        rep['person_id'] = getText(r, "person_id")
        rep['name'] = getText(r, "name")
        rep['party'] = getText(r, "party")
        rep['constituency'] = getText(r, "constituency")
        reps.append(rep)
    return reps

def numDebates(person):
    '''
    Returns the total number of debates for the specified person
    '''
    params = {"type":"representatives", "person":person}
    result = request( "getDebates", params )
    dom = xml.parseString(result)
    info = dom.getElementsByTagName("info")
    return int(getText(dom, "total_results"))

def termCount(term,person=None,debates=True,comments=True,hansard=True):
    '''
    Return count of records where term was found.
    Not the same as the total frequency of term for the record.
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

# some tests
if __name__ == '__main__':
    import vis
    print "%d reps" % len(vis.reps)
    for r in vis.reps[:10]:
        print "Person %s, %s num debates: %d" % (r['person_id'], r['name'], numDebates(r['person_id']))
    for term in ['transport','economy','promiscuity','broadband','alcohol','crowdsourcing']:
        print '%s total: %s' % (term, termCount(term))
        print '%s debates: %s' % (term, termCount(term, comments=False, hansard=False))
        print '%s hansard: %s' % (term, termCount(term, debates=False, comments=False))
        print '%s comments: %s' % (term, termCount(term, hansard=False, debates=True))
