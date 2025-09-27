import streamlit as st
import pandas as pd
import spacy
from spacy import displacy

st.title("Named Entity Recognition")

text=st.text_area('input text here......')
nlp_model=spacy.load('en_core_web_sm')

if st.button('Analyze entity'):
    if text:
        doc=nlp_model(text)
        html_page=displacy.render(doc,style='ent',page=True)
        st.write(html_page,unsafe_allow_html=True)
        ents_data = [{"Text": ent.text, "Label": ent.label_} for ent in doc.ents]
        if ents_data:
            df = pd.DataFrame(ents_data)
            st.subheader("Entities Table")
            st.dataframe(df, use_container_width=True)
        else:
            st.info("No named entities found.")


    
