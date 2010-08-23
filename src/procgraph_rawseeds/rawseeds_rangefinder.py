import numpy

from procgraph.components.textlog import TextLog
from procgraph.components.basic import register_block


class RawseedsRangeFinder(TextLog):
    ''' This block reads a range-finder log in Rawseeds format. 
    
    File format: ::
        
        Timestamp [seconds.microseconds]
        # of ranges [unitless]
        Angular offset [1/4 degree]
        R1..R181 Ranges (zero padded to 181 ranges) [m]
    
    '''
    
    def parse_format(self, line):
        """ returns a tuple (timestamp, array of (name, value) )"""
        elements = line.split(',')
        timestamp = float(elements[0])
        num_readings = int(elements[1]) #@UnusedVariable
        offset = float(elements[2])
        readings = numpy.array(map(float, elements[3:]))
        return timestamp, [('readings', readings)]


register_block(RawseedsRangeFinder, 'RawseedsRF')


