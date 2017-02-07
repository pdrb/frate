frate
=======

Python script to measure file growing rate in real time.

Show the number of lines and KB per second the file is growing.

One useful use case is to monitor the "acess.log" of a webserver, to get a
estimative of requests per second.

Install
-------

Install using pip:

::

    pip install frate

or

Download and set executable permission on the script file:

::

    chmod +x frate.py

or

Download and run using the python interpreter:

::

    python frate.py

Usage
-----

::

    Usage: frate file

    show file growing rate, 'control-c' to stop

    Options:
    --version   show program's version number and exit
    -h, --help  show this help message and exit

Examples
--------

Show growing rate of file "access.log":

::

    $ frate access.log

or use the complete path of file:

::

    $ frate /var/log/nginx/access.log


Notes
-----

- Works on Python 2
- Tested on Linux
