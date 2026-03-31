import streamlit as st
import time

st.set_page_config(page_title="Runamo - Ёвари Омӯзгор", page_icon="📝")

st.markdown("""
    <div style="text-align: center;">
        <h1 style="color: #1A664D;">РУНАМО</h1>
        <p>Ёвари рақамии омӯзгор</p>
    </div>
""", unsafe_allow_html=True)

if 'page' not in st.session_state:
    st.session_state.page = 'welcome'

if st.session_state.page == 'welcome':
    st.info("Тарроҳ: Отахонзода Хусрав")
    if st.button("ОҒОЗ КАРДАН"):
        st.session_state.page = 'app'
        st.rerun()

elif st.session_state.page == 'app':
    topic = st.text_input("Мавзӯи дарс:")
    if st.button("СОХТАН"):
        with st.spinner('Интизор шавед...'):
            time.sleep(2)
        st.success(f"Нақшаи дарс барои '{topic}' омода шуд!")
      




















