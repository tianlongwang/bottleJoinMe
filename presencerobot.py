#!/usr/bin/env python
from bottle import route, run, request, template
import time
import tokinit
import os

#ip = "140.180.9.84"

@route('/control')
def control():
	new_state = request.GET.get('state', None)
	translate = {'w':'Moving Forward','x':'Moving Backward','a':'Turning Left','d':'Turning Right','s':'stop'};
	if new_state is not None:
		with open('./state','w') as fw:
			fw.write(new_state) 
	with open('./state','r') as f:
		state = f.read()
	description = translate[state]
	return template('./template.html', description=description)

@route('/value')
def value():
	with open('./state','r') as f:
		 state = f.read()
	return template('{{state}}', state=state)

@route('/')
@route('/video')
def video():
	session_token = tokinit.get_session_token()
	session = session_token['session']
	token = session_token['token']
	with open('./session','w') as fs:
		fs.write(session)
	with open('./token','w') as ft:
		ft.write(token)
	return template('./video.html',session=session,token=token)

@route('/session')
def session():
	with open('./session', 'r') as fsr:
		session = fsr.read()
	return session

@route('/token')
def token():	
	return tokinit.get_session_token()['token']

port = (os.environ.get("PORT", 5000))
run(host='0.0.0.0', port=port)
		
#run(server='gae')
#run(server='gevent', port=os.environ.get('PORT', 5000))
#run(host=ip, port=8080)
