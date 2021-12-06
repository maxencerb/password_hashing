import tink
from tink import daead, cleartext_keyset_handle

def read_keyset(filename):
  with open(filename, 'rt') as f:
    return cleartext_keyset_handle.read(
      tink.JsonKeysetReader(f.read())
    )

if __name__ == '__main__':
    daead.register()

    keyset_handle = tink.new_keyset_handle(daead.deterministic_aead_key_templates.AES256_SIV)

    with open('keyset.json', 'wt') as f:
        cleartext_keyset_handle.write(
            tink.JsonKeysetWriter(f), keyset_handle
        )