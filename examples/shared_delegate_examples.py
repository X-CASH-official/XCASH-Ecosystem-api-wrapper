from xcash.sharedDelegate import SharedDelegate
from pprint import pprint

delegate = SharedDelegate("http://xpayment.x-network.eu")  # API base from the delegate

# Delegate statistics data from delegate website
statistics = delegate.get_delegate_website_statistic()

# Get all blocks found by delegate and its details
blocks_found = delegate.get_blocks_found(start=20, amount="all")

# Return list of delegates which voted
voters = delegate.get_delegate_voter_list()
pprint(voters)

# Get the public address information
delegate_public_address = None  # Provide public address of delegate
delegate_data = delegate.get_public_address_information(public_address=delegate_public_address)

# Get payment information about any delegate that has staked on the shared delegate
delegate_public_address = None  # Provide public address of delegate
payments = delegate.get_public_address_payment_information(public_address=delegate_public_address)
pprint(payments)
