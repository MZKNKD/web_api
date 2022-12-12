import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/menta")
async def calc_numbers(a, b):
    return int(a) * int(b)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
