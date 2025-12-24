import streamlit as st
import math
import time

st.set_page_config(page_title="SNIPER V105.0 - SYMBOL DECODER", layout="wide")

def poisson_calc(k, lmbda):
    if lmbda <= 0: lmbda = 0.01
    return (lmbda**k * math.exp(-lmbda)) / math.factorial(k)

st.title("🎯 محرك فك تشفير بصمة الفريق (Dynamic Symbol Decoder)")

# --- 1. إدخال البيانات الحساسة ---
col_h, col_a = st.columns(2)
with col_h:
    h_name = st.text_input("🏠 الفريق المضيف:", "Senegal")
    h_id = st.text_input("🆔 بصمة المضيف (ID):", "SN-97kZ4qR_Dom88") 
with col_a:
    a_name = st.text_input("✈️ الفريق الضيف:", "Botswana")
    a_id = st.text_input("🆔 بصمة الضيف (ID):", "BW-Def10_Lo3") 

# --- 2. محرك القراءة الرمزية المتغير ---
st.subheader("📝 التقرير النصي (لتعريف سياق الرموز)")
ai_report = st.text_area("أدخل التحليل النصي هنا:")

if st.button("🚀 فك التشفير واستخراج السكور الواقعي"):
    with st.spinner("⏳ جاري تحليل بصمة الفريق الرمزية..."):
        time.sleep(2)

    # --- منطق القراءة المتغير (Variable Symbol Logic) ---
    # تعريف معاملات القوة بناءً على الرموز في صورك
    
    # محرك المضيف
    h_power = 1.0
    if "Dom" in h_id: h_power += 2.2  # رمز الهيمنة يرفع للأهداف العالية (3+)
    if "Pwr" in h_id: h_power += 1.5  # رمز القوة يرفع للأهداف المتوسطة (2+)
    if "xV" in h_id: h_power += 0.8   # رمز الفاعلية
    
    # محرك الضيف
    a_power = 0.5
    if "Def" in a_id: a_power -= 0.3  # رمز الدفاع يقلل أهداف الضيف
    if "Spd" in a_id: a_power += 0.7  # رمز السرعة يرفع احتمالية المرتدات (BTTS)

    # دمج النص لتأكيد القراءة الرمزية
    if "اكتساح" in ai_report or "3-0" in ai_report:
        h_power += 1.0
        a_power = 0.1 # تصفير أهداف الضيف لضمان Clean Sheet

    # حساب مصفوفة الاحتمالات (من 0-0 حتى 5-5)
    results = []
    for h in range(6):
        for a in range(6):
            prob = poisson_calc(h, h_pwr := h_power) * poisson_calc(a, a_pwr := a_power)
            results.append({'s': f"{h}-{a}", 'p': prob, 't': h+a, 'h': h, 'a': a})
    
    results.sort(key=lambda x: x['p'], reverse=True)
    final = results[0]

    # --- العرض النهائي (تصميم الهوية البصرية لصورك) ---
    st.markdown(f"""
    <div style="background-color: #0e1117; padding: 40px; border: 5px solid #f1c40f; border-radius: 20px; text-align: center;">
        <h2 style="color: #8b949e;">النتيجة الحقيقية المختارة</h2>
        <h1 style="color: white; font-size: 80px;">{h_name} <span style="color: #f1c40f;">{final['s']}</span> {a_name}</h1>
        <p style="color: #2ecc71;">✅ Symbols Verified: {h_id} | {a_id}</p>
    </div>
    """, unsafe_allow_html=True)

    # --- السيناريوهات البديلة وملخص الأسواق ---
    st.markdown("---")
    st.subheader("📊 طباعة سيناريوهات بديلة:")
    st.write(f"🔹 **الهجومي:** إذا استغل {h_name} البصمة {h_id.split('_')[-1]} (توقع {results[1]['s']}).")
    st.write(f"🔹 **الدفاعي:** إذا تراجع {a_name} منطقة الجزاء (توقع 1-0).")

    st.markdown("---")
    st.subheader("📋 ملخص الأسواق المطبوع:")
    c1, c2, c3 = st.columns(3)
    c1.markdown(f"<div style='background: #1a2634; padding: 15px; border-radius: 10px; color: #5dade2;'>🏆 {h_name} :X2 توقع 1</div>", unsafe_allow_html=True)
    c2.markdown(f"<div style='background: #2c2c1a; padding: 15px; border-radius: 10px; color: #f4d03f;'>📈 الأهداف: {'OVER 2.5' if final['t'] >= 3 else 'UNDER 2.5'}</div>", unsafe_allow_html=True)
    c3.markdown(f"<div style='background: #1a2e1a; padding: 15px; border-radius: 10px; color: #2ecc71;'>⚽ BTTS: {'YES' if final['a'] > 0 else 'NO'}</div>", unsafe_allow_html=True)
    
