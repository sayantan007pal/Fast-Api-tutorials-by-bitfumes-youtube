from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"Data": "Blog list"}


@app.get('/blog/{id}')
def show(id):
    #here the type of id  is not specified so by default it becomes string
    return {"Data": id}

"""
☁  Fast-Api-tutorials-by-bitfumes-youtube [main] uvicorn main:app --reload
INFO:     Will watch for changes in these directories: ['/Users/sayantanpal100/Desktop/Udemy Projects/Fast-Api-tutorials-by-bitfumes-youtube']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [35486] using StatReload
INFO:     Started server process [35489]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     127.0.0.1:62241 - "GET / HTTP/1.1" 200 OK
INFO:     127.0.0.1:62281 - "GET /blog HTTP/1.1" 404 Not Found
INFO:     127.0.0.1:62328 - "GET /blog/200 HTTP/1.1" 200 OK
INFO:     127.0.0.1:62361 - "GET /blog/sdfsfsfgvsfvsdf HTTP/1.1" 200 OK


{
"Data": "sdfsfsfgvsfvsdf"
}



"""