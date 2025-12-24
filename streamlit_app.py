import streamlit as st
import math
import time

st.set_page_config(page_title="SNIPER V111.0 - FULL SYSTEM", layout="wide")

def poisson_calc(k, lmbda):
    if lmbda <= 0: lmbda = 0.01
    return (lmbda**k * math.exp(-lmbda)) / math.factorial(k)

st.title("🔬 المحلل التفكيكي المتكامل (Names & Symbols Analyzer)")

# --- 1. إعادة خانات الأسماء والبصمات (IDs) ---
col_h, col_a = st.columns(2)
with col_h:
    h_name = st.text_input("🏠 اسم الفريق المضيف:", "Nigeria")
    h_id = st.text_input("🆔 بصمة المضيف (مثل NG-Dom88):", "NG-95xV_Dom88_Pwr91")
with col_a:
    a_name = st.text_input("✈️ اسم الفريق الضيف:", "Opponent")
    a_id = st.text_input("🆔 بصمة الضيف (مثل OP-Spd70):", "OP-70kM_Spd65_Res40")

# --- 2. محرك التفكيك والمقارنة الذكي ---
if st.button("🚀 تحليل المواجهة بالكامل"):
    with st.spinner("⏳ جاري تفكيك الرموز ومقارنة نقاط القوة والضعف..."):
        time.sleep(1.5)

    # مصفوفة الأوزان الرمزية الدقيقة
    weights = {
        "Dom": 2.5,  # رمز الهيمنة القصوى
        "Pwr": 1.5,  # قوة التهديف
        "xV": 0.8,   # فاعلية الهجمات
        "Spd": 1.2,  # سرعة المرتدات (مفتاح الـ BTTS)
        "Res": -1.1, # قوة المقاومة (تخصم من أهداف الخصم)
        "Def": -1.6  # الدفاع الصارم
    }

    # تحليل المضيف (المقارنة التفاعلية)
    h_pwr = 0.8
    for k, v in weights.items():
        if k in h_id: h_pwr += v
    
    # تحليل الضيف (المقارنة التفاعلية)
    a_pwr = 0.4
    for k, v in weights.items():
        if k in a_id:
            if v > 0: a_pwr += v # رموز هجومية للضيف ترفع أهدافه
            else: h_pwr += v # رموز دفاعية للضيف تخفض أهداف المضيف

    # حساب الاحتمالات (Poisson Distribution)
    results = []
    for h in range(6):
        for a in range(6):
            p = poisson_calc(h, h_pwr) * poisson_calc(a, a_pwr)
            results.append({'s': f"{h}-{a}", 'p': p, 'h': h, 'a': a})
    
    results.sort(key=lambda x: x['p'], reverse=True)
    final = results[0]

    # --- 3. العرض الاحترافي (تنسيق الهوية البصرية لصورك) ---
    st.markdown(f"""
    <div style="background-color: #0e1117; padding: 45px; border: 5px solid #f1c40f; border-radius: 25px; text-align: center;">
        <h1 style="color: white; font-size: 70px;">
            {h_name} <span style="color: #f1c40f;">{final['s']}</span> {a_name}
        </h1>
        <p style="color: #8b949e; font-size: 18px; margin-top: 10px;">
            تم التحليل بناءً على منطق الهيمنة المتغير وفك تشفير الرموز الفردية
        </p>
    </div>
    """, unsafe_allow_html=True)

    # --- 4. السيناريوهات البديلة والأسواق ---
    st.markdown("---")
    st.subheader("📊 طباعة سيناريوهات بديلة:")
    st.write(f"🔹 **الهجومي:** ({final['h']+1}-{final['a']}) إذا استغلت البصمة الرمز الهجومي {h_id.split('_')[-1]}.")
    st.write(f"🔹 **الدفاعي:** ({final['h']}-{final['a']-1 if final['a']>0 else 0}) إذا تراجع {a_name} لمنطقة الجزاء.")

    st.markdown("---")
    st.subheader("📋 ملخص الأسواق المطبوع:")
    c1, c2, c3 = st.columns(3)
    c1.markdown(f"<div style='background: #1a2634; padding: 15px; border-radius: 10px; color: #5dade2;'>🏆 التوقع: {'1' if final['h']>final['a'] else 'X2'} </div>", unsafe_allow_html=True)
    c2.markdown(f"<div style='background: #2c2c1a; padding: 15px; border-radius: 10px; color: #f4d03f;'>📈 الأهداف: {'OVER 2.5' if (final['h']+final['a']) >= 2.5 else 'UNDER 2.5'}</div>", unsafe_allow_html=True)
    c3.markdown(f"<div style='background: #1a2e1a; padding: 15px; border-radius: 10px; color: #2ecc71;'>⚽ BTTS: {'YES' if final['a'] > 0 else 'NO'}</div>", unsafe_allow_html=True)
    
