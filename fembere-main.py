import streamlit as st
# Inject your theme colors and fonts using CSS + Google Fonts

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Pinyon+Script&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Anton&display=swap');

    /* Apply base styles to body */
    body, .css-1d391kg {  /* The class may vary; .css-1d391kg is often the main content container */
        background-color: #1b1b1f !important;
        color: #fdf6ec !important;
        font-family: 'Anton', sans-serif !important;
    }

    /* Title uses Pinyon Script */
    .title-pinyon {
        font-family: 'Pinyon Script', cursive !important;
        font-size: 4rem !important;
        font-weight: normal !important;
        color: #f5d372 !important;
        margin-bottom: 0.3rem !important;
        text-shadow: 1px 1px 4px #000000cc !important;
    }

    /* Style stButton buttons */
    div.stButton > button {
        background-color: #f5d372 !important;
        color: #1b1b1f !important;
        font-weight: bold !important;
        border-radius: 12px !important;
        padding: 0.7em 1.5em !important;
        font-size: 1.1rem !important;
        transition: background-color 0.3s ease !important;
        border: none !important;
        cursor: pointer !important;
    }
    div.stButton > button:hover {
        background-color: #e0c75a !important;
    }

    /* Container background */
    .stApp > .main > div {
        background-color: #2b2b30 !important;
        padding: 2rem !important;
        border-radius: 15px !important;
    }

    /* Radio buttons bigger font */
    label[data-baseweb="radio"] > div {
        font-size: 1.3rem !important;
    }
    </style>
""", unsafe_allow_html=True)


# Track correct guesses
if "riddle_correct_total" not in st.session_state:
    st.session_state.riddle_correct_total = 0

# App state
defaults = {
    "step": 1,
    "selected_vibe": None,
    "riddle_unlocked": False,
    "speaks_shona": None,
}
for k, v in defaults.items():
    st.session_state.setdefault(k, v)

correct_answer = "fembere"
vibe_messages = {
    "The Romantic": "You are deep in love and willing to give your all. This song mirrors that devotion.",
    "The Overthinker": "You analyse every lyric like a puzzle. If love feels uncertain to you right now, this song will hit deep.",
    "The Savage": "You do not play games. You want honesty and clarity — and this one is straight to the point. Give it a listen.",
    "The Dreamer": "You love the dream of love. Maybe you never say much, but your heart writes novels. This song gets you.",
}

# STEP 1: Pick vibe
if st.session_state.step == 1:
    st.title("Unlock My Track")
    st.subheader("Who Are You Today?")
    vibe = st.radio("Pick your vibe:", list(vibe_messages.keys()), index=0)

    if st.button("Next"):
        st.session_state.selected_vibe = vibe
        st.session_state.step = 2

# STEP 2: Show vibe message
elif st.session_state.step == 2:
    st.subheader("A message for you")
    st.info(vibe_messages[st.session_state.selected_vibe])

    col1, col2 = st.columns(2)
    if col1.button("Back"):
        st.session_state.step = 1
    if col2.button("Proceed to Unlock Track"):
        st.session_state.step = 3

# STEP 3: Solve riddle
elif st.session_state.step == 3:
    st.subheader("Solve This Riddle To Unlock The Track")
    st.markdown(
        "> If I am not a mind reader,\n"
        "> If I want to know exactly what my love wants,\n"
        "> If I am not a fan of guessing games,\n"
        "> In Shona, I say “handi... ?”"
    )

    guess = st.text_input("Your answer:").strip().lower()

    if st.button("Unlock"):
        if guess == correct_answer:
            st.session_state.riddle_unlocked = True
            st.session_state.riddle_correct_total += 1
            st.session_state.step = 4
        else:
            st.session_state.step = 5

    if st.button("Back"):
        st.session_state.step = 2

# STEP 4: Correct riddle
elif st.session_state.step == 4:
    st.success("🎉 You unlocked the track!")
    try:
        st.image("Fembere.png", caption="Fembere", use_container_width=True)
    except:
        st.warning("Image not found.")

    st.markdown("The track is **Fembere**.")
    st.markdown('<h1 class="subheader-pinyon">Fembere</h1>', unsafe_allow_html=True)

    st.markdown("**Total correct answers so far:** " + str(st.session_state.riddle_correct_total))

    with st.expander("What does 'handi fembere' mean?"):
        st.write("In Shona, *'handi fembere'* means **'I will not guess'**. No games. Just truth.")

    st.markdown("#### Stream it here:")
    st.markdown("[Listen on DistroKid](https://distrokid.com/hyperfollow/atashii/fembere)")

    if st.button("Ask Me Questions"):
        st.session_state.step = 7

    if st.button("Back"):
        st.session_state.step = 3
        st.session_state.riddle_unlocked = False

# STEP 5: Do you speak Shona?
elif st.session_state.step == 5:
    st.warning("Do you speak Shona?")
    lang = st.radio("Please select:", ["Yes", "No"])

    if st.button("Submit"):
        if lang == "Yes":
            st.session_state.step = 3
        else:
            st.session_state.step = 6

    if st.button("Back"):
        st.session_state.step = 3

# STEP 6: Explain for non-speakers
elif st.session_state.step == 6:
    st.subheader("What does 'handi fembere' mean?")
    st.write("""
        In Shona, *'handi fembere'* means **'I will not guess'**.  
        It’s something we say when we want direct, honest communication — not games or mixed signals.  
        It’s also the title of this track, because love should be clear.
    """)

    st.markdown("Now that you know, feel free to enjoy the track!")
    if st.button("Unlock Track Anyway"):
        st.session_state.riddle_unlocked = True
        st.session_state.step = 4

    if st.button("Back"):
        st.session_state.step = 5

# STEP 7: Q&A
elif st.session_state.step == 7:
    st.subheader("Ask Me Anything")

    q = st.selectbox("Pick a question:", [
        "What inspired this track?",
        "Are you dropping more music soon?",
        "Is this song about someone special?",
        "What is your vibe as an artist?"
    ])

    answers = {
        "What inspired this track?": "From being in love but realising love only works when both people are truly happy.",
        "Are you dropping more music soon?": "Absolutely. This is just the beginning.",
        "Is this song about someone special?": "Let’s just say I plan on staying in love for the future — don’t ask me who.",
        "What is your vibe as an artist?": "Flirty but deep. I write for people who feel everything but don’t always know how to say it.",
    }

    st.success(answers[q])

    if st.button("Back to Track"):
        st.session_state.step = 4
