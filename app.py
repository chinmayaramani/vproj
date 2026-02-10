import streamlit as st
import random
from datetime import datetime

st.set_page_config(page_title="Will you be my Valentine? 💘", page_icon="💘", layout="centered")

# --- Simple CSS styling ---
st.markdown("""
<style>
.big-title { font-size: 48px; font-weight: 800; text-align: center; }
.sub { font-size: 18px; text-align: center; opacity: 0.9; }
.card {
  background: rgba(255,255,255,0.08);
  border: 1px solid rgba(255,255,255,0.15);
  padding: 18px;
  border-radius: 18px;
  margin-top: 14px;
}
.center { text-align: center; }
.small { font-size: 14px; opacity: 0.8; }
</style>
""", unsafe_allow_html=True)

# --- Personalize ---
HER_NAME = "My Love"   # change this
YOUR_NAME = "Chinmaya" # change this

# --- Session state ---
if "no_count" not in st.session_state:
    st.session_state.no_count = 0
if "accepted" not in st.session_state:
    st.session_state.accepted = False

st.markdown(f"<div class='big-title'>Hey {HER_NAME} 💗</div>", unsafe_allow_html=True)
st.markdown("<div class='sub'>I made this just for you.</div>", unsafe_allow_html=True)

st.markdown("""
<div class="card center">
  <h2>Will you be my Valentine? 💘</h2>
  <p class="small">Choose wisely 😌</p>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="large")

with col1:
    yes = st.button("YES 💖", use_container_width=True)

with col2:
    no = st.button("NO 🙃", use_container_width=True)

if yes:
    st.session_state.accepted = True

if no and not st.session_state.accepted:
    st.session_state.no_count += 1

if st.session_state.accepted:
    st.balloons()
    st.success("YAYYYY! 💘💘💘")
    st.markdown(f"""
    <div class="card">
      <h3>Okay it's official 😭💗</h3>
      <p>Happy Valentine’s Day, {HER_NAME}.</p>
      <p>I’m really grateful for you — and I’d love to make this day special.</p>
      <p><b>Love,</b><br>{YOUR_NAME}</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
      <h4>Tonight’s plan 🍓✨</h4>
      <ul>
        <li>One cute date</li>
        <li>Your favorite food</li>
        <li>Photos + a small surprise</li>
      </ul>
    </div>
    """, unsafe_allow_html=True)

else:
    if st.session_state.no_count > 0:
        responses = [
            "Hmm… that button seems suspicious 😤",
            "Try again 😭",
            "Nope. Wrong choice 😌",
            "Okay but like… really? 🥲",
            "I’ll pretend I didn’t see that 😅",
        ]
        st.warning(f"{random.choice(responses)}  (Attempts: {st.session_state.no_count})")

    st.markdown("""
    <div class="center small" style="margin-top:10px;">
      Tip: the correct answer is obvious 😌
    </div>
    """, unsafe_allow_html=True)
