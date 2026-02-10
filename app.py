import streamlit as st
import random

st.set_page_config(page_title="For Nikku", page_icon="💗", layout="centered")

# --- Personalize ---
HER_FULL_NAME = "Nikita Singh"
HER_NICKNAME = "Nikku"
YOUR_NAME = "Chinmaya"

# Optional: passcode lock. Leave empty "" to disable.
SECRET_CODE = ""  # e.g. "1402"

# --- Style (clean, not loud) ---
st.markdown("""
<style>
[data-testid="stAppViewContainer"]{
  background: radial-gradient(circle at 18% 12%, rgba(255,255,255,0.55), transparent 35%),
              linear-gradient(135deg, #ffd1dc 0%, #ffb8c9 50%, #f7a6c7 100%);
}
[data-testid="stHeader"]{ background: rgba(0,0,0,0); }

.wrap { max-width: 720px; margin: 0 auto; }
.title { font-size: 44px; font-weight: 900; text-align: center; margin: 8px 0 0 0; }
.subtitle { font-size: 15px; text-align: center; opacity: 0.9; margin: 6px 0 18px 0; }

.card{
  background: rgba(255,255,255,0.20);
  border: 1px solid rgba(255,255,255,0.38);
  padding: 18px 18px;
  border-radius: 18px;
  box-shadow: 0 10px 30px rgba(0,0,0,0.08);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  margin-top: 14px;
}

.small { font-size: 13px; opacity: 0.85; }
.center { text-align: center; }
hr { border: none; height: 1px; background: rgba(255,255,255,0.35); margin: 14px 0; }

button[kind="primary"], button[kind="secondary"]{
  border-radius: 14px !important;
  padding: 0.8rem 1rem !important;
  font-weight: 700 !important;
}
</style>
""", unsafe_allow_html=True)

# --- Optional lock screen ---
if "unlocked" not in st.session_state:
    st.session_state.unlocked = False

if SECRET_CODE.strip() and not st.session_state.unlocked:
    st.markdown("<div class='wrap'>", unsafe_allow_html=True)
    st.markdown(f"<div class='title'>For {HER_NICKNAME}</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>Enter the code.</div>", unsafe_allow_html=True)

    code = st.text_input("Secret code", type="password")
    if st.button("Unlock", use_container_width=True):
        if code.strip() == SECRET_CODE.strip():
            st.session_state.unlocked = True
            st.rerun()
        else:
            st.error("Wrong code. Try again.")
    st.markdown("</div>", unsafe_allow_html=True)
    st.stop()

# --- Session state ---
if "no_count" not in st.session_state:
    st.session_state.no_count = 0
if "accepted" not in st.session_state:
    st.session_state.accepted = False

# --- Header ---
st.markdown("<div class='wrap'>", unsafe_allow_html=True)
st.markdown(f"<div class='title'>Hey {HER_NICKNAME}</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Made in Canada, meant for you.</div>", unsafe_allow_html=True)

# --- Main prompt card ---
st.markdown(f"""
<div class="card center">
  <div style="font-size:20px; font-weight:800;">Will you be my Valentine?</div>
  <div class="small" style="margin-top:6px;">Just answer honestly. No pressure.</div>
</div>
""", unsafe_allow_html=True)

# --- Buttons ---
col1, col2 = st.columns(2, gap="large")
with col1:
    yes = st.button("Yes", use_container_width=True)
with col2:
    no = st.button("No", use_container_width=True)

if yes:
    st.session_state.accepted = True

if no and not st.session_state.accepted:
    st.session_state.no_count += 1

# --- Responses ---
if st.session_state.accepted:
    st.balloons()
    st.markdown(f"""
<div class="card">
  <div style="font-size:18px; font-weight:800; margin-bottom:8px;">Okay, good.</div>

  <p>Everyone thinks you’re the “scary” one — the Aishwarya Rai vibe, the baddie energy, the sharp face.
  But I know you’re actually soft. You just don’t waste kindness on people who don’t deserve it.</p>

  <p>We’ve done three years of long distance. Different countries, different time zones, and still…
  you’ve stayed my favourite person. I wait all year for those summer days when I get to see you properly.</p>

  <p>I keep thinking about your Bali trip and how you looked so happy there.
  One day you’ll get that beach farmhouse. And when you do, I’m coming with you — no debate.</p>

  <hr/>

  <p>Also, I owe you a proper date. Pink outfit. A nice café. Sunflowers.
  And tiramisu — the one you like from Baked by Nini’s.</p>

  <p style="margin-top:14px;"><b>Happy Valentine’s Day, {HER_NICKNAME}.</b></p>
  <p class="small">— {YOUR_NAME}</p>
</div>
""", unsafe_allow_html=True)

else:
    if st.session_state.no_count > 0:
        soft_lines = [
            "Are you sure?",
            "I’ll pretend I didn’t see that.",
            "Try again — without the attitude.",
            "Okay, comedian.",
            "Be nice to me.",
        ]
        st.markdown(f"""
<div class="card center">
  <div style="font-weight:800;">{random.choice(soft_lines)}</div>
  <div class="small" style="margin-top:6px;">No clicks so far: {st.session_state.no_count}</div>
</div>
""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
