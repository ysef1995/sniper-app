import streamlit as st
import math
import time

st.set_page_config(page_title="SNIPER V117.0 - ULTIMATE", layout="wide")

def poisson_calc(k, lmbda):
    if lmbda <= 0: lmbda = 0.01
    return (lmbda**k * math.exp(-lmbda)) / math.factorial(k)

st.title("⚖️ محرك المواجهة والطباعة (Clash Logic)")

# --- 1. إدخال الأسماء والرموز (تحليل فردي) ---
col_h, col_a = st.columns(2)
with col_h:
    h_name = st.text_input("🏠 الفريق المضيف (مثلاً تونس):", "Nigeria")
    h_id = st.text_input("🆔 رموز المضيف (مثل Dom88_Def90):", "NG-Dom88_Def90")
with col_a:
    a_name = st.text_input("✈️ الفريق الضيف (مثلاً أوغندا):", "Tanzania")
    a_id = st.text_input("🆔 رموز الضيف (مثل Spd70_Res40):", "TZ-Spd70_Res40")

# --- 2. محرك فك التشفير والمقارنة المتقاطعة ---
if st.button("🚀 تحليل التصادم والطباعة النهائية"):
    with st.spinner("⏳ جاري موازنة الهجوم ضد الدفاع..."):
        time.sleep(1.5)

    def get_val(id_text, key):
        try:
            part = [p for p in id_text.split('_') if key in p][0]
            return int(''.join(filter(str.isdigit, part)))
        except: return 50

    # تفكيك رموز المضيف والضيف
    h_atk = get_val(h_id, "Dom") or get_val(h_id, "Pwr")
    h_def = get_val(h_id, "Def")
    a_atk = get_val(a_id, "Spd") or get_val(a_id, "Pwr")
    a_def = get_val(a_id, "Res") or get_val(a_id, "Def")

    # --- منطق التصادم المباشر (The Clash Logic) ---
    # أهداف المضيف = هجوم المضيف ÷ دفاع الضيف
    h_mu = (h_atk / 30) * (1 - (a_def / 150))
    # أهداف الضيف = هجوم الضيف ÷ دفاع المضيف (لمنع خطأ الـ 2-1 والـ 2-0)
    a_mu = (a_atk / 40) * (1 - (h_def / 130))

    # مصفوفة النتائج من 0-0 إلى 5-5
    outcomes = []
    for h in range(6):
        for a in range(6):
            p = poisson_calc(h, h_mu) * poisson_calc(a, a_mu)
            outcomes.append({'score': f"{h}-{a}", 'prob': p, 'h': h, 'a': a})
    
    outcomes.sort(key=lambda x: x['prob'], reverse=True)
    final = outcomes[0]

    # --- 3. تصميم الطباعة (الهوية البصرية لصورك) ---
    st.markdown(f"""
    <div style="background-color: #ffffff; padding: 40px; border: 12px solid #1e1e1e; border-radius: 20px; text-align: center; color: #1e1e1e;">
        <h2 style="color: #666;">التحليل الرمزي للمواجهة</h2>
        <div style="display: flex; justify-content: space-around; align-items: center; margin-top: 30px;">
            <h1 style="font-size: 50px;">{h_name}</h1>
            <div style="background: #1e1e1e; color: #f1c40f; padding: 20px 40px; border-radius: 15px; font-size: 80px; font-weight: bold;">
                {final['score']}
            </div>
            <h1 style="font-size: 50px;">{a_name}</h1>
        </div>
        <div style="background: #f4f4f4; margin-top: 30px; padding: 15px; border-radius: 10px;">
            <p style="font-size: 20px;">🛡️ دفاع المضيف: {h_def} مقابل ⚔️ هجوم الضيف: {a_atk}</p>
            <p style="color: #2ecc71; font-weight: bold;">✅ تم تحليل {final['score']} بناءً على تفوق هجومي بنسبة {int(h_mu*20)}%</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # --- 4. ملخص الأسواق المعتمد ---
    st.markdown("---")
    st.subheader("📋 ملخص الأسواق المعتمد للطباعة:")
    c1, c2, c3 = st.columns(3)
    c1.info(f"🏆 الفوز: {'1' if final['h'] > final['a'] else ('2' if final['a'] > final['h'] else 'X')}")
    c2.warning(f"📈 الأهداف: {'OVER 2.5' if (final['h']+final['a']) >= 2.5 else 'UNDER 2.5'}")
    c3.success(f"⚽ BTTS: {'YES' if final['a'] > 0 else 'NO'}")
    
