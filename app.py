# app.py
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Streamlit Docker 배포 테스트 앱")

st.write("간단한 테스트를 위해 무작위 데이터를 생성하여 차트를 그립니다.")

# 무작위 데이터 생성
data = np.random.randn(100)

# Matplotlib으로 히스토그램 그리기
fig, ax = plt.subplots()
ax.hist(data, bins=20)
ax.set_title("무작위 데이터 히스토그램")
ax.set_xlabel("값")
ax.set_ylabel("빈도")

# Streamlit에 차트 표시
st.pyplot(fig)