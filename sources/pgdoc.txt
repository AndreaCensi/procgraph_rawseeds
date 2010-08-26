.. |towrite| replace:: **to write** 

.. _`pgdoc:procgraph_rawseeds`:

Summary 
============================================================


:ref:`module:procgraph_rawseeds`

Routines for reading the data from the Rawseeds project.

======================================================================================================================================================================================================== ========================================================================================================================================================================================================
:ref:`RawseedsCam <block:RawseedsCam>`                                                                                                                                                                   This model reads the images of a Rawseed camera log.                                                                                                                                                    
:ref:`RawseedsCamFiles <block:RawseedsCamFiles>`                                                                                                                                                         This block reads the filenames for the Rawseeds camera log.                                                                                                                                             
:ref:`RawseedsGPS <block:RawseedsGPS>`                                                                                                                                                                   This block reads the GPS log from Rawseeds format.                                                                                                                                                      
:ref:`RawseedsHokuyo <block:RawseedsHokuyo>`                                                                                                                                                             This block reads a Hokuyo log in Rawseeds format.                                                                                                                                                       
:ref:`RawseedsOdo <block:RawseedsOdo>`                                                                                                                                                                   Read an odometry log file in Rawseeds format.                                                                                                                                                           
:ref:`RawseedsRF <block:RawseedsRF>`                                                                                                                                                                     This block reads a range-finder log in Rawseeds format.                                                                                                                                                 
:ref:`camera_display <block:camera_display>`                                                                                                                                                             None                                                                                                                                                                                                    
:ref:`camera_expectation <block:camera_expectation>`                                                                                                                                                     None                                                                                                                                                                                                    
:ref:`camera_filters <block:camera_filters>`                                                                                                                                                             None                                                                                                                                                                                                    
:ref:`camera_video <block:camera_video>`                                                                                                                                                                 None                                                                                                                                                                                                    
:ref:`compression_test <block:compression_test>`                                                                                                                                                         None                                                                                                                                                                                                    
:ref:`decode <block:decode>`                                                                                                                                                                             None                                                                                                                                                                                                    
:ref:`gray_pipeline <block:gray_pipeline>`                                                                                                                                                               None                                                                                                                                                                                                    
:ref:`master <block:master>`                                                                                                                                                                             None                                                                                                                                                                                                    
:ref:`rangefinder_display <block:rangefinder_display>`                                                                                                                                                   None                                                                                                                                                                                                    
:ref:`rawseeds_big_movie <block:rawseeds_big_movie>`                                                                                                                                                     Creates a big movie file displaying all data                                                                                                                                                            
:ref:`rawseeds_display_all <block:rawseeds_display_all>`                                                                                                                                                 None                                                                                                                                                                                                    
:ref:`rawseeds_odometry <block:rawseeds_odometry>`                                                                                                                                                       None                                                                                                                                                                                                    
:ref:`rawseeds_read_all <block:rawseeds_read_all>`                                                                                                                                                       A model that reads all data from a Rawseeds log, to check it can be read correctly.                                                                                                                     
:ref:`rawseeds_read_all_small <block:rawseeds_read_all_small>`                                                                                                                                           Reads the whole log to check that it does not contain errors.                                                                                                                                           
:ref:`rawseeds_read_camera <block:rawseeds_read_camera>`                                                                                                                                                 Reads the whole log to check that it does not contain errors.                                                                                                                                           
:ref:`rawseeds_read_gps <block:rawseeds_read_gps>`                                                                                                                                                       Reads the GPS log to check that it does not contain errors.                                                                                                                                             
:ref:`rawseeds_read_hokuyo <block:rawseeds_read_hokuyo>`                                                                                                                                                 Reads the whole log to check that it does not contain errors.                                                                                                                                           
:ref:`rawseeds_read_sick <block:rawseeds_read_sick>`                                                                                                                                                     Reads the whole log to check that it does not contain errors.                                                                                                                                           
:ref:`rawseeds_synchronized_camera <block:rawseeds_synchronized_camera>`                                                                                                                                 Outputs the syncrhonized data of 3 cameras (omnidirectional, )                                                                                                                                          
:ref:`rawseeds_synchronized_camera_test <block:rawseeds_synchronized_camera_test>`                                                                                                                       Tests the rawseeds_synchronized_camera model by writing out a movie.                                                                                                                                    
:ref:`rawseeds_synchronized_laser <block:rawseeds_synchronized_laser>`                                                                                                                                   This model reads and synchronizes the 4 laser sources in a Rawseeds log.                                                                                                                                
:ref:`rawseedscam2con2der2video <block:rawseedscam2con2der2video>`                                                                                                                                       None                                                                                                                                                                                                    
:ref:`rawseedscam2der2video <block:rawseedscam2der2video>`                                                                                                                                               None                                                                                                                                                                                                    
:ref:`rawseedscam2gray2der2video <block:rawseedscam2gray2der2video>`                                                                                                                                     None                                                                                                                                                                                                    
:ref:`rawseedscam2video <block:rawseedscam2video>`                                                                                                                                                       None                                                                                                                                                                                                    
:ref:`rf_display <block:rf_display>`                                                                                                                                                                     Makes a plot of range finder data                                                                                                                                                                       
:ref:`svs_pipeline <block:svs_pipeline>`                                                                                                                                                                 Pipeline for SVS data                                                                                                                                                                                   
:ref:`test_dynamics <block:test_dynamics>`                                                                                                                                                               None                                                                                                                                                                                                    
:ref:`test_nearness <block:test_nearness>`                                                                                                                                                               None                                                                                                                                                                                                    
:ref:`test_pose2commands <block:test_pose2commands>`                                                                                                                                                     None                                                                                                                                                                                                    
:ref:`testing_resize <block:testing_resize>`                                                                                                                                                             None                                                                                                                                                                                                    
:ref:`transcode <block:transcode>`                                                                                                                                                                       None                                                                                                                                                                                                    
:ref:`transcode_filter <block:transcode_filter>`                                                                                                                                                         None                                                                                                                                                                                                    
======================================================================================================================================================================================================== ========================================================================================================================================================================================================


.. _`module:procgraph_rawseeds`:


.. rst-class:: procgraph:module

Module ``procgraph_rawseeds``
============================================================



.. rst-class:: procgraph:desc

Routines for reading the data from the Rawseeds project.

.. _`block:RawseedsCam`:


.. rst-class:: procgraph:block

RawseedsCam
------------------------------------------------------------
This model reads the images of a Rawseed camera log.


.. rst-class:: procgraph:parameters

Parameters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``dir``: Directory containing the images.

- ``fps_limit`` (default: 100): Limit the frames per second (default is disabled).


.. rst-class:: procgraph:source

Implemented in `/src/procgraph_rawseeds/rawseeds_camera.py <https://github.com/AndreaCensi/procgraph_rawseeds/blob/master//src/procgraph_rawseeds/rawseeds_camera.py>`_. 


.. _`block:RawseedsCamFiles`:


.. rst-class:: procgraph:block

RawseedsCamFiles
------------------------------------------------------------
This block reads the filenames for the Rawseeds camera log.


.. rst-class:: procgraph:source

Implemented in `/src/procgraph_rawseeds/rawseeds_camera.py <https://github.com/AndreaCensi/procgraph_rawseeds/blob/master//src/procgraph_rawseeds/rawseeds_camera.py>`_. 


.. _`block:RawseedsGPS`:


.. rst-class:: procgraph:block

RawseedsGPS
------------------------------------------------------------
This block reads the GPS log from Rawseeds format. 

Example: ::

    1223309581.123667, $GPGGA,143516.80,4530.37118644,N,00909.99763524,E,2,6,1.7,131.984,M,48.022,M,0.8,0000*7
    1223309581.133660, $GPGST,143516.80,0.504,0.238,0.147,54.6,0.212,0.183,0.585*6

We ignore the GPGST lines for now.


.. rst-class:: procgraph:source

Implemented in `/src/procgraph_rawseeds/rawseeds_gps.py <https://github.com/AndreaCensi/procgraph_rawseeds/blob/master//src/procgraph_rawseeds/rawseeds_gps.py>`_. 


.. _`block:RawseedsHokuyo`:


.. rst-class:: procgraph:block

RawseedsHokuyo
------------------------------------------------------------
This block reads a Hokuyo log in Rawseeds format. 

File format: ::

    Timestamp [seconds.microseconds]
    R1..R681* Ranges [m]


.. rst-class:: procgraph:source

Implemented in `/src/procgraph_rawseeds/rawseeds_hokuyo.py <https://github.com/AndreaCensi/procgraph_rawseeds/blob/master//src/procgraph_rawseeds/rawseeds_hokuyo.py>`_. 


.. _`block:RawseedsOdo`:


.. rst-class:: procgraph:block

RawseedsOdo
------------------------------------------------------------
Read an odometry log file in Rawseeds format. 

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


.. rst-class:: procgraph:source

Implemented in `/src/procgraph_rawseeds/rawseeds_odometry.py <https://github.com/AndreaCensi/procgraph_rawseeds/blob/master//src/procgraph_rawseeds/rawseeds_odometry.py>`_. 


.. _`block:RawseedsRF`:


.. rst-class:: procgraph:block

RawseedsRF
------------------------------------------------------------
This block reads a range-finder log in Rawseeds format. 

File format: ::

    Timestamp [seconds.microseconds]
    # of ranges [unitless]
    Angular offset [1/4 degree]
    R1..R181 Ranges (zero padded to 181 ranges) [m]


.. rst-class:: procgraph:source

Implemented in `/src/procgraph_rawseeds/rawseeds_rangefinder.py <https://github.com/AndreaCensi/procgraph_rawseeds/blob/master//src/procgraph_rawseeds/rawseeds_rangefinder.py>`_. 


.. _`block:camera_display`:


.. rst-class:: procgraph:block

camera_display
------------------------------------------------------------

.. rst-class:: procgraph:source

Implemented in `/src/procgraph_rawseeds/models/to_sort/camera_display.pg <https://github.com/AndreaCensi/procgraph_rawseeds/blob/master//src/procgraph_rawseeds/models/to_sort/camera_display.pg>`_. 


.. _`block:camera_expectation`:


.. rst-class:: procgraph:block

camera_expectation
------------------------------------------------------------

.. rst-class:: procgraph:source

Implemented in `/src/procgraph_rawseeds/models/to_sort/camera_expectation.pg <https://github.com/AndreaCensi/procgraph_rawseeds/blob/master//src/procgraph_rawseeds/models/to_sort/camera_expectation.pg>`_. 


.. _`block:camera_filters`:


.. rst-class:: procgraph:block

camera_filters
------------------------------------------------------------

.. rst-class:: procgraph:source

Implemented in `/src/procgraph_rawseeds/models/to_sort/camera_filters.pg <https://github.com/AndreaCensi/procgraph_rawseeds/blob/master//src/procgraph_rawseeds/models/to_sort/camera_filters.pg>`_. 


.. _`block:camera_video`:


.. rst-class:: procgraph:block

camera_video
------------------------------------------------------------

.. rst-class:: procgraph:source

Implemented in `/src/procgraph_rawseeds/models/to_sort/camera_video.pg <https://github.com/AndreaCensi/procgraph_rawseeds/blob/master//src/procgraph_rawseeds/models/to_sort/camera_video.pg>`_. 


.. _`block:compression_test`:


.. rst-class:: procgraph:block

compression_test
------------------------------------------------------------

.. rst-class:: procgraph:source

Implemented in `/src/procgraph_rawseeds/models/to_sort/compression_test.pg <https://github.com/AndreaCensi/procgraph_rawseeds/blob/master//src/procgraph_rawseeds/models/to_sort/compression_test.pg>`_. 


.. _`block:decode`:


.. rst-class:: procgraph:block

decode
------------------------------------------------------------

.. rst-class:: procgraph:source

Implemented in `/src/procgraph_rawseeds/models/video_tests.pg <https://github.com/AndreaCensi/procgraph_rawseeds/blob/master//src/procgraph_rawseeds/models/video_tests.pg>`_. 


.. _`block:gray_pipeline`:


.. rst-class:: procgraph:block

gray_pipeline
------------------------------------------------------------

.. rst-class:: procgraph:source

Implemented in `/src/procgraph_rawseeds/models/to_sort/nearness.pg <https://github.com/AndreaCensi/procgraph_rawseeds/blob/master//src/procgraph_rawseeds/models/to_sort/nearness.pg>`_. 


.. _`block:master`:


.. rst-class:: procgraph:block

master
------------------------------------------------------------

.. rst-class:: procgraph:source

Implemented in `/src/procgraph_rawseeds/models/to_sort/video_frame.pg <https://github.com/AndreaCensi/procgraph_rawseeds/blob/master//src/procgraph_rawseeds/models/to_sort/video_frame.pg>`_. 


.. _`block:rangefinder_display`:


.. rst-class:: procgraph:block

rangefinder_display
------------------------------------------------------------

.. rst-class:: procgraph:source

Implemented in `/src/procgraph_rawseeds/models/to_sort/rangefinder_display.pg <https://github.com/AndreaCensi/procgraph_rawseeds/blob/master//src/procgraph_rawseeds/models/to_sort/rangefinder_display.pg>`_. 


.. _`block:rawseeds_big_movie`:


.. rst-class:: procgraph:block

rawseeds_big_movie
------------------------------------------------------------
Creates a big movie file displaying all data


.. rst-class:: procgraph:parameters

Parameters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``logdir``: Rawseeds log directory


.. rst-class:: procgraph:source

Implemented in `/src/procgraph_rawseeds/models/rawseeds_big_movie.pg <https://github.com/AndreaCensi/procgraph_rawseeds/blob/master//src/procgraph_rawseeds/models/rawseeds_big_movie.pg>`_. 


.. _`block:rawseeds_display_all`:


.. rst-class:: procgraph:block

rawseeds_display_all
------------------------------------------------------------

.. rst-class:: procgraph:source

Implemented in `/src/procgraph_rawseeds/models/to_sort/all.pg <https://github.com/AndreaCensi/procgraph_rawseeds/blob/master//src/procgraph_rawseeds/models/to_sort/all.pg>`_. 


.. _`block:rawseeds_odometry`:


.. rst-class:: procgraph:block

rawseeds_odometry
------------------------------------------------------------

.. rst-class:: procgraph:source

Implemented in `/src/procgraph_rawseeds/models/to_sort/rawseeds_odometry.pg <https://github.com/AndreaCensi/procgraph_rawseeds/blob/master//src/procgraph_rawseeds/models/to_sort/rawseeds_odometry.pg>`_. 


.. _`block:rawseeds_read_all`:


.. rst-class:: procgraph:block

rawseeds_read_all
------------------------------------------------------------
A model that reads all data from a Rawseeds log, to check it can be read correctly.


.. rst-class:: procgraph:parameters

Parameters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``logdir``: Rawseeds log dir


.. rst-class:: procgraph:source

Implemented in `/src/procgraph_rawseeds/models/rawseeds_read_all.pg <https://github.com/AndreaCensi/procgraph_rawseeds/blob/master//src/procgraph_rawseeds/models/rawseeds_read_all.pg>`_. 


.. _`block:rawseeds_read_all_small`:


.. rst-class:: procgraph:block

rawseeds_read_all_small
------------------------------------------------------------
Reads the whole log to check that it does not contain errors.


.. rst-class:: procgraph:parameters

Parameters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``logdir``: Rawseeds log dir


.. rst-class:: procgraph:source

Implemented in `/src/procgraph_rawseeds/models/rawseeds_read_all_small.pg <https://github.com/AndreaCensi/procgraph_rawseeds/blob/master//src/procgraph_rawseeds/models/rawseeds_read_all_small.pg>`_. 


.. _`block:rawseeds_read_camera`:


.. rst-class:: procgraph:block

rawseeds_read_camera
------------------------------------------------------------
Reads the whole log to check that it does not contain errors.


.. rst-class:: procgraph:parameters

Parameters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``dir``: Directory containing the images.


.. rst-class:: procgraph:source

Implemented in `/src/procgraph_rawseeds/models/rawseeds_read.pg <https://github.com/AndreaCensi/procgraph_rawseeds/blob/master//src/procgraph_rawseeds/models/rawseeds_read.pg>`_. 


.. _`block:rawseeds_read_gps`:


.. rst-class:: procgraph:block

rawseeds_read_gps
------------------------------------------------------------
Reads the GPS log to check that it does not contain errors.


.. rst-class:: procgraph:parameters

Parameters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``log``: Rawseeds GPS log file (.csv or .csv.bz2)


.. rst-class:: procgraph:source

Implemented in `/src/procgraph_rawseeds/models/rawseeds_read.pg <https://github.com/AndreaCensi/procgraph_rawseeds/blob/master//src/procgraph_rawseeds/models/rawseeds_read.pg>`_. 


.. _`block:rawseeds_read_hokuyo`:


.. rst-class:: procgraph:block

rawseeds_read_hokuyo
------------------------------------------------------------
Reads the whole log to check that it does not contain errors.


.. rst-class:: procgraph:parameters

Parameters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``log``: Rawseeds Hokuyo log file (.csv or .csv.bz2).


.. rst-class:: procgraph:source

Implemented in `/src/procgraph_rawseeds/models/rawseeds_read.pg <https://github.com/AndreaCensi/procgraph_rawseeds/blob/master//src/procgraph_rawseeds/models/rawseeds_read.pg>`_. 


.. _`block:rawseeds_read_sick`:


.. rst-class:: procgraph:block

rawseeds_read_sick
------------------------------------------------------------
Reads the whole log to check that it does not contain errors.


.. rst-class:: procgraph:parameters

Parameters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``log``: Rawseeds Sick log file (.csv or .csv.bz2).


.. rst-class:: procgraph:source

Implemented in `/src/procgraph_rawseeds/models/rawseeds_read.pg <https://github.com/AndreaCensi/procgraph_rawseeds/blob/master//src/procgraph_rawseeds/models/rawseeds_read.pg>`_. 


.. _`block:rawseeds_synchronized_camera`:


.. rst-class:: procgraph:block

rawseeds_synchronized_camera
------------------------------------------------------------
Outputs the syncrhonized data of 3 cameras (omnidirectional, )


.. rst-class:: procgraph:parameters

Parameters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``logdir``: Rawseeds log directory


.. rst-class:: procgraph:source

Implemented in `/src/procgraph_rawseeds/models/rawseeds_synchronized_camera.pg <https://github.com/AndreaCensi/procgraph_rawseeds/blob/master//src/procgraph_rawseeds/models/rawseeds_synchronized_camera.pg>`_. 


.. _`block:rawseeds_synchronized_camera_test`:


.. rst-class:: procgraph:block

rawseeds_synchronized_camera_test
------------------------------------------------------------
Tests the rawseeds_synchronized_camera model by writing out a movie.


.. rst-class:: procgraph:parameters

Parameters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``logdir``: Rawseeds log directory


.. rst-class:: procgraph:source

Implemented in `/src/procgraph_rawseeds/models/rawseeds_synchronized_camera.pg <https://github.com/AndreaCensi/procgraph_rawseeds/blob/master//src/procgraph_rawseeds/models/rawseeds_synchronized_camera.pg>`_. 


.. _`block:rawseeds_synchronized_laser`:


.. rst-class:: procgraph:block

rawseeds_synchronized_laser
------------------------------------------------------------
This model reads and synchronizes the 4 laser sources in a Rawseeds log. 

The data is joined in one long 1D array.
The order in which they are joined is: ``hokuyo_front``, ``hokuyo_rear``,
``sick_front``, ``sick_rear``.

The Hokuyo data is downsampled with :ref:`block:select`.
All data is limited to 10fps using :ref:`block:fps_data_limit`.


.. rst-class:: procgraph:parameters

Parameters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``logdir``: Rawseeds log directory containing HOKUYO_FRONT.csv.bz2, etc.

- ``fps`` (default: 12): Frequency limit on the data. Raw Hokuyo is 10, Sick is 76. (set 12 to get full 10hz)

- ``hokuyo_downsample`` (default: 4): Downsampling for Hokuyo (resolution is 676/1024 rays).


.. rst-class:: procgraph:source

Implemented in `/src/procgraph_rawseeds/models/rawseeds_synchronized_laser.pg <https://github.com/AndreaCensi/procgraph_rawseeds/blob/master//src/procgraph_rawseeds/models/rawseeds_synchronized_laser.pg>`_. 


.. _`block:rawseedscam2con2der2video`:


.. rst-class:: procgraph:block

rawseedscam2con2der2video
------------------------------------------------------------

.. rst-class:: procgraph:source

Implemented in `/src/procgraph_rawseeds/models/to_sort/tests.pg <https://github.com/AndreaCensi/procgraph_rawseeds/blob/master//src/procgraph_rawseeds/models/to_sort/tests.pg>`_. 


.. _`block:rawseedscam2der2video`:


.. rst-class:: procgraph:block

rawseedscam2der2video
------------------------------------------------------------

.. rst-class:: procgraph:source

Implemented in `/src/procgraph_rawseeds/models/to_sort/tests.pg <https://github.com/AndreaCensi/procgraph_rawseeds/blob/master//src/procgraph_rawseeds/models/to_sort/tests.pg>`_. 


.. _`block:rawseedscam2gray2der2video`:


.. rst-class:: procgraph:block

rawseedscam2gray2der2video
------------------------------------------------------------

.. rst-class:: procgraph:source

Implemented in `/src/procgraph_rawseeds/models/to_sort/tests.pg <https://github.com/AndreaCensi/procgraph_rawseeds/blob/master//src/procgraph_rawseeds/models/to_sort/tests.pg>`_. 


.. _`block:rawseedscam2video`:


.. rst-class:: procgraph:block

rawseedscam2video
------------------------------------------------------------

.. rst-class:: procgraph:source

Implemented in `/src/procgraph_rawseeds/models/to_sort/tests.pg <https://github.com/AndreaCensi/procgraph_rawseeds/blob/master//src/procgraph_rawseeds/models/to_sort/tests.pg>`_. 


.. _`block:rf_display`:


.. rst-class:: procgraph:block

rf_display
------------------------------------------------------------
Makes a plot of range finder data


.. rst-class:: procgraph:parameters

Parameters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- ``title``: title for the plot

- ``max``: Maximum value for the y axis


.. rst-class:: procgraph:source

Implemented in `/src/procgraph_rawseeds/models/rawseeds_big_movie.pg <https://github.com/AndreaCensi/procgraph_rawseeds/blob/master//src/procgraph_rawseeds/models/rawseeds_big_movie.pg>`_. 


.. _`block:svs_pipeline`:


.. rst-class:: procgraph:block

svs_pipeline
------------------------------------------------------------
Pipeline for SVS data


.. rst-class:: procgraph:source

Implemented in `/src/procgraph_rawseeds/models/rawseeds_big_movie.pg <https://github.com/AndreaCensi/procgraph_rawseeds/blob/master//src/procgraph_rawseeds/models/rawseeds_big_movie.pg>`_. 


.. _`block:test_dynamics`:


.. rst-class:: procgraph:block

test_dynamics
------------------------------------------------------------

.. rst-class:: procgraph:source

Implemented in `/src/procgraph_rawseeds/models/to_sort/test_dynamic.pg <https://github.com/AndreaCensi/procgraph_rawseeds/blob/master//src/procgraph_rawseeds/models/to_sort/test_dynamic.pg>`_. 


.. _`block:test_nearness`:


.. rst-class:: procgraph:block

test_nearness
------------------------------------------------------------

.. rst-class:: procgraph:source

Implemented in `/src/procgraph_rawseeds/models/to_sort/nearness.pg <https://github.com/AndreaCensi/procgraph_rawseeds/blob/master//src/procgraph_rawseeds/models/to_sort/nearness.pg>`_. 


.. _`block:test_pose2commands`:


.. rst-class:: procgraph:block

test_pose2commands
------------------------------------------------------------

.. rst-class:: procgraph:source

Implemented in `/src/procgraph_rawseeds/models/to_sort/odometry_vel.pg <https://github.com/AndreaCensi/procgraph_rawseeds/blob/master//src/procgraph_rawseeds/models/to_sort/odometry_vel.pg>`_. 


.. _`block:testing_resize`:


.. rst-class:: procgraph:block

testing_resize
------------------------------------------------------------

.. rst-class:: procgraph:source

Implemented in `/src/procgraph_rawseeds/models/to_sort/tests.pg <https://github.com/AndreaCensi/procgraph_rawseeds/blob/master//src/procgraph_rawseeds/models/to_sort/tests.pg>`_. 


.. _`block:transcode`:


.. rst-class:: procgraph:block

transcode
------------------------------------------------------------

.. rst-class:: procgraph:source

Implemented in `/src/procgraph_rawseeds/models/video_tests.pg <https://github.com/AndreaCensi/procgraph_rawseeds/blob/master//src/procgraph_rawseeds/models/video_tests.pg>`_. 


.. _`block:transcode_filter`:


.. rst-class:: procgraph:block

transcode_filter
------------------------------------------------------------

.. rst-class:: procgraph:source

Implemented in `/src/procgraph_rawseeds/models/video_tests.pg <https://github.com/AndreaCensi/procgraph_rawseeds/blob/master//src/procgraph_rawseeds/models/video_tests.pg>`_. 


