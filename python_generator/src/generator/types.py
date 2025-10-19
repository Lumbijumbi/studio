"""Type definitions for the LoliCode generator."""

from typing import TypedDict, Optional, Literal, Dict, List
from dataclasses import dataclass


@dataclass
class CustomHeader:
    """Custom header configuration."""
    key: str
    value: str
    enabled: bool


@dataclass
class CustomAssertion:
    """Custom assertion/keycheck configuration."""
    type: Literal['status', 'contains', 'regex', 'json-path']
    value: str
    expected_result: Optional[str] = None
    action: Literal['success', 'fail', 'retry', 'ban'] = 'success'


@dataclass
class VariableExtraction:
    """Variable extraction configuration."""
    type: Literal['regex', 'json', 'css', 'xpath']
    pattern: str
    variable_name: str
    is_global: bool


class SettingsDict(TypedDict, total=False):
    """Script settings."""
    use_proxy: bool
    follow_redirects: bool
    timeout: int
    retry_count: int


@dataclass
class LoliCodeConfig:
    """Configuration for LoliCode generation."""
    selected_indices: List[int]
    refine: bool = False
    custom_headers: Optional[Dict[int, List[CustomHeader]]] = None
    custom_assertions: Optional[Dict[int, List[CustomAssertion]]] = None
    variable_extractions: Optional[Dict[int, List[VariableExtraction]]] = None
    settings: Optional[SettingsDict] = None


@dataclass
class SemanticHarRequest:
    """HAR request data."""
    url: str
    method: str
    headers: Dict[str, str]
    cookies: Dict[str, str]
    body: Optional['RequestBody'] = None


@dataclass
class RequestBody:
    """Request body data."""
    data: str
    content_type: Literal['json', 'form']


@dataclass
class SemanticHarResponse:
    """HAR response data."""
    status: int


@dataclass
class SemanticHarEntry:
    """Semantic HAR entry."""
    request: SemanticHarRequest
    response: SemanticHarResponse


@dataclass
class DependencyMatrix:
    """Dependency matrix for request ordering."""
    topological_order: List[int]
