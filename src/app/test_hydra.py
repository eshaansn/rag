from omegaconf import OmegaConf
import hydra
from hydra.utils import instantiate

from app.config_schemas import config_schema 

config_schema.setup_config()

@hydra.main(config_path="configs", config_name="config", version_base=None)  # Adjust paths accordingly
def main(config):
    print(OmegaConf.to_yaml(config))  # Prints the entire config in YAML format

    # embeddings = instantiate(config.embedding)
    # database = instantiate(config.database)
    # database = database(embedding_function=embeddings.get_embedding_function())  # Pass the embedding function to the database
    db = instantiate(config.database.vector_database)
    embeddings = instantiate(config.models.embedding_model).get_embedding_function()
    db = db(embedding_function=embeddings).create_database()

    results = db.similarity_search_with_score('What is Monopoly Deal?', k=3)
    print(f"Results: {results}")

    # print(embeddings.get_embedding_function())  # Call the method to get the embedding function
    # print(database.create_database())

if __name__ == "__main__":
    main()