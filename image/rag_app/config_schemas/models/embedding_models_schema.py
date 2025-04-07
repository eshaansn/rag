from pydantic.dataclasses import dataclass
from dataclasses import field
from typing import Optional, Any, Dict

from hydra.core.config_store import ConfigStore
from omegaconf import MISSING

from langchain_aws import BedrockEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_openai import OpenAIEmbeddings


@dataclass
class EmbeddingConfig():
    _target_: str = MISSING

@dataclass
class BedrockEmbeddingConfig(EmbeddingConfig):
    _target_: str = "rag_app.models.embedding_models.BedrockEmbedding"
    model_id: str = 'amazon.titan-embed-text-v1'
    aws_access_key_id: Optional[str] = None
    aws_secret_access_key: Optional[str] = None
    region_name: Optional[str] = None
    endpoint_url: Optional[str] = None
    aws_session_token: Optional[str] = None
    normalize: Optional[bool] = True
    client: Optional[Any] = None
    model_kwargs: Optional[Dict[str, Any]] = field(default_factory=lambda: {})

@dataclass
class HuggingFaceEmbeddingConfig(EmbeddingConfig):
    _target_: str = "rag_app.models.embedding_models.HuggingFaceEmbedding"
    model_name: str = MISSING
    cache_folder: Optional[str] = None
    encode_kwargs: Optional[Dict[str, Any]] = field(default_factory=lambda: {})
    model_kwargs: Optional[Dict[str, Any]] = field(default_factory=lambda: {})
    show_progress: Optional[bool] = True
    multi_process: Optional[bool] = False

@dataclass
class OpenAIEmbeddingConfig(EmbeddingConfig):
    _target_: str = "rag_app.models.embedding_models.OpenAIEmbedding"
    model: str = "text-embedding-ada-002"
    dimension: Optional[int] = None
    api_key: Optional[str] = None
    organization: Optional[str] = None
    max_retries: int = 2
    request_timeout: Optional[float] = None


def setup_config() -> None:
    cs = ConfigStore.instance()
    cs.store(
        name="bedrock_embedding_model_schema",
        group="models/embedding_model",
        node=BedrockEmbeddingConfig
    )

    cs.store(
        name="huggingface_embedding_model_schema",
        group="models/embedding_model",
        node=HuggingFaceEmbeddingConfig
    )

    cs.store(
        name="openai_embedding_model_schema",
        group="models/embedding_model",
        node=OpenAIEmbeddingConfig
    )