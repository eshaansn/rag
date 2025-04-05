from dataclasses import dataclass
from typing import List
from langchain.prompts import ChatPromptTemplate
from langchain_aws import ChatBedrock
import hydra
from hydra.utils import instantiate
from omegaconf import DictConfig, OmegaConf
from config_schemas import config_schema

config_schema.setup_config()
# from rag_app.get_chroma_db import get_chroma_db

PROMPT_TEMPLATE = """
Answer the question based only on the following context:

{context}

---

Answer the question based on the above context: {question}
"""

# BEDROCK_MODEL_ID = "anthropic.claude-3-haiku-20240307-v1:0"


@dataclass
class QueryResponse:
    query_text: str
    response_text: str
    sources: List[str]

@hydra.main(config_path="configs", config_name="config", version_base=None) 
def main(config: DictConfig):
    db = instantiate(config.database)
    embeddings = instantiate(config.embedding).get_embedding_function()
    db = db(embedding_function=embeddings).create_database()

    query_rag(query_text="How much does a landing page cost to develop?", db=db)

def query_rag(query_text: str, db) -> QueryResponse:

    # Search the DB.
    results = db.similarity_search_with_score(query_text, k=3)
    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query_text)
    print(prompt)

    # model = ChatBedrock(model_id=BEDROCK_MODEL_ID)
    # response = model.invoke(prompt)
    # response_text = response.content

    # sources = [doc.metadata.get("id", None) for doc, _score in results]
    # print(f"Response: {response_text}\nSources: {sources}")

    # return QueryResponse(
    #     query_text=query_text, response_text=response_text, sources=sources
    # )


if __name__ == "__main__":
    main()
