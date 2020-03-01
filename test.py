from helper import *
f = open('pri.pem','r',encoding='utf-8')
pri=f.read()
print(pri)

f = open('pub.pem','r',encoding='utf-8')
pub=f.read()
print(pub)

pubkey=load_pub_key(pub)
prikey=load_pri_key(pri)


msg="helloworld"
sign_hex=sign(msg,prikey)
print(verify("helloworld",sign_hex,pubkey))

#encrypt_text = encrypt(msg,pubkey)
#print (encrypt_text)
#
#print (decrypt(encrypt_text,prikey))



