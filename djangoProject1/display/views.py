import json

from django.shortcuts import render
import requests


def index(request):
    response = requests.get("https://api-v3.mbta.com/predictions?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=departure_time&include=schedule%2Ctrip&filter%5Bdirection_id%5D=0&filter%5Bstop%5D=place-north")
    # r = response.json()
    r = response.json()
    rr = r['data']
    rr_included = r['included']
    print(r['data'])

    class Data:
        def __init__(self, time, destination, train, status):
            self.time = time
            self.destination = destination
            self.train = train
            self.status = status

    final = []
    for i in range(0, 10):
            time = rr_included[i + 10]["attributes"]["departure_time"]
            destination = rr_included[i]["attributes"]["headsign"]
            train = rr_included[i]["attributes"]["name"]
            status = rr[i]["attributes"]["status"]
            data = Data(time, destination, train, status)
            final.append(data)

    return render(request, 'index.html', {'response': final})