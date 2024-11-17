import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


def generate_password_hash(password):
    '''
    生成加密的密码
    :param password:
    :return:
    '''
    return hashlib.sha256(password.encode('utf-8')).hexdigest()


def check_password_hash(password, newPassword):
    '''
    验证密码是否正确
    :param password:
    :param newPassword:
    :return:
    '''
    return generate_password_hash(newPassword) == password


def AESEncrypt(data,key, iv, mode = AES.MODE_CBC):
    '''
    aes加密
    :param data:
    :param key:
    :param iv:
    :param mode:
    :return:
    '''
    padded_data=pad(data.encode('utf-8'),AES.block_size,style='pkcs7')
    crypto=AES.new(key=key.encode('utf-8'),iv=iv.encode('utf-8'),mode=mode)
    encrypted_data=crypto.encrypt(padded_data)
    return encrypted_data.hex()


def AESDecrypt(data,key, iv, mode = AES.MODE_CBC):
    '''
    aes解密
    :param data:
    :param key:
    :param iv:
    :param mode:
    :return:
    '''
    crypto=AES.new(key=key.encode('utf-8'),iv=iv.encode('utf-8'),mode=mode)
    decrypted_data=crypto.decrypt(bytes.fromhex(data))
    unpadded_data=unpad(decrypted_data,AES.block_size,style='pkcs7').decode(encoding='utf-8')
    return unpadded_data


