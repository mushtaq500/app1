import streamlit as st
st.sidebar.title('data')
a=st.sidebar.slider('number',1,10)
b=st.sidebar.slider('number',1,10)
if st.button('click'):
	if a > b :
		st.write('a is bigger')
	else : 
		st.write('b is bigger')

