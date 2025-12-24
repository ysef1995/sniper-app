import streamlit as st
import time

st.set_page_config(page_title="SNIPER AI ANALYST", layout="centered")

def auto_ai_prediction(h_id, a_id):
    # تحليل "بصمة القوة" (الحروف الكبيرة تزيد الهجوم، الصغيرة تزيد الدفاع)
    h_atk = sum(2 for c in h_id if c.isupper()) + sum(1 for c in h_id if c.isdigit())
    a_def = sum(1.5 for c in a_id if c.islower())
    
    # حساب الفارق الفني آلياً
    diff = h_atk - a_def
    
    if diff > 8: # حالة اكتساح (3-0 أو 3-1)
        return (3, 1 if "k" in a_id.lower() else 0)
    elif diff > 4: # حالة ندية (2-1 أو 2-0)
        return (2, 1 if "m" in a_id.lower() else 0)
    else: # حالة مباراة مغلقة (1-0 أو 0-0)
        return (1 if diff > 0 else 0, 0)

st.markdown("<h2 style='text-align: center; color: #f1c40f;'>🧠 AI SCORE PREDICTOR</h2>", unsafe_allow_html=True)

# واجهة المستخدم كما في الفيديو
col1, col2 = st.columns(2)
with col1:
    h_n = st.text_input("🏠 المضيف:", "Senegal")
    h_i = st.text_input("🆔 ID المضيف:", "SN82Xp")
with col2:
    a_n = st.text_input("✈️ الضيف:", "Botswana")
    a_i = st.text_input("🆔 ID الضيف:", "bt45mz")

if st.button("🚀 ANALYZE & PREDICT"):
    with st.spinner('جاري تحليل موازين القوى...'):
        time.sleep(2)
        h_s, a_s = auto_ai_prediction(h_i, a_i)
    
    st.markdown(f"""
    <div style="background: #1e1e1e; color: white; padding: 25px; border-radius: 20px; border: 4px solid #f1c40f; text-align: center;">
        <div style="display: flex; justify-content: space-around; align-items: center;">
            <div style="font-size: 20px; font-weight: bold;">{h_n}</div>
            <div style="background: #333; color: #f1c40f; font-size: 55px; font-weight: bold; padding: 10px 30px; border-radius: 15px;">
                {h_s}-{a_s}
            </div>
            <div style="font-size: 20px; font-weight: bold;">{a_n}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
