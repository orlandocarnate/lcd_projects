# CTA Bus Tracker using a Raspberry Pi and an I2C LCD 16x2
A CTA Bus Tracker LCD Display using CTA's Bus Tracker API, Python, Raspberry Pi 3, and I2C LCD 16x2 Display.

## About
A CTA Bus Tracker app `cta_tracker.py` written in Python that displays information on a I2C LCD Display. 
This device displays:
* Current Time
* Route and Direction
* Stop Location
* Estimated time of arrival
* Final stop destination

## CTA Bus Tracker API
I used CTA's Bus Tracker API to retrieve info about my local bus route and estimated arrival time at a specific bus stop.
To get your own API key go to this link: https://www.transitchicago.com/developers/bustracker/

## Installed Packages
Below are instructions on installing i2c-tools and python-smbus onto the Raspberry Pi OS:
`sudo apt-get install i2c-tools`
`sudo apt-get install python-smbus`

I found instructions on finding the I2C address at [CircuitBasics.com](https://www.circuitbasics.com/raspberry-pi-i2c-lcd-set-up-and-programming/)

I also 3D printed a case for the LCD from [Thingiverse](https://www.thingiverse.com/thing:3976921)


## Notes
Parameters needed for the URL query string:
* key = API Key
* rt = Route
* stpid = Bus Stop id
* format = JSON

The response keys used:
* rtdir = Route direction
* des = last bus stop
* prdtm = Predicted time of arrival to bus stop stpid

### Virtual Environment
* python3-venv https://www.techcoil.com/blog/how-to-use-python-3-virtual-environments-to-run-python-3-applications-on-your-raspberry-pi/
* https://docs.python.org/3/library/venv.html
`python3 -m venv ~/my_venv_folder`

To activate the environment:
`source ~/my_venv_folder/bin/activate`

ex install:
`pip install flask`

To exit environment:
`deactivate`

### Example JSON response from the CTA Bus Tracker API
```
http://ctabustracker.com/bustime/api/v2/getpredictions?key=YOUR_API_KEY_HERE&rt=60&stpid=6339&format=json

{
	"bustime-response": {
		"prd": [
			{
				"tmstmp": "20200801 17:57",
				"typ": "A",
				"stpnm": "Blue Island & 15th Street",
				"stpid": "6339",
				"vid": "1663",
				"dstp": 16216,
				"rt": "60",
				"rtdd": "60",
				"rtdir": "Eastbound",
				"des": "Randolph/Harbor Dr",
				"prdtm": "20200801 18:19",
				"tablockid": "60 -205",
				"tatripid": "1032776",
				"dly": false,
				"prdctdn": "21",
				"zone": ""
			}
		]
	}
}
```

### JSON Error Example
```
{
	"bustime-response": {
		"error": [
			{
				"stpid": "6339",
				"msg": "No arrival times"
			}
		]
	}
}
```
