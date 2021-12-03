import tink
from tink import daead

daead.register()
keyset_handle = tink.new_keyset_handle(daead.deterministic_aead_key_templates.AES256_SIV)
daead_primitive = keyset_handle.primitive(daead.DeterministicAead)
ASSOCIATED_DATA = b"associated data"

database = 'database.txt'
secret_key = 'xxx' # use Tink to generate your secret key here

def hash_password(pwd):
  # implement your scheme

  return hash

def encryption_machine(msg):
    # encrypt using AES-SIV
    ciphertext = daead_primitive.encrypt_deterministically(msg, ASSOCIATED_DATA)
    return ciphertext

def save_to_database(user, pwd):
  # use a file as a database
  # format: user, hashed_password
  # for example: file.write(user, hash_password(pwd))
  pass

def check_password(user, pwd):
  # read from database
  # and check for authentication
  return false/true
