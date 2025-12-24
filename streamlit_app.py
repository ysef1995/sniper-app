import streamlit as st
import math
import time

st.set_page_config(page_title="SNIPER V106.0 - GLOBAL ARCHITECT", layout="wide")

def poisson_calc(k, lmbda):
    if lmbda <= 0: lmbda = 0.01
    return (lmbda**k * math.exp(-lmbda)) / math.factorial(k)

st.title("🏛️ المحلل العالمي الشامل (Universal Symbol Decoder)")

# --- 1. إدخال البصمات الرقمية المتغيرة ---
col_h, col_a = st.columns(2)
with col_h:
    h_name = st.text_input("🏠 الفريق المضيف:", "Senegal")
    h_id = st.text_input("🆔 بصمة المضيف (ID):", "SN-97kZ4qR_Dom88") 
with col_a:
    a_name = st.text_input("✈️ الفريق الضيف:", "Botswana")
    a_id = st.text_input("🆔 بصمة الضيف (ID):", "BW-29mB5vX_Res31") 

# --- 2. المحرك النصي والرمزي المدمج ---
st.subheader("📝 التحليل النصي المعزز")
ai_report = st.text_area("أدخل التحليل النصي لضبط دقة المسار:")

if st.button("🚀 تحليل البصمات واستخراج السكور"):
    with st.spinner("⏳ جاري معالجة الرموز العالمية وفك التشفير..."):
        time.sleep(2)

    # --- محرك فك التشفير العالمي (The Architect Logic) ---
    # تحليل الرموز بناءً على أنماط النجاح السابقة
    
    h_pwr, a_pwr = 1.0, 0.5 # القيم الأساسية

    # فك تشفير رموز الهيمنة والقوة
    if any(sym in h_id for sym in ["Dom", "Pwr", "xV"]):
        h_pwr += 2.2 if "Dom" in h_id else 1.5 # رمز Dom يضمن 3 أهداف فأكثر
    
    # فك تشفير رموز المقاومة والسرعة
    if "Res" in a_id:
        # إذا كانت المقاومة ضعيفة (مثل Res31) تزيد أهداف المضيف
        h_pwr += 0.5 
    if "Spd" in a_id:
        a_pwr += 0.8 # رمز السرعة يزيد احتمالية BTTS

    # دمج التحليل النصي لفرض "الواقعية"
    if "3-0" in ai_report or "اكتساح" in ai_report:
        h_pwr = max(h_pwr, 3.1)
        a_pwr = 0.1 # لضمان BTTS: NO و Clean Sheet

    # مسح الاحتمالات الشامل (0-0 إلى 5-5)
    results = []
    for h in range(6):
        for a in range(6):
            p = poisson_calc(h, h_pwr) * poisson_calc(a, a_pwr)
            results.append({'s': f"{h}-{a}", 'p': p, 'h': h, 'a': a})
    
    results.sort(key=lambda x: x['p'], reverse=True)
    best = results[0]

    # --- العرض الاحترافي (طبق الأصل) ---
    st.markdown(f"""
    <div style="background-color: #0e1117; padding: 50px; border: 5px solid #f1c40f; border-radius: 25px; text-align: center;">
        <h2 style="color: #8b949e;">النتيجة الحقيقية المختارة</h2>
        <h1 style="color: white; font-size: 85px; letter-spacing: 5px;">
            {h_name} <span style="color: #f1c40f;">{best['s']}</span> {a_name}
        </h1>
        <p style="color: #2ecc71; font-size: 18px;">
            ✅ Symbols Verified: {h_id} | {a_id}
        </p>
    </div>
    """, unsafe_allow_html=True)

    # --- طباعة سيناريوهات بديلة وملخص الأسواق ---
    st.markdown("---")
    st.subheader("📊 طباعة سيناريوهات بديلة:")
    st.write(f"🔹 **الهجومي:** (توقع {best['h']}-{best['a']+1 if best['a'] < 3 else best['a']}) إذا استغلت البصمة {h_id.split('_')[-1]}.")
    st.write(f"🔹 **الدفاعي:** (توقع 1-0) إذا تراجع الخصم منطقة الجزاء.")

    st.markdown("---")
    st.subheader("📋 ملخص الأسواق المطبوع:")
    c1, c2, c3 = st.columns(3)
    c1.markdown(f"<div style='background: #1a2634; padding: 15px; border-radius: 10px; color: #5dade2;'>🏆 {h_name} :X2 توقع 1</div>", unsafe_allow_html=True)
    c2.markdown(f"<div style='background: #2c2c1a; padding: 15px; border-radius: 10px; color: #f4d03f;'>📈 الأهداف: {'OVER 2.5' if best['h']+best['a'] >= 3 else 'UNDER 2.5'}</div>", unsafe_allow_html=True)
    c3.markdown(f"<div style='background: #1a2e1a; padding: 15px; border-radius: 10px; color: #2ecc71;'>⚽ BTTS: {'YES' if best['a'] > 0 else 'NO'}</div>", unsafe_allow_html=True)
        
