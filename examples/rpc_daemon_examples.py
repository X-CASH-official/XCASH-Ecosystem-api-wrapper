from xcash.rpc import XcashDaemonRpc
from pprint import pprint

rpc_url = None  # If none a http://localhost:18281/json_rpc will be used

daemon_rpc = XcashDaemonRpc(rpc_url=rpc_url)

# Get block count
count = daemon_rpc.get_block_count()
pprint(count)

# Block hash by block_height
block_hash = daemon_rpc.on_get_block_hash(block_height=425000)
pprint(block_hash)

# get block template
wallet_address = "XCA1XPzaSeXgwrBrGbh96UD5bk21a4WabcrgtB14A7WGGdcagjVQVV1PMAg5Rj1SM3ca8ZPDvysi78HyZF9imGg48wRK2Ntqov"
reserve_size = 128
template = daemon_rpc.get_block_template(wallet_address=wallet_address, reserve_size=reserve_size)
pprint(template)

# submit block
block_blob_data = "0c0ceadfe6eb051eb5164dfe508a6d7681d8b490a915cde9d0762d1b936beda7d4c9ee8bc9dc280000000002c7a31a" \
                  "01ff8ba31a01f69a92cabb0102ecb13a092850dd0387b40a162e6b154c677e6a4a5ab6530b9c508fac4c5b9168a30101b5" \
                  "3cfbe508ca940be5544d91c7cb6f34d4a62af1faa16453a3406f443979ca5202800000000000000000000000000000" \
                  "00000000000000000000000000000000000000000000000000000000000000000000000000000000" \
                  "00000000000000000000000000000000000000000000000000000000000000000000000000000" \
                  "000000000000000000000000000000000000000000000000000000000000000000000000002ac" \
                  "c77f92091e5ebccdd904da4a03e4eb9153f13e338add4b314b436858fb7ea33bc2ea30b4982c433631" \
                  "1f38caed30601f72ae22a44f11ae04ccd59663e135df"

result = daemon_rpc.submit_block(block_blob_data=list(block_blob_data))
pprint(block_blob_data)

# Last block header
last_block_header = daemon_rpc.get_last_block_header()
pprint(last_block_header)

# Header by block hash
block_hash = "062537808276507cb05b5d5f80dbc8dd2bb79a9213be9958dfed1517742cc6a1"
block_header = daemon_rpc.get_block_header_by_hash(hash=block_hash)
pprint(block_header
       )
# Header by block height
block_height = 800000
block_header_height = daemon_rpc.get_block_header_by_height(height=block_height)
pprint(block_header_height)

# Get block headers by range
start_height = 800000
end_height = 850000
headers_of_range = daemon_rpc.get_block_headers_range(start_height=start_height, end_height=end_height)
pprint((headers_of_range))

# get block by height or hash
height = 800000
hash = "062537808276507cb05b5d5f80dbc8dd2bb79a9213be9958dfed1517742cc6a1"

by_height = daemon_rpc.get_block(height_hash=height)  # By height
pprint(by_height)
by_hash = daemon_rpc.get_block(height_hash=hash)
pprint(by_hash)

# Get connections
all_connections = daemon_rpc.get_connections()
pprint(all_connections)

# Get information about the chain
chain_info = daemon_rpc.get_info()
pprint(chain_info)

# Hard Fork information
hf_info = daemon_rpc.hard_fork_info()
pprint(hf_info)

# Get all bans
all_bans = daemon_rpc.get_bans()
pprint(all_bans)

# flush tx pool
result = daemon_rpc.flush_txpool()
pprint(result)

# get output histogram
amounts_list = [100000000000]
hist = daemon_rpc.get_output_histogram(amounts=amounts_list)
pprint(hist)

# Get coinbase tx sum
height = 425000
count = 1
tx_sum = daemon_rpc.get_coinbase_tx_sum(height=height, count=count)

# Get current version
version = daemon_rpc.get_version()
pprint(version)

# Get fee estimations
fees = daemon_rpc.get_fee_estimate()
pprint(fees)

# Get alternate chains
alternates = daemon_rpc.get_alternate_chains()
pprint(alternates)

# relay tx
tx_ids = ["9fd75c429cbe52da9a52f2ffc5fbd107fe7fd2099c0d8de274dc8a67e0c98613"]
relay_result = daemon_rpc.relay_tx(tx_ids=tx_ids)

# sync info
sync_info = daemon_rpc.sync_info()
pprint(sync_info)
