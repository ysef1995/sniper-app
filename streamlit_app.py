import streamlit as st
import math
import time

# إعداد الواجهة الاحترافية (Dark Mode)
st.set_page_config(page_title="SNIPER V79.0 - FULL ODDS", layout="wide")

def poisson_probability(k, lmbda):
    return (lmbda**k * math.exp(-lmbda)) / math.factorial(k)

st.title("🚜 SNIPER V79.0 - محرك الأسواق المتكامل")

# 1. الأسماء والـ IDs
col_team, col_id = st.columns(2)
with col_team:
    h_n = st.text_input("🏠 اسم المضيف:", "Tunisie")
    a_n = st.text_input("✈️ اسم الضيف:", "Ouganda")
with col_id:
    h_id = st.text_input("🆔 ID المضيف:", "101")
    a_id = st.text_input("🆔 ID الضيف:", "102")

st.markdown("---")

# 2. إدخال جميع الأودز (1X2, Over/Under, BTTS)
st.subheader("💰 إدخال أودز الأسواق يدوياً (Manual Odds)")
o1, o2, o3 = st.columns(3)
with o1:
    st.write("**السوق الرئيسي (1X2)**")
    odd_1 = st.number_input(f"Odd Win {h_n}:", value=1.40)
    odd_x = st.number_input("Odd Draw (X):", value=4.50)
    odd_2 = st.number_input(f"Odd Win {a_n}:", value=8.00)
with o2:
    st.write("**الأهداف (2.5)**")
    odd_over = st.number_input("Odd Over 2.5:", value=1.90)
    odd_under = st.number_input("Odd Under 2.5:", value=1.80)
with o3:
    st.write("**التسجيل (BTTS)**")
    odd_btts_y = st.number_input("Odd BTTS Yes:", value=2.10)
    odd_btts_n = st.number_input("Odd BTTS No:", value=1.70)

st.markdown("---")

# 3. إحصائيات الهيمنة (V37.0)
st.subheader("📊 إحصائيات الهيمنة (Dominance Stats)")
s1, s2 = st.columns(2)
with s1:
    h_xg = st.number_input("xG (Home):", value=2.0)
    h_ppg = st.number_input("PPG (Home):", value=2.2)
with s2:
    a_xg = st.number_input("xG (Away):", value=0.7)
    a_ppg = st.number_input("PPG (Away):", value=0.8)

if st.button("🚀 تشغيل المحرك وطباعة التقرير النهائي"):
    with st.spinner("⏳ جاري مراجعة الأودز ومنطق الهيمنة..."):
        time.sleep(2)

    # حساب القوة النسبية بناءً على الأودز والهيمنة
    # نستخدم الأودز لضبط الـ xG الحقيقي (إذا كان Under منخفض، نقلل الأهداف)
    final_h_xg = h_xg * (1 / odd_1)
    final_a_xg = a_xg * (1 / odd_2) * 5 # تعديل لوزن الفريق الضعيف
    
    # فلتر منع العبث: إذا كان Odd Under 2.5 أقل من 1.80، نكبح الجماح الهجومي
    if odd_under < 1.80:
        final_h_xg *= 0.8
        final_a_xg *= 0.6

    # حساب الاحتمالات
    scores = []
    for h in range(6):
        for a in range(6):
            p = poisson_probability(h, final_h_xg) * poisson_probability(a, final_a_xg)
            scores.append({'s': f"{h}-{a}", 'p': p, 'total': h+a})
    
    scores.sort(key=lambda x: x['p'], reverse=True)
    
    # اختيار النتيجة بناءً على سياق الأهداف (Under/Over)
    if odd_under < odd_over:
        final_res = [s for s in scores if s['total'] <= 2][0]
    else:
        final_res = scores[0]

    # العرض النهائي للفيديو
    st.markdown(f"<div style='text-align: center; background: #0e1117; padding: 40px; border: 4px solid #f1c40f; border-radius: 20px;'>"
                f"<h1 style='color: white;'>{h_n} <span style='color: #f1c40f;'>{final_res['s']}</span> {a_n}</h1>"
                f"<h3 style='color: #8b949e;'>النتيجة المدققة بناءً على كامل أودز الأسواق</h3>"
                f"</div>", unsafe_allow_html=True)

    # طباعة احتمالات الأسواق
    st.markdown("---")
    st.subheader("📋 طباعة توقعات الأسواق المقارنة:")
    st.write(f"✅ **سوق 1X2:** {h_n} (بناءً على Odd {odd_1})")
    st.write(f"⚽ **سوق BTTS:** {'نعم' if odd_btts_y < 2.0 else 'لا'} (بناءً على Odd {odd_btts_y})")
    st.write(f"📈 **سوق الأهداف:** {'Under 2.5' if odd_under < odd_over else 'Over 2.5'}")
    
