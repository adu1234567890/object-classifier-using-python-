from web3 import Web3

# Connect to your Ethereum node provider (Infura, Alchemy, or local Ganache)
infura_url = 'https://sepolia.infura.io/v3/a93adc56320a433e9792a2bc44e9bc7d'
w3 = Web3(Web3.HTTPProvider(infura_url))

if w3.is_connected():
    print("Connected to the Ethereum network")
else:
    print("Failed to connect to the network")
