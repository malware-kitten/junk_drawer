from wincrypto import CryptCreateHash, CryptHashData, CryptDeriveKey, CryptEncrypt, CryptImportKey, CryptExportKey, CryptDecrypt
from wincrypto.constants import CALG_MD5, CALG_RC4, bType_SIMPLEBLOB
from inspect import getmembers

f = open('encoded.bin','rb')
data = f.read()
f.close()

md5hasher = CryptCreateHash(CALG_MD5)
CryptHashData(md5hasher, 'passphrase')
rc4_key = CryptDeriveKey(md5hasher, CALG_RC4)
buf = CryptDecrypt(rc4_key, data)

print(buf)
