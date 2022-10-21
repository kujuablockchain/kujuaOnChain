from cryptography.hazmat.primitives import serialization
from binascii import hexlify, unhexlify


class Wallet:
    def __init__(self):
        try:
            # *********** Wallet settings ***********
            self.wallet_address = ""
            self.private_key_encrypted = ""  # PEM format
            self.passphrase = ""
            if self.private_key_encrypted != "":
                self.private_key_decrypted = serialization.load_pem_private_key(
                    data=unhexlify(self.private_key_encrypted.encode("utf-8")),
                    password=self.passphrase.encode("utf-8"),
                )
        except:
            raise Exception(
                "You may be missing some inputs in the file under the kujuaRelayChain module at kujuaRelayChain.Client.inputs. Please fill those in first and try again."
            )


wallet = Wallet()


class Node:
    def __init__(self):
        # *********** Gateway settings **********
        # Get these values from the /info page of a gateway
        self.node_url = "http://testnet.kujua.org"
        self.gt_node_url = "http://testnet.kujua.org"


node = Node()


class Dummy:
    def __init__(self):
        # ********* Transaction settings ********
        self.amount = 0.0002
        self.recipient_address = ""


dummy = Dummy()


class Contract:
    def __init__(self):
        # -----------------------------------------------------------------------
        # ************ Contract Import Modules ************
        # needed for the contract example below. All modules that a gateway
        # supports are imported with a trailing _jua outside of the contract code
        # -----------------------------------------------------------------------
        import datetime as datetime_jua

        example_code = """
class Contract():
    def results(self, days, passed_results: dict):
        calculated_date = (datetime_jua.datetime.utcnow() + datetime_jua.timedelta(days=days)).strftime("%Y-%m-%d")
        return {'status': 'complete', 'contents': "{} days from today the date will be {}".format(days, calculated_date)}

contract = Contract()
"""
        # --------------------------------- end ---------------------------------

        # Standard smart contract creation values
        self.standard_contract_address = ""
        self.standard_contract = {}
        if self.standard_contract_address != "":
            self.standard_contract[self.standard_contract_address] = {
                "description": "this is a description of what this contract does.",
                "executable": hexlify(str(example_code).encode("utf-8")).decode(
                    "utf-8"
                ),
            }

        # Binded smart contract creation values
        self.binded_contract_address = ""
        self.binded_contract = {}
        if self.binded_contract_address != "":
            self.binded_contract[self.binded_contract_address] = {
                "description": "this is a description of what this cluster does.",
                "executable": hexlify(str(example_code).encode("utf-8")).decode(
                    "utf-8"
                ),
            }

        # Term creation values
        self.term_address = ""
        self.term = {}
        if self.term_address != "":
            self.term[self.term_address] = {
                "type": "pre",
                # one of 'pre' or 'post' meaning this contract runs before or after a contract runs, terms are 'pre' by default. A 'post' run is necessary if we need to overide a contracts result if it violates the term
                "description": "this is a description of what this term does e.g regulates that contracts should be less than a thousand years in duration.",
                "executable": hexlify(str(example_code).encode("utf-8")).decode(
                    "utf-8"
                ),
            }


contract = Contract()


class Cluster:
    def __init__(self):
        # Cluster creation settings
        self.cluster_address = (
            "cx5ef02d1a8e45bb005f5f388c8125ed95e536536f6df8544c39a424e19a147a40"
        )
        self.terms = [
            "tx835face552f097e86d51407af7627df8e07566e419555c141fcbde72e7dc683b"
        ]
        self.enforcement_cycle = 30
        self.monthly_min_amount = 0.5759
        self.monthly_min_percentage = 10
        self.monthly_min_percentage_desc = "total_outgoing_balance divided by 2"
        self.monthly_min_percentage_calc = "total_outgoing_balance / 2"
        self.enforced_duration = 44
        self.poll_date_cycle = "01--28--01--02--03--12"
        self.poll_activation_population = 4000
        self.poll_membership_duration = 0
        self.poll_member_active_duration = 0
        self.cvi_poll_type = 1
        self.cvi_verifier_addresses = [
            "0x59a4e48cc661b10ea598f20088df4572f12d6a8caa08f3136d7af01efdb6497a"
        ]
        self.cvi_threshold = 70
        self.cvi_dissolve_threshold = 67
        self.cvi_addresses_recalc_cycle = "01--28--01"
        self.cvi_signature_expiration_cycle = "01--28--01"

        self.obj_create_temp_dict = {}


cluster = Cluster()
