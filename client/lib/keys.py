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


def get_encrypt_data(secret: bytes, public_pem: bytes):
    """Generate a random key and encrypt data and public from client"""

    symmetric_key = Fernet.generate_key()  # Generating a random bytes key
    cipher = Fernet(symmetric_key)  # create the cipher

    # Encrypt data
    secret_encrypted = cipher.encrypt(secret)

    # Encrypt the symmetric key with clients public key
    pubkey = rsa.PublicKey.load_pkcs1(public_pem)
    encrypted_public_key = rsa.encrypt(message=symmetric_key, pub_key=pubkey)
    return secret_encrypted, encrypted_public_key


def get_decrypted_data(secret: bytes, encrypted_public_key: bytes, private_pem: bytes):
    """Decrypt client data and return it"""

    # Load PEM
    private_key = rsa.PrivateKey.load_pkcs1(private_pem)

    # Decrypt the encrypted key with private key
    decrypted_public_key = rsa.decrypt(crypto=encrypted_public_key, priv_key=private_key)
    cipher = Fernet(decrypted_public_key)

    # Decrypt the secret
    decrypted_data = cipher.decrypt(secret)

    return decrypted_data.decode('utf-8')