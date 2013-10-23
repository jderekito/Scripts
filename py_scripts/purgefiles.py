#!/usr/bin/python
# author: jdmorgan@unca.edu
# date: 10/2011
# python version: 2.7
# usage:  purgefiles.py -t DATETIME -d NDAYS FILE1 [ FILE2 ... ]
#          purgefiles.py -t 2011-14 -d 2 FileOne
#    where DATETIME is a string representing a date and/or time, N is a
#    number representing a number of days, and FILE1, FILE2, ...  are the
#    names of files.
#    The program deletes any of the files FILE1, FILE2, ... that
#    are more than N days older than DATETIME
# To run in cmd prompt on Windows: C:\Data\Python>C:\Python27\python.exe purgefiles.py -t 2011-12 -d 2 FileOne
import os, sys
import re
import optparse
import datetime

#.....................................................
#YYYYMMDDHHmmss
def FormatDate (filename):
    retDateStr = ""
    #YY
    if len(filename)==4:
        retDateStr = filename + "0101000000"
    #MM
    if len(filename)==6:
        retDateStr = filename + "01000000"
    #DD
    if len(filename)==8:
        retDateStr = filename + "000000"
    #HH
    if len(filename)==10:
        retDateStr = filename + "0000"        
    #mm
    if len(filename)==12:
        retDateStr = filename + "00"            
    #ss
    if len(filename)==14:
        retDateStr = filename            
    return retDateStr
#-------------------------------------------------------

#Verify input args   
parser = optparse.OptionParser()
parser.add_option('-t', help='mandatory date_time arg', dest='dateTime', type="string")
parser.add_option('-d', help='mandatory days_older file_name', dest='days', type="string")
(opts, args) = parser.parse_args()

if opts.dateTime is None:
   print "A mandatory param dateTime is missing\n"
   parser.print_help()
   exit(-1)
else:
   DATETIME = opts.dateTime

if opts.days is None:
   print "A mandatory param days is missing\n"
   parser.print_help()
   exit(-1)
else:
   NDAYS = opts.days

#get the files in the current directory
path = os.getcwd()
listing = os.listdir(path) 
 
for argfile in args: #loop through input filename args  
    print argfile + ' being processed for DATETIME: ' +  DATETIME
    for curfile in listing: #loop through files in current directory
        if curfile.find(argfile) != -1: #check if the current file matches the argfile param name
            print curfile + ' current file being checked...'
            print re.sub("\D", "", curfile) + ' digits from current file being checked'
            print re.sub("\D", "", DATETIME) + ' digits from DATETIME being checked'
            curFileDate = FormatDate (re.sub("\D", "", curfile))
            inArgDate = FormatDate (re.sub("\D", "", DATETIME))
            print curFileDate + ' curFileDate...'
            print inArgDate + ' inArgDate...'
            dt1 = datetime.datetime.strptime(curFileDate, '%Y%m%d%H%M%S')
            dt2 = datetime.datetime.strptime(inArgDate, '%Y%m%d%H%M%S')
            if dt1 < dt2:
               print "'%s' comes before '%s'" % (dt1,dt2)
            else:
               print "'%s' comes on or after '%s'" % (dt1,dt2)
            dt2minusNDAYS = dt2 - datetime.timedelta(int(NDAYS))
            print NDAYS +" days before '%s' is '%s'" % (dt2, dt2minusNDAYS)
            if dt1 < dt2minusNDAYS:
                print "delete this file!!!!!!"
