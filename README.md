# Pi Wallet Scanner

This Python project generates random Pi wallets using BIP39 mnemonic phrases and checks their balance via the Pi Network API. If a wallet with any balance is found, it saves the mnemonic and public key to `wallet.txt`.

---

## Features

- Generate Pi wallets from BIP39 mnemonic (256 bits strength)
- Check wallet balance using Pi Network API
- Multi-threaded scanning (default 10 threads)
- Save wallets with non-zero balance to a file

---

## Requirements

- Python 3.7 or higher
- The following Python libraries:
  - `requests`
  - `mnemonic`
  - `bip_utils`

---

## Installation

1. Clone or download this repository.

2. (Optional) Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install dependencies:
    ```bash
    pip install -r requirements.txt

4. Run
    ```bash
    python run.py