from typing import Optional

from hydra.core.config_store import ConfigStore
from omegaconf import MISSING
from dataclasses import dataclass, field
from config_schemas.database import vector_databases_schema, loaders_schema, text_splitters_schema


@dataclass
class DatabaseConfig:
    vector_database: vector_databases_schema.VectorDatabaseConfig = field(default_factory=lambda: vector_databases_schema.VectorDatabaseConfig())
    loader: loaders_schema.LoaderConfig = field(default_factory=lambda: loaders_schema.LoaderConfig())
    text_splitter: text_splitters_schema.TextSplitterConfig = field(default_factory=lambda: text_splitters_schema.TextSplitterConfig())

def setup_config() -> None:
    vector_databases_schema.setup_config()
    loaders_schema.setup_config()
    text_splitters_schema.setup_config()

    cs = ConfigStore.instance()
    cs.store(name="database_schema", node=DatabaseConfig, group="database")