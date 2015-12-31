from django.shortcuts import render
from django.http import HttpResponse
from django.http import StreamingHttpResponse
from django.shortcuts import render
from task.models import SavedCache
from django.utils import timezone
from django.shortcuts import redirect
from facepy import GraphAPI
import json
from geopy.geocoders import Nominatim
import requests
from urllib import quote_plus as qp
import yaml	
import ast

# Create your views here.
def byteify(input):
    if isinstance(input, dict):
        return {byteify(key):byteify(value) for key,value in input.iteritems()}
    elif isinstance(input, list):
        return [byteify(element) for element in input]
    elif isinstance(input, unicode):
        return input.encode('utf-8')
    else:
        return input

def index(request):
	if request.method == 'GET':
		print 'test'
		return render(request,'task/index.html')
	elif request.method == 'POST':
		common = ['address','timing','latitude','AddressCountry','Og:type','zipcode','name','AddressRegion','longitude','source']
		print request.META['HTTP_USER_AGENT']
		name =  request.POST.get("name", "")
		location = request.POST.get("location", "")
		temp_location = location
		fbtoken = request.POST.get("fbtoken", "")
		gkey = request.POST.get("gkey", "")
		acc_token = fbtoken
		searched_data=''
		try:
			print 'heya in cache'
			searched_data = SavedCache.objects.filter(name=name,location=location)[0].data

			print 'Cached data, i am here'


			if 'Chrome' in request.META['HTTP_USER_AGENT']:
				#Browser
				d = searched_data
				d= ast.literal_eval(d)
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
				complete_map={'google':g_mapped,'facebook':fb_mapped,'common':common,'fb_uncommon':fb_uncommon,'g_uncommon':g_uncommon}
				fb_mapped['longitude'] = fb_mapped['longitude'][len("Decimal('"):-2]
				fb_mapped['latitude'] = fb_mapped['latitude'][len("Decimal('"):-2]
				fb_mapped['zipcode'] = fb_mapped['zipcode'][2:-1]	
				fb_mapped['address'] = fb_mapped['address'][2:-1]
				print facebook['name']

				return render(request,'task/temp_results.html',complete_map)
				pass
			else:	
				return StreamingHttpResponse(json.dumps(searched_data, sort_keys=True, indent=4, separators=(',', ': ')),   content_type='application/json')

		
		except Exception, e:
			print '---------'
			print searched_data
			print '---------'
			print "Couldn't do it: %s" % e
			print 'Damn'
			if 'lan:' in location:
				location = location.split(':')[1]
				print location
				lat = location.split(',')[0]
				lon = location.split(',')[1]
				location = lat+','+lon
				print 'lan: detected, formatted : ',location
			else:
				geolocator = Nominatim()
				location = geolocator.geocode(location,timeout=10)
				location = str(location.latitude)+','+str(location.longitude)

			if acc_token:
				graph = GraphAPI(acc_token)
			else:
				graph = GraphAPI('CAACEdEose0cBAKgyLsPPMIJy4ZB2UFIN3Q2a2XVgnqMY1ITNYyU6AQQCmQUBZAtNElA2NEkEl7R4ApavpbAf0QBoGY5MW3XD1kgPcpLhDYLqn3lQNA4Ih40mTFfgV7VjlWAPXZBY8R5EJdVTZCjJ84DVisSPJXfkKfgmhC0QWywjktClrQRNUNnGH22x96vmTxZBB8xBaBQZDZD')

			search=name
			search = qp(search)
			
			result = graph.get('search?type=place&q='+search+'&center='+location)
			page_id = result['data'][0]['id']

			params = 'fields=phone,likes,current_location,about,website,food_styles,description,hours,awards,price_range,location,booking_agent,is_verified,offers,public_transit,founded,products,emails,parking,phone,name'
			a =  str(page_id)+'?'+params
			cache={}
			cache['facebook'] = {}
			cache['google'] = {}

	 		cache['facebook'] = {'fb_page_url':'http://facebook.com/'+page_id}
	 		params = params.split(',')
	 		for each in params:
	 			try:
	 				cache['facebook'][each] = str(graph.get(a)[each]).encode('utf-8')
	 			except:
	 				pass		
	 		#Google Data
	 		if gkey:
	 			url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location='+location+'&radius=50000&name='+name+'&key='+gkey
	 		else:	
				url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location='+location+'&radius=50000&name='+name+'&key=AIzaSyDAERlVmOrLWdq0pHF5fK3c2cHmCSvy55I'
			r = requests.get(url)
			google_result = r.json()		
			cache['google']=google_result
			str_cache = str(cache)
			print name,location
			SavedCache.objects.create(name=name,location=temp_location,data = str_cache)
			if 'Chrome' in request.META['HTTP_USER_AGENT']:
				#Browser
				d = (str_cache)
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
					fb_mapped['phone'] = facebook['phone']
				except:
					pass
				try:			
					fb_location = yaml.safe_load(facebook['location'])
				except:
					pass	
				try:
					fb_mapped['state'] = fb_location['state']
				except:
					pass	
				try:
					fb_mapped['latitude'] = fb_location['latitude']
				except:
					pass
				try:
					fb_mapped['longitude'] = fb_location['longitude']
				except:
					pass
				try:
					fb_mapped['AddressCountry'] = fb_location['country']
				except:
					pass
				try:
					fb_mapped['city'] = fb_location['city']
				except:
					pass
				try:
					fb_mapped['address'] = fb_location['street']
				except:
					pass
				try:
					fb_mapped['zipcode'] = fb_location['zip']
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
				complete_map={'google':g_mapped,'facebook':fb_mapped,'common':common,'fb_uncommon':fb_uncommon,'g_uncommon':g_uncommon}

				return render(request,'task/temp_results.html',complete_map)
				pass
			else:
				return StreamingHttpResponse(json.dumps(str_cache, sort_keys=True, indent=4, separators=(',', ': ')),   content_type='application/json')

