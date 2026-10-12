
import streamlit as st
import requests as rq
import time as tm

st.set_page_config(page_title='M.Mahdi Rabiei')

URL = 'https://api.github.com/users/Mhadi-1382'


def get_data_github():
    '''Get data of github profile.'''
    response = rq.get(url=URL)

    return response.json()

def typing(text: str):
    for item in text:
        yield item
        tm.sleep(0.02)


data = get_data_github()
text_format = f'''
# Hello 👋

**{data.get('name', 'M.Mahdi Rabiei')}**
—
*{data.get('bio', 'Fullstack Developer and Graphic Designer.')}*

---

Profile on Github: {data.get('html_url', 'https://github.com/Mhadi-1382')}
'''

st.write_stream(typing(text=text_format))
