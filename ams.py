import requests
from time import sleep
from geopy.distance import geodesic as GD

# source =(59.33111 , 18.057)
# target =(59.33111 , 18.059)
# print("The distance between Abuja and Dakar is: ", GD(source,target).m)

SANDBOX_NAME = 'ams'
API_ADDR = f'http://IP_Address/{SANDBOX_NAME}'

x = 18.056134
y = 59.33111

x_max = 18.059
x_min = 18.057

ue = "term1"
flag = 0



speed = input('Please enter speed (m/s) for UE: ')



data = {
  "assetName": ue,
  "assetType": "UE",
  "subType": "UE",
  "location": {
    "type": "Point",
    "coordinates": [x, y]
  },
  "radius": 100,
  "path": {
    "type": "LineString",
    "coordinates": [ [x_min, y], [x_max, y] ]
  },
  "eopMode": "LOOP",
  "velocity": int(speed)
}



r = requests.post(f'{API_ADDR}/gis/v1/automation/MOBILITY?run=true', json=data)
# if r.status_code != 200:
#     print(f'Mobility Error {r.status_code}')
# else:
#     print('Mobility is OK')   



step = ((int(speed) / 5) * 0.002) / 114

while True:
    if flag == 0 and data['location']['coordinates'][0] < x_max:
        data['location']['coordinates'][0] = data['location']['coordinates'][0] + step
    else:
        flag = 1
           
    if flag == 1 and data['location']['coordinates'][0] > x_min:
        data['location']['coordinates'][0] = data['location']['coordinates'][0] - step
    else:
        flag = 0
    
    s = f'{API_ADDR}/gis/v1/geodata/{ue}'
 
    #start = time.perf_counter()
    response = requests.post(f'{API_ADDR}/gis/v1/geodata/{ue}', json=data)
    #request_time = time.perf_counter() - start
    #print(request_time, "secs.")
    
    sleep(0.02)
   
    #if response.status_code != 200:
     #   print(f'Error in updating GIS data for {ue} code: {response.status_code}')
    #else:
     #   print('location updated')