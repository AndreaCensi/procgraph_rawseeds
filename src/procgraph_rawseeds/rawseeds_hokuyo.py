import numpy

from procgraph.components.textlog import TextLog


from procgraph import Block

class RawseedsHokuyo(TextLog):
    ''' This block reads a Hokuyo log in Rawseeds format. 
    
        File format: ::
        
            Timestamp [seconds.microseconds]
            R1..R681* Ranges [m]
    
    '''
    
    Block.config('file', 'Filename. If it ends with ``bz2`` it is treated as compressed.')
    
    Block.output('readings', 'Range finder readings')
    
    def parse_format(self, line):
        """ returns a tuple (timestamp, array of (name, value) )"""
        elements = map(str.strip, line.split(','))
        timestamp = float(elements.pop(0))
        readings = numpy.array(map(float, elements))
        
        # XXX should be 682 ???
        # if len(elements) != 681:
        #    print elements
        #    raise Exception('Expected 681 readings instead of %s' % len(elements))
            
        return timestamp, [('readings', readings)]

 
