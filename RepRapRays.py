import re
import fileinput
import sys
import os.path
import shutil

#=============================================================================================
# RepRapRays.py modifies reprap gcode files to control a laser
# It strips out E-values and replaces them with laser off commands and adds laser on commands
# v0.1, written by Alan McKiernan (amk), GPL2 licence
#=============================================================================================

#getting the name of the file to process and checking that the file is there
print ' '
print '===RepRapRays.py takes a reprap gcode file, makes a copy, strips out E-values and replaces them with laser off commands and adds laser on commands==='
if len(sys.argv) != 2: 
        print 'Usage: python RepRapRays.py <filename.gcode>' 
        sys.exit() 
else:
  inFilename = sys.argv[1] #source Gcode filename

if os.path.isfile(inFilename) == 0:
  print inFilename,
  print "could not be found"
  sys.exit()

#create a copy of the Gcode file -> this is the one that will be processed
outFilename = inFilename[:-6] + "_LASER.gcode"
shutil.copyfile(inFilename,outFilename)
file = outFilename
print "Processing ", inFilename,
print " to output ", file

#Here are the laser on/off M-codes
#####------> Change to suit your setup (M107/M107 are usually RepRap fan on/off commands!)
laser_on = "M106\n"
laser_off = "\nM107"

#Here is the section that strips out the E-values and replaces them with laser on/off commands
for line in fileinput.input(file, inplace=1):
   m = re.search(r"E[0-9]+[\S]*", line) #searches line for E-value
   if m:
     if m.group() in line:
       line = laser_on + line   #add laser_on to start of line
       line=line.replace(m.group(),laser_off) #replace E-value with laser_off
   print line,
print "all done, happy 'lasering'!"
print ' '
   





