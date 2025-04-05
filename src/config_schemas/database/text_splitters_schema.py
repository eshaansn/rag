from pydantic.dataclasses import dataclass
from dataclasses import field
from typing import Optional, Any, Dict

from hydra.core.config_store import ConfigStore
from omegaconf import MISSING

from typing import List, Union, Literal


@dataclass
class TextSplitterConfig():
    _target_: str = MISSING

@dataclass
class RecursiveCharacterTextSplitterConfig(TextSplitterConfig):
    _target_: str = "database.text_splitters.RecursiveCharacterTextSplitterClass"
    separators: Optional[List[str]] = None
    keep_separator: Optional[bool] = False
    chunk_size: int = 600
    chunk_overlap: int = 120
    is_separator_regex: bool = False
    kwargs: Optional[dict] = field(default_factory=lambda: {})

def setup_config() -> None:
    cs = ConfigStore.instance()
    cs.store(
        name="recursive_character_text_splitter_schema",
        group="database/text_splitter",
        node=RecursiveCharacterTextSplitterConfig,
    )