import streamlit as st
st.set_page_config(layout='wide')
import json
import pandas as pd
import s3fs
import numpy as np
import matplotlib.pyplot as plt

FS = s3fs.S3FileSystem(anon=False)

@st.cache(ttl = 3600*10)
def get_data():
    return pd.read_json('outputs/allscores-nocrawl-metals-usa.json')
    

if __name__ == '__main__':
    _, col, _ = st.columns([1,5,1])

    df = get_data()
    st.dataframe(df[['name','title','twitter_handle','vocality','pagerank','mentions','vocality_scaled','pagerank_scaled','mentions_scaled','overall_score']], height=1600)
