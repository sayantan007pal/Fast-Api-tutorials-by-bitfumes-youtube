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

@app.get('/blogs/unpublished')
def unpublished():
    # Fetch unpublished blog posts
    return {"Data": "Unpublished blog posts"}

"""
☁  Fast-Api-tutorials-by-bitfumes-youtube [main] uvicorn main:app --reload


INFO:     127.0.0.1:53877 - "GET /blog/unpublished HTTP/1.1" 422 Unprocessable Content


{
"detail": [
    {
        "type": "int_parsing",
        "loc": [
            "path",
            "id"
        ],
        "msg": "Input should be a valid integer, unable to parse string as an integer",
        "input": "unpublished"
    }
]
}

"""

"""
here error is coming as fastAPI read routes like a ladder i.e
 1. It checks for exact matches first
 2. If no exact match is found, it checks for path parameters
 3. Finally, it checks for query parameters

thus the error is occurring because FastAPI is trying to match the request path "/blog/unpublished" with the defined routes "/blog/{id}" and is getting confused because "unpublished" is not a valid integer.
"""