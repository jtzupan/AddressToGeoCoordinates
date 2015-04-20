


#command line arguments should specify the input and ouput file
#
import sys
import csv
import urllib2
import xml.etree.ElementTree as et
csv.field_size_limit(sys.maxsize)

if len(sys.argv) == 3:
    file_In = sys.argv[1]
    file_Out = sys.argv[2]


fileIn = open(file_In, 'rb')
fileOut = open(file_Out, 'wb')
fw = csv.writer(fileOut)

fw.writerow(['Address','Lat','Long'])

#program steps
#open the list of address from the file

#iterate through the file
#for each line of the file, the program should
# 1 - format the address into the format required for the api call
# 2 - concatenate the base url + address + api key
# 3 - append the lat and long of the address to the specified output file


htmlBase = 'https://maps.googleapis.com/maps/api/geocode/xml?address='
api = ''

for line in fileIn:

    finalAddress =  line.rstrip('\r\n').replace('"', '')
    us =  htmlBase + line.rstrip('\r\n').replace(' ', '+') + api
    finalURL = us.replace('"', '')
    #print finalURL

    try:
        tree = et.parse(urllib2.urlopen(finalURL)) 
    except: 
        fw.writerow([line])
    try:
        for e in tree.findall('/result/geometry/location/lat'):
            lat = e.text
        for e in tree.findall('/result/geometry/location/lng'):
            long = e.text
    except:
        lat = 'no info'
        long = 'no info'
    fw.writerow([finalAddress, lat, long])

fileOut.close()
