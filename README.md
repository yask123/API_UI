
# Documentation 
A Web app and an API to crawl, index restaurant facebook pages and google places data.


### API End Point
```http://localhost:8000/ ```


To request data for the given query: 

###Required Parameters


* Facebook access token `fbtoken`

* Google API key `gkey` (Optional)

* Name of the restaurant `name`

* Location of restaurant `location`:

    Format (For City/State/Country) : `Delhi`

    Format (For latitude/longitude) : `lan:28.6139,77.2090`

### Example

```python
import requests

r = requests.post("http://localhost:8000/", data = {"name":name,"location":location,"fbtoken":token})
d = json.loads(r.text.strip())
```
### Response
```javascript

{
  'google': {
    u'status': u'OK',
    u'next_page_token': u'CoQC_gAAAKmR5ZdHrCzA5YxxXNE7V9Ku0CSuLfE5IqC_F-HrG7CVtPtdnS5Jtj101bk2apPGTHZrNlX_mSJfSmGuDMlaoUDS21vIuqc9wqjTbu0airMpTR-tlE_nSXYVayysNuwPXfpyWAaI1Cp0cZ7MSXFk0cG3BmTZKtGGgLyrMw_6kWQp62GJI8qEWTE_jFpk_pMUvfV_9UUrM36XaukYXXuvVvRFE6CGDTXz7AjmIF9T8ZNDi8N2Bc3eKDYGtCjxNYDYekiNcMZs2X8pmNX0h2PwOn_9ykc1QDiRX_eCryI2LyvRHT_R3-iC3jYz1-jNSsEVdn_TE4F1rD54xo5qWk1avQcSEHbnE583sF5dkWRbLicZ6xgaFDEraGYkl309epfbDoOiX0UM-Fdy',
    u'html_attributions': [
      
    ],
    u'results': [
      {
        u'rating': 4,
        u'name': u'Starbucks',
        u'reference': u'CmRcAAAAi9s2DPwxabDznD4SEzfNhT57CIoS0tJQrsVUmGGgTzdb0y_VUXHEIUoSED50BUmCcTUs0blEOGNWQjBmstTbdM73tze7dsR9AJbnsz8HdM-yTtaMj7xoDKThRUCvwI_FEhCJtGky-DbtljKuj7JB15wEGhTiTB1yrwAMwiSfwYPuj62bPHWRjw',
        u'price_level': 2,
        u'geometry': {
          u'location': {
            u'lat': 40.719354,
            u'lng': -73.9898599
          }
        },
        u'opening_hours': {
          u'weekday_text': [
            
          ],
          u'open_now': False
        },
        u'place_id': u'ChIJvVFW2YZZwokRca6P_hbHpmY',
        u'vicinity': u'80 Delancey Street, New York',
        u'photos': [
          {
            u'photo_reference': u'CmRdAAAAjYPcQ7Eyaix4lrHzWsMIW6ol_gn1jxW3Gz1qaLsIi4VbQ3vQ2unWIr1Pueo8OQ2_Ei9QHv05ZXKnVuvDu2w5mPdBoLHSr_4crvJP5-4aBVqu17QpfVFUYo_peCcxuq4GEhCSQUs4qajtQCwzf-GXc3rdGhRRNzrwl1o1bwVl1-_Ho7c9zKXaiA',
            u'width': 4320,
            u'html_attributions': [
              u'<a href="https://maps.google.com/maps/contrib/106905294470212349895/photos">David Sonenberg</a>'
            ],
            u'height': 2432
          }
        ],
        u'scope': u'GOOGLE',
        u'id': u'e493b381c69f56b47a2a616193d1138d930310ed',
        u'types': [
          u'cafe',
          u'food',
          u'store',
          u'point_of_interest',
          u'establishment'
        ],
        u'icon': u'https://maps.gstatic.com/mapfiles/place_api/icons/cafe-71.png'
      },
      ......
    ]
  },
  'facebook': {
    'website': 'www.starbucks.com ',
    'name': 'Starbucks',
    'parking': "{u'street': 0, u'lot': 0, u'valet': 0}",
    'hours': "{u'sun_1_close': u'22:30', u'sat_1_close': u'23:00', u'sun_1_open': u'07:00', u'fri_1_close': u'23:00', u'thu_1_open': u'06:00', u'tue_1_close': u'23:00', u'sat_1_open': u'06:30', u'mon_1_open': u'06:00', u'mon_1_close': u'23:00', u'wed_1_open': u'06:00', u'wed_1_close': u'23:00', u'tue_1_open': u'06:00', u'fri_1_open': u'06:00', u'thu_1_close': u'23:00'}",
    'phone': '(212) 780-0027',
    'location': "{u'city': u'New York', u'zip': u'100035703', u'country': u'United States', u'longitude': Decimal('-73.9874725'), u'state': u'NY', u'street': u'145 2nd Ave', u'latitude': Decimal('40.7294388')}",
    'fb_page_url': u'http://facebook.com/149957095031686',
    'is_verified': 'False',
    'likes': '244'
  }
}
```
### API2Mongo Python Helper Script
  

