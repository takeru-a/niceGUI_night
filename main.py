from nicegui import ui

title = '自己分析ツール'

with ui.header().style('background-color: #3874c8').props('elevated'):
    ui.label(title).style('font-size: 300%; font-weight: 1300')
with ui.left_drawer(top_corner=True, bottom_corner=True).style('background-color: #d7e3f4'):
    ui.icon('grade')
with ui.right_drawer(top_corner=True, bottom_corner=True).style('background-color: #ebf1fa').props('bordered'):
    ui.icon('grade')

ui.label('設問に答えて下さい！').classes('w-max')

score = 0
def reset(e):
    global score
    score = 0
    ui.open('/', e.socket)
def cal_score(x):
    n = x % 4
    return n
@ui.page('/result/')
def page_result():
    ans = ["他人のへその緒、手でちぎってそう","虫眼鏡で太陽見てそう","クリスマスイブ当日に別れてそう","徹夜して通販番組見てそう"]
    imgs = ["baby.png","mushi.jpg","cp.jpg","tv.jpg"]
    items = ["笑顔が優しくなる手鏡","キュートになれるサラダ","気持ちが伝わるペン","信じる気持ちが芽生えるポップコーン"]
    num = cal_score(score)
    with ui.header().style('background-color: #3874c8').props('elevated'):
        ui.label(title).style('font-size: 300%; font-weight: 1300')
    with ui.left_drawer(top_corner=True, bottom_corner=True).style('background-color: #d7e3f4'):
        ui.icon('grade')
    with ui.right_drawer(top_corner=True, bottom_corner=True).style('background-color: #ebf1fa').props('bordered'):
        ui.icon('grade')
    # ui.label(f'score: {score}')
    with ui.card().style('align:center'):
        ui.label(f"診断結果：あなたは{ans[num]}やな").style('font-size: 200%; font-weight: 1300')     
    ui.add_static_files('/imgs', 'imgs')
    with ui.image(f'imgs/{imgs[num]}'):
        ui.label(f'ラッキーアイテム：{items[num]}').classes('absolute-bottom text-subtitle2')
    ui.button('RETURN', on_click=lambda e: reset(e))
    # ui.link('RETURN', '/')

questions = ["当てはまる","やや当てはまる", "あまり当てはまらない","当てはまらない","どちらとも言えない"]          
  
def scoring(x):
    global score
    i = 4
    for s in questions:
        if s == x.value:
            score += i
        i = i - 1    

    
with ui.column():
    with ui.card().style('align:center'):
        with ui.row():   
            ui.label("質問1").props()
            ui.label("普段は非常に意欲的で、エネルギッシュである。").style('font-size: 100%; font-weight: 1300')           
        with ui.column():
            v = ui.select(questions, value="",on_change=lambda x: scoring(x))
            print(v)
    with ui.card().style('align:center'):
        with ui.row():   
            ui.label("質問2").props()
            ui.label("自分自身は創造的というより実用的であると思う。").props()      
        with ui.column():
            v = ui.select(questions, value="",on_change=lambda x: scoring(x))
    with ui.card().style('align:center'):
        with ui.row():   
            ui.label("質問3").props()
            ui.label("他人の感情に共感することは難しいと感じることがよくある。").props()         
        with ui.column():
            v = ui.select(questions, value="",on_change=lambda x: scoring(x))
    with ui.card().style('align:center'):
        with ui.row():   
            ui.label("質問4").props()
            ui.label("入念な計画立案者というよりは、その場で即興で物事を行うタイプである。").props()        
        with ui.column():
            v = ui.select(questions, value="",on_change=lambda x: scoring(x))
    with ui.card().style('align:center'):
        with ui.row():   
            ui.label("質問5").props()
            ui.label("本、アート、または映画などの型にはまらない、曖昧な物事に常に興味をもってきた。").props()         
        with ui.column():
            v = ui.select(questions, value="",on_change=lambda x: scoring(x))
    with ui.card().style('align:center'):
        with ui.row():   
            ui.label("質問6").props()
            ui.label("プレッシャーがあるときでも常にリラックスし、集中できる。").props()        
        with ui.column():
            v = ui.select(questions, value="",on_change=lambda x: scoring(x))
    with ui.card().style('align:center'):
        with ui.row():   
            ui.label("質問7").props()
            ui.label("自然の中を歩いているときに、自分の思索に没頭してしまうことがよくある。").props()         
        with ui.column():
            v = ui.select(questions, value="",on_change=lambda x: scoring(x))
    with ui.card().style('align:center'):
        with ui.row():   
            ui.label("質問8").props()
            ui.label("新しい職場での社交活動に参加し始めるのにそれほど時間を要しない。").props()        
        with ui.column():
            v = ui.select(questions, value="",on_change=lambda x: scoring(x))
    with ui.card().style('align:center'):
        with ui.row():   
            ui.label("質問9").props()
            ui.label("詳細な計画を立てるのに時間を費やすよりも、どちらかというと即興で物事を実行する。").props()         
        with ui.column():
            v = ui.select(questions, value="",on_change=lambda x: scoring(x))
    with ui.card().style('align:center'):
        with ui.row():   
            ui.label("質問10").props()
            ui.label("友達が何かに悲しんでいる場合、問題対処の方法を提案するよりも、情緒的なサポートをすることの方が多い。").props()        
        with ui.column():
            v = ui.select(questions, value="",on_change=lambda x: scoring(x))

    ui.button('sumbit',on_click=lambda e: ui.open(page_result, e.socket)).props('icon=send')
    
ui.run()

