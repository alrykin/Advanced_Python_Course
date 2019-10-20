import hashlib

salt = "salty_water_)"
password = salt + '222'
h = hashlib.md5(password.encode())
print(h.hexdigest())
# 111 = e693bfb096a07f43734313ad43a49a0e
# 222 = 03a8e51475b544c8a72bd51f0f5920ce
