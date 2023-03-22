import requests
import csv
import datetime
import time
import schedule
from web3 import Web3

def retrieve_and_save_nft_data():
    # Connect to an Ethereum client node
    w3 = Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/YOUR-PROJECT-ID"))

    # Define the endpoint for querying all NFT collection addresses
    endpoint = "https://api.opensea.io/api/v1/collections"

    # Make a GET request to the endpoint to retrieve all collections
    response = requests.get(endpoint)
    collections = response.json()["data"]

    # Extract all addresses and names of the NFT collections
    collections_data = [(collection["contract_address"], collection["name"]) for collection in collections]

    # Verify if the addresses are valid Ethereum addresses
    data = []
    for collection in collections_data:
        address = collection[0]
        collection_name = collection[1]
        if w3.isAddress(address):
            data.append([address, collection_name])
            print(f"{address} ({collection_name}) is a valid Ethereum address.")
        else:
            print(f"{address} ({collection_name}) is not a valid Ethereum address.")

    # Save the data in a CSV file with a unique timestamp file name
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"NFT_collections_{timestamp}.csv"
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Address", "Collection Name"])
        writer.writerows(data)

    print(f"Data saved to {filename}.")

# Schedule the task to run every 60 minutes
schedule.every(60).minutes.do(retrieve_and_save_nft_data)

# Start the scheduler
while True:
    schedule.run_pending()
    time.sleep(1)
