import streamlit as st
import hashlib
import math

# --- وظائف التشفير المتقدمة ---
def generate_team_id(name, xg, ppg, rating):
    raw = f"{name}{xg}{ppg}{rating}"
    return hashlib.md5(raw.encode()).hexdigest()[:12].upper()

def generate_market_id(o1, ox, o2, ou, btts):
    raw = f"{o1}{ox}{o2}{ou}{btts}"
    return "ODDS-" + hashlib.sha1(raw.encode()).hexdigest()[:10].upper()

# --- منطق SNIPER V37 الأصلي ---
def calculate_overall_rating(xg, xga, ppg):
    return (xg * 30) - (xga * 15) + (ppg * 20)

# --- واجهة التطبيق ---
st.set_page_config(page_title="SNIPER V37.0 - STREAM ID", layout="wide")

st.markdown("<h1 style='text-align: center; color: #D4AF37;'>🚜 SNIPER V37.0 - ID MATCH SUR IA</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>نظام تحليل الهيمنة وتوليد المعرفات الذكية</p>", unsafe_allow_html=True)

# تقسيم الشاشة لخانة الإدخال
with st.sidebar:
    st.header("📥 إدخال البيانات")
    home_name = st.text_input("اسم صاحب الأرض", "Home Team")
    away_name = st.text_input("اسم الضيف", "Away Team")
    
    st.divider()
    st.subheader("📊 إحصائيات الفرق")
    col1, col2 = st.columns(2)
    with col1:
        h_xg = st.number_input(f"xG {home_name}", value=1.5)
        h_xga = st.number_input(f"xGA {home_name}", value=1.0)
        h_ppg = st.number_input(f"PPG {home_name}", value=2.0)
    with col2:
        a_xg = st.number_input(f"xG {away_name}", value=1.2)
        a_xga = st.number_input(f"xGA {away_name}", value=1.3)
        a_ppg = st.number_input(f"PPG {away_name}", value=1.5)
    
    st.divider()
    st.subheader("💰 أودز الأسواق")
    o1 = st.number_input("Odd Win 1", value=2.1)
    ox = st.number_input("Odd Draw X", value=3.2)
    o2 = st.number_input("Odd Win 2", value=3.5)
    ou = st.number_input("Odd Over 2.5", value=1.9)
    btts = st.number_input("Odd BTTS Yes", value=1.8)

# --- المعالجة والعرض ---
if st.button("🚀 GENERATE STREAM DASHBOARD"):
    # الحسابات
    h_rating = calculate_overall_rating(h_xg, h_xga, h_ppg)
    a_rating = calculate_overall_rating(a_xg, a_xga, a_ppg)
    
    id_home = generate_team_id(home_name, h_xg, h_ppg, h_rating)
    id_away = generate_team_id(away_name, a_xg, a_ppg, a_rating)
    id_market = generate_market_id(o1, ox, o2, ou, btts)
    
    # العرض الذهبي للستريم
    st.divider()
    
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(f"""
        <div style="background-color: #1e1e1e; padding: 20px; border-radius: 10px; border-left: 5px solid #D4AF37;">
            <h3 style="color: white; margin:0;">[TEAM A] {home_name.upper()}</h3>
            <p style="color: #D4AF37; font-family: monospace; font-size: 20px;">ID MATCH SUR IA: {id_home}</p>
        </div>
        """, unsafe_allow_html=True)
        
    with c2:
        st.markdown(f"""
        <div style="background-color: #1e1e1e; padding: 20px; border-radius: 10px; border-left: 5px solid #D4AF37;">
            <h3 style="color: white; margin:0;">[TEAM B] {away_name.upper()}</h3>
            <p style="color: #D4AF37; font-family: monospace; font-size: 20px;">ID MATCH SUR IA: {id_away}</p>
        </div>
        """, unsafe_allow_html=True)
        
    st.markdown(f"""
    <div style="background-color: #1e1e1e; padding: 30px; border-radius: 10px; margin-top: 20px; text-align: center; border: 1px solid #333;">
        <h4 style="color: #888;">📊 GLOBAL MARKET MASTER ID</h4>
        <h2 style="color: white; letter-spacing: 5px;">{id_market}</h2>
        <p style="color: #444;">1X2 | O/U 2.5 | BTTS SYSTEM</p>
    </div>
    """, unsafe_allow_html=True)
    
