import os
import urllib.request
import json
import datetime
import I2C_LCD_driver
from time import *

mylcd = I2C_LCD_driver.lcd()

padding = " " * 16

mylcd.lcd_clear()

api_key = os.environ.get('CTA_BUS_API_KEY')
 
while True:
    url = 'http://ctabustracker.com/bustime/api/v2/getpredictions?key=' + api_key + '&rt=60&stpid=6339&format=json'
    req = urllib.request.Request(url)

    data_dump = urllib.request.urlopen(req).read()
    parsed_json = json.loads(data_dump)

    current_time = datetime.datetime.now().strftime('%m/%d, %I:%M%p') 

    # Next steps: try checking of key is not 'error' then continue

    try:
        date = datetime.datetime.strptime(parsed_json['bustime-response']['prd'][0]['prdtm'], '%Y%m%d %H:%M')
        route = 'Route: ' + parsed_json['bustime-response']['prd'][0]['rt'] + ' ' +  parsed_json['bustime-response']['prd'][0]['rtdir']
        bus_stop = 'Stop: ' + parsed_json['bustime-response']['prd'][0]['stpnm']
        predicted_arrival = 'Arrival: ' + datetime.datetime.strftime(date, '%I:%M%p')
        destination = parsed_json['bustime-response']['prd'][0]['des']
        print(route)
        print(bus_stop)
        print(predicted_arrival)
        print(current_time)
        print(destination)
    except:
        print(parsed_json)
        route = 'Waiting for Route Data...'
        bus_stop = 'Waiting for Latest Bus Data...'
        predicted_arrival = 'Waiting for Arrival Data...'
        destination = 'Waiting for Destination Data...'
    finally:
        # Scroll Text
        for x in range(10):

            mylcd.lcd_display_string(current_time, 1)
            mylcd.lcd_display_string(predicted_arrival, 2)
            sleep(10)

            mylcd.lcd_display_string(route,1)
            mylcd.lcd_display_string(bus_stop,2)
            sleep(1)

            # Scroll Right to Left First Line
            for i in range (0, len(route)-16+1):
                mylcd.lcd_display_string(padding,1)
                line1 = route[i:len(route)]
                mylcd.lcd_display_string(line1,1)
                sleep(0.1)

            # Scroll Right to Left Second Line
            for i in range (0, len(bus_stop)-16+1):
                mylcd.lcd_display_string(padding,2)
                line2 = bus_stop[i:len(bus_stop)]
                mylcd.lcd_display_string(line2,2)
                sleep(0.1)
            sleep(2)
            mylcd.lcd_clear()

            # Scroll Destination
            mylcd.lcd_display_string('Destination:',1)
            mylcd.lcd_display_string(destination,2)
            sleep(2)
            for i in range (0, len(destination)-16+1):
                line2 = destination[i:len(destination)]
                mylcd.lcd_display_string(line2,2)
                sleep(0.1)
            sleep(5)


    sleep(30)
    mylcd.lcd_clear()

# while True:
#     for i in range (0, len(long_string)):
#         lcd_text = long_string[i:(i+16)]
#         mylcd.lcd_display_string(lcd_text, 2)
#         sleep(0.4)
#         mylcd.lcd_display_string(str_pad,2)
