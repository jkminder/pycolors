from abc import ABC, abstractmethod
from plotly.colors import n_colors
from collections import OrderedDict
import plotly.graph_objects as go

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
    hex = hex[1:]
    return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))

# DEFAULT = OrderedDict({'charcoal': { "DEFAULT": '#264653', 100: '#080e11', 200: '#0f1c22', 300: '#172b32', 400: '#1f3943', 500: '#264653', 600: '#3f7489', 700: '#609db6', 800: '#95bece', 900: '#cadee7' }, 'persian_green': { "DEFAULT": '#2a9d8f', 100: '#081f1d', 200: '#113f39', 300: '#195e56', 400: '#217e73', 500: '#2a9d8f', 600: '#3acbba', 700: '#6cd8cb', 800: '#9de5dc', 900: '#cef2ee' }, 'saffron': { "DEFAULT": '#e9c46a', 100: '#3b2c09', 200: '#755912', 300: '#b0851a', 400: '#e0ad2e', 500: '#e9c46a', 600: '#edd086', 700: '#f1dca4', 800: '#f6e7c3', 900: '#faf3e1' }, 'sandy_brown': { "DEFAULT": '#f4a261', 100: '#401f04', 200: '#803e09', 300: '#c05e0d', 400: '#f07e22', 500: '#f4a261', 600: '#f6b681', 700: '#f8c8a1', 800: '#fbdac0', 900: '#fdede0' }, 'burnt_sienna': { "DEFAULT": '#e76f51', 100: '#371107', 200: '#6e220f', 300: '#a43316', 400: '#db441e', 500: '#e76f51', 600: '#ec8b73', 700: '#f1a896', 800: '#f5c5b9', 900: '#fae2dc' } })

DEFAULT =  OrderedDict({ 'rich_black': { "DEFAULT": '#001219', 100: '#000405', 200: '#00070a', 300: '#000b0f', 400: '#000f14', 500: '#001219', 600: '#00587a', 700: '#009ddb', 800: '#3dc8ff', 900: '#9ee4ff' }, 'midnight_green': { "DEFAULT": '#005f73', 100: '#001417', 200: '#00272f', 300: '#003b46', 400: '#004e5e', 500: '#005f73', 600: '#00a3c4', 700: '#13d8ff', 800: '#62e5ff', 900: '#b0f2ff' }, 'dark_cyan': { "DEFAULT": '#0a9396', 100: '#021d1e', 200: '#043b3b', 300: '#065859', 400: '#087577', 500: '#0a9396', 600: '#0ed3d7', 700: '#39eff2', 800: '#7bf4f7', 900: '#bdfafb' }, 'tiffany_blue': { "DEFAULT": '#94d2bd', 100: '#153229', 200: '#2a6551', 300: '#3f977a', 400: '#61bd9e', 500: '#94d2bd', 600: '#a9dbca', 700: '#bee4d7', 800: '#d4ede5', 900: '#e9f6f2' }, 'vanilla': { "DEFAULT": '#e9d8a6', 100: '#403410', 200: '#7f6720', 300: '#bf9b30', 400: '#d9bc66', 500: '#e9d8a6', 600: '#ede0b7', 700: '#f2e7c9', 800: '#f6efdb', 900: '#fbf7ed' }, 'gamboge': { "DEFAULT": '#ee9b00', 100: '#301f00', 200: '#603e00', 300: '#905d00', 400: '#c07d00', 500: '#ee9b00', 600: '#ffb327', 700: '#ffc65d', 800: '#ffd993', 900: '#ffecc9' }, 'alloy_orange': { "DEFAULT": '#ca6702', 100: '#281400', 200: '#512901', 300: '#793d01', 400: '#a25202', 500: '#ca6702', 600: '#fd850d', 700: '#fda349', 800: '#fec286', 900: '#fee0c2' }, 'rust': { "DEFAULT": '#bb3e03', 100: '#250c01', 200: '#4a1801', 300: '#702402', 400: '#953102', 500: '#bb3e03', 600: '#f95104', 700: '#fc7c41', 800: '#fda880', 900: '#fed3c0' }, 'rufous': { "DEFAULT": '#ae2012', 100: '#230604', 200: '#460d07', 300: '#69130b', 400: '#8c190f', 500: '#ae2012', 600: '#e72b1a', 700: '#ed6053', 800: '#f3958d', 900: '#f9cac6' }, 'auburn': { "DEFAULT": '#9b2226', 100: '#1f0708', 200: '#3e0e0f', 300: '#5d1417', 400: '#7c1b1e', 500: '#9b2226', 600: '#cf2e33', 700: '#dc6165', 800: '#e89698', 900: '#f3cacc' } })

class TailwindColorPalette(ColorPalette):
    def __init__(self, palette=DEFAULT):
        self.names = list(palette.keys())
        self.palette = list(palette.values())

    def __len__(self):
        return len(self.palette)

    def __getitem__(self, key):
        return self.palette[key]["DEFAULT"]

    def get_dark_shade(self, key):
        return self.palette[key][100]

    def get_shade(self, key, shade):
        return self.palette[key][shade]

    def get_light_shade(self, key):
        return self.palette[key][900]

    def plot_color_grid(self):
        fig = go.Figure()

        for i, color_name in enumerate(self.names):
            color_dict = self.palette[i]
            y_positions = list(range(len(color_dict), 0, -1))

            # Plot all shades
            for shade, hex_color in color_dict.items():
                if shade == "DEFAULT":
                    continue
                fig.add_trace(go.Scatter(
                    x=[i], y=[y_positions[int(shade/100)]],
                    mode='markers',
                    marker=dict(size=30, color=hex_color),
                    name=f'{color_name} - {shade}',
                    text=f'{color_name} - {shade}: {hex_color}',
                    hoverinfo='text'
                ))

            # Plot default color
            fig.add_trace(go.Scatter(
                x=[i], y=[0],
                mode='markers',
                marker=dict(size=30, color=color_dict["DEFAULT"], line=dict(color='black', width=2)),
                name=f'{color_name} - DEFAULT',
                text=f'{color_name} - "DEFAULT": {color_dict["DEFAULT"]}',
                hoverinfo='text'
            ))

        fig.update_layout(
            title='Color Palette Grid',
            xaxis=dict(tickmode='array', tickvals=list(range(len(self.names))), ticktext=[f"[{i}] {name}" for i, name in enumerate(self.names)]),
            yaxis=dict(tickmode='array', tickvals=list(range(11)), ticktext=['DEFAULT'] + list(range(900, 0, -100))),
            showlegend=False,
            height=800,
            width=1000
        )

        fig.show()
