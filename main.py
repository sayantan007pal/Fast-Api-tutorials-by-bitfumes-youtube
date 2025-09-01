from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"Data": "Blog list"}


@app.get('/blogs/unpublished')
def unpublished():
    # Fetch unpublished blog posts
    return {"Data": "Unpublished blog posts"}

@app.get('/blogs/{id}')
def show(id: int):
    #here the type of id  is specified to be int
    # Fetch blog post by id
    return {"Data": id}



"""
☁  Fast-Api-tutorials-by-bitfumes-youtube [main] uvicorn main:app --reload


INFO:     127.0.0.1:56602 - "GET /blogs/unpublished HTTP/1.1" 200 OK


{
"Data": "Unpublished blog posts"
}

"""

"""
Now the API is able to correctly identify the route for unpublished blog posts.
as the request path "/blogs/unpublished" matches the defined route 
as while running  the FastAPI application, it checks for exact matches first thus 
 path "/blogs/unpublished" is checked before the "blogs/{id}" route is checked.
"""