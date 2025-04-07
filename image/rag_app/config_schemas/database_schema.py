from typing import Optional

from hydra.core.config_store import ConfigStore
from omegaconf import MISSING
from dataclasses import dataclass, field
from rag_app.config_schemas.database import vector_databases_schema, loaders_schema, text_splitters_schema


@dataclass
class DatabaseConfig:
    vector_database: vector_databases_schema.VectorDatabaseConfig = MISSING
    loader: loaders_schema.LoaderConfig = MISSING
    text_splitter: text_splitters_schema.TextSplitterConfig = MISSING

def setup_config() -> None:
    vector_databases_schema.setup_config()
    loaders_schema.setup_config()
    text_splitters_schema.setup_config()

    cs = ConfigStore.instance()
    cs.store(name="database_schema", node=DatabaseConfig, group="database")