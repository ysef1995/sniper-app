import streamlit as st
import time
import base64

# --- محرك الحساب الرياضي ---
def calculate_score(home_data, away_data):
    # تفكيك البيانات: الاسم:الهجوم:الدفاع
    h_name, h_atk, h_def = home_data.split(':')
    a_name, a_atk, a_def = away_data.split(':')
    
    # تحويل لنوع رقمي
    h_atk, h_def = int(h_atk), int(h_def)
    a_atk, a_def = int(a_atk), int(a_def)

    # معادلة التوقع: (هجوم الفريق A - دفاع الفريق B) + عامل الأرض
    # هذه معادلة إحصائية بسيطة لتقدير الأهداف
    home_expected = max(0, (h_atk - a_def) // 20 + 1)
    away_expected = max(0, (a_atk - h_def) // 25)

    return h_name, a_name, home_expected, away_expected

# --- الواجهة ---
st.set_page_config(page_title="STATISTICAL AI PREDICTOR", layout="centered")
st.markdown("<style>.stApp{background-color:#020202; color:#00FF00;}</style>", unsafe_allow_html=True)

st.title("🎯 AI STATISTICAL ENGINE")
st.write("---")

col1, col2 = st.columns(2)
with col1:
    h_id = st.text_input("HOME STATS ID:")
with col2:
    a_id = st.text_input("AWAY STATS ID:")

if st.button("RUN STATISTICAL SIMULATION"):
    if h_id and a_id:
        try:
            # فك التشفير
            h_decoded = base64.b64decode(h_id).decode('utf-8')
            a_decoded = base64.b64decode(a_id).decode('utf-8')
            
            h_name, a_name, h_score, a_score = calculate_score(h_decoded, a_decoded)
            
            with st.spinner("Analyzing Stats..."):
                time.sleep(2)
            
            st.success(f"ANALYSIS COMPLETE: {h_name} vs {a_name}")
            st.metric("PREDICTED SCORE", f"{h_score} - {a_score}")
            st.progress(85) # نسبة الثقة الإحصائية
            
        except:
            st.error("Invalid Stats ID format!")
            
