import streamlit as st
import math
import time

st.set_page_config(page_title="SNIPER V110.0 - DECODER", layout="wide")

def poisson_calc(k, lmbda):
    if lmbda <= 0: lmbda = 0.01
    return (lmbda**k * math.exp(-lmbda)) / math.factorial(k)

st.title("🔬 محلل الرموز التفكيكي (Granular Symbol Analyzer)")

# 1. إدخال البصمات الرقمية
col_h, col_a = st.columns(2)
with col_h:
    h_id = st.text_input("🆔 بصمة المضيف الفردية (مثلاً TN-88xV2zQ_Pwr91):", "NG-95xV_Dom88_Pwr91")
with col_a:
    a_id = st.text_input("🆔 بصمة الضيف الفردية (مثلاً UG-42kM7tY_Spd65):", "OP-70kM_Spd65_Res40")

# 2. محرك التفكيك والمقارنة
if st.button("🚀 تفكيك الرموز وتحليل المواجهة"):
    with st.spinner("⏳ جاري تحليل كل رمز على حدة..."):
        time.sleep(1.5)

    # --- مصفوفة الأوزان الرمزية (The Logic Matrix) ---
    weights = {
        "Dom": 2.5,  # هيمنة كاملة (تضمن أهداف)
        "Pwr": 1.5,  # قوة هجومية (ترفع السكور)
        "xV": 0.8,   # فاعلية أمام المرمى
        "Spd": 1.2,  # سرعة (مفتاح الـ BTTS والهدف المباغت)
        "Res": -1.0, # مقاومة دفاعية (تقلص أهداف الخصم)
        "Def": -1.5  # دفاع صلب (يمنع الأهداف)
    }

    # تحليل رموز المضيف
    h_score_potential = 0.5
    for key, val in weights.items():
        if key in h_id: h_score_potential += val
    
    # تحليل رموز الضيف (المقارنة)
    a_score_potential = 0.3
    for key, val in weights.items():
        if key in a_id:
            # إذا كان الرمز هجومي للضيف (مثل Spd) يزيد أهدافه
            if val > 0: a_score_potential += val
            # إذا كان الرمز دفاعي للضيف (مثل Res) يقلل أهداف المضيف
            else: h_score_potential += val 

    # ضبط الحدود الدنيا (منع النتائج السالبة)
    h_lmbda = max(h_score_potential, 0.1)
    a_lmbda = max(a_score_potential, 0.1)

    # حساب الاحتمالات
    results = []
    for h in range(6):
        for a in range(6):
            p = poisson_calc(h, h_lmbda) * poisson_calc(a, a_lmbda)
            results.append({'s': f"{h}-{a}", 'p': p, 'h': h, 'a': a})
    
    results.sort(key=lambda x: x['p'], reverse=True)
    final = results[0]

    # --- العرض الاحترافي (تنسيق الصور الخاصة بك) ---
    st.markdown(f"""
    <div style="background-color: #0e1117; padding: 45px; border: 5px solid #f1c40f; border-radius: 25px; text-align: center;">
        <h2 style="color: #8b949e; margin-bottom: 20px;">النتيجة الحقيقية بعد مقارنة الرموز</h2>
        <h1 style="color: white; font-size: 85px; letter-spacing: 5px;">
             <span style="color: #f1c40f;">{final['s']}</span>
        </h1>
        <p style="color: #2ecc71; font-size: 18px; margin-top: 20px;">
            🤖 تم التحليل بناءً على فك تشفير {len(h_id.split('_')) + len(a_id.split('_'))} رمزاً فريداً
        </p>
    </div>
    """, unsafe_allow_html=True)

    # --- ملخص الأسواق المعتمد على المقارنة ---
    st.markdown("---")
    st.subheader("📊 طباعة سيناريوهات بديلة (بناءً على الرموز):")
    st.write(f"🔹 **الهجومي:** ({final['h']+1}-{final['a']}) إذا تغلب رمز الـ Pwr على الـ Res.")
    st.write(f"🔹 **الدفاعي:** ({final['h']}-{final['a']-1 if final['a']>0 else 0}) إذا تراجع الخصم دفاعياً.")

    st.markdown("---")
    st.subheader("📋 ملخص الأسواق المطبوع:")
    c1, c2, c3 = st.columns(3)
    c1.markdown(f"<div style='background: #1a2634; padding: 15px; border-radius: 10px; color: #5dade2;'>🏆 توقع: {'1' if final['h']>final['a'] else 'X2'}</div>", unsafe_allow_html=True)
    c2.markdown(f"<div style='background: #2c2c1a; padding: 15px; border-radius: 10px; color: #f4d03f;'>📈 الأهداف: {'OVER 2.5' if (final['h']+final['a']) >= 2.5 else 'UNDER 2.5'}</div>", unsafe_allow_html=True)
    c3.markdown(f"<div style='background: #1a2e1a; padding: 15px; border-radius: 10px; color: #2ecc71;'>⚽ BTTS: {'YES' if final['a'] > 0 else 'NO'}</div>", unsafe_allow_html=True)
    
