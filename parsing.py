import json

from utils import parse_html_to_scratch_favicon, save_favicon_as_png

filename_full = 'resources/ship24_couriers_response.json'
filename_head = 'resources/ship24_couriers_response_head.json'
filename_problem = 'resources/ship24_couriers_response_problem.json'

f = open(filename_full)
data = json.load(f)
couriers: list = data['data']['couriers']


total_websites = 0
icon_collected = 0
errors: list[str] = []
swift_code: dict[str, str] = {}

for courier in couriers:
    website = courier['website']
    total_websites += 1
    if not website:
        continue

    courierName = courier['courierName']
    icon = parse_html_to_scratch_favicon(website)
    print(f"courierName: {courierName}")
    print(f"icon: {icon}\n")
    if not icon:
        continue

    isSaved = save_favicon_as_png(icon, courierName)
    if isSaved:
        swift_code[courierName] = courierName
        icon_collected += 1
    else:
        errors.append(courierName)

print('total: ', total_websites)
print('collected: ', icon_collected)
print(errors)
print(swift_code)

