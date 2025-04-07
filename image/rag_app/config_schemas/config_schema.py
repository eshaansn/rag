from typing import Optional

from hydra.core.config_store import ConfigStore
from omegaconf import MISSING
from dataclasses import dataclass, field
from rag_app.config_schemas import database_schema, model_schema

@dataclass
class Config:
    database: database_schema.DatabaseConfig = MISSING
    models: model_schema.ModelConfig = MISSING

def setup_config() -> None:
    model_schema.setup_config()
    database_schema.setup_config()

    cs = ConfigStore.instance()
    cs.store(name="config_schema", node=Config)