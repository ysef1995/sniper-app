import streamlit as st
import math
import time

# إعداد الواجهة
st.set_page_config(page_title="SNIPER V78.0 INTELLIGENT", layout="wide")

def poisson_probability(k, lmbda):
    return (lmbda**k * math.exp(-lmbda)) / math.factorial(k)

# --- محرك قراءة التحليل النصي (الذكاء الاصطناعي المبسط) ---
def analyze_text_report(report_text, current_h_xg, current_a_xg):
    # الكلمات التي توحي بمباراة مغلقة (تمنع 3-1)
    defensive_keywords = ["دفاعي", "مغلقة", "حذر", "غيابات هجومية", "صعب التسجيل", "under", "defensive"]
    # الكلمات التي توحي بانفجار هجومي (تدعم 3-1)
    offensive_keywords = ["اكتساح", "هجوم كاسح", "ضعف دفاعي", "over", "offensive", "open match"]
    
    adjustment = 1.0
    for word in defensive_keywords:
        if word in report_text.lower():
            adjustment = 0.7  # خفض الأهداف المتوقعة بنسبة 30%
            break
    for word in offensive_keywords:
        if word in report_text.lower():
            adjustment = 1.3  # رفع الأهداف المتوقعة بنسبة 30%
            break
            
    return current_h_xg * adjustment, current_a_xg * adjustment

st.title("🧠 SNIPER V78.0 - المحلل الذكي للـ ID")

# إدخال البيانات الأساسية
col1, col2 = st.columns(2)
with col1:
    h_name = st.text_input("🏠 الفريق المضيف:", "Tunisie")
    h_id = st.text_input("🆔 ID الفريق (للمراجعة):", "12345")
with col2:
    a_name = st.text_input("✈️ الفريق الضيف:", "Ouganda")
    odd_under25 = st.number_input("📉 Odd Under 2.5 (فلتر الأمان):", value=1.60)

# خانة التحليل النصي (هنا تضع ما قرأته في الـ ID)
st.subheader("📝 التحليل النصي المستخلص من الـ ID:")
analysis_input = st.text_area("أدخل ملخص التحليل (مثلاً: مباراة دفاعية قوية، أو غياب المهاجمين):", 
                              placeholder="مثال: الفريق المضيف يلعب بطريقة دفاعية بحتة والضيف يعاني هجومياً...")

# إدخال الأودز اليدوية
st.markdown("---")
st.subheader("💰 أودز الأسواق")
c1, c2, c3 = st.columns(3)
with c1: odd_1 = st.number_input("Odd Win 1:", value=1.50)
with c2: odd_o2 = st.number_input("Odd Over 2.5:", value=2.20)
with c3: odd_by = st.number_input("Odd BTTS Yes:", value=2.10)

if st.button("🚀 تشغيل التحليل المقارن"):
    # 1. إحصائيات مبدئية
    base_h_xg = (1 / odd_1) * 2.0
    base_a_xg = 0.8
    
    # 2. 🔥 المعالجة الذكية للنص (هذا هو طلبك) 🔥
    final_h, final_a = analyze_text_report(analysis_input, base_h_xg, base_a_xg)
    
    # 3. حساب الاحتمالات
    scores = []
    for h in range(5):
        for a in range(5):
            p = poisson_probability(h, final_h) * poisson_probability(a, final_a)
            scores.append({'s': f"{h}-{a}", 'p': p, 'total': h+a})
    
    scores.sort(key=lambda x: x['p'], reverse=True)
    
    # فلتر Odds للواقعية
    if odd_under25 < 1.70:
        final_res = [s for s in scores if s['total'] <= 2][0]
    else:
        final_res = scores[0]

    # العرض النهائي
    st.markdown(f"<div style='text-align: center; border: 3px solid #f1c40f; padding: 20px; border-radius: 15px;'>"
                f"<h2>التوقع النهائي بناءً على التحليل النصي والأودز</h2>"
                f"<h1 style='font-size: 60px; color: #f1c40f;'>{h_name} {final_res['s']} {a_name}</h1>"
                f"</div>", unsafe_allow_html=True)
    
