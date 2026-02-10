import streamlit as st
import random

# =========================
# CONFIG
# =========================
st.set_page_config(page_title="For Nikku", page_icon="💗", layout="centered")

HER_FULL_NAME = "Nikita Singh"
HER_NICKNAME = "Nikku"
YOUR_NAME = "Chinmaya"

# Optional lock (leave "" to disable)
SECRET_CODE = ""  # e.g. "1402"

# =========================
# STYLES (Luxury + clean)
# =========================
st.markdown(
    """
<style>
/* --- App background --- */
[data-testid="stAppViewContainer"]{
  background:
    radial-gradient(1200px 600px at 15% 10%, rgba(255,255,255,0.55), rgba(255,255,255,0) 60%),
    radial-gradient(900px 500px at 85% 35%, rgba(255,220,235,0.55), rgba(255,255,255,0) 60%),
    linear-gradient(135deg, #ffd1dc 0%, #ffb6c9 45%, #f7a6c7 100%);
}
[data-testid="stHeader"]{ background: transparent; }
[data-testid="stToolbar"]{ right: 0.6rem; }

/* --- Layout container --- */
.wrap{
  max-width: 860px;
  margin: 0 auto;
  padding: 14px 8px 40px;
  position: relative;
}

/* --- Floating blur blobs (subtle motion) --- */
@keyframes drift1 { 0%{transform:translate(0,0)} 50%{transform:translate(18px,-12px)} 100%{transform:translate(0,0)} }
@keyframes drift2 { 0%{transform:translate(0,0)} 50%{transform:translate(-16px,10px)} 100%{transform:translate(0,0)} }
.blob{
  position: fixed;
  filter: blur(40px);
  opacity: 0.45;
  z-index: 0;
  pointer-events: none;
}
.blob.one{ width: 320px; height: 320px; left: -90px; top: 120px; background: #ffffff; animation: drift1 10s ease-in-out infinite; }
.blob.two{ width: 360px; height: 360px; right: -120px; top: 220px; background: #ffe3ef; animation: drift2 11s ease-in-out infinite; }
.blob.three{ width: 300px; height: 300px; left: 35%; bottom: -120px; background: #ffd1dc; animation: drift1 12s ease-in-out infinite; }

/* --- Typography --- */
.kicker{
  text-align:center;
  font-size: 13px;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  opacity: 0.85;
  margin: 0;
}
.hero{
  text-align:center;
  font-weight: 900;
  font-size: 54px;
  line-height: 1.02;
  margin: 10px 0 6px;
}
.subhero{
  text-align:center;
  font-size: 16px;
  opacity: 0.92;
  margin: 0 0 18px;
}

/* --- Glass cards --- */
.card{
  background: rgba(255,255,255,0.22);
  border: 1px solid rgba(255,255,255,0.42);
  border-radius: 22px;
  padding: 18px 18px;
  box-shadow: 0 18px 45px rgba(0,0,0,0.10);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  position: relative;
  z-index: 1;
}
.card.soft{
  background: rgba(255,255,255,0.18);
}
.card + .card{ margin-top: 14px; }

.hr{
  height:1px;
  background: rgba(255,255,255,0.45);
  border: none;
  margin: 14px 0;
}

.center{ text-align:center; }
.muted{ opacity: 0.82; }
.small{ font-size: 13px; opacity: 0.82; }

/* --- "Chip" tags --- */
.chips{ display:flex; gap:10px; flex-wrap:wrap; justify-content:center; margin-top:10px; }
.chip{
  padding: 8px 12px;
  border-radius: 999px;
  background: rgba(255,255,255,0.25);
  border: 1px solid rgba(255,255,255,0.42);
  font-size: 13px;
  font-weight: 650;
}

/* --- Buttons --- */
button[kind="primary"], button[kind="secondary"]{
  border-radius: 16px !important;
  padding: 0.86rem 1rem !important;
  font-weight: 800 !important;
  border: 1px solid rgba(255,255,255,0.5) !important;
  box-shadow: 0 14px 30px rgba(0,0,0,0.10) !important;
}
button[kind="primary"]{ background: rgba(255,255,255,0.35) !important; }
button[kind="secondary"]{ background: rgba(255,255,255,0.18) !important; }

/* --- Mobile tweaks --- */
@media (max-width: 540px){
  .hero{ font-size: 42px; }
  .subhero{ font-size: 15px; }
}
</style>

<div class="blob one"></div>
<div class="blob two"></div>
<div class="blob three"></div>
""",
    unsafe_allow_html=True,
)

# =========================
# OPTIONAL LOCK
# =========================
if "unlocked" not in st.session_state:
    st.session_state.unlocked = False

if SECRET_CODE.strip() and not st.session_state.unlocked:
    st.markdown("<div class='wrap'>", unsafe_allow_html=True)
    st.markdown("<p class='kicker'>PRIVATE LINK</p>", unsafe_allow_html=True)
    st.markdown(f"<div class='hero'>For {HER_NICKNAME}</div>", unsafe_allow_html=True)
    st.markdown("<p class='subhero'>Enter the code and open it.</p>", unsafe_allow_html=True)

    st.markdown("<div class='card center'>", unsafe_allow_html=True)
    code = st.text_input("Secret code", type="password", placeholder="hint: something meaningful…")
    if st.button("Unlock", use_container_width=True):
        if code.strip() == SECRET_CODE.strip():
            st.session_state.unlocked = True
            st.rerun()
        else:
            st.error("Wrong code. Try again.")
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    st.stop()

# =========================
# STATE
# =========================
if "accepted" not in st.session_state:
    st.session_state.accepted = False
if "no_count" not in st.session_state:
    st.session_state.no_count = 0

# =========================
# HERO
# =========================
st.markdown("<div class='wrap'>", unsafe_allow_html=True)
st.markdown("<p class='kicker'>MADE IN CANADA • FOR INDIA</p>", unsafe_allow_html=True)
st.markdown(f"<div class='hero'>Hey {HER_NICKNAME}.</div>", unsafe_allow_html=True)
st.markdown(
    "<p class='subhero'>Luxury pink, long-distance proof, and one simple question.</p>",
    unsafe_allow_html=True,
)

# =========================
# QUESTION CARD
# =========================
st.markdown(
    f"""
<div class="card center">
  <div style="font-size:20px; font-weight:900; margin-bottom:6px;">
    Will you be my Valentine?
  </div>
  <div class="muted">No dramatic speech. Just… you and me.</div>
  <div class="chips">
    <div class="chip">NIFT Gandhinagar energy</div>
    <div class="chip">Café dates</div>
    <div class="chip">Bali dream</div>
    <div class="chip">3 years strong</div>
  </div>
</div>
""",
    unsafe_allow_html=True,
)

# Buttons
c1, c2 = st.columns(2, gap="large")
with c1:
    yes = st.button("Yes", use_container_width=True, type="primary")
with c2:
    no = st.button("No", use_container_width=True, type="secondary")

if yes:
    st.session_state.accepted = True
if no and not st.session_state.accepted:
    st.session_state.no_count += 1

# =========================
# RESULTS
# =========================
if st.session_state.accepted:
    st.balloons()

    st.markdown(
        f"""
<div class="card">
  <div style="display:flex; justify-content:space-between; align-items:flex-start; gap:14px; flex-wrap:wrap;">
    <div style="flex:1; min-width:220px;">
      <div style="font-size:18px; font-weight:900;">Okay. Good choice.</div>
      <div class="small">This page is officially yours now.</div>
    </div>
    <div class="chip">Happy Valentine’s Day</div>
  </div>

  <hr class="hr"/>

  <div style="font-size:16px; line-height:1.7;">
    <p>
      People see the baddie vibe — the “she’s rude” first impression, the Aishwarya Rai type elegance.
      But I know the version that’s actually soft and kind, just selective.
    </p>

    <p>
      We’ve done three years of long distance — Canada and India, time zones, calls, and those summer visits I wait for all year.
      And still, you’re the person I choose the easiest.
    </p>

    <p>
      I loved seeing you talk about Bali. One day you’ll get that beach farmhouse.
      When you do, I’m showing up — not as a visitor, as your person.
    </p>

    <p>
      Next time we’re together: a proper café date, pink outfit, sunflowers, and tiramisu from Baked by Nini’s.
      No “we’ll see”. It’s happening.
    </p>

    <p style="margin-top:14px;">
      <b>{HER_FULL_NAME}</b> — will you be my Valentine?
    </p>
    <p class="small">— {YOUR_NAME}</p>
  </div>
</div>
""",
        unsafe_allow_html=True,
    )

    # “Lookbook” section (premium feel; replace text with your own)
    st.markdown(
        """
<div class="card soft">
  <div style="font-size:18px; font-weight:900;">A small “lookbook” of us</div>
  <div class="small">Not photos (yet). Just the vibe.</div>
  <hr class="hr"/>
  <div style="display:grid; grid-template-columns:1fr 1fr; gap:12px;">
    <div class="card soft" style="margin:0; padding:14px;">
      <div style="font-weight:850;">The café version of you</div>
      <div class="small">Fancy, pink, and judging the menu like a designer.</div>
    </div>
    <div class="card soft" style="margin:0; padding:14px;">
      <div style="font-weight:850;">The soft version of you</div>
      <div class="small">Only I get this one. That’s my flex.</div>
    </div>
    <div class="card soft" style="margin:0; padding:14px;">
      <div style="font-weight:850;">Bali dream</div>
      <div class="small">Beach farmhouse. Golden hour. You winning at life.</div>
    </div>
    <div class="card soft" style="margin:0; padding:14px;">
      <div style="font-weight:850;">Us, long distance</div>
      <div class="small">Still solid. Still ours. Still growing.</div>
    </div>
  </div>
</div>
""",
        unsafe_allow_html=True,
    )

else:
    if st.session_state.no_count > 0:
        lines = [
            "Be serious for a second.",
            "Try again — without the attitude.",
            "That’s not very Nikku-coded.",
            "I’ll pretend I didn’t see that.",
            "Okay, comedian. One more time.",
        ]
        st.markdown(
            f"""
<div class="card center">
  <div style="font-size:16px; font-weight:900;">{random.choice(lines)}</div>
  <div class="small">No attempts: {st.session_state.no_count}</div>
</div>
""",
            unsafe_allow_html=True,
        )

st.markdown("</div>", unsafe_allow_html=True)
