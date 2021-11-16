from time import time

from block import Block
from transactions import Transactions

class BlockChain:

    def __init__(self):
        self.chain = [self.genesis()]

    def genesis(self):
        return Block('0', time(), '0')

    def next_block(self, new_block):
        new_block = {
                'proof': new_block.proof,
                'timestamp': time(),
                'previous hash': new_block.currenthash or self.last_block().currenthash,
                }

        return Block(new_block['proof'], new_block['timestamp'], new_block['previous hash'])
    
    def last_block(self):
        return self.chain[-1]
    
    def append_block(self, block):
        newblock = self.chain[0]

        for i in range(2):
            block  = self.next_block(block)
            block.prevhash = self.last_block().currenthash
            block.currenthash = block.hashin()

            self.chain.append(block)
    
    def get_txtion(self, block):
        priv, pub = Transactions.get_pair()
        Block.append_transaction(self.append_block())
        
    def output(self):
        for b in self.chain:
            print(b)

bc = BlockChain()
bc.append_block(Block('0','0','0'))
#bc.pofw()
bc.output()
