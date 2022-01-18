from chain.chain import Chain


if __name__ == '__main__':
    chain = Chain()

    head = chain.last()
    proof = chain.proof_of_work(head)

    chain.add_block(head, proof)

    for block in chain.block_chain:
        print(block)