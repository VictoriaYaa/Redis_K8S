import os
import time
import requests
import redis
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables from .env file
load_dotenv()

# Redis connection details from environment variables
REDIS_HOST = os.getenv('REDIS_HOST')
REDIS_PORT = os.getenv('REDIS_PORT')
REDIS_DB = os.getenv('REDIS_DB')
REDIS_PASSWORD = os.getenv('REDIS_PASSWORD')    

# Initialize Redis connection
redis_client = redis.StrictRedis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    db=REDIS_DB,
    password=REDIS_PASSWORD,
    decode_responses=True
)

# API endpoint for Bitcoin ticker
API_URL = 'https://api.blockchain.com/v3/exchange/tickers/BTC-USD'


# GET request to the Bitcoin API to retrieve the latest Bitcoin price
def fetch_bitcoin_price():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        data = response.json()
        return data['last_trade_price']
    except requests.RequestException as e:
        print(f"Error fetching Bitcoin price: {e}")
        return None

# Saving the price to Redis

def save_price_to_redis(price):
    timestamp = datetime.now().isoformat()
    redis_client.set(timestamp, price)
    print(f"Saved price {price} at timestamp {timestamp}")

def main():
    while True:
        price = fetch_bitcoin_price()
        if price is not None:
            save_price_to_redis(price)
        time.sleep(300) # Every 5 min

if __name__ == "__main__":
    main()