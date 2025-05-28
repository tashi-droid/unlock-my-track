import streamlit as st

# Page config
st.set_page_config(page_title="Unlock My Track", layout="centered",
                   initial_sidebar_state="collapsed")

# Theme styling
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Pinyon+Script&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Anton&display=swap');

    html, body, [class*="css"] {
        background-color: #1b1b1f;
        color: #fdf6ec;
        font-family: 'Anton', sans-serif;
    }
    .title-pinyon {
        font-family: 'Pinyon Script', cursive !important;
        font-size: 3.8rem;
        font-weight: normal;
        color: #f5d372;
        margin-bottom: 0.3rem;
        text-shadow: 1px 1px 4px #000000cc;
    }
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
    .stApp > .main > div {
        background-color: #2b2b30;
        padding: 2rem;
        border-radius: 15px;
    }
    label[data-baseweb="radio"] > div {
        font-size: 1.3rem;
    }
    </style>
""", unsafe_allow_html=True)

# Session state initialization
for var, val in {
    "step": 1,
    "selected_vibe": None,
    "show_message": False,
    "riddle_unlocked": False,
    "wrong_guess": False,
    "speaks_shona": None
}.items():
    if var not in st.session_state:
        st.session_state[var] = val

# Step 1: Vibe selection
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
        st.session_state.show_message = False

    if st.button("Next"):
        if st.session_state.selected_vibe:
            st.session_state.step = 2

# Step 2: Vibe message
elif st.session_state.step == 2:
    st.markdown('<h1 class="title-pinyon">What your vibe says about you.</h1>', unsafe_allow_html=True)
    vibe = st.session_state.selected_vibe
    messages = {
        "The Romantic": "You are deep in love and willing to give your all. This song mirrors that devotion.",
        "The Overthinker": "You analyse every lyric like a puzzle. If love feels uncertain, this will hit deep.",
        "The Savage": "You do not play games. You want honesty and clarity — and this one is straight to the point.",
        "The Dreamer": "You love the dream of love. Maybe you never say much, but your heart writes novels. This song gets you."
    }
    st.info(messages.get(vibe, ""))

    if st.button("Proceed to Unlock Track"):
        st.session_state.step = 3
    if st.button("Back"):
        st.session_state.step = 1

# Step 3: Riddle
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
            st.session_state.step = 5
            st.session_state.riddle_unlocked = True
            st.session_state.wrong_guess = False
            st.session_state.speaks_shona = None
        else:
            st.error("Wrong guess. Hint: It is a Shona word meaning 'to guess'. Try again!")
            st.session_state.step = 4
            st.session_state.wrong_guess = True

    if st.button("Back"):
        st.session_state.step = 2

# Step 4: Ask if user speaks Shona (after wrong guess)
elif st.session_state.step == 4 and st.session_state.wrong_guess:
    st.write("## Do You Speak Shona?")
    answer = st.radio("Please select:", ["Yes", "No"])

    if st.button("Submit"):
        if answer == "Yes":
            st.session_state.speaks_shona = True
            st.session_state.step = 3
        else:
            st.session_state.speaks_shona = False
            st.session_state.step = 6

    if st.button("Back"):
        st.session_state.step = 3
        st.session_state.wrong_guess = False

# Step 5: Track Unlocked
elif st.session_state.step == 5 and st.session_state.riddle_unlocked:
    st.markdown('<h1 class="title-pinyon">Track Unlocked</h1>', unsafe_allow_html=True)

    try:
        st.image("Fembere.png", caption="Fembere", use_column_width=True)
    except Exception:
        st.error("Cover art image 'Fembere.png' not found.")

    st.write("The track is *Fembere*.")
    with st.expander("What does 'handi fembere' mean?"):
        st.write("""
            In Shona, *'handi fembere'* means **'I will not guess'** — it is a bold call for honesty.  
            You want clarity, not confusion. Love without mixed signals.  
            And *'fembera'* means **'to guess'** — so, no games here.
        """)

    st.markdown("#### Stream it here:")
    st.markdown("(https://distrokid.com/hyperfollow/atashii/fembere)")
    st.markdown("[Instagram](https://www.instagram.com/akanaka._.tashi/)")
    st.markdown("[TikTok](https://tiktok.com/@atashii_sings)")

    if st.button("Ask Me Questions"):
        st.session_state.step = 7

    if st.button("Back"):
        st.session_state.step = 3
        st.session_state.riddle_unlocked = False
        st.session_state.wrong_guess = False
        st.session_state.speaks_shona = None

# Step 6: Explain meaning to non-Shona speakers
elif st.session_state.step == 6 and st.session_state.speaks_shona is False:
    st.markdown('<div class="title-pinyon">What Does "Fembere" Mean?</div>', unsafe_allow_html=True)
    st.write("""
        In Shona, *'fembera'* means **to guess**.  
        So when someone says *'handi fembere'*, they’re saying **“I will not guess.”**

        It’s something people say when they want honesty — no mixed signals, no games.  
        That’s the theme of this track. Direct love. Real talk.
    """)

    if st.button("Unlock the Track"):
        st.session_state.step = 5
        st.session_state.riddle_unlocked = True
        st.session_state.wrong_guess = False

# Step 7: Q&A Page
elif st.session_state.step == 7:
    st.write("## Ask Me Anything")
    question = st.selectbox("Pick a question:", [
        "What inspired this track?",
        "Are you dropping more music soon?",
        "Is this song about someone special?",
        "What is your vibe as an artist?"
    ])

    answers = {
        "What inspired this track?": "This track came from a place of being in love — but realizing love only works when both people are truly happy. I was being honest about my needs, but I could feel he was not, and that gap inspired everything.",
        "Are you dropping more music soon?": "Absolutely. This is just the beginning. More tracks are on the way — real, raw, and full of feeling.",
        "Is this song about someone special?": "Let us just say I plan on staying in love for the future — do not ask me who.",
        "What is your vibe as an artist?": "Flirty but deep — I write for people who feel everything but do not always know how to say it. I sing it for us."
    }

    st.write(answers.get(question, ""))

    if st.button("Back to Track"):
        st.session_state.step = 5
