import streamlit as st
import json
import time
from send_requests import getField
from send_requests import getSeason
from send_requests import CreateReport
from send_requests import getReport
from pr5 import decodeId
from Hello import getUserId


st.set_page_config(page_title="Отчеты", page_icon="🗒")

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
print(f"The user  {encoded_user_id} is on page field")
user_id = ""
try:
    user_id = decodeId(encoded_user_id)
    if len(user_id) == 0:
        st.write('blocked')
    else:
        st.write(user_id)
except Exception as e:
    print(f"Error occuped {e}")


st.markdown("### Отчеты")
st.markdown("___")
st.markdown("Эта страница необходима для просмотра отчетов")

seasons = tuple(getSeasonsArray(user_id))

fields = tuple(getFieldsArray(user_id))

url_column = st.text_input("Вставьте сюда ссылку на вашу гугл папку для отчета")
with st.expander("Параметры отчета"):
    field_column, season_column, nothing_column, button_column = st.columns(4)
    field_option = ""
    with field_column:
        field_option = st.selectbox("Выберите поле:", fields)
    season_option = ""    
    with season_column:
        season_option = st.selectbox("Выберите сезон:", seasons)
    if button_column.button("Сгенерировать"):
        if len(user_id) != 0 and season_option != "Создайте сезон" and field_option != "Cоздайте поле" and len(url_column) != 0:
            CreateReport(user_id, season_option, field_option,"False", url_column)
            time.sleep(3)
            report_url = getReport(url_column)
            nothing_column.markdown(report_url)
        else:
            nothing_column.markdown("У вас нет сезона/поля добавьте его/их")

st.pdf("https://drive.google.com/file/d/1YS6mXY66pRK54ybaac7Z8QNofLryq5TN/view")
#st.pdf()