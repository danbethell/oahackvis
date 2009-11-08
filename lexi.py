'''
Express lexical queries in a form palatable to OA API.
'''
import xml.dom.minidom as xml
import oa

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
        result = oa.request( "getHansard", parms)
        dom = xml.parseString(result)
        count += dom.getElementsByTagName("match")
    if debates:
        result = oa.request( "getDebates", parms)
        dom = xml.parseString(result)
        count += dom.getElementsByTagName("match")
    if comments:
        result = oa.request( "getComments", parms)
        dom = xml.parseString(result)
        count += dom.getElementsByTagName("match")
    return len(count)


if __name__ == '__main__':
    for term in ['transport','economy','promiscuity','broadband','alcohol','crowdsourcing']:
        print '%s debates %s' % (term, termCount(term, comments=False, hansard=False))
        print '%s hansard %s' % (term, termCount(term, debates=False, comments=False))
        print '%s comments %s' % (term, termCount(term, hansard=False, debates=True))
