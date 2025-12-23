import streamlit as st
import math
import time

# إعدادات الواجهة الاحترافية
st.set_page_config(page_title="IA SCORE EXACT PRO", layout="wide")

def poisson_calculation(k, lmbda):
    if lmbda <= 0: lmbda = 0.001
    return (lmbda**k * math.exp(-lmbda)) / math.factorial(k)

st.title("🎯 IA SCORE EXACT - المنصة الاحترافية")

# --- الخطوة 1: إدخال الـ IDs الرمزية (الأحرف) ---
st.subheader("🔑 إدخال معرفات المقابلة (AI Match IDs)")
col_h, col_a = st.columns(2)
with col_h:
    h_name = st.text_input("🏠 الفريق المضيف:", "تونس")
    h_id_ia = st.text_input("🆔 ID IA (أحرف/رموز):", "TX-99")
with col_a:
    a_name = st.text_input("✈️ الفريق الضيف:", "أوغندا")
    a_id_ia = st.text_input("🆔 ID IA (أحرف/رموز):", "UG-12")

st.markdown("---")

# --- الخطوة 2: التحليل النصي ---
st.subheader("📝 التقرير التحليلي للذكاء الاصطناعي")
ai_report = st.text_area("أدخل التحليل النصي المستخرج من IA:", 
                         placeholder="لصق التحليل هنا... مثال: مباراة دفاعية حذرة")

if st.button("🚀 استخراج النتيجة الدقيقة (START ANALYSIS)"):
    with st.spinner("⏳ جاري فك تشفير المعرفات الرمزية ومطابقة النص..."):
        time.sleep(1.5)

    # 1. محرك فك تشفير الـ ID الرمزي
    # تحويل الأحرف إلى قيمة رقمية للقوة (Power Level)
    h_pwr = sum(ord(c) for c in h_id_ia) / 150.0
    a_pwr = sum(ord(c) for c in a_id_ia) / 250.0

    # 2. 🔥 تصحيح الخطأ البرمجي ومنطق الواقعية 🔥
    # فحص الكلمات المفتاحية لتعديل النتيجة
    defensive_words = ["دفاع", "مغلقة", "حذر", "تراجع", "صعوبة"]
    offensive_words = ["اكتساح", "هجوم", "كاسح", "أهداف", "مفتوحة"]

    if any(word in ai_report for word in defensive_words):
        h_pwr *= 0.6  # تقليل القوة الهجومية للمضيف
        a_pwr *= 0.4  # تقليل القوة الهجومية للضيف
    elif any(word in ai_report for word in offensive_words):
        h_pwr += 1.0  # رفع القوة الهجومية

    # 3. حساب احتمالات النتائج (توزيع بواسون)
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

    # 4. طباعة ملخص الأسواق المقارن
    st.markdown("---")
    st.subheader("📋 ملخص الأسواق المطبوع:")
    c1, c2, c3 = st.columns(3)
    c1.info(f"🏆 **توقع 1X2:** {h_name if h_pwr > a_pwr else a_name}")
    c2.warning(f"📈 **توقع الأهداف:** {'OVER 2.5' if final_result['total'] >= 3 else 'UNDER 2.5'}")
    c3.success(f"⚽ **BTTS:** {'YES' if '1' in final_result['score'] or '2' in final_result['score'] and '0' not in final_result['score'] else 'NO'}")
    
