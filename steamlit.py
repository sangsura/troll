import streamlit as st
import numpy as np
import pandas as pd
ten=st.text_input("Nhập tên vào đây:")

if ten:

    click = st.button("nhập tên xong click vào đây!")
    if click:
        st.write(ten,"óc chó xem sex ít thôi nhé!")
        st.image("gaixinh.png")

