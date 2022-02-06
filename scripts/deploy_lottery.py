
import os
from dotenv import load_dotenv
from brownie import accounts, Lottery

load_dotenv()
def main():
    deploay_account = accounts.add(os.environ['PRIVATE_KEY_1'])
    deploay_details = {
        'from':deploay_account,
        'value': 0
    }

    guess_number = Lottery.deploy(deploay_details)
    return guess_number