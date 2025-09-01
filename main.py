from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"Hello": "World"}




"""
☁  Fast-Api-tutorials-by-bitfumes-youtube [main] ⚡  uvicorn main:app --reload
INFO:     Will watch for changes in these directories: ['/Users/sayantanpal100/Desktop/Udemy Projects/Fast-Api-tutorials-by-bitfumes-youtube']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [7611] using StatReload
INFO:     Started server process [7613]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     127.0.0.1:49566 - "GET / HTTP/1.1" 404 Not Found
WARNING:  StatReload detected changes in 'main.py'. Reloading...
INFO:     Shutting down
INFO:     Waiting for application shutdown.
INFO:     Application shutdown complete.
INFO:     Finished server process [7613]
INFO:     Started server process [9114]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     127.0.0.1:50384 - "GET / HTTP/1.1" 200 OK
INFO:     127.0.0.1:50394 - "GET / HTTP/1.1" 200 OK
INFO:     127.0.0.1:50394 - "GET / HTTP/1.1" 200 OK



"""