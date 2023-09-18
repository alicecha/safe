# Initialise variable safe_address, value = 0xBbA4C8eB57DF16c4CfAbe4e9A3Ab697A3e0C65D8
# Initialise list walletconnect_txs, value = []

# Make API call to https://safe-transaction-mainnet.safe.global/api/v1/safes/{safeAddress}/multisig-transactions/ and save results

# Iterate over results, saving tx hash where contain "WalletConnect" in origin field into walletConnectTxs

# Count number tx hashes saved
