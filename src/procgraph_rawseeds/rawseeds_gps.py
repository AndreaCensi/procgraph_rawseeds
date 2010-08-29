from procgraph.components.textlog import TextLog
from procgraph.components.basic import register_block

from procgraph import block_config, block_output

class RawseedsGPS(TextLog):
    ''' This block reads the GPS log from Rawseeds format. 

    Example of GPS file format: ::
    
        1223309581.123667, $GPGGA,143516.80,4530.37118644,N,00909.99763524,E,2,6,1.7,131.984,M,48.022,M,0.8,0000*7
        1223309581.133660, $GPGST,143516.80,0.504,0.238,0.147,54.6,0.212,0.183,0.585*6

    We ignore the GPGST lines for now.
    
    '''
    block_config('file', 'Filename. If it ends with ``bz2`` it is treated as compressed.')
    block_output('latitude')
    block_output('longitude')
    block_output('altitude')
     
    
    def parse_format(self, line):
        """ Should return a tuple (timestamp, array of (name, value) )"""
        
        if not 'GPGGA' in line:
            return None
        
        timestamp, sentence = line.split(',', 1)
        
        timestamp = float(timestamp)
        
        fields = """format utc latitude northsouth longitude eastwest quality
                      number_of_satellites_in_use horizontal_dilution altitude
                      above_sea_unit geoidal_separation geoidal_separation_unit
                      data_age diff_ref_stationID""".split()
              
        sentence = sentence.split(',')
        if len(sentence) != len(fields):
            raise Exception('Wrong format for "%s" expected %d fields instead of %d.'\
                            % line, len(fields), len(sentence))        
        
        data = {}
        for field in fields:
            data[field] = sentence.pop(0)
        
        # snippet copied from http://snippets.dzone.com/posts/show/4782
        latitude_in = float(data['latitude'])
        longitude_in = float(data['longitude'])
        if data['northsouth'] == 'S':
            latitude_in = -latitude_in
        if data['eastwest'] == 'W':
            longitude_in = -longitude_in

        latitude_degrees = int(latitude_in / 100)
        latitude_minutes = latitude_in - latitude_degrees * 100
        
        longitude_degrees = int(longitude_in / 100)
        longitude_minutes = longitude_in - longitude_degrees * 100
        
        output = [
                  ('latitude', latitude_degrees + (latitude_minutes / 60)),
                  ('longitude', longitude_degrees + (longitude_minutes / 60)) ,
                  ('altitude', float(data['altitude']))
        ]
        
        return timestamp, output


register_block(RawseedsGPS)


