from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get("/blogs")
def index(limit:int=10, published: Optional[bool]=None):    # here for the query parameters like limit and published, limit is set to 10 by default and published is optional so if any value of limit is given then it will take that value otherwise it will take the default value and for published if no value is given then it will take the default value of None
    if published:
        return {"Data": f"Published blog posts with limit {limit}"}
    else:
        return {"Data": f"Unpublished blog posts with limit {limit}"}




"""
☁  Fast-Api-tutorials-by-bitfumes-youtube [main] uvicorn main:app --reload


INFO:     127.0.0.1:58467 - "GET /blogs?limit=23&published=false HTTP/1.1" 200 OK


{
"Data": "Unpublished blog posts with limit 23"
}



INFO:     127.0.0.1:58765 - "GET /blogs?published=false HTTP/1.1" 200 OK


{
"Data": "Unpublished blog posts with limit 10"
}     


INFO:     127.0.0.1:58995 - "GET /blogs?limit=23 HTTP/1.1" 200 OK


{
"Data": "Unpublished blog posts with limit 23"
}





"""

