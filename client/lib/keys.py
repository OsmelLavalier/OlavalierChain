import os
import rsa

from cryptography.fernet import Fernet


# TODO: implement decryption logic so another client can access the data sent


def generate_key_pair():
    """Generate public/private key pair"""

    pubkey, privkey = rsa.newkeys(nbits=2048)
    return pubkey, privkey


def get_keys_as_pem(pubkey: rsa.key.PublicKey, privkey: rsa.key.PrivateKey):
    """Get public/private key pair in PEM format"""

    return pubkey.save_pkcs1('PEM'), privkey.save_pkcs1('PEM')


def get_encrypt_data(secret: bytes):
    """Generate a random key and encrypt data from client"""

    symmetric_key = Fernet.generate_key()  # Generating a random key
    cipher = Fernet(symmetric_key)  # create the cipher

    # Encrypt data
    secret_encrypted = cipher.encrypt(secret)
    return secret_encrypted


def get_decrypted_data(secret: bytes):
    """Decrypt client data and return it"""
    pass


def save_keys(pubkey: rsa.key.PublicKey, privkey: rsa.key.PrivateKey, pubkeyname: str, privkeyname: str):
    """Save key pair locally"""

    with open(os.path.join(os.path.dirname(__file__), pubkeyname), mode='wb') as pub_file:
        pub_file.write(pubkey.save_pkcs1('PEM'))

    with open(os.path.join(os.path.dirname(__file__), privkeyname), mode='wb') as priv_file:
        priv_file.write(privkey.save_pkcs1('PEM'))
