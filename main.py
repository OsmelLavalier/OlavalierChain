from chain.chain import Chain

#TODO: fix tests and add test function to check if proof is null or not.

if __name__ == '__main__':
    chain = Chain()
    #Yes
    for _ in range(5):
        chain.mine()

    for b in chain.block_chain:
        print(b)