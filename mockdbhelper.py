MOCK_USERS = [{'email': 'test@example.com', 
					'salt': '8Fb23mMNHD5Zb8pr2qWA3PE9bH0=', 
					'hashed': '1736f83698df3f8153c1fbd6ce2840f8aace4f200771a46672635374073cc876cf0aa6a31f780e576578f791b5555b50df46303f0c3a7f2d21f91aa1429ac22e'}, 
					{'email': 'test2@example.com', 
					'salt': '8Fb23mMNHD5Zb8pr2qWA3PE9bH0=', 
					'hashed': '1736f83698df3f8153c1fbd6ce2840f8aace4f200771a46672635374073cc876cf0aa6a31f780e576578f791b5555b50df46303f0c3a7f2d21f91aa1429ac22e'}]
					
MOCK_MESSAGES = [{'_id': '1', 'message': 'First test message', 'enc_message': '1e29117a973ef8531e2c509ba4f8036ab7c31825d3e99cd27eac094a21ed64b9c8abccb932a10a0f028ca5d378e45450768b0038f4fdaf953c8d1ce2036808c2', 'owner': 'test@example.com', 'reciever': 'test2@example.com'},
					  {'_id': '2', 'message': 'Second test message', 'enc_message': '97df7b1f8d103caecaeb690222b6c2c60941fc095db65be306c4b6339763c711f5d50b1a80d99057f8f3b6918278101588819b84483acb2184ff1e19923ec2e4' , 'owner': 'test2@example.com', 'reciever': 'test@example.com'}]

class MockDBHelper:
	def get_user(self, email):
		user = [x for x in MOCK_USERS if x.get('email') == email]
		if user:
			return(user[0])
		return(None)
	
	def add_user(self, email, salt, hashed):
		MOCK_USERS.append({"email": email, "salt": salt, "hashed":hashed})
	
	def add_message(self, reciever, message, enc_message, owner):
		MOCK_MESSAGES.append({'_id': str(len(MOCK_MESSAGES) + 1), 'message': message, 'enc_message': enc_message,'owner': owner, 'reciever': reciever})
		return(str(len(MOCK_MESSAGES) + 1))
	
	def get_messages(self, owner_id):
		messages = []
		for message in MOCK_MESSAGES:
			if message.get('owner') == owner_id:
				messages.append(message)
		return(messages)
	
	def get_dashboard_messages(self, owner_id):
		messages = []
		for message in MOCK_MESSAGES:
			if message.get('reciever') == owner_id:
				messages.append(message)
		return(messages)