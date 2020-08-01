# CTA Bus Tracker using a Raspberry Pi and an I2C LCD 16x2
I created a Python app that shows the estimated time the next bus will arrive at my stop onto an LCD 16x2 display.
The Python file is called `cta_tracker.py`

## CTA Bus Tracker API
I used CTA's Bus Tracker API to retrieve info about my local bus route and estimated arrival time at a specific bus stop.
To get your own API key go to this link: https://www.transitchicago.com/developers/bustracker/

## Installed Packages
Below are instructions on installing i2c-tools and python-smbus onto the Raspberry Pi OS:
`sudo apt-get install i2c-tools`
`sudo apt-get install python-smbus`

I found instructions on finding the I2C address at [CircuitBasics.com](https://www.circuitbasics.com/raspberry-pi-i2c-lcd-set-up-and-programming/)

I also 3D printed a case for the LCD from [Thingiverse](https://www.thingiverse.com/thing:3976921)


<Photos Here>


## Virtual Environment
* python3-venv https://www.techcoil.com/blog/how-to-use-python-3-virtual-environments-to-run-python-3-applications-on-your-raspberry-pi/
* https://docs.python.org/3/library/venv.html
`python3 -m venv ~/my_venv_folder`

To activate the environment:
`source ~/my_venv_folder/bin/activate`

ex install:
`pip install flask`

To exit environment:
`deactivate`

### Example JSON data from the CTA API Tracker
JSON error example:
```
{
	"bustime-response": {
		"error": [
			{
				"rt": "60",
				"stpid": "6339",
				"msg": "No arrival times"
			}
		]
	}
}
```
