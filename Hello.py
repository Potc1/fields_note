import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)
def getUserId():
    id_tg = components.declare_component(
        "tg_id",
        path="./components_for_tg"
    )
    user_id = id_tg()
    return user_id

st.write("# Welcome to Streamlit! 👋")


st.sidebar.success("Select a demo above.")

st.markdown(
    """
    Streamlit is an open-source app framework built specifically for
    Machine Learning and Data Science projects.
    **👈 Select a demo from the sidebar** to see some examples
    of what Streamlit can do!
    ### Want to learn more?
    - Check out [streamlit.io](https://streamlit.io)
    - Jump into our [documentation](https://docs.streamlit.io)
    - Ask a question in our [community
        forums](https://discuss.streamlit.io)
    ### See more complex demos
    - Use a neural net to [analyze the Udacity Self-driving Car Image
        Dataset](https://github.com/streamlit/demo-self-driving)
    - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
"""
)
st.markdown("### id_user: ")
id_tg = components.declare_component(
    "tg_id",
    path="./components_for_tg"
)
user_id = id_tg()
st.markdown(user_id)
