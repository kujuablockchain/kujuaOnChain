# kujuaOnChain
Kujua blockchain main functionalities. You only need to change the values in 'inputs.py' file to your own for the function you want to run.

You can find more functionalities on the developer page at https://kujua.org/developer

Creating a wallet address:
```python
from kujuaOnChain.Client import inputs, functions

results = functions.generate_address(inputs.wallet.passphrase, '0x')
print(results)

# address type indicators are as follows
# 0x: standard wallet address
# sx: standard smart contract
# bx: binded contract
# cx: cluster
```


Requesting test dummy coins:

Only 0.0200 coins are given per account per hour, therefore when testing, send small amounts such as ~ 0.0002 so your funds do not deplete while testing.

```python
from kujuaOnChain.Client import inputs, functions

results = functions.get_dummy_coins(inputs.node.node_url, inputs.wallet.wallet_address)
print(results)
```



Get balance:

```python
from kujuaOnChain.Client import inputs, functions

results = functions.get_account_balance(inputs.node.node_url,
                                    	inputs.wallet.wallet_address)
print(results)
```



Determine fees for a transaction:

```python
from kujuaOnChain.Client import inputs, functions

fees = functions.calculate_fees(inputs.dummy.amount,
                                inputs.node.node_url,
                                inputs.dummy.recipient_address)
print(fees)
```



Broadcast a transaction:

```python
from kujuaOnChain.Client import inputs, functions

fees = functions.calculate_fees(inputs.dummy.amount,
                                inputs.node.node_url,
                                inputs.dummy.recipient_address)
print(fees)

broadcast = functions.broadcast(inputs.wallet.wallet_address,
                                inputs.wallet.private_key_encrypted,  # only use a dummy address's private key until we make kujuaOffChainRelay public
                                inputs.wallet.passphrase,
                                inputs.dummy.amount,
                                fees['content']['full_fee'],
                                inputs.node.node_url,
                                str(),
                                inputs.dummy.recipient_address,
                                str(),
                                0,
                                0,
                                str(),
                                str(),
                                (None,),
                                {},
                                True,
                                inputs.node.validator_node_url,
                                False)
print(broadcast)
```
You can then see your transaction on any running node or the blockchain explorer at http://testnet.kujua.org/explorer.

These are the standard functionalities. If you wish to execute smart contracts for clusters, staking etc then see the developer page at https://kujua.org/developer and use the same downloaded library.
