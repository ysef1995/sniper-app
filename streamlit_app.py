import streamlit as st
import math
import time

st.set_page_config(page_title="SNIPER V108.0 - DYNAMIC", layout="wide")

def poisson_calc(k, lmbda):
    if lmbda <= 0: lmbda = 0.01
    return (lmbda**k * math.exp(-lmbda)) / math.factorial(k)

st.title("⚖️ محرك ميزان القوى (Dynamic Match Balance)")

# إدخال البصمات (IDs) التي تحدد قوة كل طرف في هذه المباراة
col_h, col_a = st.columns(2)
with col_h:
    h_name = st.text_input("🏠 الفريق المضيف:", "Tunisia")
    h_id = st.text_input("🆔 ID المضيف:", "TN-Pwr91") 
with col_a:
    a_name = st.text_input("✈️ الفريق الضيف:", "Uganda")
    a_id = st.text_input("🆔 ID الضيف:", "UG-Def80") # هنا رمز دفاعي قوي سيغير النتيجة

if st.button("🚀 تحليل التوازن واستخراج السكور"):
    with st.spinner("⏳ جاري موازنة القوى الرمزية..."):
        time.sleep(1.2)

    # --- منطق الميزان (The Balance Logic) ---
    # استخراج القيم الرقمية من الرموز (افتراضياً)
    h_val = int(''.join(filter(str.isdigit, h_id))) if any(c.isdigit() for c in h_id) else 50
    a_val = int(''.join(filter(str.isdigit, a_id))) if any(c.isdigit() for c in a_id) else 50

    # حساب القوة الهجومية للمضيف بناءً على ضعف/قوة دفاع الضيف
    # إذا كان دفاع الضيف (Def80) قوياً، ستنخفض القوة الهجومية للمضيف
    if "Def" in a_id and a_val > 70:
        h_attack = 1.2  # مباراة مغلقة (توقع 1-0)
        match_type = "مباراة دفاعية مغلقة"
    elif "Dom" in h_id or h_val > 85:
        h_attack = 3.2  # مباراة اكتساح (توقع 3-0 أو 3-1)
        match_type = "هجوم كاسح"
    else:
        h_attack = 1.9  # مباراة متوازنة (توقع 2-1)
        match_type = "توازن نسبي"

    # احتمالية تسجيل الضيف بناءً على رمز السرعة (Spd)
    a_attack = 1.1 if "Spd" in a_id else 0.3

    # حساب السكور الأكثر احتمالية
    results = []
    for h in range(6):
        for a in range(6):
            p = poisson_calc(h, h_attack) * poisson_calc(a, a_attack)
            results.append({'s': f"{h}-{a}", 'p': p, 'h': h, 'a': a})
    
    results.sort(key=lambda x: x['p'], reverse=True)
    final = results[0]

    # --- العرض المرئي للنتيجة ---
    st.markdown(f"""
    <div style="background-color: #0e1117; padding: 40px; border: 5px solid #f1c40f; border-radius: 20px; text-align: center;">
        <h2 style="color: #8b949e;">النتيجة الواقعية بناءً على التوازن</h2>
        <h1 style="color: white; font-size: 80px;">{h_name} <span style="color: #f1c40f;">{final['s']}</span> {a_name}</h1>
        <p style="color: #2ecc71;">📊 نوع المباراة المستنتج: {match_type}</p>
    </div>
    """, unsafe_allow_html=True)

    # --- طباعة السيناريوهات والأسواق ---
    st.markdown("---")
    st.subheader("📋 ملخص الأسواق المطبوع:")
    c1, c2, c3 = st.columns(3)
    c1.markdown(f"<div style='background: #1a2634; padding: 15px; border-radius: 10px; color: #5dade2;'>🏆 الفائز: {h_name if final['h'] > final['a'] else 'تعادل'}</div>", unsafe_allow_html=True)
    c2.markdown(f"<div style='background: #2c2c1a; padding: 15px; border-radius: 10px; color: #f4d03f;'>📈 الأهداف: {'OVER 2.5' if (final['h']+final['a']) >= 3 else 'UNDER 2.5'}</div>", unsafe_allow_html=True)
    c3.markdown(f"<div style='background: #1a2e1a; padding: 15px; border-radius: 10px; color: #2ecc71;'>⚽ BTTS: {'YES' if final['a'] > 0 else 'NO'}</div>", unsafe_allow_html=True)
    
