from src.block_chain.tests.chain import Chain, genesis

"""All instances of Chain will be replaced with pytest.fixtures"""


def test_genesis_block_has_been_added():
    """Test the blockchain has already a genesis block"""

    chain = Chain()

    assert len(chain.block_chain) == 1
    assert chain.last().__str__() == genesis().__str__()


def test_next_block_creation():
    """Test to next block is created from the last"""

    chain = Chain()

    last = chain.last()
    _next = chain.next_block(last)

    assert _next.index - 1 == last.index
    assert _next.previous_hash == last.hash
    assert _next.previous_hash != _next.hash


def test_found_valid_proof():
    """Test to find a valid proof for a certain block"""

    chain = Chain()

    last = chain.last()
    proof = chain.proof_of_work(last)

    assert proof[:4] == '0000'


def test_add_valid_block_to_chain():
    """Test add valid block with proof to the blockchain"""

    chain = Chain()
    last = chain.last()
    proof = chain.proof_of_work(last)

    last_len = len(chain.block_chain)

    assert chain.add_block(last, proof) is not False
    assert len(chain.block_chain) - 1 == last_len

    new_last = chain.last()
    assert new_last.index - 1 == last.index
    assert new_last.previous_hash == last.hash
    assert new_last.hash[:4] == '0000'
    assert new_last.nonce != 0
