import rsa
from client.client import Client

# TODO: fix tests
# TODO: add verification error in error.py

if __name__ == '__main__':
    client = Client(name='Foo', last_name='Bar', message='I hope you recieve this.', amount=100)

    signature, signature_hash, secret = client.sign_transaction()

    # Open public key file and load in key
    pubkey = rsa.PublicKey.load_pkcs1(client.public_pem)

    # Verify the signature to show if successful or failed
    try:
        rsa.verify(message=secret, signature=signature, pub_key=pubkey)
        print("Signature successfully verified")
    except rsa.verify:
        print('Signature not verified')

