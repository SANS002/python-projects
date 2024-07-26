import streamlit as st
import plotly.express as px
import pandas as pd
import os
import matplotlib.pyplot as plt
import plotly.figure_factory as ff
import warnings
warnings.filterwarnings('ignore')

st.set_page_config(page_title="Data Visualizer",page_icon=':bar_chart:',layout="wide")

st.title(':bar_chart: start visualize your data')
st.markdown('<style>div.block-container{padding-top:2rem;}</style>',unsafe_allow_html=True)

fl = st.file_uploader(":file_folder: upload a file",type=(["csv","txt","xlsx","xls"]))
if fl is not None:
    filename =fl.name
    st.write(filename)
    df=pd.read_csv(filename,encoding="ISO-8859-1")
else:
    os.chdir(r'C:\Users\santh\Desktop\python projects\python-projects\datavisualizer')
    df = pd.read_csv(r"C:\Users\santh\Desktop\python projects\python-projects\datavisualizer\SampleSuperstore.csv",encoding="ISO-8859-1")
#creating columns in st

#region filter
region = st.sidebar.multiselect("pick your Region",df["Region"].unique())

if not region:
    df2=df.copy()
else:
    df2 = df[df["Region"].isin(region)]

#for state filter
State = st.sidebar.multiselect("pick your State",df2["State"].unique())
if not State:
    df3 = df2.copy()
else:
    df3 = df2[df2["State"].isin(State)]

#City filter
City = st.sidebar.multiselect("pick the City",df3["City"].unique())

#filter data bssed on above contination
if not region and not State and not City:
    filtered_df = df
elif not State and City:
    filtered_df = df[df["Region"]].isin(region)
elif not region and not City:
    filtered_df = df[df['State'].isin(State)]
elif State and City :
    filtered_df = df3[df['State'].isin(State)& df3['City'].isin(City)]
elif region and City :
    filtered_df = df3[df['Region'].isin(region)& df3['City'].isin(City)]
elif region and State :
    filtered_df = df3[df['Region'].isin(region)& df3['State'].isin(State)]
elif City:
    filtered_df = df3[df3['City'].isin(City)]
else:
    filtered_df=df3[df3['Region'].isin(region)]

Category = filtered_df.groupby( by = ["Category"], as_index = False )["Sales"].sum()

cl1, cl2,cl3,cl4 = st.columns((4))
with cl1: 
    with st.subheader("Category Based Sales"):
        fig = px.bar (Category,x="Category",y="Sales",text=["${:,.2f}".format(x) for x in Category['Sales']],template="seaborn")
        st.plotly_chart(fig,use_container_width=True,height=200)
with cl2:
    with st.subheader("Region Based Sales"):
        fig = px.pie(filtered_df, values= "Sales",names="Region",hole=0.5)
        fig.update_traces(text = filtered_df['Region'],textposition ="outside")
        st.plotly_chart(fig,use_container_width= True)

with cl3:
    with st.expander("Category_ViewDtata"):
        st.write(Category.style.background_gradient(cmap = 'Blues'))
        csv = Category.to_csv(index = False).encode('utf-8')
        st.download_button("categorydownload", data = csv, mime='text/csv')

with cl4:
    with st.expander("Region_ViewData"):
        Region = filtered_df.groupby( by = ["Region"], as_index = False )["Sales"].sum()
        st.write(Region.style.background_gradient(cmap = 'Oranges'))
        csv = Region.to_csv(index = False).encode('utf-8')
        st.download_button("regiondownload", data = csv, mime='text/csv')
#showing line chart for sales and profit
st.subheader("line chart of sales and profit")
linechart = pd.DataFrame(filtered_df.groupby(filtered_df["Profit"])["Sales"].sum()).reset_index()
fig2 = px.line(linechart, x = "Sales",y="Profit" ,labels={"Sales:" "Profit"},height=500, width= 1000, template="gridon")
st.plotly_chart(fig2,use_container_width=True)

with st.expander("View Data for sales and profit"):
     st.write(linechart.style.background_gradient(cmap = 'Oranges'))
     csv = linechart.to_csv(index= False).encode('utf-8')
     st.download_button("Download data", data=csv , mime='text/csv')

st.subheader("Hierarchical view of Sales using TreeMap")
fig3 = px.treemap(filtered_df,path=["Region","Category"], values='Sales',hover_data= ['Sales'],
                color ="Sub-Category")
fig3.update_layout(width=800,height=650)
st.plotly_chart(fig3,use_container_width= True)

chart1,chart2= st.columns(2)
with chart1:
    st.subheader('segment wise sales')
    fig = px.pie(filtered_df,values="Sales",names="Segment",template ="plotly_dark")
    fig.update_traces(text = filtered_df['Segment'],textposition= 'inside')
    st.plotly_chart(fig,use_container_width=True)
with chart2:
    st.subheader('Category wise sales')
    fig = px.pie(filtered_df,values="Sales",names="Category",template ="gridon")
    fig.update_traces(text = filtered_df['Category'],textposition= 'inside')
    st.plotly_chart(fig,use_container_width=True)

st.subheader(":point_right: Sales summary")
with st.expander("summary table"):
    df_sample = df[0:5][["Region","Sales","Profit","Category","City","Quantity"]]
    fig = ff.create_table(df_sample,colorscale="Cividis")
    st.plotly_chart(fig,use_container_width=True)

data1 = px.scatter(filtered_df,x= "Sales",y='Profit',size= "Quantity")
data1['layout'].update(title ="Relationship between Sales and profit using Scatter plot",
                       titlefont = dict(size = 20 ),xaxis = dict(title = "Sales",titlefont = dict(size=19)),
                       yaxis = dict(title="Profit",titlefont = dict(size = 19)))

st.plotly_chart(data1,use_container_width= True)

with st.expander('View your entaire dataset'):
    st.write(filtered_df.iloc[:500,1:20:2].style.background_gradient(cmap="Blues"))

csv = df.to_csv(index = False).encode('utf-8')
st.download_button("download data",data = csv,mime='text/csv')

    







