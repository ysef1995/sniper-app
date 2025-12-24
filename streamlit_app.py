import streamlit as st
import math
import time

st.set_page_config(page_title="SNIPER V116.0 - CLASH MATRIX", layout="wide")

def poisson_calc(k, lmbda):
    if lmbda <= 0: lmbda = 0.01
    return (lmbda**k * math.exp(-lmbda)) / math.factorial(k)

st.title("⚔️ محرك التصادم الرمزي (Clash Matrix Analyzer)")

# --- 1. إدخال البيانات (الأسماء والرموز التفصيلية) ---
col_h, col_a = st.columns(2)
with col_h:
    h_name = st.text_input("🏠 اسم فريق المضيف:", "المنتخب الأول")
    h_id = st.text_input("🆔 رموز المضيف (مثل Dom88_Def90):", "Dom85_Def75")
with col_a:
    a_name = st.text_input("✈️ اسم فريق الضيف:", "المنتخب الثاني")
    a_id = st.text_input("🆔 رموز الضيف (مثل Spd70_Res40):", "Spd80_Res60")

# --- 2. محرك التفكيك والمقارنة التصادمية ---
if st.button("🚀 إجراء تحليل التصادم والطباعة"):
    with st.spinner("⏳ جاري مقارنة الهجوم بالدفاع لكل طرف..."):
        time.sleep(1.5)

    # دالة استخراج الأرقام من الرموز
    def get_val(id_text, key, default=50):
        try:
            part = [p for p in id_text.split('_') if key in p][0]
            return int(''.join(filter(str.isdigit, part)))
        except: return default

    # تفكيك رموز المضيف
    h_atk = get_val(h_id, "Dom") or get_val(h_id, "Pwr") or 50
    h_def = get_val(h_id, "Def") or 50
    
    # تفكيك رموز الضيف
    a_atk = get_val(a_id, "Spd") or get_val(a_id, "Pwr") or 40
    a_def = get_val(a_id, "Res") or get_val(a_id, "Def") or 40

    # --- ميزان التصادم (The Clash Logic) ---
    # 1. قوة هجوم المضيف المتبقية بعد اصطدامها بدفاع الضيف
    # إذا كان a_def (دفاع الضيف) قوي، ستقل أهداف المضيف
    h_effective_mu = (h_atk / 35) * (1 - (a_def / 200)) 
    
    # 2. قوة هجوم الضيف المتبقية بعد اصطدامها بدفاع المضيف
    # إذا كان h_def (دفاع المضيف) صلب، ستقل أهداف الضيف (هنا يتقرر الـ 2-1 أو 2-0)
    a_effective_mu = (a_atk / 45) * (1 - (h_def / 180))

    # حساب مصفوفة الاحتمالات من 0-0 إلى 5-5
    outcomes = []
    for h in range(6): # من 0 إلى 5
        for a in range(6): # من 0 إلى 5
            prob = poisson_calc(h, h_effective_mu) * poisson_calc(a, a_effective_mu)
            outcomes.append({'score': f"{h}-{a}", 'prob': prob, 'h': h, 'a': a})
    
    # ترتيب النتائج لاختيار الأكثر دقة
    outcomes.sort(key=lambda x: x['prob'], reverse=True)
    final = outcomes[0]

    # --- 3. تصميم الطباعة الاحترافي ---
    st.markdown("---")
    st.markdown(f"""
    <div style="background-color: #ffffff; padding: 35px; border: 8px solid #1e1e1e; border-radius: 20px; text-align: center; color: #1e1e1e;">
        <h3 style="color: #666; margin-bottom: 0;">التحليل الرمزي للمواجهة</h3>
        <h1 style="font-size: 45px; margin-top: 10px;">
            {h_name} <span style="background: #1e1e1e; color: #f1c40f; padding: 10px 30px; border-radius: 10px; margin: 0 15px;">{final['score']}</span> {a_name}
        </h1>
        <div style="display: flex; justify-content: center; gap: 20px; margin-top: 20px;">
            <div style="background: #f0f2f6; padding: 10px 20px; border-radius: 10px;">
                <b>🛡️ دفاع المضيف:</b> {h_def} مقابل <b>⚔️ هجوم الضيف:</b> {a_atk}
            </div>
        </div>
        <p style="color: #2ecc71; font-weight: bold; margin-top: 15px;">✅ تم تحليل {final['score']} بناءً على تفوق هجومي بنسبة {int(h_effective_mu*25)}%</p>
    </div>
    """, unsafe_allow_html=True)

    # --- 4. ملخص الأسواق المعتمد ---
    st.markdown("---")
    st.subheader("📋 ملخص الأسواق المعتمد للطباعة:")
    c1, c2, c3 = st.columns(3)
    c1.info(f"🏆 التوقع الرئيسي: {'فوز المضيف' if final['h'] > final['a'] else ('فوز الضيف' if final['a'] > final['h'] else 'تعادل')}")
    c2.warning(f"📈 إجمالي الأهداف: {'OVER 2.5' if (final['h']+final['a']) >= 2.5 else 'UNDER 2.5'}")
    c3.success(f"⚽ BTTS: {'YES' if final['a'] > 0 else 'NO'}")
