from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import geneticAlgorithm as ga


class Routes(BaseModel):
    name: str
    possibleEdges: list[list]


app = FastAPI()
origins = ['http://localhost:4200', 'http://localhost']
app.add_middleware(CORSMiddleware, allow_origins=origins, allow_methods=["*"], allow_headers=["*"])


@app.post("/routes/{origin}")
async def route(routes: list[Routes], origin: str):

    distances_conv = ga.convert_to_distances(routes)
    ga.distances = distances_conv
    ga.origen = origin
    try:
        full_route = ga.genetic_algorithm()
        ga.max_values = []
        ga.avg_values = []
        ga.min_values = []
    except Exception as e:
        full_route = None

    return full_route
