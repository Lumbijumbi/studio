"""Generator package initialization."""

from .lolicode_generator import LoliCodeGenerator, generate_lolicode
from .types import (
    LoliCodeConfig,
    CustomHeader,
    CustomAssertion,
    VariableExtraction,
    SemanticHarEntry,
    SemanticHarRequest,
    SemanticHarResponse,
    RequestBody,
    DependencyMatrix,
    SettingsDict,
)

__all__ = [
    'LoliCodeGenerator',
    'generate_lolicode',
    'LoliCodeConfig',
    'CustomHeader',
    'CustomAssertion',
    'VariableExtraction',
    'SemanticHarEntry',
    'SemanticHarRequest',
    'SemanticHarResponse',
    'RequestBody',
    'DependencyMatrix',
    'SettingsDict',
]
