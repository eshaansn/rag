from langchain_chroma import Chroma
from abc import ABC, abstractmethod
from typing import Optional, Any, Union, Tuple
CHROMA_DB_INSTANCE = None  


class VectorDatabase(ABC):
    @abstractmethod
    def create_database(self):
        """
        Creates the database for the model.
        """

class ChromaDB(VectorDatabase):
    def __init__(
        self, 
        collection_name: str,
        persist_directory: str,
        embedding_function: Any,
        collection_metadata: Optional[dict] = None,
        client: Optional[Any] = None,
        client_settings: Optional[Any] = None,
        relevance_score_fn: Optional[Any] = None,
        create_collection_if_not_exists: Optional[bool] = True
        ):
        self.persist_directory = persist_directory
        self.collection_name = collection_name
        self.embedding_function = embedding_function
        self.collection_metadata = collection_metadata
        self.client = client
        self.client_settings = client_settings
        self.relevance_score_fn = relevance_score_fn
        # self.create_collection_if_not_exists = create_collection_if_not_exists

    def create_database(self) -> Chroma:
        """
        Creates the database for the model.
        """
        global CHROMA_DB_INSTANCE
        if not CHROMA_DB_INSTANCE:
            CHROMA_DB_INSTANCE = Chroma(
                persist_directory=self.persist_directory,
                embedding_function=self.embedding_function,
                collection_name=self.collection_name,
                collection_metadata=self.collection_metadata,
                client=self.client,
                client_settings=self.client_settings,
                relevance_score_fn=self.relevance_score_fn,
                # create_collection_if_not_exists=self.create_collection_if_not_exists
            )
            print(f"✅ Init ChromaDB {CHROMA_DB_INSTANCE} from {self.persist_directory}")
        return CHROMA_DB_INSTANCE