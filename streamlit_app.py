import streamlit as st
import math
import time

# --- محرك التوازن الذكي V48.0 ---
def analyze_balanced_v48(h_id, a_id):
    def extract(id_str):
        parts = id_str.split("-")
        try:
            ppg, xg = int(parts[1])/100, int(parts[2])/100
            return ppg, xg
        except: return 1.5, 1.2

    h_ppg, h_xg = extract(h_id)
    a_ppg, a_xg = extract(a_id)
    diff = h_ppg - a_ppg

    # --- المنطق المرن حسب فجوة المستوى ---
    
    # 1. وضع الهيمنة الكاسحة (لنتائج 3-0 و 4-0)
    if diff >= 1.3:
        h_l, a_l = 3.2, 0.4
        strat = "HIGH DOMINANCE 🚜 (فارق مستوى شاسع)"
        
    # 2. وضع المباراة المفتوحة (لنتائج 3-1 و 2-1)
    elif 0.8 <= diff < 1.3:
        h_l, a_l = 2.4, 1.1 
        strat = "OPEN ATTACK ⚔️ (مباراة هجومية)"
        
    # 3. وضع القمة الأفريقية (لنتائج 1-0 و 0-0)
    else:
        h_l, a_l = 1.1, 0.5
        strat = "AFRICAN REALITY 🛡️ (مباراة تكتيكية مغلقة)"

    def get_score(l1, l2):
        bh, ba, mp = 0, 0, 0
        for h in range(6):
            for a in range(6):
                p = (math.exp(-l1)*(l1**h)/math.factorial(h)) * (math.exp(-l2)*(l2**a)/math.factorial(a))
                if p > mp: mp, bh, ba = p, h, a
        return bh, ba

    g_h, g_a = get_score(h_l, a_l)
    return g_h, g_a, strat

# --- الواجهة المحدثة ---
st.set_page_config(page_title="SNIPER V48 - BALANCED", layout="wide")
st.markdown("<h1 style='text-align: center; color: #D4AF37;'>🛰️ SNIPER AI - V48.0 BALANCED</h1>", unsafe_allow_html=True)

c1, c2 = st.columns(2)
with c1:
    h_n = st.text_input("🏠 Home Team")
    h_i = st.text_input("🆔 Home ID", placeholder="Ex: DZ-240-185-V48")
with c2:
    a_n = st.text_input("✈️ Away Team")
    a_i = st.text_input("🆔 Away ID", placeholder="Ex: SD-095-075-V48")

if st.button("🚀 EXECUTE SMART ANALYSIS", use_container_width=True):
    with st.status("🧠 Evaluating Tactical Gap...", expanded=True) as s:
        time.sleep(10)
        s.update(label="✅ Analysis Synced", state="complete")

    score_h, score_a, strategy = analyze_balanced_v48(h_i, a_i)

    # التزامن التلقائي للسطر السفلي
    f_1x2 = "HOME (1)" if score_h > score_a else "DRAW (X)" if score_h == score_a else "AWAY (2)"
    f_goals = "OVER 2.5" if (score_h + score_a) >= 2.5 else "UNDER 2.5"
    f_btts = "YES" if (score_h > 0 and score_a > 0) else "NO"

    st.markdown(f"""
    <div style="background: #000; padding: 35px; border: 2px solid #D4AF37; border-radius: 20px; text-align: center; color: white;">
        <h3 style="color: #666; margin-bottom: 5px;">STRATEGY:</h3>
        <h2 style="color: #D4AF37; margin-top: 0;">{strategy}</h2>
        <div style="display: flex; justify-content: center; align-items: center; gap: 50px; margin: 30px 0;">
            <div><h1 style="font-size: 110px; margin:0;">{score_h}</h1><p>{h_n}</p></div>
            <div style="font-size: 40px; color: #D4AF37;">VS</div>
            <div><h1 style="font-size: 110px; margin:0;">{score_a}</h1><p>{a_n}</p></div>
        </div>
        <div style="display: flex; justify-content: space-around; background: #111; padding: 20px; border-radius: 15px;">
            <div><p style="color:#D4AF37; margin:0;">🚩 1X2</p><b style="font-size: 18px;">{f_1x2}</b></div>
            <div><p style="color:#D4AF37; margin:0;">⚽ GOALS</p><b style="font-size: 18px;">{f_goals}</b></div>
            <div><p style="color:#D4AF37; margin:0;">🔄 BTTS</p><b style="font-size: 18px;">{f_btts}</b></div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
