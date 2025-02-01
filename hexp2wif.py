import hashlib
import base58

def hex_to_wif(hex_key):
    # Step 1: Add version byte (0x80 for mainnet)
    version_byte = b'\x80'
    hex_key_bytes = bytes.fromhex(hex_key)
    extended_key = version_byte + hex_key_bytes

    # Step 2: Perform double SHA-256 hash on the extended key
    sha256_1 = hashlib.sha256(extended_key).digest()
    sha256_2 = hashlib.sha256(sha256_1).digest()

    # Step 3: Take the first 4 bytes of the double hash (checksum)
    checksum = sha256_2[:4]

    # Step 4: Append the checksum to the extended key
    final_key = extended_key + checksum

    # Step 5: Encode the result in Base58
    wif = base58.b58encode(final_key)
    return wif.decode('utf-8')

# Example usage:
hex_key = '000000000000000000000000000000000000000000000002832ed74f2b5e35ee'
wif_key = hex_to_wif(hex_key)
print(f"WIF: {wif_key}")
