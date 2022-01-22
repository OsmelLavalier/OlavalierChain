import hashlib
import json

from client.client import Client


class Transactions:
    """Transactions class to implement logic behind each transaction"""
    def __init__(self):
        self.reciever = Client()
        self.sender = Client()

        self.transaction_id = self.__hash__()  # Transaction identifier

    def __hash__(self):
        return hashlib.sha256(json.dumps(self.__dict__, indent=4, sort_keys=True).encode('utf-8')).hexdigest()

    def __str__(self):
        return json.dumps(self.__dict__, indent=4, sort_keys=True)
