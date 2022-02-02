import hashlib
import json

# TODO: Eventually add transaction to __init__

class Block:
    """Represents a block structure in the blockchain"""
    def __init__(self, timestamp, index, previous_hash, nonce=0):
        self.transactions = []
        self.timestamp = timestamp
        self.index = index
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.proof = None
        self.hash = self.__hash__()

    def __hash__(self):
        return hashlib.sha256(json.dumps(self.__dict__, sort_keys=True, indent=4).encode('utf-8')).hexdigest()

    def __str__(self):
        return json.dumps(self.__dict__, sort_keys=True, indent=4, default=str)
