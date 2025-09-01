import json
import matplotlib.pyplot as plt
import os

# Get the directory of the current script
script_dir = os.path.dirname(__file__)
json_path = os.path.join(script_dir, 'decoyboardapp-locations.json')

# Load the JSON data
with open(json_path, 'r') as f:
    data = json.load(f)

lats = [gym['latitude'] for gym in data['gyms']]
lons = [gym['longitude'] for gym in data['gyms']]
names = [gym['name'] for gym in data['gyms']]

plt.figure(figsize=(10, 6))
plt.scatter(lons, lats)

for lon, lat, name in zip(lons, lats, names):
    plt.text(lon, lat, name, fontsize=8)

plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Climbing Gym Locations')
plt.grid(True)
plt.show()