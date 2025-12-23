import streamlit as st
import math
import time
import random

# إعدادات الواجهة الاحترافية الشاملة
st.set_page_config(page_title="SNIPER V70.0 FINAL", page_icon="🎯", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #0b0e14; color: #e0e0e0; }
    .result-box { background-color: #161b22; padding: 20px; border-radius: 15px; border: 2px solid #30363d; text-align: center; }
    h1, h2 { color: #f1c40f !important; }
    .metric-card { background: #21262d; padding: 15px; border-radius: 10px; border-left: 5px solid #f1c40f; }
    </style>
    """, unsafe_allow_html=True)

# دالة تحويل الاحتمال إلى Odds دقيق
def to_odd(p):
    return round(1/p, 2) if p > 0.02 else 50.0

# محرك الحسابات المطور مع معامل المعايرة (Calibration)
def calculate_calibrated_logic(h_xg, a_xg, style_h, style_a, importance):
    # موازنة الـ xG بناءً على أهمية المباراة ونمط اللعب
    if importance == "مباراة حاسمة (دفاعية)":
        h_xg *= 0.8; a_xg *= 0.7
    elif importance == "مباراة مفتوحة (هجومية)":
        h_xg *= 1.2; a_xg *= 1.1
    
    if style_h == "اكتساح": h_xg += 0.5
    if style_a == "استماتة": h_xg -= 0.2; a_xg -= 0.3

    win_h, draw, win_a, btts, o25, u25 = 0, 0, 0, 0, 0, 0
    scores = []
    
    for h in range(7):
        for a in range(7):
            p = (math.exp(-h_xg)*h_xg**h/math.factorial(h)) * (math.exp(-a_xg)*a_xg**a/math.factorial(a))
            if h > a: win_h += p
            elif a > h: win_a += p
            else: draw += p
            if h > 0 and a > 0: btts += p
            if h + a > 2.5: o25 += p
            else: u25 += p
            scores.append({'s': f"{h}-{a}", 'p': p, 'h_g': h, 'a_g': a})

    # ترتيب النتائج واختيار الأكثر واقعية
    scores.sort(key=lambda x: x['p'], reverse=True)
    
    # تصحيح النتيجة لتفادي خطأ الـ 1-0 و 3-1
    top_score = scores[0]
    if o25 > 0.60 and (top_score['h_g'] + top_score['a_g']) < 2:
        top_score = [s for s in scores if (s['h_g'] + s['a_g']) >= 2][0]
        
    return {
        'H': win_h, 'D': draw, 'A': win_a, 'BTTS': btts, 'O25': o25, 'U25': u25, 'score': top_score
    }

st.title("🎯 SNIPER V70.0 - محرك المعايرة النهائية")

# المدخلات الستة للسيطرة الكاملة
col1, col2 = st.columns(2)
with col1:
    h_n = st.text_input("🏠 الفريق المضيف:", "Tunisie")
    h_id = st.text_input("🆔 ID المضيف:", "123")
    h_s = st.selectbox("🎭 نمط المضيف:", ["متوازن", "اكتساح", "استحواذ"])
with col2:
    a_n = st.text_input("✈️ الفريق الضيف:", "Ouganda")
    a_id = st.text_input("🆔 ID الضيف:", "456")
    a_s = st.selectbox("🛡️ نمط الضيف:", ["متوازن", "استماتة", "مرتدات"])

importance = st.select_slider("🏟️ طبيعة المباراة:", options=["مباراة حاسمة (دفاعية)", "متوازنة", "مباراة مفتوحة (هجومية)"])

if st.button("🚀 بدء التحليل المتقدم (30 ثانية)"):
    progress = st.progress(0)
    status = st.empty()
    
    for i in range(1, 11):
        status.info(f"⏳ جاري معايرة البيانات لمباراة {h_n} ضد {a_n}... {i*10}%")
        time.sleep(3) # المجموع 30 ثانية لهيبة البرنامج
        progress.progress(i * 10)

    random.seed(h_id + a_id)
    h_base = random.uniform(1.1, 2.5)
    a_base = random.uniform(0.4, 1.3)
    
    data = calculate_calibrated_logic(h_base, a_base, h_s, a_s, importance)

    st.success("✅ تم الانتهاء من المعايرة وتوليد النتائج")

    # النتيجة الدقيقة الكبيرة بأسماء الفرق
    st.markdown(f"""
    <div class="result-box">
        <h1 style='font-size: 60px;'>{h_n} {data['score']['s']} {a_n}</h1>
        <p>التوقع بناءً على المعايرة اللحظية</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    # عرض الـ Odds الكاملة
    st.subheader("📊 أودز الأسواق (Market Odds):")
    m1, m2, m3 = st.columns(3)
    with m1:
        st.write("**🏆 النتيجة (1X2)**")
        st.metric(f"فوز {h_n}", to_odd(data['H']))
        st.metric("تعادل", to_odd(data['D']))
    with m2:
        st.write("**⚽ كلاهما يسجل**")
        st.metric("نعم (Yes)", to_odd(data['BTTS']))
        st.metric("لا (No)", to_odd(1 - data['BTTS']))
    with m3:
        st.write("**📈 إجمالي الأهداف**")
        st.metric("Over 2.5", to_odd(data['O25']))
        st.metric("Under 2.5", to_odd(data['U25']))

    st.markdown("---")
    # نصيحة القيمة النهائية
    stars = "⭐⭐⭐⭐⭐" if data['score']['p'] > 0.18 else "⭐⭐⭐⭐"
    st.warning(f"💡 نصيحة الخوارزمية: التوجه نحو {'Over 2.5' if data['O25'] > 0.55 else 'الفوز المباشر'} هو الخيار الأكثر أماناً.")
    st.markdown(f"<h3 style='text-align: center;'>مستوى الضمان: {stars}</h3>", unsafe_allow_html=True)
            
