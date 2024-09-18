from abc import ABC, abstractmethod
from plotly.colors import n_colors
from collections import OrderedDict

class ColorPalette(ABC):
    @abstractmethod
    def __len__(self):
        pass

    @abstractmethod
    def __getitem__(self, key):
        pass

    @abstractmethod
    def get_dark_shade(self, key):
        pass

    @abstractmethod 
    def get_light_shade(self, key):
        pass

    def get_shaded(self, key, n):
        return n_colors(self.get_dark_shade(key), self.get_light_shade(key), n)

def to_rgb(hex):
    return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))

DEFAULT = OrderedDict({'charcoal': { "DEFAULT": '#264653', 100: '#080e11', 200: '#0f1c22', 300: '#172b32', 400: '#1f3943', 500: '#264653', 600: '#3f7489', 700: '#609db6', 800: '#95bece', 900: '#cadee7' }, 'persian_green': { "DEFAULT": '#2a9d8f', 100: '#081f1d', 200: '#113f39', 300: '#195e56', 400: '#217e73', 500: '#2a9d8f', 600: '#3acbba', 700: '#6cd8cb', 800: '#9de5dc', 900: '#cef2ee' }, 'saffron': { "DEFAULT": '#e9c46a', 100: '#3b2c09', 200: '#755912', 300: '#b0851a', 400: '#e0ad2e', 500: '#e9c46a', 600: '#edd086', 700: '#f1dca4', 800: '#f6e7c3', 900: '#faf3e1' }, 'sandy_brown': { "DEFAULT": '#f4a261', 100: '#401f04', 200: '#803e09', 300: '#c05e0d', 400: '#f07e22', 500: '#f4a261', 600: '#f6b681', 700: '#f8c8a1', 800: '#fbdac0', 900: '#fdede0' }, 'burnt_sienna': { "DEFAULT": '#e76f51', 100: '#371107', 200: '#6e220f', 300: '#a43316', 400: '#db441e', 500: '#e76f51', 600: '#ec8b73', 700: '#f1a896', 800: '#f5c5b9', 900: '#fae2dc' } })

class TailwindColorPalette(ColorPalette):
    def __init__(self, palette=DEFAULT):
        self.palette = palette

    def __len__(self):
        return len(self.palette)

    def __getitem__(self, key):
        return self.palette[key]

    def get_dark_shade(self, key):
        return self.palette[key][100]

    def get_light_shade(self, key):
        return self.palette[key][900]