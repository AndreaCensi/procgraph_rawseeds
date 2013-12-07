from setuptools import setup, find_packages

setup(
    name="procgraph_rawseeds",
    version="1.0",
    package_dir={'': 'src'},
    packages=find_packages(),
   
    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    install_requires=['procgraph'],

    package_data={
        '': ['*.pg']
    },

    # metadata for upload to PyPI
    author="Andrea Censi",
    author_email="andrea@cds.caltech.edu",
    description="ProcGraph blocks to read the data from the Rawseeds project.",
    license="LGPL",
    keywords="procgraph rawseeds robot robotics logs camera rangefinder laser",
    url="https://github.com/AndreaCensi/procgraph_rawseeds",

)
