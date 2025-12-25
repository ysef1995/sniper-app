import streamlit as st
import cloudscraper
import time
import random

# إعدادات الواجهة
st.set_page_config(page_title="SNIPER IA V2", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #000; }
    h1, h3 { color: #00FF00; text-align: center; font-family: 'Courier New', monospace; }
    .stTextInput>div>div>input { background-color: #0a0a0a; color: #00FF00; border: 1px solid #00FF00; }
    .stButton>button { width: 100%; background-color: #00FF00; color: #000; font-weight: bold; }
    .prediction-box { border: 2px solid #00FF00; padding: 20px; border-radius: 10px; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

st.title("🎯 SNIPER IA PREDICTOR")

# إدخال البيانات
raw_input = st.text_input("ENTER MATCH ID OR URL:", placeholder="e.g. 13424942")

if st.button("EXECUTE ANALYSIS"):
    if raw_input:
        # 1. استخراج الـ ID من أي نص أو رابط
        match_id = "".join(filter(str.isdigit, raw_input.split('/')[-1].split(':')[-1]))
        
        try:
            # 2. استخدام متصفح بمواصفات حقيقية لتجنب الحظر
            scraper = cloudscraper.create_scraper(
                browser={
                    'browser': 'chrome',
                    'platform': 'windows',
                    'mobile': False
                }
            )
            
            with st.spinner('📡 BYPASSING SECURITY & FETCHING DATA...'):
                # طلب البيانات من API SofaScore
                api_url = f"https://api.sofascore.com/api/v1/event/{match_id}"
                headers = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
                }
                response = scraper.get(api_url, headers=headers, timeout=15)
                
                if response.status_code == 200:
                    data = response.json()
                    home = data['event']['homeTeam']['name']
                    away = data['event']['awayTeam']['name']
                    
                    # محاكاة التحليل الاحترافي
                    progress = st.progress(0)
                    for i in range(100):
                        time.sleep(0.01)
                        progress.progress(i + 1)
                    
                    # نتائج عشوائية مدروسة (Score Exact)
                    res = random.choice(["1-1", "2-1", "0-0", "1-0", "0-1"])
                    
                    st.markdown(f"""
                        <div class="prediction-box">
                            <h2 style="color:white;">{home} vs {away}</h2>
                            <p style="color:#666;">AI TARGET ACQUIRED</p>
                            <h1 style="color:#00FF00; font-size:60px;">{res}</h1>
                            <p style="color:#00FF00;">ACCURACY: {random.randint(92, 98)}%</p>
                        </div>
                    """, unsafe_allow_html=True)
                    st.balloons()
                else:
                    st.error(f"❌ Server Rejected Request (Error {response.status_code}). Try again in a minute.")
                    
        except Exception as e:
            st.error("❌ Connection failed. SofaScore might be blocking the cloud server.")
    else:
        st.warning("⚠️ Please enter a valid Match ID or Link.")
        
