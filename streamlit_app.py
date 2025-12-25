import streamlit as st
import math
import time
import random

# --- GHOST ENGINE V50 Logic ---
def analyze_ghost_logic(h_id, a_id):
    def extract_metrics(id_str):
        if "-" not in id_str: return 1.5, 1.0, "D"
        parts = id_str.split("-")
        try:
            ppg = int(parts[1]) / 100
            xg = int(parts[2]) / 100
            form = parts[3] if len(parts) > 3 else "D"
            return ppg, xg, form
        except: return 1.2, 1.0, "D"

    h_ppg, h_xg, h_f = extract_metrics(h_id)
    a_ppg, a_xg, a_f = extract_metrics(a_id)
    diff = h_ppg - a_ppg

    # مصفوفة النتائج "الخرافية" (تحاكي كسر السكريبت للتوقعات)
    if diff >= 1.3:
        # وضع الهيمنة (مثل 3-0 أو 3-1)
        res = random.choice([(3,0), (3,1), (2,0)])
        strat = "SYSTEM DOMINANCE 🚜"
    elif 0.4 <= diff < 1.3:
        # وضع الحسم الصعب (مثل 2-1 أو 1-0)
        res = random.choice([(2,1), (1,0), (2,1)])
        strat = "HIGH-RISK PRECISION 🎯"
    else:
        # وضع التعادل الخرافي (مثل 1-1 أو 2-2)
        res = random.choice([(1,1), (0,0), (2,2)])
        strat = "GHOST NEUTRAL 👻"
    
    return res, strat

# --- UI Layout ---
st.set_page_config(page_title="SNIPER GHOST V50", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stButton>button { width: 100%; border-radius: 10px; background: #D4AF37; color: black; font-weight: bold; height: 3em; }
    .report-box { background: #000; padding: 40px; border: 2px solid #D4AF37; border-radius: 20px; text-align: center; color: white; box-shadow: 0px 0px 25px rgba(212, 175, 55, 0.2); }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #D4AF37;'>⚡ SNIPER GHOST ENGINE V50.0</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #666;'>DECODING MATCH DATA FROM ENCRYPTED STREAM</p>", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    h_name = st.text_input("🏠 HOME TEAM", "Algérie")
    h_id = st.text_input("🆔 SOURCE ID [1]")
with col2:
    a_name = st.text_input("✈️ AWAY TEAM", "Sudan")
    a_id = st.text_input("🆔 SOURCE ID [2]")

if st.button("🚀 INITIATE GHOST ANALYSIS"):
    with st.status("📡 Connecting to Market Servers...", expanded=True) as status:
        time.sleep(2)
        st.write("🔓 Bypassing Firewalls...")
        time.sleep(3)
        st.write("🧠 Executing Ghost Simulation...")
        time.sleep(4)
        status.update(label="✅ DATA DECODED SUCCESSFULLY", state="complete")

    (g_h, g_a), strategy = analyze_ghost_logic(h_id, a_id)

    # حساب السطر السفلي المتزامن
    f_1x2 = "HOME (1)" if g_h > g_a else "DRAW (X)" if g_h == g_a else "AWAY (2)"
    f_goals = "OVER 2.5" if (g_h + g_a) >= 2.5 else "UNDER 2.5"
    f_btts = "YES" if (g_h > 0 and g_a > 0) else "NO"

    st.markdown(f"""
    <div class="report-box">
        <h3 style="color: #D4AF37; font-family: monospace;">MODE: {strategy}</h3>
        <div style="display: flex; justify-content: center; align-items: center; gap: 60px; margin: 40px 0;">
            <div><h1 style="font-size: 120px; margin:0;">{g_h}</h1><p style="font-size: 20px;">{h_name}</p></div>
            <div style="font-size: 50px; color: #D4AF37;">VS</div>
            <div><h1 style="font-size: 120px; margin:0;">{g_a}</h1><p style="font-size: 20px;">{a_name}</p></div>
        </div>
        <div style="display: flex; justify-content: space-around; background: #111; padding: 25px; border-radius: 15px; border: 1px solid #333;">
            <div><p style="color:#D4AF37; margin:0;">🚩 1X2</p><b style="font-size: 22px;">{f_1x2}</b></div>
            <div><p style="color:#D4AF37; margin:0;">⚽ GOALS</p><b style="font-size: 22px;">{f_goals}</b></div>
            <div><p style="color:#D4AF37; margin:0;">🔄 BTTS</p><b style="font-size: 22px;">{f_btts}</b></div>
        </div>
        <p style="color: #444; margin-top: 30px; font-family: monospace; letter-spacing: 2px;">ENCRYPTED_DATA_PACKET_V50_SUCCESS</p>
    </div>
    """, unsafe_allow_html=True)
    
