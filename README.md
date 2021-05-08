```
Preqrequisite: Install python3  
pip3 install -r requirements.txt  
Change pincodes as desired 
Modify district id in line number 10 as well
curl to get district id

curl 'https://cdn-api.co-vin.in/api/v2/admin/location/districts/34' \
  -H 'authority: cdn-api.co-vin.in' \
  -H 'sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"' \
  -H 'accept: application/json, text/plain, /' \
  -H 'authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX25hbWUiOiJlMTk2NmVmNS04YTRmLTQ1ZDctODhjMi03Mjg5ZGQxZGE0NTQiLCJ1c2VyX2lkIjoiZTE5NjZlZjUtOGE0Zi00NWQ3LTg4YzItNzI4OWRkMWRhNDU0IiwidXNlcl90eXBlIjoiQkVORUZJQ0lBUlkiLCJtb2JpbGVfbnVtYmVyIjo5NTU5NDEzODcwLCJiZW5lZmljaWFyeV9yZWZlcmVuY2VfaWQiOjcwMTc4NTQ5MzUyMzkwLCJzZWNyZXRfa2V5IjoiYjVjYWIxNjctNzk3Ny00ZGYxLTgwMjctYTYzYWExNDRmMDRlIiwidWEiOiJNb3ppbGxhLzUuMCAoTWFjaW50b3NoOyBJbnRlbCBNYWMgT1MgWCAxMF8xNV83KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvOTAuMC40NDMwLjkzIFNhZmFyaS81MzcuMzYiLCJkYXRlX21vZGlmaWVkIjoiMjAyMS0wNS0wOFQxMjo0MTowNS44MDlaIiwiaWF0IjoxNjIwNDc3NjY1LCJleHAiOjE2MjA0Nzg1NjV9.mwlihJZjIashluXkzWJFACcdYG1r2MuUik_OXvC4EGE' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36' \
  -H 'origin: https://selfregistration.cowin.gov.in' \
  -H 'sec-fetch-site: cross-site' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-dest: empty' \
  -H 'referer: https://selfregistration.cowin.gov.in/' \
  -H 'accept-language: en-GB,en-US;q=0.9,en;q=0.8' \
  --compressed
python3 main.py
```
----
```
when slots are available it will play a song.
For testing, 
keep line 7: MIN_CAPACITY = 0
otherwise it should be the minimum number of people for which you want to book slots.
```
