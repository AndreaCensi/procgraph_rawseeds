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

