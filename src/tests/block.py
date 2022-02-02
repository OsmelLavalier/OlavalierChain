from time import time
from src.bc.block import Block

"""All instances of Chain will be replaced with pytest.fixtures"""


def test_create_simple_block():
    """Test creation of a simple block"""
    _create_block = {
        'timestamp': time(),
        'index': 0,
        'previous_hash': '0'
    }

    block = Block(**_create_block)
    for key, value in _create_block.items():
        assert value == block.__getattribute__(key)

    assert block.hash is not None
