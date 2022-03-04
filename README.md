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
- [ ] RPC 
  - [X] Daemon
  - [ ] Wallet
- [X] [PyPi published](https://pypi.org/project/xcash/)

## Setup

Package can be installed with [pip](https://pypi.org/project/pip/), the python package index.

```shell
pip3 install xcash
```

or

```shell
pip install xcash
```

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



