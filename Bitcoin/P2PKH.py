import base58

def bitcoin_address_validation(bitcoinAddress):
    """
    Base58 (P2PKH)
    """
    try:
        base58Decoder = base58.b58decode(bitcoinAddress).hex()
        prefixAndHash = base58Decoder[:len(base58Decoder) - 8]
        checksum = base58Decoder[len(base58Decoder) - 8:]
        hash = prefixAndHash
        for x in range(1, 3):
            hash = hashlib.sha256(binascii.unhexlify(hash)).hexdigest()
        if (checksum == hash[:8]):
            valid = True
        else:
            valid = False
    except:
        valid = False
        pass
    return valid
