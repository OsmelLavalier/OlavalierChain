from time import time
from block.block import Block
from error.error import BlockNotValid

def genesis():
    return Block(time(), 0, '0')


class Chain:
    """Represents structure of the blockchain with adequate functions"""
    def __init__(self):
        self.unconfirmed_transactions = []
        self.block_chain = [genesis()]

        self.__difficulty = 4

    def last(self):
        return self.block_chain[-1]

    def next_block(self, block):
        _new_block = {
            'timestamp': block.timestamp,
            'index': block.index + 1,
            'previous_hash': self.last().hash,
            'nonce': block.nonce
        }

        return Block(**_new_block)

    def add_block(self, block, proof):
        _new_block = self.next_block(block)
        _new_block.hash = proof
        if not self.is_valid_proof(_new_block, proof):
            raise BlockNotValid(message=f"Block at index: {_new_block.index} with hash: {_new_block.hash} is not valid.")
        if _new_block.previous_hash != block.hash:
            return False

        self.block_chain.append(_new_block)
        return True

    def is_valid_proof(self, block, proof):
        return block.hash.startswith(self.__difficulty * '0') and block.hash == proof

    def proof_of_work(self, block):
        _hash = block.hash
        while not _hash.startswith(self.__difficulty * '0'):
            block.nonce += 1
            _hash = block.__hash__()

        return _hash
