import streamlit as st

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Great+Vibes&display=swap');

    .aesthetic-title {
        font-family: 'Great Vibes', cursive;
        font-size: 3em;
        text-align: center;
        color: #f5d372; /* gold tone */
        margin-top: 1em;
        margin-bottom: 1em;
        text-shadow: 1px 1px 4px #00000055;
    }
    </style>

    <div class="aesthetic-title">Unlock My Track</div>
""", unsafe_allow_html=True)

st.header("Who Are You Today?")
vibe = st.radio("Pick your vibe:", ["The Romantic", "The Overthinker", "The Savage", "The Dreamer"])

st.write("Hmm... interesting choice 👀")

if vibe == "The Romantic":
    st.info("You're deep in love and willing to give your all. This song mirrors that devotion.")
elif vibe == "The Overthinker":
    st.info("You analyse every lyric like a puzzle. If love feels uncertain, this will hit deep.")
elif vibe == "The Savae♕ ":
    st.info("You don’t play games. You want honesty, clarity — and this one’s straight to the point.")
else:
    st.info("You love the dream of love. Maybe you never say much, but your heart writes novels. This song gets you.")
