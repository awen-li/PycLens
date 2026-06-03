"""Base APIs for pybcSEC research-question analyses."""

from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path


class RQAnalyze(ABC):
    """Base class for research-question analysis stages."""

    def __init__(self, data_dir: Path) -> None:
        self.data_dir = data_dir

    @abstractmethod
    def analyze(self) -> None:
        """Run the analysis and write its outputs."""
