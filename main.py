from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel


class Routes(BaseModel):
    name: str
    possibleEdges: list[list]


app = FastAPI()
origins = ['http://localhost:4200', 'http://localhost']
app.add_middleware(CORSMiddleware, allow_origins=origins, allow_methods=["*"], allow_headers=["*"])


@app.post("/routes/{origin}")
async def route(routes: list[Routes], origin: str):

    return {"origin": origin, "routes": routes}
