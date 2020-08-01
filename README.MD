# CTA Bus Tracker using a Raspberry Pi and an I2C LCD 16x2
I created a Python app that shows the estimated time the next bus will arrive at my stop onto an LCD 16x2 display.

<Photos Here>

## Virtual Environment
* python3-venv https://www.techcoil.com/blog/how-to-use-python-3-virtual-environments-to-run-python-3-applications-on-your-raspberry-pi/

## I2C Tools
https://www.circuitbasics.com/raspberry-pi-i2c-lcd-set-up-and-programming/
sudo apt-get install i2c-tools
sudo apt-get install python-smbus

## Using venv for python3 virtual environment
Documentation: https://docs.python.org/3/library/venv.html
python3 -m venv ~/my_venv_folder

To activate the environment:
source ~/my_venv_folder/bin/activate

ex install:
pip install flask

To exit environment:
deactivate



		
		
## CTA Tracker API project
`cta_tracker.py`

### Pictures

### JSON data
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
