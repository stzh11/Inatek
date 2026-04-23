import uvicorn

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8081, reload=False, log_level="debug")