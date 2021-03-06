#!/usr/bin/env python
#
# Author: Mike McKerns (mmckerns @caltech and @uqfoundation)
# Copyright (c) 1997-2016 California Institute of Technology.
# Copyright (c) 2016-2018 The Uncertainty Quantification Foundation.
# License: 3-clause BSD.  The full license text is available at:
#  - https://github.com/uqfoundation/pyina/blob/master/LICENSE

__doc__ = """
# An example of running ez_map to process a batch file
# BE VERY CAREFUL with this script, as it executes system calls. 
# To run:

python parallel_batch.py [batchfile.txt] [#nodes]
"""

def runshell(input):
    """
    This function just calls popen on the input string, and the stdout is printed.
    """
    import socket
    from subprocess import Popen, PIPE
    print "%s executing: %s" % (socket.gethostname(), input)
    pipe = Popen(input, shell=True, stdout=PIPE).stdout
    pipe.readlines()
    return 0

    
if __name__ == "__main__":

    import sys
    if len(sys.argv) > 2: nnodes = int(sys.argv[2])
    else: nnodes = 1

    try:
        from pyina.ez_map import ez_map

        batchfile = sys.argv[1]
        inputlist = []
        inputlist = open(batchfile).readlines()
        out = ez_map(runshell, inputlist, nodes=nnodes)
    except:
        print __doc__


# End of file
