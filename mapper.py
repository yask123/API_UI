import requests
import ast 
import json
token=''
import yaml


name= 'starbucks'
location='new york'
url = 'http://127.0.0.1:8000/'+token
r = requests.post("http://localhost:8000/", data = {"name":name,"location":location,"fbtoken":token})
d = json.loads(r.text.strip())


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




