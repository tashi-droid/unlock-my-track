import streamlit as st

# Page config with your theme colors (background, text)
st.set_page_config(page_title="Unlock My Track", layout="centered",
                   initial_sidebar_state="collapsed")

# Inject your theme colors and fonts using CSS + Google Fonts
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

# --- Session State Init ---
if "step" not in st.session_state:
    st.session_state.step = 1
if "selected_vibe" not in st.session_state:
    st.session_state.selected_vibe = None
if "wrong_guess" not in st.session_state:
    st.session_state.wrong_guess = False
if "riddle_unlocked" not in st.session_state:
    st.session_state.riddle_unlocked = False
if "speaks_shona" not in st.session_state:
    st.session_state.speaks_shona = None

# --- Step 1: Vibe Selection ---
if st.session_state.step == 1:
    st.markdown('<h1 class="title-pinyon">Unlock My Track</h1>', unsafe_allow_html=True)
    st.write("## Who Are You Today?")
    vibe = st.radio("Pick your vibe:", ["The Romantic", "The Overthinker", "The Savage", "The Dreamer"],
                    index=0 if st.session_state.selected_vibe is None else
                    ["The Romantic", "The Overthinker", "The Savage", "The Dreamer"].index(st.session_state.selected_vibe))

    if vibe != st.session_state.selected_vibe:
        st.session_state.selected_vibe = vibe

    if st.button("Next"):
        st.session_state.step = 2

# --- Step 2: Vibe Description ---
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

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Back"):
            st.session_state.step = 1
    with col2:
        if st.button("Proceed to Unlock Track"):
            st.session_state.step = 3

# --- Step 3: Riddle ---
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

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Back"):
            st.session_state.step = 2
    with col2:
        if st.button("Unlock"):
            if guess.strip().lower() == "fembere":
                st.session_state.riddle_unlocked = True
                st.session_state.step = 4
                st.session_state.wrong_guess = False
                st.session_state.speaks_shona = None
            else:
                st.session_state.wrong_guess = True
                st.session_state.step = 5

# --- Step 4: Show meaning if user does NOT speak Shona before unlocking track ---
elif st.session_state.step == 5 and st.session_state.wrong_guess:
    st.write("## Do You Speak Shona?")
    answer = st.radio("Please select:", ["Yes", "No"])

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Back"):
            st.session_state.step = 3
            st.session_state.wrong_guess = False
    with col2:
        if st.button("Submit"):
            if answer == "Yes":
                st.session_state.speaks_shona = True
                st.session_state.step = 3
            else:
                st.session_state.speaks_shona = False
                st.session_state.step = 6  # Show meaning page first

# --- Step 5b: Meaning of handi fembere for non-Shona speakers ---
elif st.session_state.step == 6 and st.session_state.speaks_shona == False:
    st.markdown('<h1 class="title-pinyon">What does "handi fembere" mean?</h1>', unsafe_allow_html=True)
    st.write(
        """
        In Shona, *'handi fembere'* means **'I will not guess'** — it's a bold call for honesty.  
        You want clarity, not confusion. Love without mixed signals.  
        And *'fembera'* means **'to guess'** — so, no games here.
        """
    )
    if st.button("Unlock Track"):
        st.session_state.riddle_unlocked = True
        st.session_state.step = 4

    if st.button("Back"):
        st.session_state.step = 3
        st.session_state.wrong_guess = False
        st.session_state.speaks_shona = None

# --- Step 6: Track Unlocked with Coming Soon message ---
elif st.session_state.step == 4 and st.session_state.riddle_unlocked:
    st.markdown('<h1 class="title-pinyon">Track Unlocked</h1>', unsafe_allow_html=True)

    try:
        st.image("Fembere.png", caption="Fembere", use_column_width=True)
    except Exception:
        st.warning("Optional: upload 'Fembere.png' to show the cover art.")

    st.write("The track is *Fembere*.")

    st.markdown("🎵 **Coming Soon!** 🎵")
    st.info("This track isn’t out yet, but stay tuned! You’ll be the first to know when it drops.")

    with st.expander("More about the phrase"):
        st.write(
            "In Shona, *'handi fembere'* means **'I will not guess'** — it's a bold call for honesty. "
            "You want clarity, not confusion. Love without mixed signals. "
            "*'Fembera'* means **'to guess'**, so — no games here."
        )

    st.markdown("#### Presave and follow me for updates:")
    st.markdown("[🎧 Listen on DistroKid](https://distrokid.com/hyperfollow/atashii/fembere)")
    st.markdown("[Instagram](https://www.instagram.com/akanaka._.tashi/)")
    st.markdown("[TikTok](https://tiktok.com/@atashii_sings)")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Back"):
            st.session_state.step = 3
            st.session_state.riddle_unlocked = False
            st.session_state.wrong_guess = False
            st.session_state.speaks_shona = None
    with col2:
        if st.button("Ask Me Questions"):
            st.session_state.step = 7

# --- Step 7: Q&A ---
elif st.session_state.step == 7:
    st.write("## Ask Me Anything")
    question = st.selectbox("Pick a question:", [
        "What inspired this track?",
        "Are you dropping more music soon?",
        "Is this song about someone special?",
        "What is your vibe as an artist?"
    ])

    if question == "What inspired this track?":
        st.write("This track came from a place of being in love — but realizing love only works when both people are truly happy.")
    elif question == "Are you dropping more music soon?":
        st.write("Absolutely. This is just the beginning. More tracks are on the way — real, raw, and full of feeling.")
    elif question == "Is this song about someone special?":
        st.write("Let’s just say I plan on staying in love for the future — don’t ask me who.")
    elif question == "What is your vibe as an artist?":
        st.write("Flirty but deep — I write for people who feel everything but don’t always know how to say it. I sing it for us.")

    if st.button("Back to Track"):
        st.session_state.step = 4
