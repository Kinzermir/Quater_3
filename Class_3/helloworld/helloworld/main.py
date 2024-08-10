from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"message": "Hello World"}


@app.post("/todo")
async def todopost():
    return {"message": "Hello World"}

@app.post("/todo2")
async def todopost_2():
    return {"message": "Hello World"}

