

from abc import ABC, abstractmethod


class ThemeFactory(ABC):

    @abstractmethod
    def createColor(self):
        pass

    @abstractmethod
    def createFont(self):
        pass

    def createTheme(self):
        color = self.createColor()
        font = self.createFont()
        print(f"{color.color} and {font.font}")
