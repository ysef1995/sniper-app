import streamlit as st
import math
import time

st.set_page_config(page_title="SNIPER V126.0 - MASTER", layout="wide")

def poisson_calc(k, lmbda):
    if lmbda <= 0: lmbda = 0.01
    return (lmbda**k * math.exp(-lmbda)) / math.factorial(k)

st.title("🏆 المحلل الشامل (The Master Logic)")

col_h, col_a = st.columns(2)
with col_h:
    h_name = st.text_input("🏠 صاحب الأرض:", "Nigeria")
    h_id = st.text_input("🆔 ID المضيف:", "NGA-82yV_Str91")
with col_a:
    a_name = st.text_input("✈️ الضيف:", "Tanzania")
    a_id = st.text_input("🆔 ID الضيف:", "TAN-44kM_Res78")

if st.button("🚀 تحليل المواجهة بالمنطق المطور"):
    with st.spinner('⏳ جاري موازنة القوى ومنع أخطاء الـ Clean Sheet...'):
        time.sleep(1)

    # تفكيك الأرقام والرموز
    def parse_final(id_text, pos):
        nums = [int(s) for s in "".join((c if c.isdigit() else " ") for c in id_text).split()]
        v_atk = nums[-1] if pos == "h" else nums[0]
        v_def = nums[0] if pos == "h" else nums[-1]
        # رموز الاختراق (تحويل 3-0 إلى 3-1)
        has_penetration = any(k in id_text for k in ["kM", "Spd", "Str", "Res"])
        return v_atk, v_def, has_penetration

    h_atk, h_def, h_pen = parse_final(h_id, "h")
    a_atk, a_def, a_pen = parse_final(a_id, "a")

    # --- ميزان القوى الماستر ---
    # 1. أهداف المضيف (حساب الفجوة)
    gap_h = h_atk - a_def
    if gap_h >= 30: h_mu = 3.2    # فارق ضخم -> 3 أهداف
    elif gap_h >= 12: h_mu = 2.2  # فارق متوسط -> 2 أهداف
    else: h_mu = 1.2             # مباراة مغلقة -> 1 هدف

    # 2. أهداف الضيف (منطق الهدف المباغت)
    # الخلل السابق كان هنا؛ قمنا الآن بزيادة فرصة الهدف إذا وجد رمز kM
    gap_a = a_atk - h_def
    a_mu = (a_atk / h_def) * 1.2
    
    if a_pen and gap_a > -55: 
        a_mu = max(a_mu, 0.95) # إجبار المحرك على توقع هدف للضيف (3-1/2-1)
    else:
        a_mu = 0.15 # إبقاء الشباك نظيفة (3-0/1-0)

    # حساب مصفوفة الاحتمالات
    results = []
    for h in range(6):
        for a in range(6):
            p = poisson_calc(h, h_mu) * poisson_calc(a, a_mu)
            results.append({'s': f"{h}-{a}", 'p': p, 'h': h, 'a': a})
    
    results.sort(key=lambda x: x['p'], reverse=True)
    final = results[0]

    # عرض النتيجة بأسلوبك المعتاد
    st.markdown(f"""
    <div style="background-color: #ffffff; padding: 40px; border: 10px solid #1e1e1e; border-radius: 20px; text-align: center; color: #1e1e1e;">
        <h2 style="color: #666; font-weight: bold;">التحليل الرمزي للمواجهة</h2>
        <div style="display: flex; justify-content: space-around; align-items: center; margin: 30px 0;">
            <h1 style="font-size: 55px;">{h_name}</h1>
            <div style="background: #1e1e1e; color: #f1c40f; padding: 20px 45px; border-radius: 12px; font-size: 80px; font-weight: bold;">
                {final['s']}
            </div>
            <h1 style="font-size: 55px;">{a_name}</h1>
        </div>
        <p style="color: #2ecc71; font-weight: bold;">✅ تم التحليل بناءً على فجوة تهديفية {gap_h} نقطة ومعامل اختراق مفعل</p>
    </div>
    """, unsafe_allow_html=True)
    
