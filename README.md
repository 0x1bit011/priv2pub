
![Snap 2025-01-23 at 5 32 26 PM](https://github.com/user-attachments/assets/14dbb2c6-04bd-4759-a4d8-e6262d9d7cb3)



Sure, here is a shell script that uses `openssl` to generate a Bitcoin private key and derive the corresponding public key. This script assumes you have `openssl` installed on your system.

```sh
#!/bin/bash

# Generate a new private key
openssl ecparam -name secp256k1 -genkey -noout -out private_key.pem

# Convert the private key to hexadecimal format
PRIVATE_KEY_HEX=$(openssl ec -in private_key.pem -text -noout | grep "priv:" -A 3 | tail -n +2 | tr -d '\n[:space:]:')

# Display the private key in hexadecimal format
echo "Private Key (hex): $PRIVATE_KEY_HEX"

# Derive the public key
openssl ec -in private_key.pem -pubout -out public_key.pem

# Convert the public key to hexadecimal format
PUBLIC_KEY_HEX=$(openssl ec -in private_key.pem -pubout -outform DER | tail -c 65 | xxd -p -c 65)

# Display the public key in hexadecimal format
echo "Public Key (hex): $PUBLIC_KEY_HEX"

# Clean up generated files
rm private_key.pem public_key.pem
```


**Explanation:**

1. **Generate a Private Key:**
   - `openssl ecparam -name secp256k1 -genkey -noout -out private_key.pem`: Generates a new EC private key using the secp256k1 curve and saves it to `private_key.pem`.

2. **Convert Private Key to Hexadecimal:**
   - The private key is extracted from the PEM file, converted to hexadecimal, and stored in the `PRIVATE_KEY_HEX` variable.

3. **Derive the Public Key:**
   - `openssl ec -in private_key.pem -pubout -out public_key.pem`: Derives the public key from the private key and saves it to `public_key.pem`.

4. **Convert Public Key to Hexadecimal:**
   - The public key is extracted from the PEM file in DER format, converted to hexadecimal, and stored in the `PUBLIC_KEY_HEX` variable.

5. **Display Keys:**
   - Both the private and public keys are printed in hexadecimal format.

6. **Clean Up:**
   - The generated PEM files are removed.

To run the script, save it to a file (e.g., `generate_keys.sh`), make it executable (`chmod +x generate_keys.sh`), and then execute it (`./generate_keys.sh`).
