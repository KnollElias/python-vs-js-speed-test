from fastapi import FastAPI
import time
import requests
import uvicorn

app = FastAPI()

@app.get("/")
async def root():
    start = time.time()
    response = {"message": "Hello from FastAPI"}
    end = time.time()
    return {"response": response, "time_taken": end - start}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
