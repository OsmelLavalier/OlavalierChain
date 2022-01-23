import os
import json
import rsa

from .lib import keys


# TODO: implement functions that we are passing
# TODO: eventually move some of this functionality to transactions.py

class Client:
    """Client in blockchain which represents a sender or reciever"""

    PATH_TO_CLIENT_SECRET = os.path.join(os.path.dirname(__file__), 'client_secret.json')

    def __init__(self, name: str, last_name: str, message: str, amount: float):
        self.name: str = name
        self.last_name: str = last_name
        self.message: str = message
        self.amount: float = amount

        # Keys and PEM
        self.public_key, self.private_key = keys.generate_key_pair()

        self.public_pem = keys.get_keys_as_pem(self.public_key, self.private_key)[0]
        self.private_pem = keys.get_keys_as_pem(self.public_key, self.private_key)[1]

    def sign_transaction(self):
        """Signs this transaction with private key and SHA-256 method"""

        # Get encrypted secret
        secret = keys.get_encrypt_data(secret=self.__bytes__())

        # Secret hash
        _hash_value = rsa.compute_hash(message=secret, method_name='SHA-512')

        # Sign the message with the owners private key
        _signature = rsa.sign(message=secret, priv_key=self.private_key, hash_method='SHA-512')
        return _signature, _hash_value, secret

    @classmethod
    def sign_incoming_transaction(cls, other_client):
        """Signs incoming transaction from another client with public key"""
        pass

    @classmethod
    def verify_signature(cls, other_client):
        """Verify the signature of the transaction, may raise """
        pass

    @classmethod
    def make_transaction(cls, other_client):
        """Make the transaction once signing is verified"""
        pass

    def to_file(self):
        with open(Client.PATH_TO_CLIENT_SECRET, mode='w') as client_secret:
            json.dump(json.loads(self.__bytes__().decode('utf-8')), fp=client_secret, indent=4, sort_keys=True)

    def __bytes__(self):
        """Return specific object of Client attributes"""

        _encoded_object = {
            'public_key': self.public_key.__str__(),
            'name': self.name,
            'last_name': self.last_name,
            'message': self.message,
            'amount': self.amount
        }
        return json.dumps(_encoded_object, indent=4, sort_keys=True).encode('utf-8')

    def __str__(self):
        return json.dumps(json.loads(self.__bytes__().decode('utf-8')), indent=4, sort_keys=True)
