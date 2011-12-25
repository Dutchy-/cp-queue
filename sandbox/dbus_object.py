#!//usr/bin/env python

print("Setting up the main loop")
from dbus.mainloop.glib import DBusGMainLoop

DBusGMainLoop(set_as_default=True)

print("Connecting to the bus")
import dbus
s = dbus.SessionBus()


def test_object():
	try:
		# this gets the proxy
		s.get_object('org.iapps.cpqueue', '/org/iapps/cpqueue/main')
		print(str(s))
	except ValueError:
		print("The object did not exist!")

print("Getting a nonexisting object")
test_object()

print("Creating a new python class to export")
import dbus.service
class TestExport(dbus.service.Object):
	def __init__(self, path):
		bus_name = dbus.service.BusName('org.iapps.cpqueue', bus=dbus.SessionBus())
		dbus.service.Object.__init__(self, bus_name, path)

test = TestExport('/org/iapps/cpqueue/main')
test_object()

exit()
