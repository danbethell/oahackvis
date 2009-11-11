#!/usr/bin/env python
import random
import oa

# get representatives
reps = oa.getRepresentatives()

def numRepresentatives():
    '''
    Returns the number of representatives
    '''
    return len(reps)

def getName( index ):
    '''
    Returns the name of representative at index
    '''
    return reps[index]['name']

assigned_colours = {}
def getColour( index ):
    '''
    Returns a random colour for the party of representative at index
    '''
    party = reps[index]['party']
    some_colours = [
        (1,.5,.5),
        (.5,1,.5),
        (.5,.5,1),
        (1,1,.5),
        (.5,1,1),
        (1,.5,1)
        ]
    if not party in assigned_colours:
        assigned_colours[party] = some_colours[len(assigned_colours)%6]
    return assigned_colours[party]

def termCount( index, term ):
    '''
    Returns the number of time representive at index used 'term' in debates & hansard
    '''
    global reps
    store_key = "termcount_%s" % term # store the result with each rep using this key
    if not reps[index].has_key( store_key ):
        reps[index][store_key] = oa.termCount( term, reps[index]['person_id'], debates=True, hansard=True, comments=False )
    return reps[index][store_key]

def numDebates( index ):
    '''
    Returns the number of debates for the reprentative at index
    '''
    if not reps[index].has_key("num_debates"):
        reps[index]['num_debates'] = oa.numDebates( reps[index]['person_id'] )
    return reps[index]['num_debates']

# some tests
if __name__ == '__main__':
    print "%d reps" % numRepresentatives()
    for i in range(0, 10):
        print "Person %s, %s num debates: %d" % (reps[i]['person_id'], reps[i]['name'], numDebates(i))
        print (reps[i]['party'], str(getColour(i)))
        print "used the word 'web' %d times" % termCount(i, "web")
