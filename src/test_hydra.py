from omegaconf import OmegaConf
import hydra
from hydra.utils import instantiate

from config_schemas import config_schema 

config_schema.setup_config()

@hydra.main(config_path="configs", config_name="config", version_base=None)  # Adjust paths accordingly
def main(config):
    print(OmegaConf.to_yaml(config))  # Prints the entire config in YAML format

    # embeddings = instantiate(config.embedding)
    # database = instantiate(config.database)
    # database = database(embedding_function=embeddings.get_embedding_function())  # Pass the embedding function to the database


    # print(embeddings.get_embedding_function())  # Call the method to get the embedding function
    # print(database.create_database())

if __name__ == "__main__":
    main()