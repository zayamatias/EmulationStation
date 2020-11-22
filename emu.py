#!/usr/bin/python2.7

import subprocess
import sys
import os
import signal

firstrun = True
defaultimage = '/home/pi/default.jpg'
process = subprocess.Popen('/home/pi/EmulationStation/emulationstation', stdout=subprocess.PIPE)
output = ''
lastimage = ''
pid = 0
if firstrun:
    command = ["fim","--device","7","-q","-w",defaultimage]
    proc2 = subprocess.Popen (command, stdin=subprocess.PIPE, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    lastimage = defaultimage
    output =''
    pid = proc2.pid
    firstrun = False
for c in iter(lambda: process.stdout.read(1), ''):  # replace '' with b'' for Python 3
   if c != '#':
      output = output+ c
   else:
      try:
         index = output.index(lastimage)
         output = output.replace(lastimage,'')
      except:
         index = 0
      if output != lastimage and output!='':
         if pid!=0:
            try:
               os.kill(pid, signal.SIGKILL) #or signal.SIGKILL
            except:
               index = 1
         if output == "UNKNOWN":
            output = defaultimage
         try:
            command = ["fim","--device","7","-q","-w",output]
            proc2 = subprocess.Popen (command, stdin=subprocess.PIPE, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
            lastimage = output
            output =''
            pid = proc2.pid
         except Exception as e:
            pid = 0
      else:
         index = 1
