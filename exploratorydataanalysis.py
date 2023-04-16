import pandas as pd
import numpy as np
import streamlit as st
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

# web app title
st.markdown('''
# The EDA App 
''')

#upload csv data
with st.sidebar.header('1. Upload you csv data'):
     uploaded_file=st.sidebar.file_uploader('upload you input csv')
     st.sidebar.markdown('''
     [Example csv  input file](https://github.com/bharath23-design)''')   
    
# pandas csv data    
if uploaded_file is not None:
    @st.cache_data()
    def load_csv():
        csv=pd.read_csv(uploaded_file)
        return csv
    
    df=load_csv()
    pr=ProfileReport(df,explorative=True)
    st.header('Input Profiling Report')
    st.write(df)
    st.write('_____')
    st.header('Pandas Profiling Report')
    st_profile_report(pr)
    
else:
    st.info('Awaiting for csv file to be uploaded')
    if st.button('Press to use Example Dataset'):
        @st.cache_data()
        def load_data():
            a=pd.DataFrame(
            
            np.random.rand(100,5),
            columns=['a','b','c','d','e']
            )
            return a
        df=load_data()
        pr=ProfileReport(df,explorative=True)
        st.header('Input Dataframe')
        st.write(df)
        st.write('______')
        st.header('pandas profiling report')
        st_profile_report(pr)