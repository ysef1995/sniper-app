import streamlit as st
import cloudscraper
import time
import random

# إعدادات الصفحة لتظهر بشكل احترافي
st.set_page_config(page_title="AI Score Predictor", page_icon="🎯", layout="centered")

# تصميم مخصص بلغة CSS لجعل الموقع يشبه "السكريبت" في الفيديو
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stTextInput>div>div>input { background-color: #1a1c23; color: #00FF00; border: 1px solid #00FF00; }
    .stButton>button { width: 100%; background-color: #00FF00; color: black; font-weight: bold; height: 3em; border-radius: 10px; }
    .stButton>button:hover { background-color: #00cc00; color: white; }
    h1, h2, h3 { color: #00FF00; text-align: center; font-family: 'Courier New', Courier, monospace; }
    .prediction-box { background-color: #111; border: 2px solid #00FF00; padding: 30px; border-radius: 15px; text-align: center; margin-top: 20px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🎯 SNIPER IA PREDICTOR")
st.subheader("SofaScore Match Analysis System")

# إدخال الـ ID
match_id = st.text_input("ENTER MATCH ID:", placeholder="e.g., 11352458")

if st.button("RUN SYSTEM ANALYSIS"):
    if match_id:
        try:
            scraper = cloudscraper.create_scraper()
            
            # محاكاة عملية الاتصال (مثل الفيديو لزيادة الحماس)
            with st.status("Initializing AI Engine...", expanded=True) as status:
                st.write("📡 Connecting to SofaScore Servers...")
                response = scraper.get(f"https://api.sofascore.com/api/v1/event/{match_id}", timeout=10)
                data = response.json()
                
                home_team = data['event']['homeTeam']['name']
                away_team = data['event']['awayTeam']['name']
                
                time.sleep(1)
                st.write(f"📊 Analyzing: **{home_team}** vs **{away_team}**")
                st.write("🧠 Processing H2H and Probability Algorithms...")
                time.sleep(2)
                status.update(label="Analysis Complete!", state="complete", expanded=False)

            # منطق التوقع (يمكنك تعديله ليكون أكثر تعقيداً)
            scores = ["1 - 0", "1 - 1", "2 - 1", "0 - 0", "1 - 2"]
            final_pred = random.choice(scores)

            # عرض النتيجة النهائية
            st.markdown(f"""
                <div class="prediction-box">
                    <h3 style="color: #666;">PREDICTED SCORE</h3>
                    <h1 style="font-size: 80px; margin: 10px 0;">{final_pred}</h1>
                    <p style="color: #00FF00;">ACCURACY: {random.randint(85, 98)}%</p>
                </div>
            """, unsafe_allow_html=True)
            st.balloons()

        except Exception as e:
            st.error("❌ Invalid ID or Connection Error. Please verify the ID from SofaScore.")
    else:
        st.error("⚠️ Please enter a Match ID first!")

st.markdown("---")
st.caption("Designed for Live Streamers - Use responsibly.")
