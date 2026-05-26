

from ThemeFactory import ThemeFactory
from DarkColor import DarkColor
from DarkFont import DarkFont


class LightTheme(ThemeFactory):

    def createColor(self):
        color = DarkColor("#1231da")
        return color

    def createFont(self):
        font = DarkFont("#1fa1f9")
        return font
