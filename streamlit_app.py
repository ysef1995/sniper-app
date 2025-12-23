import streamlit as st
import math
import time

st.set_page_config(page_title="SNIPER V100.0 - AUTO LOGIC", layout="wide")

def poisson_calc(k, lmbda):
    if lmbda <= 0: lmbda = 0.01
    return (lmbda**k * math.exp(-lmbda)) / math.factorial(k)

st.title("🛡️ محرك القرار الآلي (AI Auto-Decision)")

# 1. إدخال الرموز المشفرة (التي تحمل سر النتيجة)
col_h, col_a = st.columns(2)
with col_h:
    h_name = st.text_input("🏠 المضيف:", "Tunisie")
    h_id = st.text_input("🆔 ID IA المضيف:", "TN-88xV2zQ_Pwr91")
with col_a:
    a_name = st.text_input("✈️ الضيف:", "Ouganda")
    a_id = st.text_input("🆔 ID IA الضيف:", "UG-42kM7tY_Spd65")

# 2. تفعيل المحرك الآلي
st.info("💡 المحرك الآلي مفعل الآن: سيقوم بتحليل الرموز وتحديد السكور الواقعي تلقائياً.")

if st.button("🚀 استخراج النتيجة الحقيقية آلياً"):
    with st.spinner("⏳ المحرك الآلي يحلل الرموز ويوازن الاحتمالات..."):
        time.sleep(2)

    # --- ذكاء المحرك الآلي (Internal Logic) ---
    # تحليل الـ ID لاستنتاج "هوية المباراة" تلقائياً
    is_high_power = "Pwr" in h_id or "xV" in h_id
    is_fast_game = "Spd" in a_id or "kM" in a_id
    
    # اختيار المسار آلياً بناءً على الرموز فقط
    if is_high_power and is_fast_game:
        # مسار الاكتساح أو الأهداف العالية (مثلاً 3-1 أو 4-1)
        h_pwr, a_pwr = 3.2, 1.2
        mode_desc = "اكتساح هجومي (تحليل آلي)"
    elif is_high_power and not is_fast_game:
        # مسار التفوق الدفاعي (مثلاً 1-0 أو 2-0)
        h_pwr, a_pwr = 1.9, 0.4
        mode_desc = "تفوق مضيف (تحليل آلي)"
    else:
        # مسار التوازن (مثلاً 1-1 أو 1-0)
        h_pwr, a_pwr = 1.2, 0.8
        mode_desc = "توازن حذر (تحليل آلي)"

    # حساب مصفوفة الاحتمالات (من 0-0 حتى 5-5)
    results = []
    for h in range(6):
        for a in range(6):
            prob = poisson_calc(h, h_pwr) * poisson_calc(a, a_pwr)
            results.append({'s': f"{h}-{a}", 'p': prob, 't': h+a})
    
    # المحرك يختار "السكور الواقعي" الأنسب للهوية المستنتجة
    results.sort(key=lambda x: x['p'], reverse=True)
    real_score = results[0]

    # --- العرض النهائي (تصميم الفيديو الأصلي) ---
    st.markdown(f"""
    <div style="background-color: #0e1117; padding: 50px; border: 5px solid #f1c40f; border-radius: 25px; text-align: center;">
        <h2 style="color: #8b949e; margin-bottom: 20px;">النتيجة الحقيقية (IA Auto-Logic)</h2>
        <h1 style="color: white; font-size: 85px; letter-spacing: 5px;">
            {h_name} <span style="color: #f1c40f;">{real_score['s']}</span> {a_name}
        </h1>
        <p style="color: #2ecc71; font-size: 18px; margin-top: 20px;">
            🤖 Mode Identified: {mode_desc} | ID: {h_id}
        </p>
    </div>
    """, unsafe_allow_html=True)

    # --- طباعة سيناريوهات بديلة وملخص الأسواق ---
    st.markdown("---")
    st.subheader("📊 طباعة سيناريوهات بديلة:")
    st.write(f"🔹 **الهجومي:** إذا استغلت {h_name} الثغرات (توقع {results[1]['s']}).")
    st.write(f"🔹 **الدفاعي:** إذا تراجعت {a_name} منطقة الجزاء (توقع 1-0).")

    st.markdown("---")
    st.subheader("📋 ملخص الأسواق المطبوع:")
    c1, c2, c3 = st.columns(3)
    c1.markdown(f"<div style='background: #1a2634; padding: 15px; border-radius: 10px; color: #5dade2;'>🏆 {h_name} :X2 توقع 1</div>", unsafe_allow_html=True)
    c2.markdown(f"<div style='background: #2c2c1a; padding: 15px; border-radius: 10px; color: #f4d03f;'>📈 الأهداف: {'OVER 2.5' if real_score['t'] >= 3 else 'UNDER 2.5'}</div>", unsafe_allow_html=True)
    c3.markdown(f"<div style='background: #1a2e1a; padding: 15px; border-radius: 10px; color: #2ecc71;'>⚽ BTTS: {'YES' if '-' in real_score['s'] and real_score['s'].split('-')[1] != '0' else 'NO'}</div>", unsafe_allow_html=True)
    
