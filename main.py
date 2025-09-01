from fastapi import FastAPI

app = FastAPI()

@app.get("/blogs")
def index(limit:int, published: bool):
    if published:
        return {"Data": f"Published blog posts with limit {limit}"}
    else:
        return {"Data": f"Unpublished blog posts with limit {limit}"}




"""
☁  Fast-Api-tutorials-by-bitfumes-youtube [main] uvicorn main:app --reload


INFO:     127.0.0.1:53505 - "GET /blogs?limit=47&published=true HTTP/1.1" 200 OK


{
"Data": "Published blog posts with limit 47"
}

INFO:     127.0.0.1:53735 - "GET /blogs?limit=47&published=false HTTP/1.1" 200 OK


{
"Data": "Unpublished blog posts with limit 47"
}        


INFO:     127.0.0.1:54311 - "GET /blogs?limit=47 HTTP/1.1" 422 Unprocessable Content


{
"detail": [
{
"type": "missing",
"loc": [
"query",
"published"
],
"msg": "Field required",
"input": null
}
]
}

"""

