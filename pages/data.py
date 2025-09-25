

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager

st.title('간단한 데이터 시각화')

# 한글 폰트 경로 지정
font_path = './fonts/NanumGothic-Regular.ttf'
font_manager.fontManager.addfont(font_path)
plt.rc('font', family='NanumGothic')

# 임의의 데이터 생성
data = pd.DataFrame({
	'x': np.arange(1, 11),
	'y': np.random.randint(10, 100, 10)
})

st.subheader('라인 그래프')
fig1, ax1 = plt.subplots()
ax1.plot(data['x'], data['y'], marker='o')
ax1.set_title('라인 그래프')
ax1.set_xlabel('x축')
ax1.set_ylabel('y값')
st.pyplot(fig1)

st.subheader('바 그래프')
fig2, ax2 = plt.subplots()
ax2.bar(data['x'], data['y'])
ax2.set_title('바 그래프')
ax2.set_xlabel('x축')
ax2.set_ylabel('y값')
st.pyplot(fig2)
