

from abc import ABC, abstractmethod


class ThemeColor(ABC):

    @abstractmethod
    def createColor(self, color: str):
        pass
