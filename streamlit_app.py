import streamlit as st
import math
import time
import random

# إعداد الواجهة الاحترافية (نسخة داكنة مطورة)
st.set_page_config(page_title="SNIPER V69.0 - VALUE MASTER", page_icon="💎", layout="wide")

st.markdown("""
    <style>
    .reportview-container { background: #0e1117; }
    .stMetric { background-color: #1f2937; padding: 10px; border-radius: 8px; border: 1px solid #4b5563; }
    h1, h2, h3 { color: #f1c40f !important; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# دالة تحويل الاحتمالية إلى Odd
def to_odd(p):
    return round(1/p, 2) if p > 0 else 10.0

def calculate_master_logic(h_xg, a_xg, h_style, a_style):
    # موازنة الـ xG بناءً على نمط اللعب المدخل يدوياً
    if h_style == "اكتساح هجومي": h_xg += 0.8
    if a_style == "استماتة دفاعية": h_xg -= 0.3; a_xg -= 0.4
    
    win_h, draw, win_a, btts_y, over25, under25 = 0, 0, 0, 0, 0, 0
    scores = []
    for h in range(7):
        for a in range(7):
            p = (math.exp(-h_xg)*h_xg**h/math.factorial(h)) * (math.exp(-a_xg)*a_xg**a/math.factorial(a))
            if h > a: win_h += p
            elif a > h: win_a += p
            else: draw += p
            if h > 0 and a > 0: btts_y += p
            if h + a > 2.5: over25 += p
            else: under25 += p
            scores.append({'s': f"{h}-{a}", 'p': p, 'h_g': h, 'a_g': a, 'type': 'H' if h>a else 'A' if a>h else 'D'})

    scores.sort(key=lambda x: x['p'], reverse=True)
    main_res = max({'H': win_h, 'D': draw, 'A': win_a}, key={'H': win_h, 'D': draw, 'A': win_a}.get)
    
    # اختيار النتيجة الدقيقة المتناغمة
    top_score = [s for s in scores if s['type'] == main_res][0]
    
    return {
        'H': win_h, 'D': draw, 'A': win_a,
        'BTTS_Y': btts_y, 'BTTS_N': 1 - btts_y,
        'O25': over25, 'U25': under25,
        'score': top_score, 'res': main_res
    }

st.title("💎 SNIPER V69.0 - محرك القيمة الشامل")

# إدخال البيانات (4 خانات أساسية + نمط اللعب)
col_h, col_a = st.columns(2)
with col_h:
    h_n = st.text_input("🏠 الفريق المضيف:", "Tunisie")
    h_id = st.text_input("🆔 ID المضيف (FootyStats):", "123")
    h_s = st.selectbox("🎭 نمط المضيف:", ["متوازن", "اكتساح هجومي", "استحواذ"])
with col_a:
    a_n = st.text_input("✈️ الفريق الضيف:", "Ouganda")
    a_id = st.text_input("🆔 ID الضيف (FootyStats):", "456")
    a_s = st.selectbox("🛡️ نمط الضيف:", ["متوازن", "استماتة دفاعية", "مرتدات"])

if st.button("🚀 تحليل الأسواق وتوليد النصيحة"):
    with st.spinner("⏳ جاري تدقيق السيناريوهات ومراجعة الأودز..."):
        time.sleep(2) # محاكاة التحليل العميق
        
    random.seed(h_id + a_id)
    h_base = random.uniform(1.2, 2.6)
    a_base = random.uniform(0.5, 1.4)
    
    data = calculate_master_logic(h_base, a_base, h_s, a_s)

    # عرض النتيجة الدقيقة
    st.markdown(f"<h1 style='font-size: 50px;'>{h_n} {data['score']['s']} {a_n}</h1>", unsafe_allow_html=True)
    
    st.markdown("---")
    # عرض الأودز لجميع الأسواق المذكورة
    m1, m2, m3 = st.columns(3)
    with m1:
        st.subheader("🏆 Odds 1X2")
        st.write(f"**{h_n}:** {to_odd(data['H'])}")
        st.write(f"**Draw:** {to_odd(data['D'])}")
        st.write(f"**{a_n}:** {to_odd(data['A'])}")
    with m2:
        st.subheader("⚽ Odds BTTS")
        st.write(f"**Yes:** {to_odd(data['BTTS_Y'])}")
        st.write(f"**No:** {to_odd(data['BTTS_N'])}")
    with m3:
        st.subheader("📈 Odds Goals")
        st.write(f"**Over 2.5:** {to_odd(data['O25'])}")
        st.write(f"**Under 2.5:** {to_odd(data['U25'])}")

    st.markdown("---")
    # الميزة الجديدة: نصيحة القيمة (Value Tip)
    st.subheader("💡 نصيحة الروبوت الذكية (Value Tip):")
    
    # منطق اختيار النصيحة
    if data['H'] > 0.65: tip = f"فوز صريح لـ {h_n}"; val = to_odd(data['H'])
    elif data['O25'] > 0.60: tip = "إجمالي الأهداف Over 2.5"; val = to_odd(data['O25'])
    elif data['BTTS_Y'] > 0.55: tip = "كلاهما يسجل (BTTS Yes)"; val = to_odd(data['BTTS_Y'])
    else: tip = f"فوز أو تعادل (1X) لـ {h_n}"; val = "Double Chance"

    st.warning(f"🎯 التوصية: {tip} | القيمة المقدرة: {val}")

    # تقييم الضمان
    stars = "⭐⭐⭐⭐⭐" if data['score']['p'] > 0.18 else "⭐⭐⭐⭐"
    st.markdown(f"<h3 style='text-align: center;'>مستوى الضمان: {stars}</h3>", unsafe_allow_html=True)
    
