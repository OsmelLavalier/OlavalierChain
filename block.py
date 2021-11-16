import hashlib
import json

from transactions import Transactions

class Block:
    def __init__(self, proof, timestamp, prevhash):
        self.transactions = []
        self.proof = proof
        self.timestamp = timestamp
        self.prevhash = prevhash
        self.currenthash = self.hashin()

    def hashin(self):
        return hashlib.sha256(
                json.dumps(self.__dict__, sort_keys=True, indent=4).encode('utf-8')).hexdigest()
    
    def append_transaction(self, new_txion):
        new_txion = {
            'sender': Transactions
        
        }
        self.transactions.append(new_txion)
    
    def __str__(self):
        return json.dumps(self.__dict__, sort_keys=True, indent=4)
    
   
