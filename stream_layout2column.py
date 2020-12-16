import streamlit as st
#import numpy as np
#import pandas as pd
from PIL import Image
import time


st.title('Streamlit 超入門')
st.title( 'ずばり当たる❣')

st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)


for i in range(100):
   latest_iteration.text(f'Iteration {i+1}')
   bar.progress(i+1)
   time.sleep(0.1)

'Done!!!!!!!'

left_column, right_column = st.beta_columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
   right_column.write('ここは右カラムです。')

expander1 = st.beta_expander('問い合わせ1')
expander1.write('問い合わせ1の回答')
expander2 = st.beta_expander('問い合わせ2')
expander2.write('問い合わせ２の回答')
expander3 = st.beta_expander('問い合わせ3')
expander3.write('問い合わ3の回答')
expander4 = st.beta_expander('問い合わせ4')
expander4.write('問い合わせ4の回答')


# text = st.sidebar.text_input('あなたの行きたいところを教えてください。')
# level = st.sidebar.slider('どれくらい行きたいかな？', 0, 100, 30)
#
# 'あなたの行きたいところ : ', text
# '行きたいレベル : ', level


#option = st.selectbox(
#    'あなたの好きな数字を教えてください。',
#    list(range(1,11))
#)


if st.checkbox('あなたの、行きたいところのイメージは：'):
   img = Image.open('sample1.jpg')
   st.image(img, caption='Sample Image', use_column_width=True)


