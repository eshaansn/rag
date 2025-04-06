from dataclasses import dataclass
from typing import List
from langchain.prompts import ChatPromptTemplate
from langchain_aws import ChatBedrock
from langchain_huggingface import ChatHuggingFace
from langchain_huggingface import HuggingFaceEndpoint
import hydra
from hydra.utils import instantiate
from omegaconf import DictConfig, OmegaConf
from app.config_schemas import config_schema

config_schema.setup_config()
# from rag_app.get_chroma_db import get_chroma_db

PROMPT_TEMPLATE = """
Answer the question based only on the following context:

{context}

---

Answer the question based on the above context: {question}
"""


@dataclass
class QueryResponse:
    query_text: str
    response_text: str
    sources: List[str]


def query_rag(config: DictConfig, query_text: str, db) -> QueryResponse:

    # Search the DB.
    results = db.similarity_search_with_score(query_text, k=3)

    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query_text)

    # print(f"Prompt: {prompt}")

    model = instantiate(config.models.chat_model).get_model()
 
    response = model.invoke(prompt)
    response_text = response.content

    sources = [doc.metadata.get("id", None) for doc, _score in results]

    return QueryResponse(
        query_text=query_text, response_text=response_text, sources=sources
    )

@hydra.main(config_path="configs", config_name="config", version_base=None) 
def main(config: DictConfig):
    print(OmegaConf.to_yaml(config))

    db = instantiate(config.database.vector_database)
    embeddings = instantiate(config.models.embedding_model).get_embedding_function()
    db = db(embedding_function=embeddings).create_database()

    respone = query_rag(config, query_text="In monopoly deal, can you use house cards as cash?", db=db)

    return f"Response: {respone.response_text}\nSources: {respone.sources}"


if __name__ == "__main__":
    main()
