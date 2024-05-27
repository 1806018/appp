import streamlit as st
import numpy as np
import pandas as pd
import time

st.set_page_config(page_title="GFG")

#Static
col1, col2, col3=st.columns(3)

with col1:
    st.header('Cat')
    st.image('https://static.streamlit.io/examples/cat.jpg',width=200)
with col2:
    st.header('Dog')
    st.image('https://static.streamlit.io/examples/dog.jpg',width=200)
with col3:
    st.header('Owl')
    st.image('https://static.streamlit.io/examples/owl.jpg',width=200)


# Dynamic
n=st.number_input('How many columns you want??',1,10)

cols=st.columns(n)
#list of columns

for col in cols:
    with col:
        st.header('Cat')
        st.image('https://static.streamlit.io/examples/cat.jpg',width=200)
#-----------------------------------------------------------------------

st.subheader('Tabs')
tab1,tab2,tab3=st.tabs(['Cat','Dog','Owl'])
tab1.image('https://static.streamlit.io/examples/cat.jpg',width=200)
tab2.image('https://static.streamlit.io/examples/dog.jpg',width=200)
tab3.image('https://static.streamlit.io/examples/owl.jpg',width=200)

#------------------------------------------------------------------------

#Dynamic
imgs=pd.read_csv('/Users/KIIT/Desktop/Animesh Program/Streamlit Project/imgs.csv')['img_link']

tabs=st.tabs(['ID']*30)

for tab in tabs:
    img=imgs[np.random.randint(1,1000)]
    tab.image(img,width=200)
#st.subheader(imgs)

#-----------------------------------------------------------------------------

st.subheader('Expander & Empty Functionalities')

cases=[]
for _ in range(100):
    cases.append(np.random.randint(1,7))

st.write(cases)

data=[]
for i in range(1,7):
    data.append(cases.count(i))
st.header('Frequency of getting a face.')
st.bar_chart({'data' : data})


with st.empty():
    st.write('you need to wait for 10 seconds')
    for seconds in range(11):
        st.write(''+str(seconds)+' secons remaining')
        time.sleep(1)
    st.write('10 seconds completed.')


with st.expander('See explanation'):
    st.write('''
            The chart shows some numbers got from rolling a dice 100 times and it's
            about how many times each face appears.
        ''')
    st.image('https://static.streamlit.io/examples/dice.jpg',width=150)

#----------------------------------------------------------------------------


st.header('Advance Display & Progress Options')

#Spinner
st.subheader('Spinner')
with st.spinner('wait for it'):
    time.sleep(5)
    st.write('Thanks for waiting!!')

#Progress
st.subheader('Progress')  
with st.empty():
    for percent_completed in range(100):
        time.sleep(.1)
        st.progress(percent_completed +1,text='Processing')
    st.success('Completed')

st.balloons()

st.snow()

#------------------------------------------------------------------------

st.subheader('Echo and Stop Commands')


def get_uname():
    return 'QWERTY'



with st.echo():
    def get_punc():
        return '!!!'


    greet='Hi, '
    name=get_uname()
    punc=get_punc()
    st.write(greet,name,punc)



f_name=st.text_input('Enter first name: ')
if not f_name:
    st.warning('please enter your first name')
    st.stop()

l_name=st.text_input('Enter last name: ')
if not l_name:
    st.warning('please enter your last name')
    st.stop()
    
st.success('Thank you.')






























