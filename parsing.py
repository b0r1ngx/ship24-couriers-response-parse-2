import json

from utils import get_favicon

filename_full = 'resources/ship24_couriers_response.json'
filename_head = 'resources/ship24_couriers_response_head.json'

f = open(filename_head)
data = json.load(f)
couriers: list = data['data']['couriers']

total_websites = 0
icon_collected = 0
for courier in couriers:
    website = courier['website']
    total_websites += 1
    if website:
        courierName = courier['courierName']
        icon = get_favicon(website)
        print(f"website: {website}")
        print(f"courierName: {courierName}")
        print(f"icon: {icon}")
        icon_collected += 1

print(total_websites)
print(icon_collected)