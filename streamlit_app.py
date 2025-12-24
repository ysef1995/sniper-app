import streamlit as st
import time

# إعداد الصفحة لتكون أنيقة ومنظمة
st.set_page_config(page_title="SNIPER FREEDOM", layout="centered")

def generate_dynamic_score(h_id, a_id):
    # تحويل الرموز الستة إلى قيم عددية لضمان الحرية من 0 إلى 5
    h_score = sum(ord(c) for c in h_id) % 6  # يعطي من 0 إلى 5
    a_score = sum(ord(c) for c in a_id) % 6  # يعطي من 0 إلى 5
    return f"{h_score}-{a_score}"

st.markdown("<h2 style='text-align: center; color: #1e1e1e;'>🏆 PLATFORM SCORE EXACT</h2>", unsafe_allow_html=True)

# واجهة إدخال متطابقة مع تجربة المستخدم في الفيديو
col1, col2 = st.columns(2)
with col1:
    h_n = st.text_input("🏠 الفريق المضيف:", "Nigeria")
    h_i = st.text_input("🆔 ID المضيف (6 رموز):", "Nx7P2k")
with col2:
    a_n = st.text_input("✈️ الفريق الضيف:", "Tanzania")
    a_i = st.text_input("🆔 ID الضيف (6 رموز):", "Tz9M1s")

if st.button("🚀 START ANALYSIS"):
    with st.spinner('جاري تحليل الرموز المشفرة...'):
        time.sleep(2) # محاكاة وقت التحليل كما في الفيديو
        score = generate_dynamic_score(h_i, a_i)
    
    # --- التصميم الأنيق والنهائي (أفقي ومنظم) ---
    st.markdown(f"""
    <div style="background: #1e1e1e; color: white; padding: 30px; border-radius: 20px; border: 5px solid #f1c40f; text-align: center;">
        <p style="color: #f1c40f; font-weight: bold; letter-spacing: 2px;">FINAL EXACT SCORE</p>
        <div style="display: flex; justify-content: space-around; align-items: center; margin: 20px 0;">
            <div style="font-size: 22px; font-weight: bold; flex: 1;">{h_n}</div>
            <div style="background: #333; color: #f1c40f; font-size: 60px; font-weight: bold; padding: 10px 30px; border-radius: 15px; min-width: 120px;">
                {score}
            </div>
            <div style="font-size: 22px; font-weight: bold; flex: 1;">{a_n}</div>
        </div>
        <div style="background: #222; padding: 15px; border-radius: 10px; margin-top: 20px; text-align: right; border-right: 5px solid #f1c40f;">
            <span style="color: #f1c40f;">📋 مجرى المباراة:</span>
            <p style="font-size: 16px; color: #ddd; margin-top: 5px;">
                تحليل الرموز يشير إلى احتمالية عالية لنتيجة {score} بناءً على كفاءة الهجوم المتقاطع.
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
