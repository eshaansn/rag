
from abc import ABC, abstractmethod

from typing import Optional, Any, Union, Tuple
from langchain_aws import BedrockEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_openai import OpenAIEmbeddings


class Embedding(ABC):
    @abstractmethod
    def get_embedding_function(self):
        """
        Returns the embedding function for the model.
        """
        pass

    @abstractmethod
    def embed_documents(self):
        """
        Embeds a list of documents.
        """
        pass


class BedrockEmbedding(Embedding):
    def __init__(
        self,
        model_id: str,
        aws_access_key_id: Optional[str] = None,
        aws_secret_access_key: Optional[str] = None,
        region_name: Optional[str] = None,
        endpoint_url: Optional[str] = None,
        aws_session_token: Optional[str] = None,
        normalize: Optional[bool] = None,
        client: Optional[Any] = None,
        model_kwargs: Optional[dict] = None,
    ):
        self.model_id = model_id
        self.aws_access_key_id = aws_access_key_id
        self.aws_secret_access_key = aws_secret_access_key
        self.region_name = region_name
        self.endpoint_url = endpoint_url
        self.aws_session_token = aws_session_token
        self.normalize = normalize
        self.client = client
        self.model_kwargs = model_kwargs

    def get_embedding_function(self):
        """
        Returns the embedding function for the model.
        """
        embedding_function = BedrockEmbeddings(
            model_id=self.model_id,
            aws_access_key_id=self.aws_access_key_id,
            aws_secret_access_key=self.aws_secret_access_key,
            region_name=self.region_name,
            endpoint_url=self.endpoint_url,
            aws_session_token=self.aws_session_token,
            normalize=self.normalize,
            client=self.client,
            model_kwargs=self.model_kwargs
        )

        return embedding_function
    
    def embed_documents(self, documents):
        """
        Embeds a list of documents.
        """
        embedding_function = self.get_embedding_function()
        return embedding_function.embed_documents(documents)

class HuggingFaceEmbedding(Embedding):
    def __init__(
        self,
        model_name: str,
        cache_folder: Optional[str] = None,
        encode_kwargs: Optional[dict] = None,
        model_kwargs: Optional[dict] = None,
        show_progress: Optional[bool] = None,
        multi_process: Optional[bool] = None,
    ):
        self.model_name = model_name
        self.cache_folder = cache_folder
        self.encode_kwargs = encode_kwargs
        self.model_kwargs = model_kwargs
        self.show_progress = show_progress
        self.multi_process = multi_process
    
    def get_embedding_function(self):
        """
        Returns the embedding function for the model.
        """
        embedding_function = HuggingFaceEmbeddings(
            model_name=self.model_name,
            cache_folder=self.cache_folder,
            encode_kwargs=self.encode_kwargs,
            model_kwargs=self.model_kwargs,
            show_progress=self.show_progress,
            multi_process=self.multi_process
        )

        return embedding_function

    def embed_documents(self, documents):
        """
        Embeds a list of documents.
        """
        embedding_function = self.get_embedding_function()
        return embedding_function.embed_documents(documents)

class OpenAIEmbedding(Embedding):
    def __init__(
        self,
        model: str,
        dimension: Optional[int] = None,
        api_key: Optional[str] = None,
        organization: Optional[str] = None,
        max_retries: int = 2,
        request_timeout: Optional[Union[float, Tuple[float, float], Any]] = None,
    ):
        self.model = model
        self.dimension = dimension
        self.api_key = api_key
        self.organization = organization
        self.max_retries = max_retries
        self.request_timeout = request_timeout
    
    def get_embedding_function(self):
        """
        Returns the embedding function for the model.
        """
        embedding_function = OpenAIEmbeddings(
            model=self.model,
            dimension=self.dimension,
            api_key=self.api_key,
            organization=self.organization,
            max_retries=self.max_retries,
            request_timeout=self.request_timeout
        )

        return embedding_function
    
    def embed_documents(self, documents):
        """
        Embeds a list of documents.
        """
        embedding_function = self.get_embedding_function()
        return embedding_function.embed_documents(documents)


