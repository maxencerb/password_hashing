import tink
from tink import KeysetHandle, daead, cleartext_keyset_handle
import bcrypt
from keyset_tink import read_keyset


daead.register()
keyset_handle = read_keyset("keyset.json")
daead_primitive = keyset_handle.primitive(daead.DeterministicAead)
ASSOCIATED_DATA = b"associated data"

database = 'database.txt'


def hash_password(pwd: str, salt = None):
  # use bcrypt to hash the password
  salt = bcrypt.gensalt() if salt is None else salt
  hashed_password = bcrypt.hashpw(pwd.encode(), salt)
  return hashed_password, salt

def encryption_machine(msg: bytes):
  # encrypt using AES-SIV
  ciphertext = daead_primitive.encrypt_deterministically(msg, ASSOCIATED_DATA)
  return ciphertext

def save_to_database(user: str, pwd: str):
  # use a file as a database
  # format: user, hashed_password, salt
  hashed_password, salt = hash_password(pwd)
  encrypted_password = encryption_machine(hashed_password)
  with open(database, 'a') as f:
    f.write(f'{user},{encrypted_password.hex()},{salt.hex()}\n')

def check_password(user, pwd):
  # read from database
  with open(database, 'r') as f:
    for line in f.readlines():
      user_in_database, encrypted_password, salt = line.split(',')
      if user == user_in_database:
        hashed_password = hash_password(pwd, bytes.fromhex(salt))[0]
        # and check for authentication
        encrypted_user_password = encryption_machine(hashed_password)
        return encrypted_user_password == bytes.fromhex(encrypted_password)
  return False