|Downloads|

frate
=====

Measure file growing rate in real time.

Show the number of lines and KB per second the file is growing.

One useful use case is to monitor the "acess.log" of a webserver, to get a
estimative of requests per second.

Simple example::

    $ frate /var/log/nginx/access.log

    Lines: 195.0/s, Avg: 174.6/s | Write: 18.5KB/s, Avg: 16.5KB/s


Notes
=====

- Works on Python 2 and Python 3
- Uses only Python standard library for maximum compatibility


Install
=======

Install using pip::

    pip install frate

or

Download and set executable permission on the script file::

    chmod +x frate.py

or

Download and run using the python interpreter::

    python frate.py


Usage
=====

::

    Usage: frate file

    show file growing rate, 'control-c' to stop

    Options:
    --version   show program's version number and exit
    -h, --help  show this help message and exit


.. |Downloads| image:: https://pepy.tech/badge/frate
