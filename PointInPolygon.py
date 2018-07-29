import pandas as pd
import numpy as np
from lxml import etree


#Function that checks if a point is inside polygon
def point_in_polygon(row, path):
    return path.contains_point([row['longitude'], row['latitude']])


tree = etree.ElementTree(file='PP.kml')
xmlns = '{http://www.opengis.net/kml/2.2}'

#Parse all Polygons
polygon_data = []
for _, parent in enumerate(tree.findall('//%sPolygon/..' %xmlns)):
    polygon_name = parent.find('%sname' %xmlns).text
    coordstr = parent.find('.//%scoordinates' %xmlns).text.strip().split(' ')
    for point_num, pointstr in enumerate(coordstr):
        pointlist = pointstr.split(',')
        longitude = float(pointlist[0])
        latitude = float(pointlist[1])
        vertex_data = [point_num, polygon_name, longitude, latitude]
        polygon_data.append(vertex_data)

df_poly = pd.DataFrame(polygon_data, index=np.arange(len(polygon_data)), columns=['point_num', 'polygon_name', 'longitude', 'latitude'])

#Parse all Points
point_data = []
for parent in tree.findall('.//%sPoint/..' %xmlns):
    point_name = parent.find('.//%sname' %xmlns).text
    coordstr = parent.find('.//%scoordinates' %xmlns).text.strip()
    pointlist = coordstr.split(',')
    longitude = float(pointlist[0])
    latitude = float(pointlist[1])
    point_data.append([point_name, longitude, latitude])

df_points = pd.DataFrame(point_data, index=np.arange(len(point_data)), columns=['Name', 'longitude', 'latitude'])

#Calculate if points are inside polygon
for polygon_name in df_poly.polygon_name.unique():
    polygon = df_poly[df_poly.polygon_name == polygon_name][['longitude', 'latitude']]
    polygon_path = path.Path(polygon)
    df_points[polygon_name] = df_points.apply(point_in_polygon, path=polygon_path, axis=1)

#Dump to CSV
df_points.to_csv('PP.csv', index=False)
