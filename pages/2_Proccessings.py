import streamlit as st
import json
from send_requests import getField
from send_requests import getSeason
from send_requests import createSeason
from send_requests import SetProcessing
from pr5 import Processing
from pr5 import decodeId
from Hello import getUserId

st.set_page_config(page_title="Обработки", page_icon="🚜")


def getFieldsArray(user_id):
    try:
        fields_array = json.loads(getField("", user_id))
    except Exception as e:
        print(f"Ошибка во время получения полей {e}")
        fields_array = None
    
    fields = []
    if fields_array != None:
        for index, value in enumerate(fields_array):
            if value == "Seasons":
                continue
            fields.append(value)
        return fields
    print(f"Поля пользователя {user_id} не найдены")
    return ["Cоздайте поле"]

def getSeasonsArray(user_id):
    seasons_data = json.loads(getSeason(user_id))
    print(seasons_data)
    seasons = []
    if seasons_data != None:
        seasons = [i for i in seasons_data]
        return seasons
    print("Сезоны не найдены")
    seasons.append("Создайте сезон")
    return seasons


encoded_user_id = getUserId()
print(f"The user  {encoded_user_id} is on page proccessings")

if 'procc_name' not in st.session_state:
    st.session_state['procc_name'] = ''
if 'procc_cost' not in st.session_state:
    st.session_state['procc_cost'] = 0
if 'procc_norma' not in st.session_state:
    st.session_state['procc_norma'] = 0
if 'field_option' not in st.session_state:
    st.session_state['field_option'] = ''
if 'season_option' not in st.session_state:
    st.session_state['season_option'] = ''
if 'season_name' not in st.session_state:
    st.session_state['season_name'] = ''

user_id = ""
try:
    user_id = decodeId(encoded_user_id)
    if len(user_id) == 0:
        st.write('blocked')
    else:
        st.write(user_id)
except Exception as e:
    print(f"Error occuped {e}")
    
#5775480864 - my profile id
st.markdown("# Обработки 🚜")
st.markdown("___")
st.markdown("Эта страница необходима, чтобы добавлять обработки к полям, но сначала создайте сезон!")



seasons = tuple(getSeasonsArray(user_id))

fields = tuple(getFieldsArray(user_id))



with st.expander("Добавить обработку"):
    st.session_state['procc_name'] = st.text_input("Введите название обработки", "Сев")
    #left.text_input("Введите название поля", "Поле№1")
    st.session_state['procc_norma'] = st.number_input("Введите норму на гектар")
    st.session_state['procc_cost'] = st.number_input("Введите цену")
    st.session_state['field_option'] = st.selectbox("Выберите поле:", fields)
    st.session_state['season_option'] = st.selectbox("Выберите сезон:", seasons)
    field_column, season_column, nothing_column, button_column = st.columns(4)
    if button_column.button("Добавить"):
        #nothing_column.markdown(f"Data is {procc_name}, {procc_cost}, {procc_norma}, {field_option}, {season_option}")
        if len(user_id) != 0:
            user_proc = Processing(st.session_state['procc_name'])
            if st.session_state['season_option'] != "Создайте сезон" and st.session_state['field_option'] != "Cоздайте поле":
                user_proc.setField(st.session_state['field_option'])
                user_proc.setHerbicide("", st.session_state['procc_norma'], st.session_state['procc_cost'])
                user_proc.season = st.session_state['season_option']
                SetProcessing(user_proc, user_id, user_proc.field)
            else:
                nothing_column.markdown("У вас нет сезона/поля добавьте его/их")
            #nothing_column.markdown("Создайте сезон")


with st.expander("Введите название сезона"):
    st.session_state['season_name'] = st.text_input("Введите название сезона", "Пример")
    b1, b2, b3, b4 = st.columns(4)
    if b4.button("Подтвердить"):
        if st.session_state['season_name'] != "Пример" and len(user_id) != 0:
            createSeason(user_id, st.session_state['season_name'])
            seasons = tuple(getSeasonsArray(user_id))

            

