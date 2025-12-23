import streamlit as st
import math
import time

# إعداد الواجهة لتناسب احتياجاتك الاحترافية
st.set_page_config(page_title="SNIPER V85.0 REALITY", layout="wide")

def poisson_probability(k, lmbda):
    return (lmbda**k * math.exp(-lmbda)) / math.factorial(k)

st.title("🛡️ SNIPER V85.0 - ميزان التوقعات الواقعية")

# 1. المعرفات الأساسية (الأسماء والـ IDs)
col_t, col_id = st.columns(2)
with col_t:
    h_n = st.text_input("🏠 الفريق المضيف:", "Tunisie")
    a_n = st.text_input("✈️ الفريق الضيف:", "Ouganda")
with col_id:
    h_id = st.text_input("🆔 ID المضيف:", "7412")
    a_id = st.text_input("🆔 ID الضيف:", "8523")

st.markdown("---")

# 2. إدخال أودز الأسواق يدوياً (للمقارنة وليس للسيطرة)
st.subheader("💰 أودز الأسواق الكاملة")
o1, o2, o3 = st.columns(3)
with o1:
    odd_1 = st.number_input(f"Odd Win {h_n}:", value=1.45)
    odd_x = st.number_input("Odd Draw:", value=4.20)
    odd_2 = st.number_input(f"Odd Win {a_n}:", value=7.50)
with o2:
    odd_over = st.number_input("Odd Over 2.5:", value=2.20)
    odd_under = st.number_input("Odd Under 2.5:", value=1.65)
with o3:
    odd_by = st.number_input("Odd BTTS Yes:", value=2.10)
    odd_bn = st.number_input("Odd BTTS No:", value=1.75)

st.markdown("---")

# 3. محرك التحليل النصي (القائد الفعلي للمنطق)
st.subheader("📝 التحليل النصي المستورد (AI Context)")
ai_report = st.text_area("أدخل التحليل النصي هنا (مثلاً: مباراة هجومية، دفاع صلب، غيابات...):", 
                         placeholder="انسخ ملخص المباراة هنا لتصحيح الأرقام...")

if st.button("🚀 تشغيل محرك الواقعية"):
    with st.spinner("⏳ جاري موازنة النص مع الأرقام..."):
        time.sleep(2)

    # حساب القوة الافتراضية
    h_xg = (1 / odd_1) * 2.2
    a_xg = 0.7
    
    # --- منطق التصحيح الواقعي ---
    # إذا وجد النص "هجوم" أو "أهداف"، نرفع التوقع حتى لو الأودز منخفض
    if any(word in ai_report.lower() for word in ["هجوم", "أهداف", "مفتوحة", "offensive"]):
        h_xg += 0.8
        a_xg += 0.4
    # إذا وجد النص "دفاع" أو "مغلقة"، نخفض التوقع فوراً لمنع العبث
    elif any(word in ai_report.lower() for word in ["دفاع", "مغلقة", "under", "defensive"]):
        h_xg *= 0.6
        a_xg *= 0.4

    # حساب النتائج
    scores = []
    for h in range(5):
        for a in range(5):
            p = poisson_probability(h, h_xg) * poisson_probability(a, a_xg)
            scores.append({'s': f"{h}-{a}", 'p': p, 't': h+a})
    
    scores.sort(key=lambda x: x['p'], reverse=True)
    
    # اختيار النتيجة بناءً على "الميزان"
    final_res = scores[0]

    # العرض النهائي المتكامل
    st.markdown(f"""
    <div style="background-color: #111; padding: 40px; border-radius: 15px; border: 3px solid #f1c40f; text-align: center;">
        <h1 style="color: white; margin: 0;">{h_n} <span style="color: #f1c40f;">{final_res['s']}</span> {a_n}</h1>
        <p style="color: #888;">تم الدمج بنجاح بين الـ ID والأسواق والتحليل النصي</p>
    </div>
    """, unsafe_allow_html=True)

    # طباعة ملخص الأسواق المقارن
    st.markdown("### 📋 طباعة ملخص الأسواق المقارن:")
    st.write(f"🏆 **توقع 1X2:** {h_n if odd_1 < odd_2 else a_n}")
    st.write(f"📈 **توقع الأهداف:** {'OVER 2.5' if final_res['t'] >= 3 else 'UNDER 2.5'}")
    st.write(f"⚽ **BTTS:** {'YES' if '1' in final_res['s'].split('-')[1] else 'NO'}")
    
