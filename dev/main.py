from fastapi import FastAPI

app = FastAPI()


# Hello world
@app.get("/")
async def root():
    return {"message": "Hello World"}
