#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def app():
    """
    Set appearance to wide mode.
    """
    st.title("This is the machine learning page")

    dashboardurl = 'http://10.12.105.26:8050'
    st.components.v1.iframe(dashboardurl, width=None, height=900, scrolling=True)

