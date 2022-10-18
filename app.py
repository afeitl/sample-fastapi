from fastapi import FastAPI

app = FastAPI(title="Sample Fastapi")


@app.get("/")
async def root():

    jsonStr = "{""message"": ""Hi there, World""}"
    return jsonStr

