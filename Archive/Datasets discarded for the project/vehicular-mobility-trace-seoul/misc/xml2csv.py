import xml.etree.ElementTree as ET
import csv

tree = ET.parse('OpenStreetMap Trace for a Dense Traffic.xml.xml')  # replace with your file path
root = tree.getroot()

# open a file for writing
with open('dense.csv', 'w', newline='') as out_csv:
    writer = csv.writer(out_csv)
    writer.writerow(["time", "id", "x", "y", "angle", "type", "speed", "pos", "lane", "slope"])

    for timestep in root.findall('timestep'):
        time = timestep.get('time')
        for vehicle in timestep.findall('vehicle'):
            id = vehicle.get('id')
            x = vehicle.get('x')
            y = vehicle.get('y')
            angle = vehicle.get('angle')
            type = vehicle.get('type')
            speed = vehicle.get('speed')
            pos = vehicle.get('pos')
            lane = vehicle.get('lane')
            slope = vehicle.get('slope')
            writer.writerow([time, id, x, y, angle, type, speed, pos, lane, slope])
