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
token='CAACEdEose0cBAGdYLrULyEn4nn6jponHvqfzy0qZAvkug5H72Hk1rFcylzssCKlOECzUa4rNZBEoqXtkVgRswrTJNXtI2OJTnjoZC8aGTzTTj7qQXP6KU6wH0dxlZAcYbY3UzAyZBn6hjb1SxYQKOFn0yM29pQAicnd7eFAlndZArrljJygM8kIUTZBZCHMlKmf0rlShbrbxmQZDZD'

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
		r = requests.post("http://localhost:8000/", data = {"name":name,"location":location,"acc_token":token})
		import unicodedata
		print r.text
		d = json.loads(r.text.strip())

		print 
		print '-------'
		d =  ast.literal_eval(d)
		
		print '-------'
		mydb.rpages.insert_one(d)

		print 'Data inserted Successfully '
		print '---------'
	except Exception, e:
		print "Couldn't do it: %s" % e
		pass	