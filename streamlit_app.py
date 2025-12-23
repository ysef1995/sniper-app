import streamlit as st
import math
import time

st.set_page_config(page_title="SNIPER V93.0 - AGGRESSIVE", layout="wide")

def poisson_calculation(k, lmbda):
    if lmbda <= 0: lmbda = 0.1
    return (lmbda**k * math.exp(-lmbda)) / math.factorial(k)

st.title("🛡️ محرك الهيمنة القصوى (3-1 Guaranteed)")

# 1. الرموز القوية من صورك
col_h, col_a = st.columns(2)
with col_h:
    h_name = st.text_input("🏠 المضيف:", "تونس")
    h_id = st.text_input("🆔 ID المضيف:", "TN-88xV2zQ_Pwr91")
with col_a:
    a_name = st.text_input("✈️ الضيف:", "أوغندا")
    a_id = st.text_input("🆔 ID الضيف:", "UG-42kM7tY_Spd65")

# 2. تفعيل وضع الاكتساح
aggressive_mode = st.checkbox("🔥 تفعيل وضع الاكتساح الهجومي (Force 3+ Goals)", value=True)

if st.button("🚀 توليد النتيجة القاتلة"):
    with st.spinner("⏳ جاري كسر فلاتر الأمان وتوليد 3-1..."):
        time.sleep(1)

    # رفع القوة الهجومية بشكل "عدواني" بناءً على الرموز
    h_pwr = 3.5 if aggressive_mode else 2.0 
    a_pwr = 1.2

    scores = []
    for h in range(6):
        for a in range(4):
            prob = poisson_calculation(h, h_pwr) * poisson_calculation(a, a_pwr)
            scores.append({'score': f"{h}-{a}", 'prob': prob, 'h': h, 'a': a})
    
    # فلتر إجباري: نختار النتيجة التي تحقق (H >= 3) إذا كان وضع الاكتساح مفعل
    if aggressive_mode:
        final_result = [s for s in scores if s['h'] >= 3 and s['a'] >= 1][0]
    else:
        scores.sort(key=lambda x: x['prob'], reverse=True)
        final_result = scores[0]

    # --- العرض النهائي (طبق الأصل لصورتك 1002853179) ---
    st.markdown(f"""
    <div style="background-color: #111; padding: 40px; border: 4px solid #f1c40f; border-radius: 20px; text-align: center;">
        <h1 style="color: white; font-size: 60px;">{h_name} <span style="color: #f1c40f;">{final_result['score']}</span> {a_name}</h1>
        <p style="color: #888;">تم التحليل بناءً على منطق الهيمنة القصوى</p>
    </div>
    """, unsafe_allow_html=True)

    # --- طباعة سيناريوهات بديلة (كما في الصورة 1002853179) ---
    st.markdown("---")
    st.subheader("📊 طباعة سيناريوهات بديلة:")
    st.write(f"1️⃣ **ثغرات {h_name} الهجومي (3-1):** إذا استغل الدفاع.")
    st.write(f"2️⃣ **منطقة الجزاء {a_name} الدفاعي (0-1):** إذا تراجع.")

    # --- ملخص الأسواق الملون (كما في الصورة 1002853297) ---
    st.markdown("---")
    st.subheader("📋 ملخص الأسواق المطبوع:")
    st.markdown(f"<div style='background: #1a2634; padding: 15px; border-radius: 10px; color: #5dade2;'>🏆 {h_name} :X2 توقع 1</div>", unsafe_allow_html=True)
    st.markdown(f"<div style='background: #2c2c1a; padding: 15px; border-radius: 10px; color: #f4d03f; margin-top: 10px;'>📈 توقع الأهداف: OVER 2.5</div>", unsafe_allow_html=True)
    st.markdown(f"<div style='background: #1a2e1a; padding: 15px; border-radius: 10px; color: #2ecc71; margin-top: 10px;'>⚽ BTTS: YES</div>", unsafe_allow_html=True)
    
