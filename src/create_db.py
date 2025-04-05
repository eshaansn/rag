import argparse
import hydra
from hydra.utils import instantiate
from omegaconf import OmegaConf
from database.data_utils import add_to_chroma, clear_database
from config_schemas.config_schema import config_schema 

config_schema.setup_config()

@hydra.main(config_path="configs", config_name="config", version_base=None) 
def main(config):

    # Check if the database should be cleared (using the --clear flag).
    parser = argparse.ArgumentParser()
    parser.add_argument("--reset", action="store_true", help="Reset the database.")
    
    args = parser.parse_args()
    if args.reset:
        print("✨ Clearing Database")
        clear_database()

    # Create (or update) the data store.

    print(OmegaConf.to_yaml(config))

    documents = instantiate(config.loader).load()
    print(documents[:5])
    text_splitter = instantiate(config.text_splitter)
    chunks = text_splitter.split_documents(documents)
    embeddings = instantiate(config.embedding).get_embedding_function()
    db = instantiate(config.database)
    db = db(embedding_function=embeddings).create_database()

    add_to_chroma(chunks, db)

if __name__ == "__main__":
    main()
