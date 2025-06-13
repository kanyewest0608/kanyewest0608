import streamlit as st

st.title("🎧 기분별 칸예 웨스트 노래 추천")

mood = st.selectbox(
    "오늘 당신의 기분은 어떤가요?",
    [
        "행복해요 😄",
        "우울해요 😢",
        "에너지가 넘쳐요 ⚡",
        "차분해요 🧘‍♂️",
        "화가 나요 😡",
        "사랑에 빠졌어요 ❤️",
        "감성적이에요 💭",
        "자신감 넘쳐요 💪"
    ]
)

songs = {
    "행복해요 😄": {
        "title": "Good Life",
        "lyrics": "Welcome to the good life, where nothing's too serious.",
        "youtube": "https://www.youtube.com/watch?v=FEKEjpTzB0Q"
    },
    "우울해요 😢": {
        "title": "Hey Mama",
        "lyrics": "Hey Mama, I wanna scream so loud for you.",
        "youtube": "https://www.youtube.com/watch?v=6CHs4x2uqcQ"
    },
    "에너지가 넘쳐요 ⚡": {
        "title": "Stronger",
        "lyrics": "Work it, make it, do it, makes us harder, better, faster, stronger.",
        "youtube": "https://www.youtube.com/watch?v=PsO6ZnUZI0g"
    },
    "차분해요 🧘‍♂️": {
        "title": "Ultralight Beam",
        "lyrics": "This is a God dream, this is everything.",
        "youtube": "https://www.youtube.com/watch?v=6F0P2Fv1c0E"
    },
    "화가 나요 😡": {
        "title": "Black Skinhead",
        "lyrics": "For my theme song, my leather black jeans on.",
        "youtube": "https://www.youtube.com/watch?v=YL3f5OHh06g"
    },
    "사랑에 빠졌어요 ❤️": {
        "title": "Bound 2",
        "lyrics": "I know you're tired of loving, of loving with nobody to love.",
        "youtube": "https://www.youtube.com/watch?v=7fAHtuMko6I"
    },
    "감성적이에요 💭": {
        "title": "Devil In a New Dress",
        "lyrics": "Put your hands to the constellations, the way you look should be a sin, you my sensation.",
        "youtube": "https://www.youtube.com/watch?v=9A_q6f2QZ8k"
    },
    "자신감 넘쳐요 💪": {
        "title": "Power",
        "lyrics": "No one man should have all that power.",
        "youtube": "https://www.youtube.com/watch?v=L53gjP-TtGE"
    }
}

if mood:
    song = songs[mood]
    st.subheader(f"🎵 추천 노래: {song['title']}")
    st.write(f"> {song['lyrics']}")
    st.markdown(f"[YouTube 링크]({song['youtube']})")
