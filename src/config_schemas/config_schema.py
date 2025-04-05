from typing import Optional

from hydra.core.config_store import ConfigStore
from omegaconf import MISSING
from dataclasses import dataclass, field
from . import database_schema, model_schema

@dataclass
class Config:
    database: database_schema.DatabaseConfig = field(default_factory=lambda: database_schema.DatabaseConfig)
    models: model_schema.ModelConfig = field(default_factory=lambda: model_schema.ModelConfig)

def setup_config() -> None:
    model_schema.setup_config()
    database_schema.setup_config()

    cs = ConfigStore.instance()
    cs.store(name="config_schema", node=Config)