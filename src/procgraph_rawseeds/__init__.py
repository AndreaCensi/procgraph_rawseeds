''' Routines for reading the data from the Rawseeds project. '''

import rawseeds_rangefinder 
import rawseeds_camera 
import rawseeds_odometry
import rawseeds_hokuyo 
import rawseeds_gps


__version__ = "1.0" 



# FIXME, make this easier
import os
from procgraph.core.registrar import default_library
from procgraph.core.model_loader import pg_look_for_models
dir = os.path.join(os.path.dirname(__file__), 'models')
pg_look_for_models(default_library, additional_paths=[dir], ignore_env=True,
                   assign_to_module='procgraph_rawseeds')



