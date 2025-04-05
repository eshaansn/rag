from abc import ABC, abstractmethod

from typing import Optional, Any, Union, Tuple, List, Callable, Literal

from langchain.schema import Document

from langchain.text_splitter import RecursiveCharacterTextSplitter

class TextSplitterClass(ABC):
    @abstractmethod
    def split_documents(self, documents: list[Document]) -> list[Document]:
        """
        Splits the documents into smaller chunks.
        """


class RecursiveCharacterTextSplitterClass(TextSplitterClass):
    def __init__(
        self,
        chunk_size: int,
        chunk_overlap: int,
        is_separator_regex: bool,
        length_function: Optional[Callable[[str], int]] = len,
        kwargs: Optional[dict] = None,
        separators: Optional[List[str]] = None,
        keep_separator: (Union[bool, Literal['start', 'end']]) = False,
        ):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.length_function = length_function
        self.is_separator_regex = is_separator_regex
        self.separators = separators
        self.keep_separator = keep_separator
        self.kwargs = kwargs

    def split_documents(self, documents: list[Document]) -> list[Document]:
        text_splitter = RecursiveCharacterTextSplitter(
            separators=self.separators,
            keep_separator=self.keep_separator,
            length_function=self.length_function,
            chunk_size=self.chunk_size,
            chunk_overlap=self.chunk_overlap,
            is_separator_regex=self.is_separator_regex,
            **self.kwargs
        )
        return text_splitter.split_documents(documents)
