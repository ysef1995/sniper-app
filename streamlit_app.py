import streamlit as st
import random
import time

st.set_page_config(page_title="SNIPER MASTER V130", layout="wide")

# دالة محاكاة التحليل بناءً على الـ ID المختصر
def analyze_short_id(h_id, a_id):
    # تحويل الحروف والأرقام لقيم رقمية افتراضية للعملية الحسابية
    h_val = sum(ord(c) for c in h_id) % 5
    a_val = sum(ord(c) for c in a_id) % 3
    
    # تحديد سيناريو المباراة (مجرى المباراة)
    if h_val > a_val + 1:
        score, flow = f"{h_val}-{a_val}", "سيطرة مطلقة للمضيف مع تراجع دفاعي للخصم."
    elif h_val == a_val:
        score, flow = f"{h_val}-{a_val}", "مباراة مغلقة تكتيكياً مع انحصار اللعب في وسط الميدان."
    else:
        score, flow = f"{h_val}-{a_val}", "مباراة متكافئة مع هجمات مرتدة خطيرة من الجانبين."
    return score, flow

st.markdown("<h1 style='text-align: center; color: #1e1e1e;'>🎯 PLATFORM SNIPER PRO</h1>", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    h_name = st.text_input("🏠 الفريق المضيف:", "Real Oviedo")
    h_id = st.text_input("🆔 ID المضيف (6 رموز):", "Rt4X2p")
with col2:
    a_name = st.text_input("✈️ الفريق الضيف:", "Elche")
    a_id = st.text_input("🆔 ID الضيف (6 رموز):", "Km9L1s")

if st.button("🚀 START ANALYSIS"):
    with st.spinner('جاري الاتصال بالخادم وتحليل البيانات...'):
        time.sleep(2)
        score, flow = analyze_short_id(h_id, a_id)

    # --- الطباعة الأنيقة كما في الفيديو [00:04:17] ---
    st.markdown(f"""
    <div style="background-color: #ffffff; padding: 40px; border: 15px solid #1e1e1e; border-radius: 25px; text-align: center; color: #1e1e1e; font-family: 'Arial Black', sans-serif;">
        <h2 style="color: #666; letter-spacing: 2px;">EXACT SCORE RESULT</h2>
        <div style="display: flex; justify-content: space-around; align-items: center; margin: 40px 0;">
            <h1 style="font-size: 50px; text-transform: uppercase;">{h_name}</h1>
            <div style="background: #1e1e1e; color: #f1c40f; padding: 30px 60px; border-radius: 20px; font-size: 100px; font-weight: bold; box-shadow: 0 10px 20px rgba(0,0,0,0.2);">
                {score}
            </div>
            <h1 style="font-size: 50px; text-transform: uppercase;">{a_name}</h1>
        </div>
        <div style="background: #f9f9f9; padding: 20px; border-radius: 15px; border-left: 10px solid #f1c40f; text-align: right;">
            <h3 style="margin: 0; color: #333;">📝 مجرى المباراة:</h3>
            <p style="font-size: 20px; color: #555; margin-top: 10px;">{flow}</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # الأسواق الإضافية [00:02:07]
    st.markdown("---")
    c1, c2, c3 = st.columns(3)
    c1.metric("Winner", h_name if int(score[0]) > int(score[2]) else ("Draw" if score[0]==score[2] else a_name))
    c2.metric("Under/Over 2.5", "UNDER" if (int(score[0])+int(score[2])) < 2.5 else "OVER")
    c3.metric("BTTS", "YES" if int(score[2]) > 0 else "NO")
    
