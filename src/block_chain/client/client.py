import os
import json
import rsa

from typing import Optional
from .lib import keys


# TODO: implement functions that we are passing
# TODO: eventually move some of this functionality to transactions.py

class Client:
    """Client in blockchain which represents a sender or reciever"""

    PATH_TO_CLIENT_SECRET = os.path.join(os.path.dirname(__file__), 'client_secret.json')

    def __init__(self, name: str, last_name: str, amount: Optional[float] = 0.0, message: Optional[str] = ''):
        if amount and amount < 0:
            raise ValueError(f"{amount} can't be negative.")

        self.name: str = name
        self.last_name: str = last_name
        self.amount: float = amount
        self.message: str = message

        # Keys and PEM
        self.public_key, self.private_key = keys.generate_key_pair()

        self.public_pem = keys.get_keys_as_pem(self.public_key, self.private_key)[0]
        self.private_pem = keys.get_keys_as_pem(self.public_key, self.private_key)[1]

        self.wallet: float = 0

    def sign_transaction(self, other_client):
        """Signs this transaction with private key and SHA-256 method"""

        # Get encrypted secret
        _secret, _encrypted_public_key = keys.get_encrypt_data(secret=self.__bytes__(), public_pem=other_client.public_pem)

        # Secret hash
        _hash_value = rsa.compute_hash(message=_secret, method_name='SHA-512')

        # Sign the message with the owners private key
        _signature = rsa.sign(message=_secret, priv_key=self.private_key, hash_method='SHA-512')
        return _signature, _encrypted_public_key, _secret

    def is_valid_signature(self, other_client):
        """Verify the signature of the transaction, may raise """

        _signature, _encrypted_public_key, _secret = self.sign_transaction(other_client)

        # Open public key and load in key
        pubkey = rsa.PublicKey.load_pkcs1(self.public_pem)

        # Verify the signature to show if successful or failed
        if isinstance(rsa.verify(message=_secret, signature=_signature, pub_key=pubkey), rsa.VerificationError):
            return False
        return True

    def decrypt_incoming_data(self, other_client):
        _signature, _encrypted_public_key, _secret = other_client.sign_transaction(self)

        if self.is_valid_signature(other_client):
            data = keys.get_decrypted_data(secret=_secret, encrypted_public_key=_encrypted_public_key, private_pem=self.private_pem)
            return json.loads(data)
        return None

    def make_transaction(self, other_client):
        """Make the transaction once signing is verified"""
        data = self.decrypt_incoming_data(other_client)

        print(self)

    def to_file(self):
        with open(Client.PATH_TO_CLIENT_SECRET, mode='w') as client_secret:
            json.dump(json.loads(self.__bytes__().decode('utf-8')), fp=client_secret, indent=4, sort_keys=True)

    def __bytes__(self):
        """Return specific object of Client attributes"""

        _encoded_object = {
            'public_key': self.public_key.__str__(),
            'name': self.name,
            'last_name': self.last_name,
            'amount': self.amount,
            'message': self.message
        }
        for k, v in self.__dict__.items():
            if k in _encoded_object:
                if not v:
                    _encoded_object.pop(k)
        return json.dumps(_encoded_object, indent=4, sort_keys=True).encode('utf-8')

    def __str__(self):
        return json.dumps(json.loads(self.__bytes__().decode('utf-8')), indent=4, sort_keys=True)