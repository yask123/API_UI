import requests
import ast 
import json
token='CAACEdEose0cBAH5ih8LK5os7FzsQuns4XTfdisa6GJMW2eLakqcevLYA6W2ibheTogRl4XAkXRsHz7JbRLKEk62i4SrwZBCB2FWjW5Mb22ZAZCcfxG3sz5rsBD7L3yuQzqKeuwr5xixW2Nl5puFZCgGpO3FLWY5WvOphzPzTi0chXZBdoqYZA484IIyjigsJPUqcsK8YZBMVgZDZD'
import yaml
'''
address
timing
latitude
address_2
Og:image
Og:image:width
AddressCountry
Og:type
Lunch
cuisines
zipcode
known_for
name
Og:image:height
Outdoor Seating
AddressRegion
Og:title
longitude
source
'''

'''
Facebook
website
parking
hours --> timing 
phone
location['city'] --> 
location['zip'] -->
location['country'] --> 
location['longitude'] -> longitude
location['latitude'] -> latitude
fb_page_url 
is_verified
pagelikes 
'''

'''
Google
rating
name
geometry['location']['lat']
geometry['location']['lng']
opening_hours --> timing 
address -> vicinity 
photos['width'] --> Og:image:width
photos['height'] --> Og:image:height 
types
icon
'''





























name= 'starbucks'
location='new york'
url = 'http://127.0.0.1:8000/'+token
r = requests.post("http://localhost:8000/", data = {"name":name,"location":location,"fbtoken":token})
d = json.loads(r.text.strip())
d =  ast.literal_eval(d)



google = d['google']['results']
facebook = d['facebook']
fb_location = yaml.safe_load(facebook['location'].strip())
fb_new_loc={}
for each in fb_location:
	print each.replace('u','')[1:-1] 
exit()
for each in fb_location:
	print each.replace('u','')[1:]
exit()	
if bool(each.replace('u','')[1:-1] == 'state'):
	fb_new_loc['state'] = fb_location[each]	
elif bool(each.replace('u','')[1:-1] == 'latitude'):		
	fb_new_loc['latitude'] = fb_location[each]
	print 'sdadasdasd'
elif bool(each.replace('u','')[1:-1] == 'longitude'):		
	fb_new_loc['longitude'] = fb_location[each]
elif bool(each.replace('u','')[1:-1] == 'street'):		
	fb_new_loc['street'] = fb_location[each]
elif bool(each.replace('u','')[1:-1] == 'zip'):		
	fb_new_loc['zip'] = fb_location[each]
elif bool(each.replace('u','')[1:-1] == 'city'):		
	fb_new_loc['city'] = fb_location[each]				
print fb_new_loc['latitude']	
exit()


'''
rating
name
reference
geometry
opening_hours
place_id
vicinity
photos
scope
id
types
icon

u'state'   u'NY'
u'latitude'   Decimal('40.7294388')
u'longitude'   Decimal('-73.9874725')
u'zip'   u'100035703'
u'city'   u'New York'
u'street'   u'145 2nd Ave'
u'country'   u'United States'
'''

g_mapped={}
g_mapped['address']=google[0]['vicinity']
g_mapped['name'] = google[0]['name']
g_mapped['timing'] = google[0]['opening_hours']
g_mapped['longitude'] = google[0]['geometry']['location']['lng']
g_mapped['latitude'] = google[0]['geometry']['location']['lat']
g_mapped['Og:image'] = google[0]['photos'][0]['photo_reference']
g_mapped['Og:image:height'] = google[0]['photos'][0]['height']
g_mapped['Og:image:width'] = google[0]['photos'][0]['width']
g_mapped['types'] = google[0]['types']
g_mapped['icon'] = google[0]['icon']
g_mapped['rating'] = google[0]['rating']


fb_mapped={}








fb_location = yaml.safe_load(facebook['location'])


fb_mapped['website'] = facebook['website']
fb_mapped['fb_page_url'] = facebook['fb_page_url']
fb_mapped['fb_page_likes'] = facebook['likes']
fb_mapped['parking'] = facebook['parking']
fb_mapped['fbpage_is_verified'] = facebook['is_verified']
fb_mapped['parking'] = facebook['parking']
fb_mapped['phone'] = facebook['phone']
fb_mapped['state'] = fb_location['state']
fb_mapped['latitude'] = fb_location['latitude']
fb_mapped['longitude'] = fb_location['longitude']
fb_mapped['AddressCountry'] = fb_location['country']
fb_mapped['city'] = fb_location['city']
fb_mapped['address'] = fb_location['street']
fb_mapped['zipcode'] = fb_location['zip']	
complete_map={}
complete_map={'google':g_mapped,'facebook':fb_mapped}




