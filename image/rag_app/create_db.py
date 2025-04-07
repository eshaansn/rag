import hydra
from hydra.utils import instantiate
from omegaconf import OmegaConf
from database.data_utils import add_to_chroma, clear_database
from config_schemas import config_schema 

config_schema.setup_config()

@hydra.main(config_path="configs", config_name="config", version_base=None) 
def main(config):

    documents = instantiate(config.database.loader).load()
    # print(instantiate(config.database.loader).cwd())
    # print(f"Documents: {documents[:5]}")
    text_splitter = instantiate(config.database.text_splitter)
    chunks = text_splitter.split_documents(documents)
    embeddings = instantiate(config.models.embedding_model).get_embedding_function()
    db = instantiate(config.database.vector_database)
    db = db(embedding_function=embeddings).create_database()

    add_to_chroma(chunks, db)

if __name__ == "__main__":
    main()
