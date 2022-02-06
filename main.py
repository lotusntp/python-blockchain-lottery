from web3 import Web3
import os
import json

from dotenv import load_dotenv
load_dotenv()
directory = './build/contracts/'
filename = "Lottery.json"
file_path = os.path.join(directory, filename)
with open(file_path) as json_file:
    abi = json.load(json_file)

client = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))
contract = client.eth.contract(address=os.environ['CONTRACT_ADDRESS'],abi=abi['abi'])

def buyLottery(account,private_key):

    try:
        nonce = client.eth.getTransactionCount(account)
        tx = {
            'nonce':nonce,
            'data': contract.encodeABI(fn_name='buyLottery',args=[]),
            'value': client.toWei(1,'ether'),
            'gas': 100000,
            'gasPrice': client.toWei(0.000000005,'ether'),
            'from': account,
            'to': os.environ['CONTRACT_ADDRESS']
        }

        signed_tx = client.eth.account.signTransaction(tx,private_key)
        tx_hash = client.eth.sendRawTransaction(signed_tx.rawTransaction)
        tx_receipt = client.eth.waitForTransactionReceipt(tx_hash)
        
        if tx_receipt['status'] == 1:
             trx = tx_receipt['transactionHash']
             print(f'buy lottery suscess transaction trx :: {client.toHex(trx)}')
    except Exception as inst:
        print(inst)

def getTicketSold():
    total = contract.functions.getLength().call()
    print(total)

def selectWinner():
    try:
        nonce = client.eth.getTransactionCount(os.environ['ACCOUNT_1'])
        tx = {
            'nonce':nonce,
            'data': contract.encodeABI(fn_name='selectWinner',args=[]),
            'value': 0,
            'gas': 100000,
            'gasPrice': client.toWei(0.000000005,'ether'),
            'from': os.environ['ACCOUNT_1'],
            'to': os.environ['CONTRACT_ADDRESS']
        }

        signed_tx = client.eth.account.signTransaction(tx,os.environ['PRIVATE_KEY_1'])
        tx_hash = client.eth.sendRawTransaction(signed_tx.rawTransaction)
        tx_receipt = client.eth.waitForTransactionReceipt(tx_hash)
        
        if tx_receipt['status'] == 1:
             trx = tx_receipt['transactionHash']
             print(f'Announcement lottery suscess transaction trx :: {client.toHex(trx)}')
    except Exception as inst:
        print(inst)


        

