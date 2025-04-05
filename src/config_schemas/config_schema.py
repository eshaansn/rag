from typing import Optional

from hydra.core.config_store import ConfigStore
from omegaconf import MISSING
from dataclasses import dataclass, field
from config_schemas import database_schema, embedding_schema, loaders_schema, text_splitters_schema


@dataclass
class Config:   
    database: database_schema.VectorDatabaseConfig = field(default_factory=database_schema.VectorDatabaseConfig)
    loader: loaders_schema.LoaderConfig = field(default_factory=loaders_schema.PDFLoaderConfig)
    text_splitter: text_splitters_schema.TextSplitterConfig = field(default_factory=text_splitters_schema.RecursiveCharacterTextSplitterConfig)
    embedding: embedding_schema.EmbeddingConfig = field(default_factory=embedding_schema.EmbeddingConfig)

def setup_config() -> None:
    embedding_schema.setup_config()
    database_schema.setup_config()
    loaders_schema.setup_config()
    text_splitters_schema.setup_config()

    cs = ConfigStore.instance()
    cs.store(name="config_schema", node=Config)