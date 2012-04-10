#!/usr/bin/env python
from bottle import route, run, request, template
import time
import tokinit
import os

#ip = "140.180.9.84"

@route('/control')
def control():
	new_state = request.GET.get('state', None)
	if new_state is not None:
		with open('./state','w') as fw:
			fw.write(new_state) 
	with open('./state','r') as f:
		state = f.read()
	return template('./template.html', state=state)

@route('/value')
def value():
	with open('./state','r') as f:
		 state = f.read()
	return template('{{state}}', state=state)

@route('/')
@route('/video')
def video():
	return template('./video.html')

@route('/session')
def session():
	return tokinit.get_session_token()['session']

@route('/token')
def token():	
	return tokinit.get_session_token()['token']

port = (os.environ.get("PORT", 5000))
run(host='0.0.0.0', port=port)
		
#run(server='gae')
#run(server='gevent', port=os.environ.get('PORT', 5000))
#run(host=ip, port=8080)
