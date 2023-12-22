import requests
response = requests.get('https://etip.exodus-privacy.eu.org/trackers/export')

data = response.json()

code_signatures = [tracker['code_signature'] for tracker in data['trackers']]

trackers = []
for signatures in code_signatures:
    signatures = signatures.split('|')
    for signature in signatures:
        trackers.append(signature)
custom = open('CustomTrackers.txt')
trackers.extend(custom)

custom.close()

activities = open('adhell3_activities.txt', "w")
providers = open('adhell3_providers.txt', "w")
receivers = open('adhell3_receivers.txt', "w")
services = open('adhell3_services.txt', "w")
for tracker in trackers:
    activities.write(tracker + '\n')
    providers.write(tracker + '\n')
    receivers.write(tracker + '\n')
    services.write(tracker + '\n')

print("Wrote " + str(len(trackers)) + " trackers to files")