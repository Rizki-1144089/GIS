#!/bin/python

import shapefile

sf = shapefile.Reader("D:/POLTEKPOS/Semester 5/GIS/Pertemuan4/negara.shp")
print sf
shapes = sf.shapes()
print len(shapes)

#for name in dir(shapes[3]):
#		if not name.startswitch('__'):
#				print name
