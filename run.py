import requests
import threading
import time
from mnemonic import Mnemonic
from bip_utils import Bip39SeedGenerator, Bip44, Bip44Coins

# Config
MAX_THREADS = 10
lock = threading.Lock()

def generate_wallet():
    mnemo = Mnemonic("english")
    words = mnemo.generate(strength=256)
    seed_bytes = Bip39SeedGenerator(words).Generate()
    bip44_ctx = Bip44.FromSeed(seed_bytes, Bip44Coins.STELLAR)
    public_key = bip44_ctx.PublicKey().ToAddress()
    return words, public_key

def check_balance(public_key):
    url = f"https://api2.mainnet.minepi.com/accounts/{public_key}"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            for balance in data.get("balances", []):
                if balance["asset_type"] == "native":
                    return True, balance["balance"]
            return True, "0.0000000"
        return False, f"Status: {response.status_code}"
    except Exception as e:
        return False, f"Error: {str(e)}"

def scan_wallet():
    while True:
        words, pubkey = generate_wallet()
        found, balance = check_balance(pubkey)

        if found:
            with lock:
                print("\n==============================")
                print(f"[✅ FOUND WALLET WITH BALANCE]")
                print(f"Mnemonic: {words}")
                print(f"Public Key: {pubkey}")
                print(f"Balance: {balance}")
                print("==============================\n")

                with open("wallet.txt", "a") as f:
                    f.write(f"{pubkey}\n{words}\nBalance: {balance}\n\n")
        else:
            print(f"[❌] {pubkey} not found.")

        time.sleep(0.1)

if __name__ == "__main__":
    for _ in range(MAX_THREADS):
        t = threading.Thread(target=scan_wallet)
        t.daemon = True
        t.start()

    while True:
        time.sleep(10)
