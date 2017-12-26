from plotly.offline import init_notebook_mode, iplot

init_notebook_mode()

iplot({'data': [{'y': [4, 2, 3, 4]}],
       'layout': {'title': 'Test Plot',
                  'font': dict(size=16)}},
      image='png')
