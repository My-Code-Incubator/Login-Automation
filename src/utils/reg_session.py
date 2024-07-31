import os
import hmac
import hashlib
from datetime import datetime

def generate_signature():
  micro_seconds = datetime.now().strftime("%f")  
  SECRET_KEY = os.getenv("SECRET_KEY")
  timestamp = str(micro_seconds)
  message = timestamp.encode("utf-8")
  signature = hmac.new(SECRET_KEY.encode("utf-8"), message, hashlib.sha256).hexdigest()
  print(signature)
  return signature

if __name__ == "__main__":
  generate_signature()