from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/primeNumber", StaticFiles(directory="static"), name="static")

class NumberRequest(BaseModel):
    number: int

def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

@app.post("/is_prime")
async def check_prime(request: NumberRequest):
    result = is_prime(request.number)
    return {"number": request.number, "is_prime": result}



@app.get("/")
async def root():
    return {"message": "Welcome! Static.. files are served at /static"}
