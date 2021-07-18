import streamlit as st
import time

st.title('Streamlit 超入門')

st.write('ブログレスバーの表示')
'Start!'

latest_interation = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_interation.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.05)

'Done.'

left_column, right_column = st.beta_columns(2)

button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラムです')

expander1 = st.beta_expander('問い合わせ')
expander1.write('名前')

expander2 = st.beta_expander('問い合わせ')
expander2.write('名前')

expander3 = st.beta_expander('問い合わせ')
expander3.write('名前')