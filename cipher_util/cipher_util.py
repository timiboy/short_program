# -*-coding:utf-8-*-
# 几个加解密案例

import rsa
import binascii
from hashlib import sha1
import hmac
import base64
import pyDes

class RsaUtil():
    def __init__(self):
        # openssl rsa -in private_p.pem -out rsa_pri.pem
        with open('key/rsa_pub.pem') as f:
            self.public_key = rsa.PublicKey.load_pkcs1_openssl_pem(f.read())
        # openssl x509 -in public_p.pem -noout -pubkey > rsa_pub.pem
        with open('key/rsa_pri.pem') as f:
            self.private_key = rsa.PrivateKey.load_pkcs1(f.read())

    def verifyData(self, data, signValue):
        # sha1withrsa
        signValueByte = base64.b64decode(signValue)
        if rsa.verify(data, signValueByte, self.public_key):
            print u"验签OK!"
            return True

    def signData(self, data):
        # sha1withrsa
        signValue = rsa.sign(data, self.private_key, 'SHA-1')
        return base64.b64encode(signValue)


class DesUtil():
    def __init__(self):
    	key = 'abcdefghijklmnopqrstuvwx'
        self.executer = pyDes.triple_des(key, mode=pyDes.ECB, padmode=pyDes.PAD_PKCS5)

    def encrypt(self, data):
        sealTxt = self.executer.encrypt(data)
        ret = base64.b64encode(sealTxt)
        return ret

    def decrypt(self, sealTxt):
    	sealTxt = base64.b64decode(sealTxt)
    	return self.executer.decrypt(sealTxt)

def sha1_encrypt(data):
	hashed = sha1()
	hashed.update(data)
	return hashed.hexdigest()

if __name__ == '__main__':
    r = RsaUtil()
    d = DesUtil()
    print 'test_' + sha1_encrypt('test')
    print r.verifyData('hello, world', r.signData('hello, world'))
    print d.decrypt(d.encrypt('hello, world'))

