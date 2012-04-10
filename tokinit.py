import OpenTokSDK

def get_session_token():
	api_key = '13652392' # Replace with your OpenTok API key.
	api_secret = 'ca0d3ebf52449ad8e3a89497eea96fe18c496076'  # Replace with your OpenTok API secret.
	session_address = 'presencerobot.appspot.com' # Replace with the representative URL of your session.
	opentok_sdk = OpenTokSDK.OpenTokSDK(api_key, api_secret, staging=True)
	session_properties = {OpenTokSDK.SessionProperties.p2p_preference: "enabled"}
	session = opentok_sdk.create_session(session_address, session_properties)
	connectionMetadata = 'username=Tian, userLevel=4'
	token = opentok_sdk.generate_token(session.session_id, None, None, connectionMetadata)
	return {"session":session.session_id, "token":token}
