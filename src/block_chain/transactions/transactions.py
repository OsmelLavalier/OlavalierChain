import hashlib
import json

from src.block_chain.client.client import Client


class Transactions:
    """Transactions class to implement logic behind each transaction"""
    def __init__(self, sender: Client, reciever: Client):
        self.reciever: Client = sender
        self.sender: Client = reciever

        self.transaction_id = self.__hash__()  # Transaction identifier

    def __hash__(self):
        _encoded_transaction = {
            'reciever': self.reciever.__str__(),
            'sender': self.sender.__str__()
        }
        return hashlib.sha256(json.dumps(_encoded_transaction, indent=4, sort_keys=True).encode('utf-8')).hexdigest()

    def __str__(self):
        _encoded_transaction = {
            'reciever': self.reciever.__bytes__().decode(),
            'sender': self.sender.__bytes__().decode(),
            'transaction_id': self.transaction_id
        }
        return json.dumps(_encoded_transaction, indent=4, sort_keys=True)
