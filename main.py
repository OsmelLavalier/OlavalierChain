from chain.chain import Chain
from client.lib import keys

# TODO: fix tests


if __name__ == '__main__':
    chain = Chain()
    for _ in range(5):
        chain.mine()
    for b in chain.block_chain:
        print(b)