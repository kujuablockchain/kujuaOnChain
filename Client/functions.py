from requests import get, models
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.ed25519 import (
    Ed25519PrivateKey,
    Ed25519PublicKey,
)


def calculate_fees(amount: float, node_url: str, recipient_address: str):
    try:
        api_data = get(
            node_url
            + "/transact_onchain"
            + "?function=calculate_fees"
            + "&f_args="
            + str(
                (
                    amount,
                    node_url,
                    recipient_address,
                )
            )
        )

        if api_data.status_code != 200:
            _message = "Unable to complete request with error response: {}".format(
                api_data.json()
            )
            return {"status": "error", "content": _message}
        else:
            results = api_data.json()
            return results

    except:
        _message = "The gateway you are trying to connect to may be offline, please try again later"
        return {"status": "error", "content": _message}


def broadcast(
    wallet_address: str,
    private_key_decrypted: str,
    passphrase: str,
    amount: float,
    fee: float,
    node_url: str,
    node_val_url: str,
    recipient_address: str,
    recipients_node_url: str,
    network_limit_lock_days: int,
    network_coinid_lock_days: int,
    intended_destination_address: str,
    source: str,
    contract_args: tuple,
    obj_creation_dict: dict,
    post_results: bool,
    gt_node_url: str,
    contract_interaction: bool,
):

    try:
        api_data = get(
            node_url
            + "/transact_onchain"
            + "?function=broadcast"
            + "&f_args="
            + str(
                (
                    wallet_address,
                    private_key_decrypted,
                    passphrase,
                    amount,
                    fee,
                    node_url,
                    node_val_url,
                    recipient_address,
                    recipients_node_url,
                    network_limit_lock_days,
                    network_coinid_lock_days,
                    intended_destination_address,
                    source,
                    contract_args,
                    obj_creation_dict,
                    post_results,
                    gt_node_url,
                    contract_interaction,
                )
            )
        )

        if api_data.status_code != 200:
            _message = "Unable to complete request with error response: {}".format(
                api_data.json()
            )
            return {"status": "error", "content": _message}
        else:
            return api_data.json()

    except:
        _message = "The gateway you are trying to connect to may be offline, please try again later"
        return {"status": "error", "content": _message}


def get_account_balance(node_url: str, wallet_address: str):
    try:
        api_data = get(
            node_url
            + "/transact_onchain"
            + "?function=get_account_balance"
            + "&f_args="
            + str((wallet_address,))
        )

        if api_data.status_code != 200:
            _message = "Unable to complete request with error response: {}".format(
                api_data.json()
            )
            return {"status": "error", "content": _message}
        else:
            results = api_data.json()
            return results

    except:
        _message = "The gateway you are trying to connect to may be offline, please try again later"
        return {"status": "error", "content": _message}


def get_dummy_coins(node_url: str, recipient_address: str):

    try:
        api_data = get(
            node_url
            + "/transact_onchain"
            + "?function=get_dummy_coins"
            + "&f_args="
            + str(
                (
                    node_url,
                    recipient_address,
                )
            )
        )

        if api_data.status_code != 200:
            _message = "Unable to complete request with error response: {}".format(
                api_data.json()
            )
            return {"status": "error", "content": _message}
        else:
            results = api_data.json()
            return results

    except:
        _message = "The gateway you are trying to connect to may be offline, please try again later"
        return {"status": "error", "content": _message}


def new_cluster(
    node_url: str,
    enforced_duration: int,
    enforcement_cycle: int,
    cvi_threshold: float,
    cvi_dissolve_threshold: float,
    monthly_min_percentage: float,
    monthly_min_percentage_desc: str,
    cvi_poll_type: int,
    cvi_verifier_addresses: str,
    poll_date_cycle: str,
    cluster_address: str,
    terms: list,
    monthly_min_amount: str,
    monthly_min_percentage_calc: str,
    poll_activation_population: int,
    poll_membership_duration: int,
    poll_member_active_duration: int,
    cvi_addresses_recalc_cycle: str,
    cvi_signature_expiration_cycle: str,
    passphrase: str,
):

    try:
        api_data = get(
            node_url
            + "/transact_onchain"
            + "?function=new_cluster"
            + "&f_args="
            + str(
                (
                    enforced_duration,
                    enforcement_cycle,
                    cvi_threshold,
                    cvi_dissolve_threshold,
                    monthly_min_percentage,
                    monthly_min_percentage_desc,
                    cvi_poll_type,
                    cvi_verifier_addresses,
                    poll_date_cycle,
                    cluster_address,
                    terms,
                    monthly_min_amount,
                    monthly_min_percentage_calc,
                    poll_activation_population,
                    poll_membership_duration,
                    poll_member_active_duration,
                    cvi_addresses_recalc_cycle,
                    cvi_signature_expiration_cycle,
                    passphrase,
                )
            )
        )

        if api_data.status_code != 200:
            _message = "Unable to complete request with error response: {}".format(
                api_data.json()
            )
            return {"status": "error", "content": _message}
        else:
            results = api_data.json()
            return results

    except:
        _message = "The gateway you are trying to connect to may be offline, please try again later"
        return {"status": "error", "content": _message}


def generate_address(passphrase: bytes, address_type_indicator: str):
    private_key_decrypted = Ed25519PrivateKey.generate()
    private_key_raw = private_key_decrypted.private_bytes(
        encoding=serialization.Encoding.Raw,
        format=serialization.PrivateFormat.Raw,
        encryption_algorithm=serialization.NoEncryption(),
    )
    private_key_raw_hex = private_key_raw.hex()
    private_key_encrypted = private_key_decrypted.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.BestAvailableEncryption(
            passphrase.encode("utf-8")
        ),
    )
    private_key_encrypted_hex = private_key_encrypted.hex()

    public_key = private_key_decrypted.public_key()
    public_key = public_key.public_bytes(
        encoding=serialization.Encoding.Raw, format=serialization.PublicFormat.Raw
    )
    public_key_hex = public_key.hex()
    public_key_hex = address_type_indicator + public_key_hex

    results = {
        "address": public_key_hex,
        "private_key_encrypted": private_key_encrypted_hex,
        "private_key_raw": private_key_raw_hex,  # For those that want the raw unencrypted private key
        "notes": "",
    }

    return {"status": "complete", "content": results}
