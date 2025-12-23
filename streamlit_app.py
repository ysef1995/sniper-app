import streamlit as st
import math
import time

st.set_page_config(page_title="SNIPER AI - FLEXIBLE LOGIC", layout="wide")

def poisson_calc(k, lmbda):
    if lmbda <= 0: lmbda = 0.1
    return (lmbda**k * math.exp(-lmbda)) / math.factorial(k)

st.title("🎯 IA SCORE EXACT - المحرك المرن")

# 1. إدخال المعرفات الرمزية (IDs)
col_h, col_a = st.columns(2)
with col_h:
    h_name = st.text_input("🏠 المضيف:", "تونس")
    h_id = st.text_input("🆔 ID IA المضيف:", "TN-88xV2zQ")
with col_a:
    a_name = st.text_input("✈️ الضيف:", "أوغندا")
    a_id = st.text_input("🆔 ID IA الضيف:", "UG-42kM")

# 2. التقرير النصي (مفتاح المرونة)
st.subheader("📝 التقرير التحليلي (AI Report)")
ai_report = st.text_area("أدخل التحليل النصي هنا:", 
                         placeholder="مثال: مباراة متكافئة، دفاع صلب، أو هجوم كاسح...")

if st.button("🚀 تحليل السيناريو الواقعي"):
    with st.spinner("⏳ جاري موازنة القوة الرمزية مع النص..."):
        time.sleep(1)

    # --- محرك المرونة (Dynamic Power Adjustment) ---
    # استخراج القوة الأساسية من الرموز
    h_base = 1.5 if len(h_id) > 5 else 1.0
    a_base = 0.8
    
    # تعديل النتيجة بناءً على النص (هنا تكمن المرونة)
    if any(word in ai_report for word in ["دفاع", "مغلقة", "حذر", "1-0"]):
        h_pwr, a_pwr = 1.1, 0.2  # يوجه النتيجة نحو 1-0
    elif any(word in ai_report for word in ["متكافئة", "ندية", "تعادل"]):
        h_pwr, a_pwr = 1.2, 1.2  # يوجه النتيجة نحو 1-1
    elif any(word in ai_report for word in ["اكتساح", "هجوم", "3-1"]):
        h_pwr, a_pwr = 2.8, 1.1  # يوجه النتيجة نحو 3-1
    else:
        h_pwr, a_pwr = h_base, a_base

    # حساب الاحتمالات
    scores = []
    for h in range(5):
        for a in range(4):
            prob = poisson_calc(h, h_pwr) * poisson_calc(a, a_pwr)
            scores.append({'s': f"{h}-{a}", 'p': prob, 't': h+a})
    
    scores.sort(key=lambda x: x['p'], reverse=True)
    final = scores[0]

    # --- العرض النهائي (تصميم مرن) ---
    st.markdown(f"""
    <div style="background-color: #0e1117; padding: 40px; border: 4px solid #f1c40f; border-radius: 20px; text-align: center;">
        <h1 style="color: white; font-size: 60px;">{h_name} <span style="color: #f1c40f;">{final['s']}</span> {a_name}</h1>
        <p style="color: #888;">تم التحليل بناءً على منطق الهيمنة المتغير</p>
    </div>
    """, unsafe_allow_html=True)

    # --- طباعة سيناريوهات بديلة (المرونة المطلوبة) ---
    st.markdown("---")
    st.subheader("📊 طباعة سيناريوهات بديلة:")
    st.write(f"🔹 **السيناريو الهجومي:** إذا استغل {h_name} الثغرات (توقع 2-1 أو 3-1).")
    st.write(f"🔹 **السيناريو الدفاعي:** إذا تراجع {a_name} للخلف (توقع 1-0).")

    # --- ملخص الأسواق الملون ---
    st.markdown("---")
    st.subheader("📋 ملخص الأسواق المطبوع:")
    st.markdown(f"<div style='background: #1a2634; padding: 12px; border-radius: 8px; color: #5dade2;'>🏆 {h_name} :X2 توقع 1</div>", unsafe_allow_html=True)
    st.markdown(f"<div style='background: #2c2c1a; padding: 12px; border-radius: 8px; color: #f4d03f; margin-top: 5px;'>📈 توقع الأهداف: {'OVER 2.5' if final['t'] >= 3 else 'UNDER 2.5'}</div>", unsafe_allow_html=True)
    st.markdown(f"<div style='background: #1a2e1a; padding: 12px; border-radius: 8px; color: #2ecc71; margin-top: 5px;'>⚽ BTTS: {'YES' if '1' in final['s'] else 'NO'}</div>", unsafe_allow_html=True)
    
