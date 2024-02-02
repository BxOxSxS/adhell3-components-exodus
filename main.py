import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-l', '--lite', action='store_true')
args = parser.parse_args()

response = requests.get('https://etip.exodus-privacy.eu.org/trackers/export')

data = response.json()

trackers = []
for tracker in data['trackers']:
    if args.lite and not tracker['is_in_exodus']:
        continue
    signatures = tracker['code_signature'].split('|')
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
