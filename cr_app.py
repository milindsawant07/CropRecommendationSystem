import pickle
import streamlit as st
from sklearn.tree import DecisionTreeClassifier

with open('cr_pred.pickle', 'rb') as f:
    clf = pickle.load(f)


st.title('Crop Recommendation')
n = st.number_input('N')
p = st.number_input('P')
k = st.number_input('K')
temp = st.number_input('Temperature')
hum = st.number_input('Humidity')
ph = st.number_input('Ph')
rf = st.number_input('Rainfall')

if st.button('Predict Result'):
    result = clf.predict([[n, p, k, temp, hum, ph, rf]])
    # st.success(result)

    if result == 0:
        st.success('apple')

    elif result == 1:
        st.success('banana')

    elif result == 2:
        st.success('blackgram')

    elif result == 3:
        st.success('chickpea')

    elif result == 4:
        st.success('coconut')

    elif result == 5:
        st.success('coffee')

    elif result == 6:
        st.success('cotton')

    elif result == 7:
        st.success('grapes')

    elif result == 8:
        st.success('jute')

    elif result == 9:
        st.success('kidneybeans')

    elif result == 10:
        st.success('lentil')

    elif result == 11:
        st.success('maize')

    elif result == 12:
        st.success('mango')

    elif result == 13:
        st.success('mothbeans')

    elif result == 14:
        st.success('mungbeans')

    elif result == 15:
        st.success('muskmelon')

    elif result == 16:
        st.success('orange')

    elif result == 17:
        st.success('papaya')

    elif result == 18:
        st.success('pigeonpeas')

    elif result == 19:
        st.success('pomegranate')

    elif result == 20:
        st.success('rice')

    elif result == 21:
        st.success('watermelon')

    else:
        st.success("Sorry crop can't predicted")
