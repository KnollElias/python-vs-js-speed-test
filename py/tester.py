import requests
import time

url = "http://127.0.0.1:8000/"

start_time = time.time()
for _ in range(1000):  # Send 1000 requests
    requests.get(url)
end_time = time.time()

print(f"Total time for 1000 requests: {end_time - start_time:.4f} seconds")
