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

    # QR Code
    try:
        st.image("Fembere_QR.png", caption="Scan to stream 'Fembere'", width=200)
    except Exception:
        st.warning("QR code image 'Fembere_QR.png' not found.")

    # Audio preview
    try:
        st.audio("Fembere_Preview.mp3")
    except Exception:
        st.warning("Audio preview file 'Fembere_Preview.mp3' not found.")

    if st.button("Ask Me Questions"):
        st.session_state.step = 7

    if st.button("Back"):
        st.session_state.step = 3
        st.session_state.riddle_unlocked = False
        st.session_state.wrong_guess = False
        st.session_state.speaks_shona = None
