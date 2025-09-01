from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"Data": "Blog list"}


@app.get('/blog/{id}')
def show(id: int):
    #here the type of id  is specified to be int
    # Fetch blog post by id
    return {"Data": id}



"""
☁  Fast-Api-tutorials-by-bitfumes-youtube [main] uvicorn main:app --reload
INFO:     Will watch for changes in these directories: ['/Users/sayantanpal100/Desktop/Udemy Projects/Fast-Api-tutorials-by-bitfumes-youtube']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [74075] using StatReload
INFO:     Started server process [74077]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     127.0.0.1:65195 - "GET /item_type/134jdnvjhbenfbvdfl HTTP/1.1" 404 Not Found
INFO:     127.0.0.1:65221 - "GET / HTTP/1.1" 200 OK
INFO:     127.0.0.1:65264 - "GET /1003949 HTTP/1.1" 404 Not Found
INFO:     127.0.0.1:65369 - "GET /blog/1003949 HTTP/1.1" 200 OK



{
"Data": 1003949
}


INFO:     127.0.0.1:49263 - "GET /blog/1003949hjggfhgfgchfc HTTP/1.1" 422 Unprocessable Content


{
"detail": [
    {
        "type": "int_parsing",
        "loc": [
            "path",
            "id"
        ],
        "msg": "Input should be a valid integer, unable to parse string as an integer",
        "input": "1003949hjggfhgfgchfc"
    }
]
}

"""