import json
import os
import hashlib
import time

# Difficulty target
DIFFICULTY_TARGET = "0000ffff00000000000000000000000000000000000000000000000000000000"

# Function to read JSON files from folder
def read_transactions_from_folder(folder_path):
    transactions = []
    for filename in os.listdir(folder_path):
        with open(os.path.join(folder_path, filename), 'r') as file:
            transaction = json.load(file)
            transactions.append(transaction)
    return transactions

# Function to validate a transaction
def validate_transaction(transaction):
    # Placeholder validation logic
    # Your implementation here
    
    # Placeholder: For simplicity, assume all transactions are valid
    return True

# Function to construct block header
def construct_block_header(merkle_root_hash, previous_block_hash):
    # Placeholder implementation
    # In Bitcoin, block header consists of fields like version, previous block hash, merkle root hash, timestamp, and nonce
    # For simplicity, let's construct a simple block header string
    return f"Version: 1\nPrevious Block Hash: {previous_block_hash}\nMerkle Root Hash: {merkle_root_hash}\nTimestamp: {int(time.time())}\nNonce: 0"

# Function to create coinbase transaction
def create_coinbase_transaction():
    # Placeholder implementation
    # Coinbase transaction is the first transaction in a block, which creates new bitcoins and pays them to the miner
    return "Coinbase Transaction Placeholder"

# Function to calculate merkle root hash
def calculate_merkle_root_hash(transactions):
    # Placeholder implementation
    # In Bitcoin, merkle root hash is computed from the hashes of all transactions in the block
    # For simplicity, let's assume the merkle root hash is the hash of concatenated transaction IDs
    concatenated_txids = ''.join([transaction['txid'] for transaction in transactions])
    return hashlib.sha256(concatenated_txids.encode()).hexdigest()

# Function to mine block
def mine_block(block_header, transactions):
    # Placeholder implementation
    # Mining involves repeatedly hashing the block header with different nonce values until a hash less than the difficulty target is found
    nonce = 0
    while True:
        candidate_hash = hashlib.sha256((block_header + str(nonce)).encode()).hexdigest()
        if candidate_hash < DIFFICULTY_TARGET:
            return candidate_hash
        nonce += 1

# Function to write to output file
def write_to_output_file(block_header, coinbase_transaction, transactions):
    with open("output.txt", 'w') as file:
        file.write(block_header + "\n")
        file.write(coinbase_transaction + "\n")
        for transaction in transactions:
            file.write(transaction["txid"] + "\n")

# Main function
def main():
    # Read transactions from mempool folder
    transactions = read_transactions_from_folder("mempool")

    # Validate transactions
    valid_transactions = []
    for transaction in transactions:
        if validate_transaction(transaction):
            valid_transactions.append(transaction)

    # Construct block
    coinbase_transaction = create_coinbase_transaction()
    block_transactions = [coinbase_transaction] + valid_transactions
    merkle_root_hash = calculate_merkle_root_hash(block_transactions)
    previous_block_hash = "Previous Block Hash Placeholder"  # Placeholder for previous block hash
    block_header = construct_block_header(merkle_root_hash, previous_block_hash)

    # Mine block
    block_hash = mine_block(block_header, block_transactions)

    # Output block details to output.txt
    write_to_output_file(block_header, coinbase_transaction, valid_transactions)

if __name__ == "__main__":
    main()
