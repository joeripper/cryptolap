import rsa
import binascii

def create_keys(name):
	(pubkey, privkey) = rsa.newkeys(2048)
	f_pub = open(name + '.pub_key', 'wb')
	f_priv = open(name + '.priv_key', 'wb')
	
	f_pub.write(pubkey.save_pkcs1(format='PEM'))
	f_priv.write(privkey.save_pkcs1(format='PEM'))
	
def encrypt_message(reciever, message):
	with open(reciever + '.pub_key', 'rb') as pubfile:
		keydata = pubfile.read()
	pubkey = rsa.PublicKey.load_pkcs1(keydata)
	enc_message = rsa.encrypt(message.encode('utf-8'), pubkey)
	hex_enc_message = binascii.hexlify(enc_message).decode('utf-8')
	return(hex_enc_message)