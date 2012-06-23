#!/usr/bin/env python
from bottle import route, run, request, template
import time
import tokinit
import os

#ip = "140.180.9.84"

@route('/control')
def control():
	new_state = request.GET.get('state', None)
	translate = {'w':'Moving Forward','x':'Moving Backward','a':'Turning Left','d':'Turning Right','s':'Stop Moving','r':'Looking Up','f':'Looking Down'};
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

@route('/generate')
def generate():
	session_token = tokinit.get_session_token()
	session = session_token['session']
	token = session_token['token']
	with open('./session','w') as fs: 
		fs.write(session)
	with open('./token','w') as ft: 
		ft.write(token)
	return 'generate session and token successful'

@route('/')
@route('/video')
def video():
	with open('./session','r') as fs:
		session = fs.read()
	with open('./token','r') as ft:
		token = ft.read()
	return template('./video.html',session=session,token=token)

@route('/session')
def session():
	with open('./session', 'r') as fsr:
		session = fsr.read()
	return session

@route('/token')
def token():	
	with open('./token','r') as fs:
		token = fs.read()
	return token


port = (os.environ.get("PORT", 5000))
run(host='0.0.0.0', port=port)
		
#run(server='gae')
#run(server='gevent', port=os.environ.get('PORT', 5000))
#run(host=ip, port=8080)
