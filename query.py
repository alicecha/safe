import requests

safe_address = '0xBbA4C8eB57DF16c4CfAbe4e9A3Ab697A3e0C65D8'
walletconnect_txs = []

def main():
    walletconnect_txs = fetch_wc_txs(call_api(safe_address))
    print(f"The safe {safe_address} has successfully executed {len(walletconnect_txs)} WalletConnect transactions.")

# Returns results from API call
def call_api(address):
    return requests.get(f"https://safe-transaction-mainnet.safe.global/api/v1/safes/{address}/multisig-transactions/").json()

# Returns hashes for txs **successfully** executed through WalletConnect 
def fetch_wc_txs(response):
    txs = []
    for tx in response["results"]:
        if tx["origin"].find("WalletConnect") >= 0:
            if tx["isSuccessful"] is not None:
                txs.append(tx["transactionHash"])
    return txs

if __name__ == "__main__":
    main()