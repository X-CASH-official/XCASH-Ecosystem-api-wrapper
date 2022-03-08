# XCASH Foundation ecosystem python API wrapper

![Issues](https://img.shields.io/github/issues/X-CASH-official/XCASH-Ecosystem-api-wrapper)
![Forks](https://img.shields.io/github/forks/X-CASH-official/XCASH-Ecosystem-api-wrapper)
![Stars](https://img.shields.io/github/stars/X-CASH-official/XCASH-Ecosystem-api-wrapper)
![Activity](https://img.shields.io/github/commit-activity/m/X-CASH-official/XCASH-Ecosystem-api-wrapper/main?style=plastic)
![License](https://img.shields.io/github/license/X-CASH-official/XCASH-Ecosystem-api-wrapper?style=plastic)
![Code Size](https://img.shields.io/github/languages/code-size/X-CASH-official/XCASH-Ecosystem-api-wrapper?style=plastic)
![Discord](https://img.shields.io/discord/470575102203920395?logo=Discord&style=plastic)

## What is it?

Is a client Python wrapper library around XCASH Foundation ecosystem products.

## Integrations

- [X] Blockchain Explorer api wrapper
- [X] Delegates Explorer api wrapper
- [X] Shared Delegate api wrapper
- [X] RPC
    - [X] Daemon
    - [X] Wallet
    - [X] Dpops
- [X] [PyPi published](https://pypi.org/project/xcash/)

## Setup

### Install required package

Package can be installed with [pip](https://pypi.org/project/pip/), the python package index.

```shell
pip3 install xcash
```

or

```shell
pip install xcash
```

### Ecosystem accessible products

To access products you are required to import packages and initiate them:

```python
# Access to blockchain data
from xcash.blockchainExplorer import BlockchainExplorer

blockchain_api = BlockchainExplorer()

# Access Delegates Explorer of DPOPS system
from xcash.delegatesExplorer import DelegatesExplorer

delegates_api = DelegatesExplorer()

# Access Shared delegate through api 
from xcash.sharedDelegate import SharedDelegate

delegate_api = SharedDelegate(delegate_url="DELEGATE URL")
```

### RPC server Daemon, Wallet and Dpops wallet (delegate)

#### Pre-requirements -> Start the RPC server!

In order to be able to execute calls to RPC you are required to first initiate RPC server.

Cd to the wallet folder **bin** where **xcash-wallet-rpc** is located, and open the
location with either  **cmd** (Windows) or terminal (Ubuntu)

Initiate PRC server either with:

1. Local daemon

```shell
# Windows
xcash-wallet-rpc.exe --wallet-file <Wallet Name> --password <Wallet PSW> --rpc-bind-port 18285 --disable-rpc-login 

#Ubuntu
./xcash-wallet-rpc.exe --wallet-file <Wallet Name> --password <Wallet PSW> --rpc-bind-port 18285 --disable-rpc-login 
```

2. Remote daemon

```shell
# Windows 
xcash-wallet-rpc.exe --wallet-file <Wallet Name> --password <Wallet PSW> --rpc-bind-port 18285 --disable-rpc-login --confirm-external-bind --trusted-daemon --daemon-address <daemon_address>:18281

# Ubuntu
./xcash-wallet-rpc --wallet-file <Wallet Name> --password <Wallet PSW> --rpc-bind-port 18285 --disable-rpc-login --confirm-external-bind --trusted-daemon --daemon-address <daemon_address>:18281
```

#### Import desired packages to python script

```python
# Access endpoints for XCASH Daemon
from xcash.rpc import XcashDaemonRpc

daemon = XcashDaemonRpc()

# Access endpoints for XCASH wallet
from xcash.rpc import XcashWalletRpc

wallet = XcashWalletRpc()

# Access endpoints on wallet dedicated for delegate.
from xcash.rpc import XcashDpopsWalletRpc

dpops = XcashDpopsWalletRpc()
```

## Examples

### Blockchain Explorer Api

```python
from xcash.blockchainExplorer import BlockchainExplorer
from pprint import pprint

# Initiate blockchain explorer client
blockchain_api = BlockchainExplorer()

# Get blockchain data 
blockchain_data = blockchain_api.get_blockchain_data()

# Print data
pprint(blockchain_data)

```

Examples on all available methods to communicate with XCASH blockchain Rest API can be
found [here](https://github.com/X-CASH-official/XCASH-Ecosystem-api-wrapper/blob/main/examples/blockchain_examples.py)

### Delegates Explorer Api

```python
from xcash.delegatesExplorer import DelegatesExplorer
from pprint import pprint

# Initiate delegates explorer client
delegates_api = DelegatesExplorer()

# Get delegates/DPOPS statistics 
statistics = delegates_api.get_delegate_website_statistics()

# Print data
pprint(statistics)
```

Examples on all available methods to communicate with XCASH DPOPS Delegates Explorer Rest API can be
found [here](https://github.com/X-CASH-official/XCASH-Ecosystem-api-wrapper/blob/main/examples/delegates_explorer_examples.py)

### Shared Delegate Api

```python
from xcash.sharedDelegate import SharedDelegate
from pprint import pprint

# Initiate shared delegate and provide delegates address as param to access API
url = "http://xpayment.x-network.eu"
delegate_api = SharedDelegate(delegate_url=url)

# Delegate statistics data from delegate website
statistics = delegate_api.get_delegate_website_statistic()

# Print data
pprint(statistics)
```

Examples on all available methods to communicate with Shared Delegate Rest API can be
found [here](https://github.com/X-CASH-official/XCASH-Ecosystem-api-wrapper/blob/main/examples/shared_delegate_examples.py)

### Daemon RPC call

```python
from xcash.rpc import XcashDaemonRpc
from pprint import pprint

daemon = XcashDaemonRpc()

# Get the daemon version
version = daemon.get_version()
pprint(version)
```

Examples on all available methods to communicate with Daemon RPC API can be
found [here](https://github.com/X-CASH-official/XCASH-Ecosystem-api-wrapper/blob/main/examples/rpc_daemon_examples.py)

### Wallet RPC call

````python
from xcash.rpc import XcashWalletRpc
from pprint import pprint

wallet = XcashWalletRpc()

# Get balance 
balance = wallet.get_balance()
pprint(balance)
````

Examples on all available methods to communicate with Wallet RPC API can be
found [here](https://github.com/X-CASH-official/XCASH-Ecosystem-api-wrapper/blob/main/examples/rpc_wallet_examples.py)

### DPOPS Wallet RPC call

```python
from xcash.rpc import XcashDpopsWalletRpc
from pprint import pprint

dpops_wallet = XcashDpopsWalletRpc()
status = dpops_wallet.register_delegate(delegate_name="Animus-Test", delegate_ip_address="100.100.00.00")
pprint(status)
```

Examples on all available methods to communicate with DPOPS wallet RPC API can be
found [here](https://github.com/X-CASH-official/XCASH-Ecosystem-api-wrapper/blob/main/examples/rpc_wallet_examples.py)




