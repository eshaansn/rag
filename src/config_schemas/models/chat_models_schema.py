from pydantic.dataclasses import dataclass
from dataclasses import field
from typing import Optional, Any, Dict

from hydra.core.config_store import ConfigStore
from omegaconf import MISSING

from langchain_aws import BedrockEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_openai import OpenAIEmbeddings


@dataclass
class ChatModelConfig():
    _target_: str = MISSING

@dataclass
class BedrockChatModelConfig(ChatModelConfig):
    _target_: str = "models.chat_models.BedrockChatModel"
    model_id: Optional[str] = None
    aws_access_key_id: Optional[str] = None
    aws_secret_access_key: Optional[str] = None
    aws_session_token: Optional[str] = None
    beta_use_converse_api: bool = False
    cache: Optional[bool] = False
    callback_manager: Optional[Any] = None
    callbacks: Optional[Any] = None
    config: Optional[Any] = None
    credentials_profile_name: Optional[str] = None
    custom_get_token_ids: Optional[Any] = None
    disable_streaming: bool = False
    endpoint_url: Optional[str] = None
    guardrails: Optional[Any] = None
    max_tokens: Optional[int] = None
    model_kwargs: Optional[dict] = None
    provider: Optional[str] = None
    rate_limiter: Optional[Any] = None
    region_name: Optional[str] = None
    stop_sequences: Optional[list[str]] = None  
    temperature: Optional[float] = None
    streaming: Optional[bool] = False
    tags: Optional[Any] = None
    verbose: Optional[bool] = False



@dataclass
class HuggingFaceChatModelConfig(ChatModelConfig):
    _target_: str = "models.chat_models.HuggingFaceChatModel"
    cache: Optional[bool] = False
    callback_manager: Optional[Any] = None
    callbacks: Optional[Any] = None
    custom_get_token_ids: Optional[Any] = None
    disable_streaming: bool = False
    metadata: Optional[Dict[str, Any]] = None
    model_id: Optional[str] = None
    rate_limiter: Optional[Any] = None
    # system_message: Optional[str] = None
    tags: Optional[Any] = None
    tokenizer: Optional[Any] = None
    verbose: Optional[bool] = False

    repo_id: str='microsoft/Phi-3.5-mini-instruct'
    task: str="text-generation"



@dataclass
class OpenAIChatModelConfig(ChatModelConfig):
    _target_: str = "models.chat_models.OpenAIChatModel"
    cache: Optional[bool] = False
    callback_manager: Optional[Any] = None
    callbacks: Optional[Any] = None
    custom_get_token_ids: Optional[Any] = None
    default_headers: Optional[dict] = None
    disable_streaming: bool = False
    disabled_params: Optional[Any] = None
    frequency_penalty: Optional[float] = None
    http_async_client: Optional[Any] = None
    http_client: Optional[Any] = None
    include_response_headers: bool = False
    logit_bias: Optional[dict] = None
    logprobs: Optional[bool] = False
    max_retries: Optional[int] = 6
    max_tokens: Optional[int] = None
    metadata: Optional[dict] = None
    model_name: Optional[str] = None
    n: Optional[int] = 1
    openai_api_base: Optional[str] = None
    openai_api_key: Optional[str] = None
    openai_organization: Optional[str] = None
    openai_proxy: Optional[str] = None
    presence_penalty: Optional[float] = None
    rate_limiter: Optional[Any] = None
    reasoning_effort: Optional[str] = None
    request_timeout: Optional[float] = None
    seed: Optional[int] = None
    stop: Optional[str] = None
    stream_usage: Optional[bool] = False
    steaming: Optional[bool] = False    
    temperature: Optional[float] = None
    tiktoken_model_name: Optional[str] = None
    top_logprobs: Optional[int] = None
    top_p: Optional[float] = None
    user_responses_api: Optional[str] = None
    verbose: Optional[bool] = False

def setup_config() -> None:
    cs = ConfigStore.instance()
    cs.store(
        name="bedrock_chat_model_schema",
        group="models/chat_model",
        node=BedrockChatModelConfig
    )

    cs.store(
        name="huggingface_chat_model_schema",
        group="models/chat_model",
        node=HuggingFaceChatModelConfig
    )

    cs.store(
        name="openai_chat_model_schema",
        group="models/chat_model",
        node=OpenAIChatModelConfig
    )