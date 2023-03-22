import web3

# Connect to the Ethereum network using the Infura provider
w3 = web3.Web3(web3.Web3.HTTPProvider("https://mainnet.infura.io/v3/your-project-id"))

# Your Metamask wallet private key
private_key = "0xyour_private_key"

# The NFT contract address
nft_contract_address = "0xcontract_address"

# The NFT ID you want to purchase
nft_id = 1

# Get the NFT token ID
token_id = w3.eth.getStorageAt(nft_contract_address, nft_id)

# Get the NFT token price
nft_price = w3.eth.call({"to": nft_contract_address, "data": token_id}, "pending")

# The address of the buyer
buyer_address = w3.eth.account.privateKeyToAccount(private_key).address

# Prepare the transaction to purchase the NFT
transaction = {
    "to": nft_contract_address,
    "value": nft_price,
    "gas": 21000,
    "gasPrice": w3.eth.gasPrice,
    "nonce": w3.eth.getTransactionCount(buyer_address),
    "data": token_id
}

# Sign the transaction with the buyer's private key
signed_transaction = w3.eth.account.signTransaction(transaction, private_key)

# Send the transaction to the Ethereum network
w3.eth.sendRawTransaction(signed_transaction.rawTransaction)