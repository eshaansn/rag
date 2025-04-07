from pydantic.dataclasses import dataclass
from pydantic import Field
from typing import Optional, Callable, Union, Tuple, Any

from hydra.core.config_store import ConfigStore
from omegaconf import MISSING, SI

from langchain_chroma import Chroma


@dataclass
class VectorDatabaseConfig():
    _target_: str = MISSING

@dataclass
class ChromaDBConfig(VectorDatabaseConfig):
    _target_: str = "rag_app.database.vector_databases.ChromaDB"
    _partial_: bool = True
    collection_name: str = 'rag'
    persist_directory: str = 'rag_app/data/chroma'
    collection_metadata: Optional[dict] = None
    client: Optional[Any] = None
    client_settings: Optional[Any] = None
    relevance_score_fn: Optional[Any] = None
    # create_collection_if_not_exists: Optional[bool] = True

def setup_config() -> None:

    cs = ConfigStore.instance()
    cs.store(
        name="chroma_schema",
        group="database/vector_database",
        node=ChromaDBConfig,
    )