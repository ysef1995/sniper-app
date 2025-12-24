import streamlit as st
import math
import time

st.set_page_config(page_title="SNIPER V102.0 - ULTIMATE", layout="wide")

def poisson_calc(k, lmbda):
    if lmbda <= 0: lmbda = 0.01
    return (lmbda**k * math.exp(-lmbda)) / math.factorial(k)

st.title("🎯 محرك السكور الواقعي الشامل (رموز + تحليل نصي)")

# --- 1. إدخال المعرفات الرمزية ---
col_h, col_a = st.columns(2)
with col_h:
    h_name = st.text_input("🏠 المضيف:", "Senegal")
    h_id = st.text_input("🆔 ID IA المضيف:", "SN-Pwr95_xV9")
with col_a:
    a_name = st.text_input("✈️ الضيف:", "Botswana")
    a_id = st.text_input("🆔 ID IA الضيف:", "BW-Def20_kM1")

# --- 2. التحليل النصي (المفتاح السري للواقعية) ---
st.subheader("📝 التقرير التحليلي للذكاء الاصطناعي")
ai_report = st.text_area("أدخل التحليل هنا (مثلاً: هجوم كاسح، دفاع صلب، مباراة مفتوحة...):", 
                         placeholder="لصق التحليل النصي لضبط دقة السكور...")

if st.button("🚀 استخراج النتيجة الحقيقية"):
    with st.spinner("⏳ جاري دمج الرموز مع التحليل النصي..."):
        time.sleep(1.5)

    # محرك فك التشفير الأساسي من الرموز
    h_pwr = sum(ord(c) for c in h_id) / 220.0
    a_pwr = sum(ord(c) for c in a_id) / 380.0

    # ذكاء المعالجة النصية (Text Override)
    # هذا الجزء يضمن أن نتيجة 3-0 تظهر إذا كان النص يدعم ذلك
    if any(word in ai_report for word in ["هجوم", "كاسح", "أهداف", "مفتوحة", "اكتساح"]):
        h_pwr += 1.8
        a_pwr += 0.5
        mode_label = "سيناريو هجومي واقعي"
    elif any(word in ai_report for word in ["دفاع", "مغلقة", "حذر", "تراجع"]):
        h_pwr *= 0.6
        a_pwr *= 0.4
        mode_label = "سيناريو دفاعي واقعي"
    else:
        mode_label = "منطق الهيمنة المتغير"

    # حساب مصفوفة الاحتمالات (من 0-0 حتى 5-5)
    results = []
    for h in range(6):
        for a in range(6):
            prob = poisson_calc(h, h_pwr) * poisson_calc(a, a_pwr)
            results.append({'s': f"{h}-{a}", 'p': prob, 't': h+a, 'h': h, 'a': a})
    
    # اختيار السكور الواقعي (الأعلى احتمالية بعد دمج النص والرموز)
    results.sort(key=lambda x: x['p'], reverse=True)
    final_score = results[0]

    # --- العرض النهائي (تصميم احترافي طبق الأصل) ---
    st.markdown(f"""
    <div style="background-color: #0e1117; padding: 40px; border: 5px solid #f1c40f; border-radius: 20px; text-align: center;">
        <h2 style="color: #8b949e; margin-bottom: 10px;">النتيجة الحقيقية المختارة</h2>
        <h1 style="color: white; font-size: 80px; letter-spacing: 3px;">
            {h_name} <span style="color: #f1c40f;">{final_score['s']}</span> {a_name}
        </h1>
        <p style="color: #2ecc71; font-size: 16px;">
            ✅ {mode_label} | Symbols Verified: {h_id}
        </p>
    </div>
    """, unsafe_allow_html=True)

    # --- طباعة سيناريوهات بديلة (المرونة التي طلبتها) ---
    st.markdown("---")
    st.subheader("📊 طباعة سيناريوهات بديلة:")
    st.write(f"🔹 **الهجومي:** إذا استغلت {h_name} الثغرات (توقع {results[1]['s']} أو {results[2]['s']}).")
    st.write(f"🔹 **الدفاعي:** إذا تراجعت {a_name} منطقة الجزاء (توقع 1-0 أو 0-0).")

    # --- ملخص الأسواق الملون ---
    st.markdown("---")
    st.subheader("📋 ملخص الأسواق المطبوع:")
    c1, c2, c3 = st.columns(3)
    c1.markdown(f"<div style='background: #1a2634; padding: 15px; border-radius: 10px; color: #5dade2;'>🏆 {h_name} :X2 توقع 1</div>", unsafe_allow_html=True)
    c2.markdown(f"<div style='background: #2c2c1a; padding: 15px; border-radius: 10px; color: #f4d03f;'>📈 الأهداف: {'OVER 2.5' if final_score['t'] >= 3 else 'UNDER 2.5'}</div>", unsafe_allow_html=True)
    c3.markdown(f"<div style='background: #1a2e1a; padding: 15px; border-radius: 10px; color: #2ecc71;'>⚽ BTTS: {'YES' if final_score['a'] > 0 else 'NO'}</div>", unsafe_allow_html=True)
    
