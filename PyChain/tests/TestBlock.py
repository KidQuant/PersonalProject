import unittest
import sys
import time
import re

sys.path.append('PyChain')

from Block import Block

class TestBlock(unittest.TestCase):
    def setUp(self):
        self.timestamp = int(time.time())
        self.test_block = Block(self.timestamp, {'qty': 2, 'price': 15.99})

    def test_constructor_creates_new_block(self):
        self.assertEqual(self.test_block.timestamp, self.timestamp)
        self.assertEqual(self.test_block.payload['qty'], 2)
        self.assertEqual(self.test_block.payload['price'], 15.99)

    def test_calculate_hash_returns_a_hash(self):
        hash_value = self.test_block.calculate_hash()
        regex = re.match(r'[A-Fa-f0-9]{64}', hash_value)

        self
