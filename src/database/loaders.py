from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_community.document_loaders.parsers.images import BaseImageBlobParser
from langchain.schema import Document

from abc import ABC, abstractmethod
from typing import Optional, Any, List

import os


class Loader(ABC):
    @abstractmethod
    def load(self) -> list[Document]:
        """
        Splits the documents into smaller chunks.
        """


class PDFLoader(Loader):
    def __init__(
        self, 
        path: str,
        glob: Optional[str] = None,
        silent_errors: Optional[bool] = False,
        recursive: Optional[bool] = False,
        extract_images: Optional[bool] = False,
        password: Optional[str] = None,
        mode: str = 'page',
        images_parser: Optional[Any] = None,
        headers: Optional[dict] = None,
        extraction_mode: str = 'layout',
        extraction_kwargs: Optional[dict] = None,
        ):
        self.path = path
        self.glob = glob
        self.silent_errors = silent_errors
        self.recursive = recursive
        self.extract_images = extract_images
        self.password = password
        self.mode = mode
        self.images_parser = images_parser
        self.headers = headers
        self.extraction_mode = extraction_mode
        self.extraction_kwargs = extraction_kwargs

    def cwd(self):
        print(f"CWD inside load(): {os.getcwd()}")


    def load(self) -> list[Document]:
        document_loader = PyPDFDirectoryLoader(
            path=self.path,
            glob=self.glob,
            silent_errors=self.silent_errors,
            recursive=self.recursive,
            extract_images=self.extract_images,
            password=self.password,
            mode=self.mode,
            images_parser=self.images_parser,
            headers=self.headers,
            extraction_mode=self.extraction_mode,
            extraction_kwargs=self.extraction_kwargs,
        )
        return document_loader.load()