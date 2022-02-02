from time import time
from .block_chain.block.block import Block
from .block_chain.error.error import BlockNotValid


class Chain:
    """Represents structure of the blockchain with adequate functions"""
    def __init__(self):
        self.difficulty = 4
        self.unconfirmed_transactions = []
        self.block_chain = [self.genesis()]

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
        _new_block.proof = proof
        if not self.is_valid_proof(_new_block, proof):
            raise BlockNotValid(message=f"Block at index: {_new_block.index} with hash: {_new_block.hash} is not valid.")
        if _new_block.previous_hash != block.hash:
            return False

        self.block_chain.append(_new_block)
        return True

    def is_valid_proof(self, block, proof):
        return block.proof.startswith(self.difficulty * '0') and block.proof == proof

    def proof_of_work(self, block):
        _hash = block.hash
        while not _hash.startswith(self.difficulty * '0'):
            block.nonce += 1
            _hash = block.__hash__()

        return _hash

    def mine(self):
        if not self.unconfirmed_transactions:  # TODO: raise UTException
            pass

        _last = self.last()
        proof = self.proof_of_work(_last)
        self.add_block(_last, proof)

    def genesis(self):
        ret = Block(time(), 0, '0')
        ret.proof = self.proof_of_work(ret)

        if not self.is_valid_proof(ret, ret.proof):
            raise BlockNotValid(message=f"Block at index: {ret.index} with hash: {ret.hash} is not valid.")

        return ret
