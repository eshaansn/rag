from dataclasses import dataclass
from typing import Optional, Callable, Union, Tuple, Any, Literal
from dataclasses import field

from hydra.core.config_store import ConfigStore
from omegaconf import MISSING, SI

from langchain_community.document_loaders.parsers.images import BaseImageBlobParser

@dataclass
class LoaderConfig():
    _target_: str = MISSING

@dataclass
class PDFLoaderConfig(LoaderConfig):
    _target_: str = "database.loaders.PDFLoader"
    path: str = "data/source/"
    glob: Optional[str] = "**/[!.]*.pdf"
    silent_errors: Optional[bool] = False
    recursive: Optional[bool] = False
    extract_images: Optional[bool] = False
    password: Optional[str] = None
    mode: str = 'page'
    images_parser:  Optional[Any] = None
    headers: Optional[dict] = None
    extraction_mode: str = 'layout'
    extraction_kwargs: Optional[dict] = field(default_factory=lambda: {})

def setup_config() -> None:
    cs = ConfigStore.instance()
    cs.store(
        name="pdf_loader_schema",
        group="database/loader",
        node=PDFLoaderConfig,
    )