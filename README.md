# adhell3-components-exodus
Simple python script that generates adhell3 file for components batch operation based on exodus database and a bit from custom one

## Support
Lists use partial names (starting or ending with), so to make them work, there is a need for [appropriate changes](https://gitlab.com/B.O.S.S/adhell3/-/commit/de5d618e943c940dfed759c27a8c7b0f551c0f54). As for now, they are not in the [official version](https://gitlab.com/fusionjack/adhell3), but they are available on [my fork](https://gitlab.com/B.O.S.S/adhell3)

## Download
You can download files for batch operation from the repo files or artifact from Actions tab. 

GitHub Action automatically runs update every new month and updates files

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

Trackers are obtained from [Exodus Database](https://reports.exodus-privacy.eu.org), specifically from url https://etip.exodus-privacy.eu.org/trackers/export

They are also merged with `CustomTrackers.txt`

## Customization
* You can add your own components to `CustomTrackers.txt`, they will be added to the generated files
* To make "lite" version of components use `-l` or `--lite` argument. This version exclude trackers that have set `is_in_exodus` to `false`. These trackers are not listed in [Exodus Database](https://reports.exodus-privacy.eu.org)

# Credits
Thanks to [steveglowplunk](https://xdaforums.com/m/steveglowplunk.6944590/) for creating [this post](https://xdaforums.com/t/script-disable-tracking-services-version-1-8.4099469/) from which I could get custom tracker list and the api url for exodus database
