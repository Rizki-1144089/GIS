import shapefile
r = shapefile.Reader("E:/Python/Rizki/rizki.shp")
shapes = r.shapes()
print len (shapes)