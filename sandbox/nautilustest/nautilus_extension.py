#!/usr/bin/env python
# symlink this to ~/.local/share/nautilus-python/extensions
# and restart nautilus
from gi.repository import Nautilus, GObject


class SimplePasteExtension(GObject.GObject, Nautilus.MenuProvider):
    def __init__(self):
        pass

	# the 'activate' action
    def menu_activate_cb(self, menu, file):
        print("menu_activate_cb",file)

    def get_file_items(self, window, files):
        if len(files) != 1:
            return
        
        file = files[0]

		# construct the item
        item = Nautilus.MenuItem(
            name="SimplePasteExtension::Show_File_Name",
            label="Showing %s" % file.get_name(),
            tip="Showing %s" % file.get_name()
        )
		# add a function to the 'activate' action
        item.connect('activate', self.menu_activate_cb, file)
        
        return [item]

#SimplePasteExtension().get_file_items('bla', ['bla'])
