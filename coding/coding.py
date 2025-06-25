from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from base64 import urlsafe_b64encode
import os

def cript(password1, login1):
    # Конвертируем пароль в байты.
    password = bytes(password1, 'utf-8')  
    # Добавляем "соль".
    salt = os.urandom(16)

    # Создаем ключ, используя PBKDF2HMAC.
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    # Генерируем urlsafe base64 ключ.
    key = urlsafe_b64encode(kdf.derive(password))

    # Создаем шифровальщик с использованием Fernet.
    cipher_suite = Fernet(key)

    # Шифруем сообщение.
    message = bytes(login1, 'utf-8')
    
    encrypted_msg = cipher_suite.encrypt(message)
    print('encrypted_msg=',encrypted_msg)
    #расшифровка
    decrypted_msg = cipher_suite.decrypt(encrypted_msg)
    dec=decrypted_msg.decode('utf-8')
    passw=password.decode('utf-8')
    print('расшифровка decrypted_msg=',dec,sep='')
    print('password=',passw,sep='')
    return passw
pas=input('введите password: ')
log=input('введите login: ')
cript(pas,log)
