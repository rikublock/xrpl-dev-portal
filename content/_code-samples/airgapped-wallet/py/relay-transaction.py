from xrpl.clients import JsonRpcClient
from xrpl.models.transactions import Payment
from xrpl.transaction import send_reliable_submission


def connect_node(_node):
    """
    Connects to a node
    """

    JSON_RPC_URL = _node
    _client = JsonRpcClient(url=JSON_RPC_URL)
    print("\n   ---   Connected to Node")
    return _client


def send_transaction(transaction_dict):
    """
    Connects to a node -> Send Transaction
    Main Function to send transaction to the XRPL
    """

    client = connect_node("https://s.altnet.rippletest.net:51234/")
    # TESTNET: "https://s.altnet.rippletest.net:51234/"
    # MAINNET: "https://s2.ripple.com:51234/"

    # Since we manually inserted the tx blob, we need to initialize it into a Payment so xrpl-py could process it
    my_tx_signed = Payment.from_dict(transaction_dict)

    tx = send_reliable_submission(transaction=my_tx_signed, client=client)

    tx_hash = tx.result['hash']
    tx_destination = tx.result['Destination']
    tx_xrp_amount = int(tx.result['Amount']) / 1000000
    tx_account = tx.result['Account']

    print(f"\n           XRPL Explorer: https://livenet.xrpl.org/transactions/{tx_hash}"
          f"\n         Transaction Hash: {tx_hash}"
          f"\n  Transaction Destination: {tx_destination}"
          f"\n           Transacted XRP: {tx_xrp_amount}"
          f"\n              Wallet Used: {tx_account}"
         )


if __name__ == '__main__':
    tx = "ENTER TX BLOB HERE"
    send_transaction(tx)
