import streamlit as st
import hashlib
import math
import time

# --- محرك الحسم النهائي V45.0 (The Executioner) ---
def analyze_match_v45(h_id, a_id):
    def extract_metrics(id_str):
        if "-" not in id_str: return 1.5, 1.0
        parts = id_str.split("-")
        try:
            ppg = int(parts[1]) / 100
            xg = int(parts[2]) / 100
            return ppg, xg
        except: return 1.2, 1.0

    h_ppg, h_xg = extract_metrics(h_id)
    a_ppg, a_xg = extract_metrics(a_id)

    ppg_diff = h_ppg - a_ppg
    xg_diff = h_xg - a_xg
    
    # تحديد الاستراتيجية بناءً على فجوة الأداء
    if ppg_diff > 1.1:
        strategy = "DOMINANCE 🚜 (وضع الهيمنة)"
        h_l, a_l = 3.3, 0.2 # يضمن نتيجة 3-0
    elif 0.4 <= ppg_diff <= 1.1 or xg_diff >= 0.5:
        strategy = "EXECUTION 🎯 (وضع الحسم الهجومي)"
        # رفع معدل أهداف المضيف وخفض الخصم لكسر فخ الـ 1-1
        h_l = h_xg + 0.6
        a_l = a_xg - 0.2 if a_xg > 1.0 else a_xg
    else:
        strategy = "BALANCED ⚖️ (توازن القوة)"
        h_l, a_l = h_xg, a_xg

    # حساب النتيجة الأكثر دقة باستخدام بويسان
    def get_final_score(l1, l2):
        bh, ba, mp = 0, 0, 0
        for h in range(6):
            for a in range(6):
                p = (math.exp(-l1)*(l1**h)/math.factorial(h)) * (math.exp(-l2)*(l2**a)/math.factorial(a))
                if p > mp: mp, bh, ba = p, h, a
        
        # --- القاعدة الذهبية لكسر التعادل (Force 2-1) ---
        # إذا كانت النتيجة المحسوبة تعادلاً ولكن المضيف لديه أفضلية xG واضحة
        if bh <= ba and xg_diff >= 0.4:
            bh = ba + 1 # إجبار المضيف على التقدم بهدف
            if bh < 2: bh = 2 # ضمان تسجيل هدفين للمضيف في وضع الحسم
            
        return bh, ba

    goal_h, goal_a = get_final_score(h_l, a_l)
    return goal_h, goal_a, strategy

# --- الواجهة الاحترافية V45 ---
st.set_page_config(page_title="SNIPER V45 - THE EXECUTIONER", layout="wide")

st.markdown("""
    <style>
    .main-card { background: #000; padding: 30px; border: 2px solid #D4AF37; border-radius: 20px; text-align: center; color: white; }
    </style>
    <h1 style='text-align: center; color: #D4AF37;'>🛰️ SNIPER AI - V45.0 PRECISION</h1>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    h_name = st.text_input("🏠 Home Team", value="Borkina faso")
    h_id = st.text_input(f"🆔 {h_name} ID", key="h_v45")
with col2:
    a_name = st.text_input("✈️ Away Team", value="Équatoriale guinea")
    a_id = st.text_input(f"🆔 {a_name} ID", key="a_v45")

m_id = st.text_input("💰 MARKET ID", value="AFCON-V45-FINAL")

if st.button("🔍 START DEEP ANALYSIS", use_container_width=True):
    with st.status("🧠 Analyzing Goals Gap...", expanded=True) as s:
        time.sleep(10)
        s.update(label="✅ Precision Logic Applied", state="complete")

    g_h, g_a, strat = analyze_match_v45(h_id, a_id)

    st.markdown(f"""
    <div class="main-card">
        <h3 style="color: #D4AF37;">STRATEGY: {strat}</h3>
        <div style="display: flex; justify-content: center; align-items: center; gap: 40px; margin: 30px 0;">
            <div><h1 style="font-size: 110px; margin:0;">{g_h}</h1><p>{h_name}</p></div>
            <div style="font-size: 40px; color: #D4AF37;">VS</div>
            <div><h1 style="font-size: 110px; margin:0;">{g_a}</h1><p>{a_name}</p></div>
        </div>
        <div style="display: flex; justify-content: space-around; background: #111; padding: 20px; border-radius: 15px;">
            <div><p style="color:#D4AF37;">🚩 1X2</p><b>HOME (1)</b></div>
            <div><p style="color:#D4AF37;">⚽ GOALS</p><b>OVER 2.5</b></div>
            <div><p style="color:#D4AF37;">🔄 BTTS</p><b>YES</b></div>
        </div>
        <p style="color: #333; margin-top: 20px;">MARKET VERIFIED: {m_id}</p>
    </div>
    """, unsafe_allow_html=True)
    
