import uvicorn
from fastapi import FastAPI
from mangum import Mangum
from pydantic import BaseModel
from app.query_rag import QueryResponse, query_rag
from app.config_schemas import config_schema
from hydra import compose, initialize
from hydra.utils import instantiate


app = FastAPI()
handler = Mangum(app)  # Entry point for AWS Lambda.


class SubmitQueryRequest(BaseModel):
    query_text: str


# Load config once at startup
with initialize(version_base=None, config_path="app/configs"):
    config = compose(config_name="config")


def perform_query(query_text: str) -> QueryResponse:
    # Create DB connection using config
    db = instantiate(config.database.vector_database)
    embeddings = instantiate(config.models.embedding_model).get_embedding_function()
    db = db(embedding_function=embeddings).create_database()

    
    # Return the query response
    return query_rag(config, query_text=query_text, db=db)


@app.get("/")
def index():
    return {"Hello": "World"}


@app.post("/submit_query")
def submit_query_endpoint(request: SubmitQueryRequest) -> QueryResponse:
    query_response = perform_query(request.query_text)
    return query_response


if __name__ == "__main__":
    # Run this as a server directly.
    port = 8000
    print(f"Running the FastAPI server on port {port}.")
    uvicorn.run("app_api_handler:app", host="localhost", port=port)