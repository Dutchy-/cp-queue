#!/usr/bin/env python
import pygtk
pygtk.require('2.0')
import gtk

print("Creating the clipboard object")
clip=gtk.Clipboard()
print("Clipboard: %s" % str(clip) )
print("Copy a file before calling this script")
print("This is the file: %s" % str(clip.wait_for_text()) )
