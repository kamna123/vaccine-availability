import requests
import json
import time
import datetime
import sys
import os

MIN_CAPACITY = 1
DESIRED_PIN_CODES = [560076, 560062, 560020, 560078, 560001, 560017, 560027, 560064, 560071, 560084, 560011, 560030];
MIN_AGE_LIMIT = 18
START_DATE=8
END_DATE=14

HEADERS = {
  'authority': 'cdn-api.co-vin.in',
  'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
  'accept': 'application/json, text/plain, */*',
  'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX25hbWUiOiJlMTk2NmVmNS04YTRmLTQ1ZDctODhjMi03Mjg5ZGQxZGE0NTQiLCJ1c2VyX2lkIjoiZTE5NjZlZjUtOGE0Zi00NWQ3LTg4YzItNzI4OWRkMWRhNDU0IiwidXNlcl90eXBlIjoiQkVORUZJQ0lBUlkiLCJtb2JpbGVfbnVtYmVyIjo5NTU5NDEzODcwLCJiZW5lZmljaWFyeV9yZWZlcmVuY2VfaWQiOjcwMTc4NTQ5MzUyMzkwLCJ1YSI6Ik1vemlsbGEvNS4wIChNYWNpbnRvc2g7IEludGVsIE1hYyBPUyBYIDEwXzE1XzcpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS85MC4wLjQ0MzAuOTMgU2FmYXJpLzUzNy4zNiIsImRhdGVfbW9kaWZpZWQiOiIyMDIxLTA1LTA1VDE3OjAyOjU0Ljk3M1oiLCJpYXQiOjE2MjAyMzQxNzQsImV4cCI6MTYyMDIzNTA3NH0.B9Zg_R7w4TDz-ib18W57TzoWoYvho67zrjg9TBO9w8Y',
  'sec-ch-ua-mobile': '?0',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
  'content-type': 'application/json',
  'origin': 'https://selfregistration.cowin.gov.in',
  'sec-fetch-site': 'cross-site',
  'sec-fetch-mode': 'cors',
  'sec-fetch-dest': 'empty',
  'referer': 'https://selfregistration.cowin.gov.in/',
  'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8'
}

def canBook(center, session):
  #print('center', center)
  if center.get('pincode') not in DESIRED_PIN_CODES:
    return False
  #and session.get('vaccine') == 'COVISHIELD':
  #print('center={}, available_capacity={}, min_age_limit={}'.format(center, session.get('available_capacity'), session.get('min_age_limit')))
  if session.get('available_capacity') >= MIN_CAPACITY and session.get('min_age_limit') == MIN_AGE_LIMIT: 
    return True
  return False

def playSong():
  print('playing............')
  os.system('open ./song.mp3')

lastPlayed = datetime.datetime(1970,1,1)

def checkAvailability():
  for day in range(START_DATE, END_DATE + 1, 1):
    time.sleep(1)
    dayStr = str(day)
    if len(dayStr) == 1:
      dayStr = '0' + dayStr
    url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/calendarByDistrict?district_id=294&date={}-05-2021".format(dayStr)

    payload={}
    response = requests.request("GET", url, headers=HEADERS, data=payload)
    
    json_data = response.text
    #print('json_data', json_data)
    data = {}
    try:
        data = json.loads(json_data)
    except:
        print('error in parsing json data, json_data={}'.format(json_data))
        continue
    if 'centers' not in data:
      continue
    global lastPlayed
    print('centers found={}'.format(len(data.get('centers'))))
    for center in data.get('centers'):
      for session in center.get('sessions'):
        if canBook(center, session):
          print('Try booking at center name={}, pincode={}, available_capacity={}'.format(center.get('name'), center.get('pincode'), session.get('available_capacity')))
          curTime = datetime.datetime.now()
          diff = (curTime - lastPlayed).total_seconds()
          #print('curTime={}, lastPlayed={}, diff={}'.format(curTime, lastPlayed, diff))
          if diff > 120:
            lastPlayed =  datetime.datetime.now()
            playSong()

while True:
    checkAvailability()
    time.sleep(5)
