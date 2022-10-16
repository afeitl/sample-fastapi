from fastapi import FastAPI

app = FastAPI(title="Sample Fastapi")


@app.get("/")
async def root():
    return {"message": "Hi there, World"}
