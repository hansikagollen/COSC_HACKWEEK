import streamlit as st
import lyricsgenius
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Genius API setup
genius = lyricsgenius.Genius("WI_Bm4oIDPUDrUZAcgoy1-BJQ7tjJqAy0GSKucmIdfpdNIAEaYvhaBFLtfkrF8PU")
genius.skip_non_songs = True
genius.excluded_terms = ["(Remix)", "(Live)"]
genius.remove_section_headers = True

st.set_page_config(page_title="Taylor Swift Lyrics Visualizer 🎤")

st.title("🎶 Taylor Swift Lyrics Visualizer")
song_title = st.text_input("Enter a Taylor Swift song title:")

if st.button("Get Lyrics") and song_title:
    try:
        with st.spinner("Fetching lyrics..."):
            song = genius.search_song(song_title, "Taylor Swift")
            lyrics = song.lyrics if song else None

        if lyrics:
            st.subheader("📝 Lyrics:")
            st.text_area(label="", value=lyrics, height=300)

            # Word Cloud
            st.subheader("☁️ Word Cloud:")
            wordcloud = WordCloud(width=800, height=400, background_color='white').generate(lyrics)
            fig, ax = plt.subplots(figsize=(10, 5))
            ax.imshow(wordcloud, interpolation='bilinear')
            ax.axis("off")
            st.pyplot(fig)
        else:
            st.error("Could not find lyrics. Please check the song title.")
    except Exception as e:
        st.error(f"Error: {e}")
