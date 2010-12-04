import numpy

from procgraph import Block
from procgraph.block_utils import TextLog

class RawseedsRangeFinder(TextLog):
    ''' This block reads a range-finder log in Rawseeds format. 
    
    File format: ::
        
        Timestamp [seconds.microseconds]
        # of ranges [unitless]
        Angular offset [1/4 degree]
        R1..R181 Ranges (zero padded to 181 ranges) [m]
    
    '''
    Block.alias('RawseedsRF')
    
    Block.config('file', 'Filename. If it ends with ``bz2`` it is treated as compressed.')
    
    Block.output('readings', 'Range finder readings')
    
    def parse_format(self, line):
        """ returns a tuple (timestamp, array of (name, value) )"""
        elements = line.split(',')
        timestamp = float(elements[0])
        #num_readings = int(elements[1]) 
        #offset = float(elements[2]) 
        readings = numpy.array(map(float, elements[3:]))
        return timestamp, [('readings', readings)]

 
