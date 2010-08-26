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

Module ``procgraph_rawseeds``
============================================================


Routines for reading the data from the Rawseeds project.

.. _`block:RawseedsCam`:

Block ``RawseedsCam``
------------------------------------------------------------
This model reads the images of a Rawseed camera log.

.. _`block:RawseedsCamFiles`:

Block ``RawseedsCamFiles``
------------------------------------------------------------
This block reads the filenames for the Rawseeds camera log.

.. _`block:RawseedsGPS`:

Block ``RawseedsGPS``
------------------------------------------------------------
This block reads the GPS log from Rawseeds format.


Example: ::

    1223309581.123667, $GPGGA,143516.80,4530.37118644,N,00909.99763524,E,2,6,1.7,131.984,M,48.022,M,0.8,0000*7
    1223309581.133660, $GPGST,143516.80,0.504,0.238,0.147,54.6,0.212,0.183,0.585*6

We ignore the GPGST lines for now.

.. _`block:RawseedsHokuyo`:

Block ``RawseedsHokuyo``
------------------------------------------------------------
This block reads a Hokuyo log in Rawseeds format.


File format: ::

    Timestamp [seconds.microseconds]
    R1..R681* Ranges [m]

.. _`block:RawseedsOdo`:

Block ``RawseedsOdo``
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

.. _`block:RawseedsRF`:

Block ``RawseedsRF``
------------------------------------------------------------
This block reads a range-finder log in Rawseeds format.


File format: ::

    Timestamp [seconds.microseconds]
    # of ranges [unitless]
    Angular offset [1/4 degree]
    R1..R181 Ranges (zero padded to 181 ranges) [m]

.. _`block:camera_display`:

Block ``camera_display``
------------------------------------------------------------
.. _`block:camera_expectation`:

Block ``camera_expectation``
------------------------------------------------------------
.. _`block:camera_filters`:

Block ``camera_filters``
------------------------------------------------------------
.. _`block:camera_video`:

Block ``camera_video``
------------------------------------------------------------
.. _`block:compression_test`:

Block ``compression_test``
------------------------------------------------------------
.. _`block:decode`:

Block ``decode``
------------------------------------------------------------
.. _`block:gray_pipeline`:

Block ``gray_pipeline``
------------------------------------------------------------
.. _`block:master`:

Block ``master``
------------------------------------------------------------
.. _`block:rangefinder_display`:

Block ``rangefinder_display``
------------------------------------------------------------
.. _`block:rawseeds_big_movie`:

Block ``rawseeds_big_movie``
------------------------------------------------------------
Creates a big movie file displaying all data

.. _`block:rawseeds_display_all`:

Block ``rawseeds_display_all``
------------------------------------------------------------
.. _`block:rawseeds_odometry`:

Block ``rawseeds_odometry``
------------------------------------------------------------
.. _`block:rawseeds_read_all`:

Block ``rawseeds_read_all``
------------------------------------------------------------
A model that reads all data from a Rawseeds log, to check it can be read correctly.

.. _`block:rawseeds_read_all_small`:

Block ``rawseeds_read_all_small``
------------------------------------------------------------
Reads the whole log to check that it does not contain errors.

.. _`block:rawseeds_read_camera`:

Block ``rawseeds_read_camera``
------------------------------------------------------------
Reads the whole log to check that it does not contain errors.

.. _`block:rawseeds_read_gps`:

Block ``rawseeds_read_gps``
------------------------------------------------------------
Reads the GPS log to check that it does not contain errors.

.. _`block:rawseeds_read_hokuyo`:

Block ``rawseeds_read_hokuyo``
------------------------------------------------------------
Reads the whole log to check that it does not contain errors.

.. _`block:rawseeds_read_sick`:

Block ``rawseeds_read_sick``
------------------------------------------------------------
Reads the whole log to check that it does not contain errors.

.. _`block:rawseeds_synchronized_camera`:

Block ``rawseeds_synchronized_camera``
------------------------------------------------------------
Outputs the syncrhonized data of 3 cameras (omnidirectional, )

.. _`block:rawseeds_synchronized_camera_test`:

Block ``rawseeds_synchronized_camera_test``
------------------------------------------------------------
Tests the rawseeds_synchronized_camera model by writing out a movie.

.. _`block:rawseeds_synchronized_laser`:

Block ``rawseeds_synchronized_laser``
------------------------------------------------------------
This model reads and synchronizes the 4 laser sources in a Rawseeds log.


The order in which they are joined is: ``hokuyo_front``, ``hokuyo_rear``, ``sick_front``, ``sick_rear``.

The Hokuyo data is downsampled with :ref:`block:select`.
All data is limited to 10fps using :ref:`block:fps_data_limit`.

.. _`block:rawseedscam2con2der2video`:

Block ``rawseedscam2con2der2video``
------------------------------------------------------------
.. _`block:rawseedscam2der2video`:

Block ``rawseedscam2der2video``
------------------------------------------------------------
.. _`block:rawseedscam2gray2der2video`:

Block ``rawseedscam2gray2der2video``
------------------------------------------------------------
.. _`block:rawseedscam2video`:

Block ``rawseedscam2video``
------------------------------------------------------------
.. _`block:rf_display`:

Block ``rf_display``
------------------------------------------------------------
Makes a plot of range finder data

.. _`block:svs_pipeline`:

Block ``svs_pipeline``
------------------------------------------------------------
Pipeline for SVS data

.. _`block:test_dynamics`:

Block ``test_dynamics``
------------------------------------------------------------
.. _`block:test_nearness`:

Block ``test_nearness``
------------------------------------------------------------
.. _`block:test_pose2commands`:

Block ``test_pose2commands``
------------------------------------------------------------
.. _`block:testing_resize`:

Block ``testing_resize``
------------------------------------------------------------
.. _`block:transcode`:

Block ``transcode``
------------------------------------------------------------
.. _`block:transcode_filter`:

Block ``transcode_filter``
------------------------------------------------------------