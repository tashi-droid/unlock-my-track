import streamlit as st

# Page config with your theme colors (background, text)
st.set_page_config(page_title="Unlock My Track", layout="centered",
                   initial_sidebar_state="collapsed")

# Inject your theme colors and fonts using CSS + Google Fonts
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Pinyon+Script&display=swap');
    /* Boldoni FLF is not on Google Fonts, so use a close alternative: 'Anton' or 'Playfair Display' */
    @import url('https://fonts.googleapis.com/css2?family=Anton&display=swap');

    html, body, [class*="css"] {
        background-color: #1b1b1f;
        color: #fdf6ec;
        font-family: 'Anton', sans-serif;
    }

    /* Title uses Pinyon Script */
    .title-pinyon {
        font-family: 'Pinyon Script', cursive !important;
        font-size: 3.8rem;
        font-weight: normal;
        color: #f5d372;
        margin-bottom: 0.3rem;
        text-shadow: 1px 1px 4px #000000cc;
    }

    /* Buttons styling to use primaryColor */
    div.stButton > button {
        background-color: #f5d372;
        color: #1b1b1f;
        font-weight: bold;
        border-radius: 12px;
        padding: 0.7em 1.5em;
        font-size: 1.1rem;
        transition: background-color 0.3s ease;
    }
    div.stButton > button:hover {
        background-color: #e0c75a;
    }

    /* Container background color for sections */
    .stApp > .main > div {
        background-color: #2b2b30;
        padding: 2rem;
        border-radius: 15px;
    }

    /* Radio buttons bigger font */
    label[data-baseweb="radio"] > div {
        font-size: 1.3rem;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state variables
if "step" not in st.session_state:
    st.session_state.step = 1
if "selected_vibe" not in st.session_state:
    st.session_state.selected_vibe = None
if "show_message" not in st.session_state:
    st.session_state.show_message = False
if "riddle_unlocked" not in st.session_state:
    st.session_state.riddle_unlocked = False
if "wrong_guess" not in st.session_state:
    st.session_state.wrong_guess = False
if "speaks_shona" not in st.session_state:
    st.session_state.speaks_shona = None

# --- Step 1: Vibe Selection with only one Next button ---
if st.session_state.step == 1:
    st.markdown('<h1 class="title-pinyon">Unlock My Track</h1>', unsafe_allow_html=True)

    st.write("## Who Are You Today?")
    vibe = st.radio(
        "Pick your vibe:",
        ["The Romantic", "The Overthinker", "The Savage", "The Dreamer"],
        index=0 if st.session_state.selected_vibe is None else
        ["The Romantic", "The Overthinker", "The Savage", "The Dreamer"].index(st.session_state.selected_vibe)
    )

    if vibe != st.session_state.selected_vibe:
        st.session_state.selected_vibe = vibe
        st.session_state.show_message = False  # reset message on change

    if st.button("Next"):
        if st.session_state.selected_vibe:
            st.session_state.step = 2

# --- Step 2: Show vibe message + Proceed button ---
elif st.session_state.step == 2:
    st.markdown('<h1 class="title-pinyon">What your vibe says about you.</h1>', unsafe_allow_html=True)

    vibe = st.session_state.selected_vibe
    if vibe == "The Romantic":
        st.info("You are deep in love and willing to give your all. This song mirrors that devotion.")
    elif vibe == "The Overthinker":
        st.info("You analyse every lyric like a puzzle. If love feels uncertain, this will hit deep.")
    elif vibe == "The Savage":
        st.info("You do not play games. You want honesty and clarity — and this one is straight to the point.")
    elif vibe == "The Dreamer":
        st.info("You love the dream of love. Maybe you never say much, but your heart writes novels. This song gets you.")

    if st.button("Proceed to Unlock Track"):
        st.session_state.step = 3

    if st.button("Back"):
        st.session_state.step = 1

# --- Step 3: Riddle Page ---
elif st.session_state.step == 3:
    st.write("## Solve This Riddle To Unlock The Track")
    st.markdown(
        "> If I am not a mind reader,  \n"
        "> If I want to know exactly what my love wants,  \n"
        "> If I am not a fan of guessing games,  \n"
        "> In Shona, I say “handi... ?”  \n"
        "> *(Fill in the blank — what is the missing word?)*"
    )

    guess = st.text_input("Your answer:")

    if st.button("Unlock"):
        if guess.strip().lower() == "fembere":
            st.session_state.riddle_unlocked = True
            st.session_state.step = 4
            st.session_state.wrong_guess = False
            st.session_state.speaks_shona = None
        else:
            st.error("Wrong guess. Hint: It is a Shona word meaning 'to guess'. Try again!")
            st.session_state.wrong_guess = True
            st.session_state.step = 5

    if st.button("Back"):
        st.session_state.step = 2

# --- Step 4: Wrong guess — ask if user speaks Shona ---
elif st.session_state.step == 5 and st.session_state.wrong_guess:
    st.write("## Do You Speak Shona?")
    answer = st.radio("Please select:", ["Yes", "No"])

    if st.button("Submit"):
        if answer == "Yes":
            st.session_state.speaks_shona = True
            st.session_state.step = 3
        else:
            st.session_state.speaks_shona = False
            st.session_state.riddle_unlocked = True
            st.session_state.step = 4

    if st.button("Back"):
        st.session_state.step = 3
        st.session_state.wrong_guess = False

# --- Step 5: Track unlocked page ---
elif st.session_state.step == 4 and st.session_state.riddle_unlocked:
    st.markdown('<h1 class="title-pinyon">Track Unlocked</h1>', unsafe_allow_html=True)

    try:
        st.image("Fembere.png", caption="Fembere", use_column_width=True)
    except Exception:
        st.error("Cover art image 'Fembere.png' not found.")

    st.write("The track is *Fembere*.")
    with st.expander("What does 'handi fembere' mean?"):
        st.write(
            """
            In Shona, *'handi fembere'* means **'I will not guess'** — it is a bold call for honesty.  
            You want clarity, not confusion. Love without mixed signals.  
            And *'fembera'* means **'to guess'** — so, no games here.
            """
        )

    try:
        with open('fembere_chorus.mp3', 'rb') as chorus_file:
            chorus_bytes = chorus_file.read()
            st.audio(chorus_bytes, format='audio/mp3', start_time=0)
    except FileNotFoundError:
        st.error("Chorus audio file not found. Please upload 'fembere_chorus.mp3'.")

    st.markdown("#### Stream it here:")
    st.markdown("[Instagram](https://www.instagram.com/akanaka._.tashi/)")
    st.markdown("[TikTok](https://tiktok.com/@atashii_sings)")

    if st.button("Ask Me Questions"):
        st.session_state.step = 6

    if st.button("Back"):
        st.session_state.step = 3
        st.session_state.riddle_unlocked = False
        st.session_state.wrong_guess = False
        st.session_state.speaks_shona = None

# --- Step 6: Q&A page ---
elif st.session_state.step == 6:
    st.write("## Ask Me Anything")
    question = st.selectbox("Pick a question:", [
        "What inspired this track?",
        "Are you dropping more music soon?",
        "Is this song about someone special?",
        "What is your vibe as an artist?"
    ])

    if question == "What inspired this track?":
        st.write(
            "This track came from a place of being in love — but realizing love only works when both people are truly happy. "
            "I was being honest about my needs, but I could feel he was not, and that gap inspired everything."
        )
    elif question == "Are you dropping more music soon?":
        st.write("Absolutely. This is just the beginning. More tracks are on the way — real, raw, and full of feeling.")
    elif question == "Is this song about someone special?":
        st.write("Let us just say I plan on staying in love for the future — do not ask me who.")
    elif question == "What is your vibe as an artist?":
        st.write("Flirty but deep — I write for people who feel everything but do not always know how to say it. I sing it for us.")

    if st.button("Back to Track"):
        st.session_state.step = 4
