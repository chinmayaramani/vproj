import streamlit as st
import random

# ----------------------------
# CONFIG
# ----------------------------
st.set_page_config(
    page_title="For Pooku 💘",
    page_icon="💖",
    layout="centered",
)

# ✅ Personalize here
HER_FULL_NAME = "Nikita Singh"
HER_NICKNAME = "Pooku"
YOUR_NAME = "Chinmaya"

# Optional: add a simple passcode (set to "" to disable)
SECRET_CODE = ""  # e.g., "1402" or "nikku"  (leave "" to skip lock screen)

# ----------------------------
# STYLING (Luxury Barbie Pink + floating hearts)
# ----------------------------
st.markdown(
    """
<style>
/* page background */
[data-testid="stAppViewContainer"]{
  background: radial-gradient(circle at 20% 10%, rgba(255,255,255,0.45), transparent 35%),
              linear-gradient(135deg, #ffd1dc 0%, #ffb6c1 45%, #f7a6c7 100%);
}
[data-testid="stHeader"]{ background: rgba(0,0,0,0); }

/* Force text color (fix mobile dark mode issue) */
html, body, [class*="css"], .stMarkdown, p, h1, h2, h3, h4, h5, h6, span, div {
    color: #2b2b2b !important;
}

/* Light themed buttons */
.stButton > button {
    background: rgba(255, 255, 255, 0.55) !important;
    color: #2b2b2b !important;
    border: 1px solid rgba(255,255,255,0.7) !important;
    border-radius: 14px !important;
    font-weight: 700 !important;
    box-shadow: 0 8px 20px rgba(0,0,0,0.08) !important;
    transition: all 0.2s ease-in-out !important;
}

.stButton > button:hover {
    background: rgba(255, 255, 255, 0.75) !important;
    transform: scale(1.03);
}

.big-title { font-size: 44px; font-weight: 900; text-align: center; margin-top: 8px; }
.sub { font-size: 16px; text-align: center; opacity: 0.95; margin-bottom: 14px; }

.card {
  background: rgba(255,255,255,0.18);
  border: 1px solid rgba(255,255,255,0.35);
  padding: 18px 18px;
  border-radius: 18px;
  box-shadow: 0 10px 30px rgba(0,0,0,0.08);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  margin-top: 14px;
}

.center { text-align: center; }
.small { font-size: 13px; opacity: 0.85; }
hr { border: none; height: 1px; background: rgba(255,255,255,0.35); margin: 12px 0; }

/* floating hearts */
@keyframes floatUp {
  0%   { transform: translateY(0) scale(1); opacity: 0; }
  10%  { opacity: 0.35; }
  100% { transform: translateY(-120vh) scale(1.25); opacity: 0; }
}
.heart {
  position: fixed;
  bottom: -20px;
  z-index: 0;
  font-size: 18px;
  color: rgba(255,255,255,0.55);
  animation: floatUp linear infinite;
  pointer-events: none;
}
</style>

<div class="heart" style="left:10%; animation-duration: 12s; animation-delay: 0s;">💗</div>
<div class="heart" style="left:22%; animation-duration: 10s; animation-delay: 1s;">💖</div>
<div class="heart" style="left:35%; animation-duration: 14s; animation-delay: 2s;">💞</div>
<div class="heart" style="left:50%; animation-duration: 11s; animation-delay: 0.5s;">💘</div>
<div class="heart" style="left:63%; animation-duration: 13s; animation-delay: 1.5s;">💕</div>
<div class="heart" style="left:78%; animation-duration: 9s;  animation-delay: 2.2s;">💓</div>
<div class="heart" style="left:90%; animation-duration: 15s; animation-delay: 0.2s;">💗</div>
""",
    unsafe_allow_html=True,
)

# ----------------------------
# OPTIONAL LOCK SCREEN
# ----------------------------
if "unlocked" not in st.session_state:
    st.session_state.unlocked = False

if SECRET_CODE.strip() and not st.session_state.unlocked:
    st.markdown(f"<div class='big-title'>🔒 For {HER_NICKNAME} only</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub'>Enter the secret code to open this page 💖</div>", unsafe_allow_html=True)

    code = st.text_input("Secret code", type="password", placeholder="Hint: something meaningful to us…")
    c1, c2, c3 = st.columns([1, 1, 1])
    with c2:
        if st.button("Unlock 💘", use_container_width=True):
            if code.strip() == SECRET_CODE.strip():
                st.session_state.unlocked = True
                st.rerun()
            else:
                st.error("Nope 😭 Try again, pookie.")
    st.stop()

# ----------------------------
# SESSION STATE
# ----------------------------
if "no_count" not in st.session_state:
    st.session_state.no_count = 0
if "accepted" not in st.session_state:
    st.session_state.accepted = False

# ----------------------------
# HEADER
# ----------------------------
st.markdown(f"<div class='big-title'>Hey {HER_NICKNAME} 🎀</div>", unsafe_allow_html=True)
st.markdown(
    "<div class='sub'>From My Heart to You — with Love (and a little bit of coding).</div>",
    unsafe_allow_html=True,
)

st.markdown(
    f"""
<div class="card center">
  <h2 style="margin:0;">Will you be my Valentine? 💘</h2>
  <div class="small" style="margin-top:6px;">Choose wisely, miss baddie 😌</div>
</div>
""",
    unsafe_allow_html=True,
)

# ----------------------------
# BUTTONS
# ----------------------------
col1, col2 = st.columns(2, gap="large")
with col1:
    yes = st.button("YES 💖", use_container_width=True)
with col2:
    no = st.button("NO 🙃", use_container_width=True)

if yes:
    st.session_state.accepted = True

if no and not st.session_state.accepted:
    st.session_state.no_count += 1

# ----------------------------
# MAIN LOGIC
# ----------------------------
if st.session_state.accepted:
    st.balloons()
    st.success("YAYYYY 💘💘💘")

    st.markdown(
        f"""
<div class="card">
  <h2 style="margin-top:0;">For {HER_FULL_NAME} — but only my {HER_NICKNAME} 💖</h2>
  <p>People see the <b>Aishwarya Rai</b> vibe… the baddie aura… the “don’t mess with me” look.</p>
  <p>But I know the girl who’s actually <b>soft</b>, kind-hearted, and full of love.</p>
  <hr/>
  <p>From NIFT Gandhinagar fashion dreams to your fancy cafés and cute restaurants…</p>
  <p>From School memories to pretty sunsets… you make everything feel beautiful.</p>
  <p>Three years of long distance. Different countries. Summer reunions I wait all year for.</p>
  <p>But not a single day I stopped choosing you.</p>
  <p><b>You’re my pookie, sweetie, babu, cutie, my everything.</b></p>
  <p>And when we finally get that Bali farmhouse by the beach… I’m still choosing you there too </p>
  <p style="font-size:18px;"><b>So {HER_NICKNAME}… will you be my Valentine? 💘</b></p>
  <p class="small">— Love, {YOUR_NAME} (Your Pooka)</p>
</div>
""",
        unsafe_allow_html=True,
    )

   
    # Optional: photo section (drop images in a folder and uncomment)
    # st.markdown("<div class='card'><h3>Our Lookbook 📸</h3></div>", unsafe_allow_html=True)
    # st.image(["photos/1.jpg", "photos/2.jpg", "photos/3.jpg"], caption=["", "", ""], use_container_width=True)

else:
    if st.session_state.no_count > 0:
        responses = [
            "Hmm… that button is giving *fake attitude* 😤",
            "Try again, miss baddie 😭",
            "Nope. Wrong choice ",
            "Be serious 😐💗",
            "I’ll pretend I didn’t see that ",
            "Pooks… don’t play with me 😭💘",
        ]
        st.warning(f"{random.choice(responses)}  (Attempts: {st.session_state.no_count})")

    st.markdown(
        """
<div class="center small" style="margin-top:10px;">
  Hint: the correct answer is obvious 😌💖
</div>
""",
        unsafe_allow_html=True,
    )
