import streamlit as st
import time
from PIL import Image
import pandas as pd
import numpy as np

st.title('越川自己紹介サイト')

st.write('センスは知識から始まる')
'ロード中...'

latest_interation = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_interation.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.02)

'完了しました！'

"""
# 経歴紹介   

### 　越川（Echigawa） 

"""
img = 'IMG_0908.jpeg'
if st.checkbox('画像を表示する'):
    img = Image.open('IMG_0908.jpeg')
    st.image(img, caption='Echigawa yuki', use_column_width=True) 

"""
### 【学習スキル】   
React.js.Javascript,Ruby,   
AWS,Docker,Git,GitHub等    
＊一度GitHubの草数を見に来てください。   

【ポートフォリオサイト】   
https://echigawa0921.github.io/portforio_product/   

"""
df = pd.DataFrame(
    np.random.rand(20,3),
    columns=['a','b','c']
)
st.area_chart(df)


"""
【経歴】   
8年間続けた陸上競技を大学で辞め、在学中に通信業界に参入。   
＊100m10秒台で走れます。   
   
在職中に、通信・Payment事業・インフラ事業にてBtoB・BtoC営業を行い、2019年にSVを経験。   
その人の背景や考え方を考えながらコミュニケーションを取るのが好きです！   
   
その後、株式会社divにて企業様のエンジニア採用のご支援をしています。   
入社後、「テックキャンプ」を受講し、プログラミングの楽しさに気づき個人開発・業務改善等を行う。   


【やったこと】   
```python
・Slackとスプレッドシートを連携し、「営業報告自動化」   
・PythonのBeautiful Soupを使い広告媒体から営業リストの作成   
```

【エンジニアを目指す動機】   
動機は「モノづくりというプロセス自体が好き」だからです。   
    
学生から現在に至るまで「モノづくり」が好きです。   
私の作ったモノで他者が喜んでくれる。本当にいいものを作るには、他者と密にキャッチボールをする必要がある。そのプロセスと結果がやりがいです。   
   
学生の頃、打ち込んだ陸上競技でいうと当時キャプテンをしていたので、自分の考えたメニューでチームメイトがその瞬間楽しく練習してくれたり、また結果を出したてくれることに非常に楽しさを見出していました。   
    
この出来事が私の価値観の基盤となり形成しています。   
そしてプログラミングはその創意工夫で価値を作り出すプロセスに似ています。   
プログラムを書く事で自分の考案した機能を実現しそれをユーザーに使ってもらう。そのユーザーが喜んでいただければ私もまた幸せなのです。    
そういった価値提供をしたいと考えています。    

【趣味】    
・岩盤浴   
"""
top_column, bottom_column = st.beta_columns(2)
button = top_column.button('詳細を見る')
if button:
    bottom_column.write('漫画や本を持ち込めるタイプの岩盤浴が大好きで1日中います。東京の「スパジャポ」真剣におすすめです！！関東最大級で雰囲気から本も3万冊ありぜひ調べてみてください！')

""" 
・サイクリング    
休日ロングランとかでかけます。    
高校生の夏休み中、兵庫（実家）ー京都（高校）を毎日通学してました。    
"""
import streamlit as st
import time
from PIL import Image
import pandas as pd
import numpy as np

st.title('越川自己紹介サイト')

st.write('センスは知識から始まる')
'ロード中...'

latest_interation = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_interation.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.02)

'完了しました！'

"""
# 経歴紹介   

### 　越川（Echigawa） 

"""
img = 'IMG_0908.jpeg'
if st.checkbox('画像を表示する'):
    img = Image.open('IMG_0908.jpeg')
    st.image(img, caption='Echigawa yuki', use_column_width=True) 

"""
### 【学習スキル】   
React.js.Javascript,Ruby,   
AWS,Docker,Git,GitHub等    
＊一度GitHubの草数を見に来てください。   

【ポートフォリオサイト】   
https://echigawa0921.github.io/portforio_product/   

"""
df = pd.DataFrame(
    np.random.rand(20,3),
    columns=['a','b','c']
)
st.area_chart(df)


"""
【経歴】   
8年間続けた陸上競技を大学で辞め、在学中に通信業界に参入。   
＊100m10秒台で走れます。   
   
在職中に、通信・Payment事業・インフラ事業にてBtoB・BtoC営業を行い、2019年にSVを経験。   
その人の背景や考え方を考えながらコミュニケーションを取るのが好きです！   
   
その後、株式会社divにて企業様のエンジニア採用のご支援をしています。   
入社後、「テックキャンプ」を受講し、プログラミングの楽しさに気づき個人開発・業務改善等を行う。   


【やったこと】   
```python
・Slackとスプレッドシートを連携し、「営業報告自動化」   
・PythonのBeautiful Soupを使い広告媒体から営業リストの作成   
```

【エンジニアを目指す動機】   
動機は「モノづくりというプロセス自体が好き」だからです。   
    
学生から現在に至るまで「モノづくり」が好きです。   
私の作ったモノで他者が喜んでくれる。本当にいいものを作るには、他者と密にキャッチボールをする必要がある。そのプロセスと結果がやりがいです。   
   
学生の頃、打ち込んだ陸上競技でいうと当時キャプテンをしていたので、自分の考えたメニューでチームメイトがその瞬間楽しく練習してくれたり、また結果を出したてくれることに非常に楽しさを見出していました。   
    
この出来事が私の価値観の基盤となり形成しています。   
そしてプログラミングはその創意工夫で価値を作り出すプロセスに似ています。   
プログラムを書く事で自分の考案した機能を実現しそれをユーザーに使ってもらう。そのユーザーが喜んでいただければ私もまた幸せなのです。    
そういった価値提供をしたいと考えています。    

【趣味】    
・岩盤浴   
"""
top_column, bottom_column = st.beta_columns(2)
button = top_column.button('詳細を見る')
if button:
    bottom_column.write('漫画や本を持ち込めるタイプの岩盤浴が大好きで1日中います。東京の「スパジャポ」真剣におすすめです！！関東最大級で雰囲気から本も3万冊ありぜひ調べてみてください！')

""" 
・サイクリング    
休日ロングランとかでかけます。    
高校生の夏休み中、兵庫（実家）ー京都（高校）を毎日通学してました。    
"""
