import streamlit as st
import math
import time

# إعداد الصفحة لتناسب تصميمك
st.set_page_config(page_title="SNIPER V119.0 - PRO", layout="wide")

def poisson_calc(k, lmbda):
    if lmbda <= 0: lmbda = 0.01
    return (lmbda**k * math.exp(-lmbda)) / math.factorial(k)

st.title("🎯 المحلل الرمزي المتقاطع (Cross-Clash Analyzer)")

# --- 1. إدخال البيانات (الأسماء والرموز) ---
col_h, col_a = st.columns(2)
with col_h:
    h_name = st.text_input("🏠 الفريق المضيف:", "Nigeria")
    h_id = st.text_input("🆔 رموز المضيف:", "NG-Dom88_Def90")
with col_a:
    a_name = st.text_input("✈️ الفريق الضيف:", "Tanzania")
    a_id = st.text_input("🆔 رموز الضيف:", "TZ-Spd75_Res31")

if st.button("🚀 تحليل المواجهة العميقة"):
    # تم تصحيح الخطأ هنا باستبدال الاقتباسات [Syntax Fix]
    with st.spinner('⏳ جاري تحليل صراع الرموز ومنع تصفير النتائج...'):
        time.sleep(1.2)

    def get_val(id_text, key):
        try:
            part = [p for p in id_text.split('_') if key in p][0]
            return int(''.join(filter(str.isdigit, part)))
        except: return 50

    # تفكيك الرموز للمقارنة المتقاطعة
    h_atk = get_val(h_id, "Dom") or get_val(h_id, "Pwr")
    h_def = get_val(h_id, "Def")
    a_atk = get_val(a_id, "Spd") or get_val(a_id, "Pwr")
    a_def = get_val(a_id, "Res") or get_val(a_id, "Def")

    # --- منطق المواجهة الحقيقي (Clash Logic) ---
    # أهداف المضيف: هجومه (h_atk) يتصادم مع دفاع الضيف (a_def)
    h_mu = (h_atk / 35) * (1 - (a_def / 200))
    
    # أهداف الضيف: هجومه (a_atk) يتصادم مع دفاع المضيف (h_def)
    # إضافة معامل اختراق بسيط لضمان واقعية الـ 2-1
    a_mu = (a_atk / 45) * (1 - (h_def / 180)) + 0.45

    # مصفوفة الاحتمالات من 0-0 إلى 5-5
    outcomes = []
    for h in range(6):
        for a in range(6):
            p = poisson_calc(h, h_mu) * poisson_calc(a, a_mu)
            outcomes.append({'score': f"{h}-{a}", 'prob': p, 'h': h, 'a': a})
    
    outcomes.sort(key=lambda x: x['prob'], reverse=True)
    final = outcomes[0]

    # --- تصميم الطباعة الاحترافي ---
    st.markdown(f"""
    <div style="background-color: #ffffff; padding: 40px; border: 10px solid #1e1e1e; border-radius: 20px; text-align: center; color: #1e1e1e;">
        <h2 style="color: #666; font-weight: bold;">التحليل الرمزي للمواجهة</h2>
        <div style="display: flex; justify-content: space-around; align-items: center; margin: 30px 0;">
            <h1 style="font-size: 55px; flex: 1;">{h_name}</h1>
            <div style="background: #1e1e1e; color: #f1c40f; padding: 15px 40px; border-radius: 12px; font-size: 80px; font-weight: bold; flex: 0.6;">
                {final['score']}
            </div>
            <h1 style="font-size: 55px; flex: 1;">{a_name}</h1>
        </div>
        <div style="background: #f8f9fa; padding: 15px; border-radius: 10px; border: 1px solid #ddd;">
            <p style="font-size: 18px; margin: 0;">🛡️ دفاع المضيف ({h_def}) ضد هجوم الضيف ({a_atk})</p>
            <p style="color: #2ecc71; font-weight: bold; margin-top: 5px;">✅ النتيجة المختارة: {final['score']}</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # --- ملخص الأسواق المطبوع ---
    st.markdown("---")
    st.subheader("📋 ملخص الأسواق المعتمد للطباعة:")
    c1, c2, c3 = st.columns(3)
    c1.info(f"🏆 التوقع: {'1' if final['h'] > final['a'] else ('2' if final['a'] > final['h'] else 'X')}")
    c2.warning(f"📈 الأهداف: {'OVER 2.5' if (final['h']+final['a']) >= 2.5 else 'UNDER 2.5'}")
    c3.success(f"⚽ BTTS: {'YES' if final['a'] > 0 else 'NO'}")
    
