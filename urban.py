import requests
import json
import sys

def urban(argv):
	if len(argv) == 2 and isinstance(argv[1], basestring):
		r = requests.get('http://api.urbandictionary.com/v0/define?term=' + argv[1])
		print '\n' + r.json()['list'][0]['definition'] + '\n'

if __name__ == "__main__":
	urban(sys.argv)