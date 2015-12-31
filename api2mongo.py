from pymongo import MongoClient
import requests
import json 
import yaml
import collections
import ast

myclient = MongoClient()
mydb = myclient['test']

def recurse(d):
  if type(d)==type({}):
    for k in d:
      recurse(d[k])
  else:
    print d,'*'

def byteify(input):
    if isinstance(input, dict):
        return {byteify(key):byteify(value) for key,value in input.iteritems()}
    elif isinstance(input, list):
        return [byteify(element) for element in input]
    elif isinstance(input, unicode):
        return input.encode('utf-8')
    else:
        return input       

client = MongoClient('54.86.28.234')
db = client['db_crawl']
cursor = db.rpages.find({'mining':'1'})
token='CAACEdEose0cBAEUxrAkPDlCZBQjlrEZBRa0CwgwSIJ9pNrV97xrZAXDkun3bKWEPlQF15AE4PvI6IcUgTWZCAepBfvWE1ORm7TsRlliEwx2aTEbhoVFxEMcWtqBsAbCFZASuK1tBhWeWxTjYfhgw3ZBVtDnqgVB1sWpni1HpaZAejdMOu1nV7fb19ptmvMj8e7yicCZB2gepVgZDZD'
common = ['address','timing','latitude','AddressCountry','Og:type','zipcode','name','AddressRegion','longitude','source']

for each in cursor:
	try:
		print '---------'
		name = each['data']['name']
		#print 'name:',each['data']['name']
		#print 'latitude: ',each['data']['latitude']
		lat = each['data']['latitude']
		lon = each['data']['longitude']
		#print 'longitude: ',each['data']['longitude']
		location = 'lan:'+lat+','+lon
		r = requests.post("http://localhost:8000/", data = {"name":name,"location":location,"fbtoken":token})
		import unicodedata
		print r.text
		d = json.loads(r.text.strip())

		print '-------'
		d =  ast.literal_eval(d)
		google = d['google']['results']
		facebook = d['facebook']
		g_mapped={}
		fb_mapped={}

		for each in common:
			g_mapped[each]=''
		for each in common:
			fb_mapped[each]=''

		try:
			g_mapped['address']=google[0]['vicinity']
		except:
			pass
		try:
			g_mapped['name'] = google[0]['name']
		except:
			pass
		try:
			g_mapped['timing'] = google[0]['opening_hours']
		except:
			pass
		try:
			g_mapped['longitude'] = google[0]['geometry']['location']['lng']
		except:
			pass
		try:
			g_mapped['latitude'] = google[0]['geometry']['location']['lat']
		except:
			pass
		try:
			g_mapped['Og:type'] = google[0]['types']
		except:
			pass	
		try:
			g_mapped['Og:image'] = google[0]['photos'][0]['photo_reference']
			g_mapped['Og:image:height'] = google[0]['photos'][0]['height']
			g_mapped['Og:image:width'] = google[0]['photos'][0]['width']
		except:
			pass	
		

		
		try:
			g_mapped['types'] = google[0]['types']
		except:
			pass
		try:
			g_mapped['icon'] = google[0]['icon']
		except:
			pass
		try:
			g_mapped['rating'] = google[0]['rating']
		except:
			pass
		try:
			fb_mapped['website'] = facebook['website']
		except:
			pass	
		try:				
			fb_mapped['fb_page_url'] = facebook['fb_page_url']
		except:
			pass
		try:				
			fb_mapped['fb_page_likes'] = facebook['likes']
		except:
			pass
		try:				
			fb_mapped['fbpage_is_verified'] = facebook['is_verified']
		except:
			pass
		try:
			fb_mapped['parking'] = facebook['parking']
		except:
			pass
		try:
			fb_mapped['name'] = facebook['name']
		except:
			pass	
		try:
			fb_mapped['phone'] = facebook['phone']
		except:
			pass
		try:			
			fb_location = yaml.safe_load(facebook['location'].strip())
		except:
			pass
		for each in fb_location:
			try:
				if bool(each.replace('u','')[1:-1] == 'state'):
					fb_mapped['state']  = fb_location[each]	
				elif bool(each.replace('u','')[1:-1] == 'latitde'):		
					fb_mapped['latitude'] = fb_location[each]
				elif bool(each.replace('u','')[1:-1] == 'longitde'):		
					fb_mapped['longitude'] = fb_location[each]
				elif bool(each.replace('u','')[1:-1] == 'street'):		
					fb_mapped['address'] = fb_location[each]
				elif bool(each.replace('u','')[1:-1] == 'zip'):		
					fb_mapped['zipcode'] = fb_location[each]
				elif bool(each.replace('u','')[1:-1] == 'city'):		
					fb_mapped['city'] = fb_location[each]
				elif bool(each.replace('u','')[1:-1] == 'country'):		
					fb_mapped['AddressCountry'] = fb_location[each]
			except:
				pass					
		
		complete_map={}
		fb_uncommon=[]
		g_uncommon=[]
		for each in fb_mapped:
			if each not in common:
				fb_uncommon.append(each)
		for each in g_mapped:
			if each not in common:
				g_uncommon.append(each)	
		fb_mapped['source'] = 'Facebook Pages'
		g_mapped['source'] = 'Google Places API'			
		fb_mapped['longitude'] = fb_mapped['longitude'][len("Decimal('"):-2]
		fb_mapped['latitude'] = fb_mapped['latitude'][len("Decimal('"):-2]
		fb_mapped['zipcode'] = fb_mapped['zipcode'][2:-1]	
		fb_mapped['address'] = fb_mapped['address'][2:-1]
		complete_map={'google':g_mapped,'facebook':fb_mapped}

		print '-------'
		mydb.rpages.insert_one(complete_map)

		print 'Data inserted Successfully '
		print '---------'
	except Exception, e:
		print "Couldn't do it: %s" % e
		pass	
