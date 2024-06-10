import streamlit as st
from pytube import YouTube

def main():
    st.title("YOUTUBE VIDEO DOWNLOADER")
    st.subheader('download the youtube video from the URL')
    y_url =st.text_input("Enter the URL ")#for entering the url

    #select box for the video quality select from the user (highest_resolution","lowest_resolution","audio)it's pytube pre options so we can use it 
    option = st.selectbox("select the video quality ",("highest resolution","lowest resolution","audio"))

    if st.button('download'):
        d_video = YouTube(y_url)#defin the url video from the youtube 
        st.write(d_video.title)

        if option == "audio":
            d_video.streams.get_audio_only().download()#.streams used to access the video .get_audio_only() fro getiing audio only download()for download
        elif option == "highest resolution":
            d_video.streams.get_highest_resolution().download()
        elif option == "lowest resolution":
            d_video.streams.get_lowest_resolution().download()
        else:
            st.write("Oops somthing went to wrong..!")

if __name__ == '__main__':
    main()



