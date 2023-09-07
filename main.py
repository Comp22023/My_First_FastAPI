from fastapi import FastAPI

app = FastAPI()

@app.get("/sum/{var1}/{var2}")
async def sum(var1: int, var2: int):
    return {"Ваш номер билета": var1+var2}