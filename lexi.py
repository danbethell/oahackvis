'''
Express lexical queries in a form palatable to OA API.
'''
import xml.dom.minidom as xml
import oa

def termCount(term):
    result = oa.request( "getHansard", {"search":term})
    dom = xml.parseString(result)
    count = dom.getElementsByTagName("match")
    result = oa.request( "getComments", {"search":term})
    dom = xml.parseString(result)
    count += dom.getElementsByTagName("match")
    return len(count)


if __name__ == '__main__':
    for term in ['economy','promiscuity']:
        print '%s %s' % (term, termCount("economy"))
