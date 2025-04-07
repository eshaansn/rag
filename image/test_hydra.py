from omegaconf import OmegaConf
import hydra
from hydra.utils import instantiate

from rag_app.config_schemas import config_schema 

config_schema.setup_config()

@hydra.main(config_path="rag_app/configs", config_name="config", version_base=None)  # Adjust paths accordingly
def main(config):
    # print(OmegaConf.to_yaml(config))  # Prints the entire config in YAML format

    # documents = instantiate(config.database.loader).load()
    # print(instantiate(config.database.loader).cwd())
    # print(f"Documents: {documents[:5]}")
    # text_splitter = instantiate(config.database.text_splitter)
    # chunks = text_splitter.split_documents(documents)
    embeddings = instantiate(config.models.embedding_model).get_embedding_function()
    db = instantiate(config.database.vector_database)
    db = db(embedding_function=embeddings).create_database()

    results = db.similarity_search_with_score('What is Monopoly Deal?', k=3)
    print(f"Results: {results}")

    # print(embeddings.get_embedding_function())  # Call the method to get the embedding function
    # print(database.create_database())

if __name__ == "__main__":
    main()