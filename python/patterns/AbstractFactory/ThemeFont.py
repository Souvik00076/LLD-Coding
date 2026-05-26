

from abc import ABC, abstractmethod


class ThemeFont(ABC):

    @abstractmethod
    def createFont(self, font: str):
        pass
