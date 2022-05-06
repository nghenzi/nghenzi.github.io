import asyncio
import panel as pn
from bokeh.plotting import figure

pn.config.sizing_mode = 'stretch_width'

p = figure()
p.circle([1,2,3],[4,5,6])

slider = pn.widgets.FloatSlider(start=0, end=10, name='Amplitude')

btn = pn.widgets.Button(name='btn')

def callback(new):
    return f'Amplitude is: {new}'

row = pn.Row(pn.Column( btn, 
                        slider,  
                        pn.bind(callback, slider),
                        width=120,
                        sizing_mode='fixed'), 
            p)

def replace(e):
    row[1] = pn.pane.Markdown('# asdasd')

btn.on_click(replace)

await pn.io.pyodide.show(row, 'myplot')