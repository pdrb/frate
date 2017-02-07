#!/usr/bin/python

# frate 0.1
# author: Pedro Buteri Gonring
# email: pedro@bigode.net
# date: 07/02/2017

import time
import sys
import optparse
import os


version = '0.1'


# Parse and validate arguments
def get_parsed_args():
    usage = 'usage: %prog file'
    # Create the parser
    parser = optparse.OptionParser(
        description="show file growing rate, 'control-c' to stop",
        usage=usage, version=version
    )

    # Print help if no argument is given
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(2)

    # Parse the args
    (options, args) = parser.parse_args()

    # Some args validation
    if len(args) != 1:
        parser.error('incorrect number of arguments')
    return (options, args)


# Main CLI
def cli():
    (options, args) = get_parsed_args()

    filename = args[0]
    total_lines = 0

    if os.path.isfile(filename):
        try:
            file = open(filename, 'r')
        except Exception, ex:
            print ex
            sys.exit(1)
    else:
        print '\nerror: %s is not a file' % filename
        sys.exit(1)

    sys.stdout.write('\n')

    # Set the cursor to the end of file
    file.seek(0, 2)
    # Save the starting reading position
    start_read_pos = file.tell()
    # Start timer
    start_time = time.time()

    while True:
        time.sleep(1)
        # Last position read
        file_last_pos = file.tell()
        # Used to calculate time spent reading
        init_read_time = time.time()
        # Read file and save the number of lines
        line_count = len(file.readlines())
        # Total reading time
        read_time = time.time() - init_read_time
        # Calculate the numbers of lines read per sec
        lines_per_sec = line_count / (read_time + 1)
        # Update the total number of lines read
        total_lines += line_count
        # Calculate the elapsed time since the beginning
        elapsed_time = time.time() - start_time
        # Average lines per sec
        lines_average = total_lines / elapsed_time
        # Write per sec in KB
        size_rate = (file.tell() - file_last_pos) / (read_time + 1) / 1024
        # Write average in KB
        size_average = ((file.tell() - start_read_pos) / elapsed_time) / 1024
        # '\r\x1b[K' == '\r'    Carriage Return
        #               '\x1b[' Control Sequence Initiator
        #               'K'     EL - Erase in Line
        sys.stdout.write(
            '\r\x1b[KLines: %.1f/s, Avg: %.1f/s '
            '| Write: %.1fKB/s, Avg: %.1fKB/s'
            % (lines_per_sec, lines_average, size_rate, size_average)
        )
        sys.stdout.flush()


# Run cli function if invoked from shell
if __name__ == '__main__':
    try:
        cli()
    except KeyboardInterrupt:
        print '\nQuit.\n'
        sys.exit(0)
