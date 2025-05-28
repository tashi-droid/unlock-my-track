import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Guess to Unlock", layout="centered")

# === Set background color using HTML ===
page_bg = """
<style>
body {
    background-color: #fff8f0;
}
.title-pinyon {
    font-family: 'Pinyon Script', cursive;
    font-size: 48px;
    text-align: center;
    margin-top: 20px;
    color: #5a2a27;
}
.subheading {
    font-family: 'Helvetica Neue', sans-serif;
    font-size: 20px;
    text-align: center;
    color: #333333;
    margin-bottom: 40px;
}
button {
    background-color: #5a2a27 !important;
    color: white !important;
}
</style>
<link href="https://fonts.googleapis.com/css2?family=Pinyon+Script&display=swap" rel="stylesheet">
"""
st.markdown(page_bg, unsafe_allow_html=True)

# === Session State Management ===
if 'step' not in st.session_state:
    st.session_state.step = 1
if 'guess' not in st.session_state:
    st.session_state.guess = ''
if 'riddle_unlocked' not in st.session_state:
    st.session_state.riddle_unlocked = False
if 'wrong_guess' not in st.session_state:
    st.session_state.wrong_guess = False
if 'speaks_shona' not in st.session_state:
    st.session_state.speaks_shona = None

# === STEP 1 ===
if st.session_state.step == 1:
    st.markdown('<div class="title-pinyon">Handi Fembere</div>', unsafe_allow_html=True)
    st.markdown('<div class="subheading">Unlock the song by solving this riddle:</div>', unsafe_allow_html=True)

    st.write("**Riddle:** I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?")

    st.session_state.guess = st.text_input("Your answer:", key="guess_input")

    if st.button("Submit"):
        if st.session_state.guess.strip().lower() == "echo":
            st.session_state.riddle_unlocked = True
            st.session_state.step = 7
        else:
            st.session_state.wrong_guess = True
            st.session_state.step = 3

# === STEP 3 (Wrong Answer Feedback) ===
elif st.session_state.step == 3 and st.session_state.wrong_guess:
    st.markdown("### Hmm, not quite. 👀")
    st.write("Do you speak Shona?")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Yes"):
            st.session_state.speaks_shona = True
            st.session_state.step = 4
    with col2:
        if st.button("No"):
            st.session_state.speaks_shona = False
            st.session_state.step = 6  # Go to explanation

    if st.button("Back"):
        st.session_state.step = 1

# === STEP 4 (User says they speak Shona) ===
elif st.session_state.step == 4 and st.session_state.speaks_shona:
    st.markdown("### Ngationei kana uchinyatsoziva 😉")
    st.write("What does *'fembera'* mean in Shona?")

    guess = st.text_input("Your guess:", key="shona_guess")

    if st.button("Submit Meaning"):
        if guess.strip().lower() in ["guess", "to guess", "i guess"]:
            st.success("Correct! Unlocking the track...")
            st.session_state.riddle_unlocked = True
            st.session_state.step = 7
        else:
            st.error("Nice try, but not quite.")
            st.session_state.step = 6  # Proceed to explanation

    if st.button("Back"):
        st.session_state.step = 3

# === STEP 6 (User doesn't speak Shona — Explanation) ===
elif st.session_state.step == 6 and st.session_state.speaks_shona is False:
    st.markdown('<div class="title-pinyon">What Does "Fembere" Mean?</div>', unsafe_allow_html=True)

    st.write("""
        In Shona, *'fembera'* means **to guess**.  
        So when someone says *'handi fembere'*, they’re saying **“I will not guess.”**

        It’s something people say when they want honesty — no mixed signals, no games.  
        That’s the theme of this track. Direct love. Real talk.
    """)

    if st.button("Unlock the Track"):
        st.session_state.step = 7
        st.session_state.riddle_unlocked = True
        st.session_state.wrong_guess = False

    if st.button("Back"):
        st.session_state.step = 3

# === STEP 6 (Fallback: wrong answer but didn't get to choose language) ===
elif st.session_state.step == 6 and st.session_state.speaks_shona is True:
    st.markdown("### Meaning of 'Fembera'")
    st.write("""
        'Fembera' means **to guess**.  
        So *'Handi Fembere'* means *I don’t guess* – I want the truth.
    """)
    if st.button("Unlock the Track"):
        st.session_state.step = 7
        st.session_state.riddle_unlocked = True
        st.session_state.wrong_guess = False

    if st.button("Back"):
        st.session_state.step = 4

# === STEP 7 (Track Unlocked) ===
elif st.session_state.step == 7 and st.session_state.riddle_unlocked:
    st.markdown('<div class="title-pinyon">Unlocked 🔓</div>', unsafe_allow_html=True)

    st.write("Enjoy the track **'Handi Fembere'** below:")
    st.audio("https://your-track-link.com/audio.mp3")  # Replace with real audio link

    st.markdown("💌 *Thank you for playing — this song is about keeping it real in love.*")
