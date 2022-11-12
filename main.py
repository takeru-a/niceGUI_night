from nicegui import ui
with ui.header().style('background-color: #3874c8').props('elevated'):
    ui.label('職業診断').style('font-size: 300%; font-weight: 1300')
with ui.left_drawer(top_corner=True, bottom_corner=True).style('background-color: #d7e3f4'):
    ui.icon('thumb_up')
with ui.right_drawer(top_corner=True, bottom_corner=True).style('background-color: #ebf1fa').props('bordered'):
    ui.icon('thumb_up')

ui.label('設問に答えて下さい！').classes('w-max')

score = 0

# ui.link('result', 'result')

@ui.page('/result/')
def page_result():
    ui.label('Result')
    with ui.header().style('background-color: #3874c8').props('elevated'):
        ui.label('職業診断').style('font-size: 300%; font-weight: 1300')
    with ui.left_drawer(top_corner=True, bottom_corner=True).style('background-color: #d7e3f4'):
        ui.icon('thumb_up')
    with ui.right_drawer(top_corner=True, bottom_corner=True).style('background-color: #ebf1fa').props('bordered'):
        ui.icon('thumb_up')
    ui.label(f'score: {score}')
    with ui.card().style('align:center'):
        ui.label("質問1").props()       
    ui.add_static_files('/imgs', 'imgs')
    with ui.image('imgs/cat.jpg'):
        ui.label('first image from slideshow').classes('absolute-bottom text-subtitle2')
            

  

    # ui.button('RETURN', on_click=lambda e: ui.open('#open', e.socket))
with ui.column():
    with ui.card().style('align:center'):
        with ui.row():   
            ui.label("質問1").props()       
        with ui.column():
            v = ui.select(["当てはまる","やや当てはまる","どちらとも言えない", "やや当てはまらない","当てはまらない"], value="当てはまる")
    with ui.card().style('align:center'):
        with ui.row():   
            ui.label("質問2").props()      
        with ui.column():
            v = ui.select(["当てはまる","やや当てはまる","どちらとも言えない", "やや当てはまらない","当てはまらない"], value="当てはまる")
    ui.button('sumbit',on_click=lambda e: ui.open(page_result, e.socket))
  
ui.run()

