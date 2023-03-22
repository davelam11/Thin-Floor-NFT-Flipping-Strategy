# Thin-Floor-NFT-Flipping-Strategy
This is a repo trading the ethreum NFTs based on NFT collections data retrieved from the Opensea api, using an popular approach named "Thin Floor", i.e. very few listed items set at the floor price of the NFT collections, with also 7-day trading volume as a filter to cast out all inactive NFT collections.

[Step of using this repo]:
1. Use the eth_nft_col_parser.py to parse all Ethereum NFT collection data on Opensea.
2. Use the eth_nft_col_thinfloor-vol_sorted.py to sort by floor price and trading volume, the resulted NFT collections possible to trade with.
3. Go to opensea and pick your favourite NFT(s) from the resulted NFT collections and buy it! Or you can pass the nft_id and NFT contract address to the eth_nft_buying.py to automatically purchasing it.
