# python imports
import os.path
import sys
import re
from intelhex import IntelHex
from shutil import copyfile
import time


# Get the version variables passed as argument
if __name__ == '__main__':
    
    # Check for exact number of arguments
    # The script current directory and the 
    # the dragged file directory
    if(len(sys.argv) != 2):
        sys.exit(-1)

    BASE = os.path.dirname(os.path.abspath(sys.argv[0]))
    SOURCE_DIR = os.path.dirname(os.path.abspath(sys.argv[1]))

    # Check for different operating system slashes
    if '\\' in SOURCE_DIR:
        SOURCE_FNAME = sys.argv[1].split('\\')[-1]
    elif '/' in SOURCE_DIR:
        SOURCE_FNAME = sys.argv[1].split('/')[-1]


    t = time.localtime(time.time())

    bf_year = "%.2d" %(t.tm_year - 2000)
    bf_month = "%.2d" %(t.tm_mon)
    bf_mday = "%.2d" %(t.tm_mday)
    bf_hour = "%.2d" %(t.tm_hour)
    bf_min = "%.2d" %(t.tm_min)

    TIME_STAMP = bf_year + bf_month + bf_mday + bf_hour + bf_min    # This will be addressed later -

    # Refactor the file name with the time stamp
    if '.' in SOURCE_FNAME:
        EXTENSION = SOURCE_FNAME.split('.')[-1]
        DEST_FNAME = SOURCE_FNAME.split('.' + EXTENSION)[0] + '_' + TIME_STAMP + '_' + '.' + EXTENSION
    else:
        DEST_FNAME = SOURCE_FNAME + TIME_STAMP
    
    #print "\n\n"
    #print BASE
    #print SOURCE_DIR
    #print SOURCE_FNAME
    #print DEST_FNAME
    #print TIME_STAMP
    #print "\n\n"

    SOURCE_PATH = os.path.join(SOURCE_DIR, SOURCE_FNAME)
    DEST_PATH = os.path.join(SOURCE_DIR, DEST_FNAME)

    #print SOURCE_PATH
    #print DEST_PATH


    try:

        copyfile(SOURCE_PATH, DEST_PATH)

    except:
        print "## - !!!!!!Couldn't rename " + sys.argv[1]


    