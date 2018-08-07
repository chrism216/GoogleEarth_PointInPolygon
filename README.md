# Google Earth Pro: Find out which points are inside which polygons.

You probably arrived here from [this thread](https://www.mrexcel.com/forum/excel-questions/828554-google-earth-determine-points-inside-polygon-using-coordinates.html?highlight=google+earth+points+polygons) in MrExcel.com. The thread had so many views that I imagined there might be some people interested in a Python version of this. So, here it is.

## Instructions

1. Install Python 3.x and the pandas library
2. Draw your points and polygons in Google Earth Pro. Save all of it in a file named PP.kml (save everything under one folder -> right click -> "Save place as"). Save it in the same directory as the python script. Do __not__ use the .kmz format.
3. With your command line, navigate to the directory where you saved both the python script and PP.kml, and run the script using:
```
python PointInPolygon.py
```
4. The program will produce a file named PP.csv file in that directory, containing a table detailing which points are inside which polygons.

__Alternatively, here's the [Excel file](https://www.mrexcel.com/forum/redirect-to/?redirect=https%3A%2F%2Fwww.dropbox.com%2Fs%2F707qslttz428v6w%2FPointInPolygon.xlsm%3Fdl%3D0).__

Sample files are included (PP.kml and PP.csv), so you can demo this.
