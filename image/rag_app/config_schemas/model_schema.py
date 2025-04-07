from typing import Optional

from hydra.core.config_store import ConfigStore
from omegaconf import MISSING
from dataclasses import dataclass, field
from rag_app.config_schemas.models import chat_models_schema, embedding_models_schema


@dataclass
class ModelConfig:
    chat_model: chat_models_schema.ChatModelConfig = MISSING
    embedding_model: embedding_models_schema.EmbeddingConfig = MISSING

def setup_config() -> None:
    chat_models_schema.setup_config()
    embedding_models_schema.setup_config()

    cs = ConfigStore.instance()
    cs.store(name="model_schema", node=ModelConfig, group="models")



