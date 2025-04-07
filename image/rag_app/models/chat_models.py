
from abc import ABC, abstractmethod

from typing import Optional, Any, Union, Tuple
from langchain_aws import ChatBedrock
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_openai import ChatOpenAI


class ChatModel(ABC):
    @abstractmethod
    def get_model(self) -> Any:
        """Get the model."""


class BedrockChatModel(ChatModel):
    def __init__(
        self,
        model_id: Optional[str] = None,
        aws_access_key_id: Optional[str] = None,
        aws_secret_access_key: Optional[str] = None,
        aws_session_token: Optional[str] = None,
        beta_use_converse_api: Optional[bool] = False,
        cache: Optional[bool] = False,
        callback_manager: Optional[Any] = None,
        callbacks: Optional[Any] = None,
        config: Optional[Any] = None,
        credentials_profile_name: Optional[str] = None,
        custom_get_token_ids: Optional[Any] = None,
        disable_streaming: Optional[bool] = False,
        endpoint_url: Optional[str] = None,
        guardrails: Optional[Union[str, list]] = None,
        max_tokens: Optional[int] = None,
        model_kwargs: Optional[dict] = None,
        provider: Optional[str] = None,
        rate_limiter: Optional[Any] = None,
        region_name: Optional[str] = None,
        stop_sequences: Optional[list[str]] = None,  # Use a list of strings for stop sequences
        temperature: Optional[float] = None,
        streaming : Optional[bool] = False,
        tags: Optional[Union[str, list]] = None,
        verbose: Optional[bool] = False,
    ):
        self.chat_model = ChatBedrock(
            model_id=model_id,
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            aws_session_token=aws_session_token,
            beta_use_converse_api=beta_use_converse_api,
            cache=cache,
            callback_manager=callback_manager,
            callbacks=callbacks,
            config=config,
            credentials_profile_name=credentials_profile_name,
            custom_get_token_ids=custom_get_token_ids,
            disable_streaming=disable_streaming,
            endpoint_url=endpoint_url,
            guardrails=guardrails,
            max_tokens=max_tokens,
            model_kwargs=model_kwargs,
            provider=provider,
            rate_limiter=rate_limiter,
            region_name=region_name,
            stop_sequences=stop_sequences,
            temperature=temperature,
            streaming = streaming,
            tags=tags,
            verbose=verbose
    )

    def get_model(self) -> ChatModel:
        """Get the model."""
        return self.chat_model

class HuggingFaceChatModel(ChatModel):
    def __init__(
        self,

        repo_id: str,
        task: str,
    
        cache: Optional[bool] = False,
        callback_manager: Optional[Any] = None,
        callbacks: Optional[Any] = None,
        custom_get_token_ids: Optional[Any] = None,
        disable_streaming: Optional[bool] = False,
        metadata: Optional[dict] = None,
        model_id: Optional[str] = None,
        rate_limiter: Optional[Any] = None,
        # system_message: Optional[Any] = None,
        tags: Optional[Any] = None,
        tokenizer: Optional[Any] = None,
        verbose: Optional[bool] = False,
    ):
        self.cache = cache
        self.callback_manager = callback_manager
        self.callbacks = callbacks
        self.custom_get_token_ids = custom_get_token_ids
        self.disable_streaming = disable_streaming
        self.metadata = metadata
        self.model_id = model_id
        self.rate_limiter = rate_limiter
        # self.system_message = system_message
        self.tags = tags
        self.tokenizer = tokenizer
        self.verbose = verbose

        self.repo_id = repo_id
        self.task = task

        llm = HuggingFaceEndpoint(
            repo_id=self.repo_id,
            task=self.task
        )

        self.chat_model = ChatHuggingFace(
            llm=llm,
            cache=self.cache,
            callback_manager=self.callback_manager,
            callbacks=self.callbacks,
            custom_get_token_ids=self.custom_get_token_ids,
            disable_streaming=self.disable_streaming,
            metadata=self.metadata,
            model_id=self.model_id,
            rate_limiter=self.rate_limiter,
            # system_message=self.system_message,
            tags=self.tags,
            verbose=self.verbose,
            tokenizer=self.tokenizer,
        )

    def get_model(self) -> ChatModel:
        """Get the model."""
        return self.chat_model

class OpenAIChatModel(ChatModel):
    def __init__(
        cache: Optional[bool] = False,
        callback_manager: Optional[Any] = None,
        callbacks: Optional[Any] = None,
        custom_get_token_ids: Optional[Any] = None,
        default_headers: Optional[dict] = None,
        disable_streaming: Optional[bool] = False,
        disabled_params: Optional[Any] = None,
        frequency_penalty: Optional[float] = None,
        http_async_client: Optional[Any] = None,
        http_client: Optional[Any] = None,
        include_response_headers: bool = False,
        logit_bias: Optional[dict] = None,
        logprobs: Optional[bool] = False,
        max_retries: Optional[int] = 6,
        max_tokens: Optional[int] = None,
        metadata: Optional[dict] = None,
        model_name: Optional[str] = None,
        n: Optional[int] = 1,
        openai_api_base: Optional[str] = None,
        openai_api_key: Optional[str] = None,
        openai_organization: Optional[str] = None,
        openai_proxy: Optional[str] = None,
        presence_penalty: Optional[float] = None,
        rate_limiter: Optional[Any] = None,
        reasoning_effort: Optional[str] = None,
        request_timeout: Optional[float] = None,
        seed: Optional[int] = None,
        stop: Optional[str] = None,
        stream_usage: Optional[bool] = False,
        steaming: Optional[bool] = False,
        temperature: Optional[float] = None,
        tiktoken_model_name: Optional[str] = None,
        top_logprobs: Optional[int] = None,
        top_p: Optional[float] = None,
        user_responses_api: Optional[str] = None,
        verbose: Optional[bool] = False
    ):

        self.chat_model(
            cache=cache,
            callback_manager=callback_manager,
            callbacks=callbacks,
            custom_get_token_ids=custom_get_token_ids,
            default_headers=default_headers,
            disable_streaming=disable_streaming,
            disabled_params=disabled_params,
            frequency_penalty=frequency_penalty,
            http_async_client=http_async_client,
            http_client=http_client,
            include_response_headers=include_response_headers,
            logit_bias=logit_bias,
            logprobs=logprobs,
            max_retries=max_retries,
            max_tokens=max_tokens,
            metadata=metadata,
            model_name=model_name,
            n=n,
            openai_api_base=openai_api_base,
            openai_api_key=openai_api_key,
            openai_organization=openai_organization,
            openai_proxy=openai_proxy,
            presence_penalty=presence_penalty,
            rate_limiter=rate_limiter,
            reasoning_effort=reasoning_effort,
            request_timeout=request_timeout,
            seed=seed,
            stop=stop,
            stream_usage=stream_usage,
            steaming=steaming,
            temperature=temperature,
            tiktoken_model_name=tiktoken_model_name,
            top_logprobs=top_logprobs,
            top_p=top_p,
            user_responses_api=user_responses_api, 
            verbose=verbose,
        )
    

    def get_model(self) -> ChatModel:
        """Get the model."""
        return self.chat_model