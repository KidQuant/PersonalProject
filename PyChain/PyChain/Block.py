import hashlib
import json

class Block():
    """
    Block
    Responsible for storing the data payload and comprising
    each link in the chain
    """
    def __init__(self, timestamp, payload):
        self.timestamp = timestamp
        self.payload = payload
        self.previous_hash = ''
        self.hash = ''
        self.nonce = 0

    def calculate_hash(self):
        """
        Responsible for generating a hash of each individual block. All pertinent details
        relating to the block such as index and previous hash are concatenated to a JSON
        string of the contract and hashed.
        """
        payload = "{}{}{}{}".format(self.previous_hash,
                                      self.timestamp,
                                      json.dumps(self.payload),
                                      self.nonce).encode('utf-8')

        return hashlib.sha256(payload).hexdigest()

    def mine(self, difficulty):
        """
        This function requires the hash be proceeded by N zeros (provided when
        blockchain is initialized). As long as the hash does not meet this
        requirement, it will increase the nonce value and re-hash
        """
        while self.hash[0:difficulty] != '0' * difficulty:
            self.nonce += 1
            self.hash = self.calculate_hash()

        return self.hash
