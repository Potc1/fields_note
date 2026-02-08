import streamlit as st
from pr5 import Field
from pr5 import decodeId
from send_requests import reqCreateField
from Hello import getUserId

st.set_page_config(page_title="Поля", page_icon="🌱")

st.sidebar.header("Fields")

st.markdown("# Поля 🌱")

st.markdown("___")
st.markdown("Эта страница позволяет добавить поля или просмотреть существующие")
# Достаем закодированный user_id
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
with st.expander("Введите данные поля"):
    field_name = st.text_input("Введите название поля", "Поле№1")
    #left.text_input("Введите название поля", "Поле№1")
    field_area = st.number_input("Введите площадь поля")
    #right.number_input("Введите площадь поля")
    b1, b2, b3, b4 = st.columns(4)
    if b4.button("Подтвердить"):
        if (len(user_id) != 0):
            b1.markdown(f"Name is {field_name}")
            b2.markdown(f"Area is {field_area}")
            field = Field(field_area, field_name)
            reqCreateField(field ,user_id)
