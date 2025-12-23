import streamlit as st
import math
import time
import random

# --- إعدادات الواجهة ---
st.set_page_config(page_title="SNIPER V75.0 AUTO-EXACT", page_icon="🎯", layout="wide")

def poisson_probability(k, lmbda):
    return (lmbda**k * math.exp(-lmbda)) / math.factorial(k)

# --- محرك توليد الـ xG التلقائي بناءً على الـ IDs والـ Odds ---
def generate_auto_stats(h_id, a_id, odd_h, odd_a):
    random.seed(str(h_id) + str(a_id))
    # تحويل الـ Odds إلى قوة هجومية (كلما قل الـ Odd زاد الـ xG)
    h_base_xg = (1 / odd_h) * 3.5 
    a_base_xg = (1 / odd_a) * 2.5
    return round(h_base_xg, 2), round(a_base_xg, 2)

def calculate_overall_rating(xg, xga, ppg):
    return (xg * 30) - (xga * 15) + (ppg * 20)

# --- المحرك الاستراتيجي للنتيجة العريضة (الحل لمشكلة 3-1) ---
def get_explosive_score(h_xg, a_xg, h_rate, a_rate):
    scores = []
    for h in range(6):
        for a in range(6):
            p = poisson_probability(h, h_xg) * poisson_probability(a, a_xg)
            scores.append({'s': f"{h}-{a}", 'p': p, 'h_g': h, 'a_g': a})
    
    scores.sort(key=lambda x: x['p'], reverse=True)
    
    # منطق "الاكتساح": إذا كان المضيف أقوى بـ 25 نقطة
    if h_rate - a_rate > 25:
        # نبحث عن أول نتيجة في التوب 15 تعكس تسجيل الفريقين مع فوز عريض (مثل 3-1)
        for s in scores[:15]:
            if s['h_g'] >= 3 and s['a_g'] >= 1:
                return s
    return scores[0]

st.title("🎯 SNIPER V75.0 - محرك التوقع التلقائي")

# إدخال الـ IDs والـ Odds فقط (الروبوت سيتكفل بالباقي)
col1, col2 = st.columns(2)
with col1:
    h_name = st.text_input("🏠 الفريق المضيف:", "Tunisie")
    h_id = st.text_input("🆔 ID المضيف:", "123")
    odd_h = st.number_input(f"Odd Win {h_name}:", value=1.35)
with col2:
    a_name = st.text_input("✈️ الفريق الضيف:", "Ouganda")
    a_id = st.text_input("🆔 ID الضيف:", "456")
    odd_a = st.number_input(f"Odd Win {a_name}:", value=8.50)

if st.button("🚀 توقع النتيجة الدقيقة (3-1/1-0)"):
    with st.spinner("⏳ جاري استنتاج سيناريو المباراة..."):
        time.sleep(2)
    
    # 1. توليد إحصائيات تلقائية من الـ Odds
    auto_h_xg, auto_a_xg = generate_auto_stats(h_id, a_id, odd_h, odd_a)
    
    # 2. حساب التقييم
    h_rate = calculate_overall_rating(auto_h_xg, 1.0, 2.2)
    a_rate = calculate_overall_rating(auto_a_xg, 2.0, 0.8)
    
    # 3. اختيار النتيجة بـ "منطق الاكتساح"
    final_res = get_explosive_score(auto_h_xg, auto_a_xg, h_rate, a_rate)
    
    # عرض النتيجة بوضوح للفيديو
    st.markdown(f"<div style='text-align: center; background: #161b22; padding: 30px; border-radius: 20px; border: 2px solid #f1c40f;'>"
                f"<h1 style='color: white; margin: 0;'>{h_name} <span style='color: #f1c40f;'>{final_res['s']}</span> {a_name}</h1>"
                f"<p style='color: #8b949e;'>تم التحليل بناءً على منطق الهيمنة القصوى</p>"
                f"</div>", unsafe_allow_html=True)

    # طباعة التوقعات البديلة للتأكد
    st.markdown("---")
    st.subheader("📊 طباعة سيناريوهات بديلة:")
    st.write(f"1️⃣ **السيناريو الهجومي (3-1):** إذا استغل {h_name} ثغرات الدفاع.")
    st.write(f"2️⃣ **السيناريو الدفاعي (1-0):** إذا تراجع {a_name} لمنطقة الجزاء.")
    
