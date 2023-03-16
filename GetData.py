# run raw-flight-data.sh to get the data

import json

with open('./airport_codes.json') as f:
    data = json.load(f)

# delete the unwanted data in data variable
for item in data:
    del item['nearby_airports_props']
    del item['is_no_airport_city']
    del item['is_multi_airport_city']
    del item['is_enabled']
    del item['weight']
    del item['weight_n']
    del item['nearby_airports']
    del item['has_nearby_airport']

data = sorted(data, key=lambda k: k['city'])

countries = []

for item in data:
    if item['country'] not in countries:
        countries.append(item['country'])


def returnAllData():
    # write data to ./Countries/all.json
    with open('./Countries/all.json', 'w') as f:
        # format the data and write it to the file
        json.dump(data, f, indent=4)


def countryWiseData():
    # write data of each country to ./Countries/<country>.json
    for country in countries:
        fileName = country.replace(' ', '_').lower().split("(")[0].strip()
        countryData = []
        for item in data:
            if item['country'] == country:
                countryData.append(item)

        # remove duplicate using id
        countryData = [dict(t) for t in {tuple(d.items()) for d in countryData}]

        with open('./Countries/' + fileName + '.json', 'w') as f:
            json.dump(countryData, f, indent=4)

countryWiseData()