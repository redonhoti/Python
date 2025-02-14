import hashlib
import datetime

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}"
        return hashlib.sha256(block_string.encode()).hexdigest()

blockchain = [Block(0, datetime.datetime.now(), "Genesis Block", "0")]

new_block = Block(1, datetime.datetime.now(), "Second Block", blockchain[-1].hash)
blockchain.append(new_block)

for block in blockchain:
    print(vars(block))
