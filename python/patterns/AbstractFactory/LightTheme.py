
from ThemeFactory import ThemeFactory
from LightColor import LightColor
from LightFont import LightFont


class LightTheme(ThemeFactory):

    def createColor(self):
        color = LightColor("#12312423")
        return color

    def createFont(self):
        font = LightFont("#234werewr")
        return font
