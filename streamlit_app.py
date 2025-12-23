import streamlit as st
import math
import time

# إعدادات الواجهة الاحترافية (Dark Mode)
st.set_page_config(page_title="IA SCORE EXACT PRO", layout="wide")

def poisson_calculation(k, lmbda):
    return (lmbda**k * math.exp(-lmbda)) / math.factorial(k)

st.title("🎯 IA SCORE EXACT - المنصة الاحترافية")

# --- الخطوة 1: إدخال الـ IDs الرمزية (الأحرف) كما في الفيديو ---
st.subheader("🔑 إدخال معرفات المقابلة (AI Match IDs)")
col_h, col_a = st.columns(2)
with col_h:
    h_name = st.text_input("🏠 الفريق المضيف:", "تونس")
    h_id_ia = st.text_input("🆔 ID IA (أحرف/رموز):", "TX-99")
with col_a:
    a_name = st.text_input("✈️ الفريق الضيف:", "أوغندا")
    a_id_ia = st.text_input("🆔 ID IA (أحرف/رموز):", "UG-12")

st.markdown("---")

# --- الخطوة 2: التحليل النصي (سر النتيجة الواقعية) ---
st.subheader("📝 التقرير التحليلي للذكاء الاصطناعي")
ai_report = st.text_area("أدخل التحليل النصي المستخرج من IA:", 
                         placeholder="لصق التحليل هنا... (مثلاً: تونس تهاجم بقوة، دفاع الخصم صامد)")

if st.button("🚀 استخراج النتيجة الدقيقة (START ANALYSIS)"):
    with st.spinner("⏳ جاري فك تشفير المعرفات الرمزية ومطابقة النص..."):
        time.sleep(2)

    # محرك فك تشفير الـ ID الرمزي (Logic Decoder)
    # كل حرف له قيمة رقمية تؤثر على الأهداف المتوقعة
    h_pwr = sum(ord(c) for c in h_id_ia) / 150.0
    a_pwr = sum(ord(c) for c in a_id_ia) / 250.0

    # تصحيح "الواقعية" بناءً على الكلمات المفتاحية في النص
    # لمنع نتائج مثل 3-1 في مباراة يصفها النص بأنها دفاعية
    if any(word in ai_report for ["دفاع", "مغلقة", "حذر"]):
        h_pwr = 1.2
        a_pwr = 0.2
    elif any(word in ai_report for ["اكتساح", "هجوم", "كاسح"]):
        h_pwr += 1.0

    # حساب احتمالات النتائج
    scores = []
    for h in range(5):
        for a in range(5):
            prob = poisson_calculation(h, h_pwr) * poisson_calculation(a, a_pwr)
            scores.append({'score': f"{h}-{a}", 'prob': prob, 'total': h+a})
    
    scores.sort(key=lambda x: x['prob'], reverse=True)
    final_result = scores[0]

    # --- العرض النهائي (طبق الأصل للفيديو) ---
    st.markdown(f"""
    <div style="background-color: #0e1117; padding: 50px; border: 5px solid #f1c40f; border-radius: 25px; text-align: center;">
        <h2 style="color: #8b949e; margin-bottom: 20px;">النتيجة المتوقعة بناءً على ترميز IA</h2>
        <h1 style="color: white; font-size: 80px; letter-spacing: 5px;">
            {h_name} <span style="color: #f1c40f;">{final_result['score']}</span> {a_name}
        </h1>
        <p style="color: #2ecc71; font-size: 18px; margin-top: 20px;">
            ✅ Decoded Symbols: {h_id_ia} | {a_id_ia}
        </p>
    </div>
    """, unsafe_allow_html=True)

    # طباعة ملخص الأسواق المقارن
    st.markdown("---")
    st.subheader("📋 ملخص الأسواق المطبوع:")
    c1, c2, c3 = st.columns(3)
    c1.write(f"🏆 **توقع 1X2:** {h_name}")
    c2.write(f"📈 **توقع الأهداف:** {'OVER 2.5' if final_result['total'] >= 3 else 'UNDER 2.5'}")
    c3.write(f"⚽ **BTTS:** {'YES' if '1' in final_result['score'] else 'NO'}")
    
