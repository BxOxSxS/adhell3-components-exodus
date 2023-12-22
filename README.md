# adhell3-components-exodus
Simple python script that generates adhell3 file for components batch operation based on exodus database and a bit from custom one
## Usage
### Install python
Follow [official guide](https://wiki.python.org/moin/BeginnersGuide/Download)

### Install requirements
```bash
pip install -r requirements.txt
```


### Run script
```bash
python3 main.py
```
The script will generate 4 files:
 - `adhell3_activities.txt`
 - `adhell3_providers.txt`
 - `adhell3_receivers.txt`
 - `adhell3_services.txt`

Trackers are obtained from [Exodus Database](https://reports.exodus-privacy.eu.org), specyfically from url https://etip.exodus-privacy.eu.org/trackers/export

There are also merged with `CustomTrackers.txt`

You can also simply download the latest one in the repo

## Customization
You can add your own components to `CustomTrackers.txt`, they will be added to the generated files

# Credits
Thanks to [steveglowplunk](https://xdaforums.com/m/steveglowplunk.6944590/) for creating [this post](https://xdaforums.com/t/script-disable-tracking-services-version-1-8.4099469/) from which I could get custom tracker list and the api url for exodus database
