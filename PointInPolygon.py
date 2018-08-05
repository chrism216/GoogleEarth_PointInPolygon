import pandas as pd
from lxml import etree
from matplotlib import path


tree = etree.ElementTree(file='PP.kml')
xmlns = '{http://www.opengis.net/kml/2.2}'

#Parse all Points
point_data = []
for parent in tree.findall('.//%sPoint/..' % xmlns):
    point_name = parent.find('.//%sname' % xmlns).text
    coordstr = parent.find('.//%scoordinates' % xmlns).text.strip()
    longitude, latitude, *_ = map(float, coordstr.split(','))
    point_data.append([point_name, longitude, latitude])

df_points = pd.DataFrame(point_data, columns=['Name', 'longitude', 'latitude'])

#Parse all Polygons
for parent in tree.findall('//%sPolygon/..' % xmlns):
    polygon_name = parent.find('%sname' % xmlns).text
    coordinates = parent.find('.//%scoordinates' % xmlns).text.strip().split(' ')
    
    polygon_data = []
    for pointstr in coordinates:
        longitude, latitude, *_ = map(float, pointstr.split(','))
        polygon_data.append((longitude, latitude))

    #Test points, add results to dataframe
    polygon = path.Path(polygon_data)
    df_points[polygon_name] = polygon.contains_points(df_points[['longitude', 'latitude']])

#Dump to CSV
df_points.to_csv('PP.csv', index=False)
print("Done!")
