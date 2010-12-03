import os, re

from procgraph import Generator, Block, register_model_spec
from procgraph.block_utils import expand  

class RawseedsCamFiles(Generator):
    ''' This block reads the filenames for the Rawseeds camera log.
    
        It is assumed that the files follow the regexp ``'(\w+)_(\d+)\.(\d+)\.png'``,
        that is, ``<LOGNAME>_<TIMESTAMP>.png``
    
    '''
    Block.config('dir', 'Directory containing the image files.')
    Block.output('filename', 'Image filenames')
    
    def init(self):
        dirname = self.config.dir
        dirname = expand(dirname)
        
        if not os.path.exists(dirname):
            raise Exception('Non existent directory "%s".' % dirname)
        if not os.path.isdir(dirname):
            raise Exception('The file "%s" is not a directory.' % dirname)
        
        # TODO: use proper logging
        self.info("Reading directory listings from %s" % dirname)
        all_files = os.listdir(dirname)
        
        regexp = '(\w+)_(\d+)\.(\d+)\.png'
        
        # tuples (timestamp, filename)
        frames = []
        for filename in all_files:
            m = re.match(regexp, filename)
            if m:
                signal_name = m.group(1)
                seconds = m.group(2)
                fraction = m.group(3)
                timestamp = float(seconds) + float('0.%s' % fraction)
                global_filename = os.path.join(dirname, filename)
                frames.append((timestamp, global_filename))
        
        if not frames:
            raise Exception('No frames found in dir "%s".' % dirname)
        
        
        self.info("Read %s frames -- sorting." % len(frames))
        frames.sort(key=lambda x: x[0])
        
        self.state.frames = frames
        self.state.next_frame = 0

        
        self.info("Camera log ready for %s" % dirname)
        
    def next_data_status(self):
        k = self.state.next_frame
        if k is None:
            return (False, None)
        else:
            frames = self.state.frames
            timestamp = frames[k][0]
            return (True, timestamp)
                 
    def update(self):
        frames = self.state.frames
        k = self.state.next_frame

        assert k < len(frames)
        
        timestamp, filename = frames[k] 
        
        self.set_output(0, value=filename, timestamp=timestamp)        

        if k + 1 >= len(frames):
            self.state.next_frame = None
        else:
            self.state.next_frame = k + 1
            

# Computes the variance
register_model_spec("""
--- model RawseedsCam
'''This model reads the images of a Rawseed camera log.'''
config dir    'Directory containing the images.' 
config fps_limit = 100 'Limit the frames per second (default is disabled).'
output images

import procgraph_pil

|RawseedsCamFiles dir=$dir| --> |fps_data_limit fps=$fps_limit| --> filenames

    filenames --> |imread| --> |output name=images|
 
""")
