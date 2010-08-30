from procgraph.components.textlog import TextLog
from procgraph.components.basic import register_block
from procgraph  import block_output, block_config, block_alias


class RawseedsOdometry(TextLog):
    ''' Read an odometry log file in Rawseeds format.
    
    File format: ::
    
        Timestamp [seconds.microseconds]
        Rolling Counter [signed 16bit integer]
        TicksRight [ticks]
        TicksLeft [ticks]
        X [m]*
        Y [m]*
        Theta [rad]*

    Example: ::
    
        1235561676.443740, 3225, 0, 0, 0.000, 0.000, 0.000

    *Reference frame:* A right handed reference frame is used. 
    Y axis is aligned along the front-rear direction and points 
    towards the front, X axis is parallel to the wheelbase and points 
    towards the right wheel.

'''
    block_alias('RawseedsOdo')
    
    block_config('file', 'Filename. If it ends with ``bz2`` it is treated as compressed.')
    
    block_output('pose', 'x,y,theta')
    block_output('ticks_right')
    block_output('ticks_left')
    block_output('x')
    block_output('y')
    block_output('theta')
    block_output('rolling_counter') 

    def parse_format(self, line):
        """ returns a tuple (timestamp, array of (name, value) )"""
        elements = map(str.strip, line.split(","))
        if len(elements) != 7:
            raise ValueError('Line does not conform to rawseeds format.')
       
        # elements = 
        # ['1235561676.004846', '3203', '0', '0', '0.000', '0.000', '0.000']

        timestamp = float(elements.pop(0))
        rolling_counter = float(elements.pop(0)) 
        ticks_right = int(elements.pop(0))
        ticks_left = int(elements.pop(0))
        x = float(elements.pop(0))
        y = float(elements.pop(0))
        theta = float(elements.pop(0))
        
        signals = [
            # XXX compensate for reference frame?
            ('pose', [x, y, theta]),
            ('ticks_right', ticks_right),
            ('ticks_left', ticks_left),
            ('x', x),
            ('y', y),
            ('theta', theta),
            ('rolling_counter', rolling_counter)
        ]
        
        return timestamp, signals
        
         

        
