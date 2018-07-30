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

        self.assertEqual(len(hash_value), 64)
        self.assertIsNotNone(regex)

    def test_mine_returns_a_hash(self):
        hash_value = self.test_block.mine(3)
        regex = re.match(r'[A-Fa-f0-9]{64}', hash_value)

        self.assertEqual(len(hash_value), 64)
        self.assertIsNotNone(regex)

    def test_mine_should_start_with_n_zeros(self):
        hash_value = self.test_block.mine(3)

        self.assertEqual(hash_value[0:3], '000')

if __name__ == '__main__':
    unittest.main()
    
