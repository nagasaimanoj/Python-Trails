import plotly.offline as offline
import plotly.graph_objs as go

offline.init_notebook_mode()

offline.iplot({'data': [{'y': [4, 2, 3, 4]}], 
               'layout': {'title': 'Test Plot', 
                          'font': dict(size=16)}},
             image='png')