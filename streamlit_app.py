import streamlit as st
import cloudscraper
import time
import random

# إعدادات الصفحة
st.set_page_config(page_title="SNIPER IA", page_icon="🎯", layout="centered")

# تصميم الواجهة لتشبه سكريبتات الفيديوهات
st.markdown("""
    <style>
    .stApp { background-color: #050505; }
    h1, h3 { color: #00FF00 !important; font-family: 'Courier New', monospace; text-shadow: 0 0 10px #00FF00; text-align: center; }
    .stTextInput>div>div>input { background-color: #000; color: #00FF00; border: 1px solid #00FF00; font-family: 'Courier New', monospace; }
    .stButton>button { width: 100%; background-color: #00FF00; color: #000; font-weight: bold; border: none; border-radius: 5px; height: 3em; }
    .stButton>button:hover { background-color: #008000; color: white; }
    .prediction-card { border: 2px solid #00FF00; padding: 20px; border-radius: 10px; background-color: #000; text-align: center; }
    .score-text { font-size: 70px; color: #00FF00; font-weight: bold; margin: 10px 0; }
    </style>
    """, unsafe_allow_html=True)

st.title("🎯 SNIPER IA PREDICTOR")
st.markdown("<h3>SYSTEM STATUS: ONLINE</h3>", unsafe_allow_html=True)

# المدخلات
m_id = st.text_input("ENTER MATCH ID (SOFASCORE):", "")

if st.button("EXECUTE ANALYSIS"):
    if m_id:
        try:
            scraper = cloudscraper.create_scraper()
            
            with st.spinner('🔄 ACCESSING DATABASE...'):
                # جلب البيانات من API سوفاسكور مباشرة
                url = f"https://api.sofascore.com/api/v1/event/{m_id}"
                response = scraper.get(url, timeout=10)
                data = response.json()
                
                home = data['event']['homeTeam']['name']
                away = data['event']['awayTeam']['name']
                
                # محاكاة "التحميل" لزيادة الحماس في البث
                progress_text = st.empty()
                for percent in range(0, 101, 20):
                    progress_text.text(f"📡 ANALYZING {home} VS {away}... {percent}%")
                    time.sleep(0.5)
                
            # منطق التوقع (محاكاة ذكاء اصطناعي)
            scores = ["1-1", "2-1", "1-0", "0-0", "1-2"]
            prediction = random.choice(scores)
            
            # عرض النتيجة بشكل احترافي
            st.markdown(f"""
                <div class="prediction-card">
                    <p style="color: #666;">PROBABLE SCORE EXACT</p>
                    <div class="score-text">{prediction}</div>
                    <p style="color: #00FF00;">ACCURACY: {random.randint(89, 97)}%</p>
                    <p style="color: #444;">ID: {m_id}</p>
                </div>
            """, unsafe_allow_html=True)
            st.balloons()
            
        except Exception as e:
            st.error(f"❌ ERROR: Invalid Match ID or Connection Timeout.")
    else:
        st.warning("⚠️ ACCESS DENIED: PLEASE ENTER MATCH ID")

st.markdown("<br><p style='text-align: center; color: #333;'>STREAMER VERSION V1.0</p>", unsafe_allow_html=True)
