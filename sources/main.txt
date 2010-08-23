
This module implements ProcGraph_ blocks for reading Rawseeds_ log files.

.. _ProcGraph: http://andreacensi.github.com/procgraph/
.. _Rawseeds: http://www.rawseeds.org/  

The development site is http://github.com/AndreaCensi/procgraph.

Install
-------

As simple as: ::

	$ easy_install -U procgraph_rawseeds

.. raw:: html
   :file: download.html


Usage
-----

There is a simple model called "RawseedsSynchornizedCamera" useful to do a quick check: ::
 
	--- model procgraph_rawseeds_test
	config logdir "Rawseeds log directory"
	
	|RawseedsSynchornizedCamera logdir=$logdir| --> y --> |mencoder file="out.avi"|


Blocks documentation
--------------------

See :ref:`pgdoc:procgraph_rawseeds`.

See :ref:`block:identity`.

 
