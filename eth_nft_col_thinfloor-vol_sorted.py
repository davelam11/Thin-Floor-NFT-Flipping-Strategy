import requests
import csv
import datetime
import time
import schedule
from web3 import Web3

def retrieve_and_rank_nft_collections(file_name, volume_threshold):
    # Connect to an Ethereum client node
    w3 = Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/YOUR-PROJECT-ID"))

    # Load the NFT collection addresses and names from the CSV file
    collections_data = []
    with open(file_name) as file:
            reader = csv.DictReader(file)
            for row in reader:
                collections_data.append({
                    'address': row['address'],
                    'name': row['name']
                })

    # Define the endpoint for querying NFT item data
    endpoint = "https://api.opensea.io/api/v1/assets"

    # Create a list to store the NFT collection data with trading volume and floor price information
    ranked_collections = []
    for collection in collections_data:
        address = collection[0]
        collection_name = collection[1]

        # Make a GET request to the endpoint to retrieve the NFT items for the collection
        response = requests.get(endpoint, params={
            "collection_address": address,
            "order_by": "current_price",
            "order_direction": "asc",
            "asset_contract_address": address,
        })
        items = response.json()["assets"]

        # Calculate the 7-day trading volume for the collection
        volume = sum([item["current_price"]["usd"] for item in items])

        # Determine the floor price for the collection
        floor_price = items[0]["current_price"]["usd"] if items else 0

        # Count the number of items selling at the floor price
        floor_count = len([item for item in items if item["current_price"]["usd"] == floor_price])

        # Only include collections with a trading volume above the threshold
        if volume >= volume_threshold:
            ranked_collections.append([address, collection_name, volume, floor_price, floor_count])

    # Sort the collections by floor price, and then by trading volume
    ranked_collections.sort(key=lambda x: (x[3], x[2]), reverse=True)

    return ranked_collections.to_csv("ranked_eth_nft_col_to_thinfloor.csv")

# Schedule the task to run every 60 minutes
schedule.every(60).minutes.do(retrieve_and_rank_nft_collections, volume_threshold=XX)

# Start the scheduler
while True:
    schedule.run_pending()
    time.sleep(1)
