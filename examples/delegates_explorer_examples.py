from xcash.delegatesExplorer import DelegatesExplorer
from pprint import pprint

explorer = DelegatesExplorer()

# Get delegate website statistics
statistics = explorer.get_delegate_website_statistics()
pprint(statistics)

# Get all delegates registered in DPOPS system
all_delegates = explorer.get_all_delegates()
pprint(all_delegates)

# Get round statistics
block_height = 900000
round_statistics = explorer.get_round_statistics(block_height=block_height)
pprint(round_statistics)

# Get delegate statistics by name or address 
delegate_name = "X-Payment-World"
delegate_address = "XCA1kLpg7A9c919tsQZBDYPHoLSZgCzihZPgP569CtFpJvAvQrpqW72HZzLKHRRLpSQzpdKBwJeTaUXGco7E4tHr9TynMN5yfi"

delegate_statistics = explorer.get_delegate_statistics(delegate=delegate_name)
pprint(delegate_statistics)

delegate_statistics = explorer.get_delegate_statistics(delegate=delegate_address)
pprint(delegate_statistics)

# Get delegate information 
delegate_information = explorer.get_delegate_information(delegate=delegate_name)
pprint(delegate_information)
delegate_information =explorer.get_delegate_information(delegate=delegate_name)
pprint(delegate_information)

# Get list of delegate voters 
delegate_voters_list = explorer.get_delegate_voter_list(delegate=delegate_name)
pprint(delegate_voters_list)
delegate_voters_list = explorer.get_delegate_voter_list(delegate=delegate_name)
pprint(delegate_voters_list)



