import streamlit as st
import cloudscraper
import time
import random
import re

# إعدادات الصفحة
st.set_page_config(page_title="SNIPER IA", page_icon="🎯", layout="centered")

# تصميم الواجهة
st.markdown("""
    <style>
    .stApp { background-color: #050505; }
    h1, h3 { color: #00FF00 !important; font-family: 'Courier New', monospace; text-shadow: 0 0 10px #00FF00; text-align: center; }
    .stTextInput>div>div>input { background-color: #000 !color: #00FF00; border: 1px solid #00FF00; }
    .stButton>button { width: 100%; background-color: #00FF00; color: #000; font-weight: bold; }
    .prediction-card { border: 2px solid #00FF00; padding: 20px; border-radius: 10px; background-color: #000; text-align: center; }
    .score-text { font-size: 70px; color: #00FF00; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.title("🎯 SNIPER IA PREDICTOR")
st.markdown("<h3>SYSTEM STATUS: ONLINE</h3>", unsafe_allow_html=True)

# خانة الإدخال (تقبل الرابط أو الرقم)
input_data = st.text_input("ENTER MATCH ID OR SOFASCORE URL:", "")

def extract_id(text):
    # دالة لاستخراج الـ ID من الرابط تلقائياً
    if "sofascore.com" in text:
        parts = text.split('/')
        return parts[-1] if parts[-1] else parts[-2]
    return text

if st.button("EXECUTE ANALYSIS"):
    if input_data:
        m_id = extract_id(input_data)
        try:
            scraper = cloudscraper.create_scraper()
            with st.spinner('📡 CONNECTING TO SERVER...'):
                url = f"https://api.sofascore.com/api/v1/event/{m_id}"
                response = scraper.get(url, timeout=10)
                
                if response.status_code != 200:
                    st.error("❌ Match Not Found! Double check the ID.")
                else:
                    data = response.json()
                    home = data['event']['homeTeam']['name']
                    away = data['event']['awayTeam']['name']
                    
                    # محاكاة التحليل
                    bar = st.progress(0)
                    for i in range(100):
                        time.sleep(0.02)
                        bar.progress(i + 1)
                    
                    # منطق التوقع (محاكاة IA)
                    scores = ["1-1", "2-1", "1-0", "0-0", "1-2", "2-0"]
                    prediction = random.choice(scores)
                    
                    st.markdown(f"""
                        <div class="prediction-card">
                            <p style="color: #666;">ANALYSIS COMPLETE: {home} vs {away}</p>
                            <div class="score-text">{prediction}</div>
                            <p style="color: #00FF00;">PROBABILITY: {random.randint(91, 98)}%</p>
                        </div>
                    """, unsafe_allow_html=True)
                    st.balloons()
        except Exception as e:
            st.error("❌ Connection Timeout. Try again.")
    else:
        st.warning("⚠️ PLEASE ENTER DATA FIRST")
        
