import streamlit as st
import time
import base64
import random

# --- إعدادات التصميم (Hacker Style) ---
st.set_page_config(page_title="SNIPER TEAM INJECTOR", page_icon="💀", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #000; }
    .main-header { color: #00FF00; font-family: 'Courier New', monospace; text-align: center; text-shadow: 0 0 10px #00FF00; margin-bottom: 20px; }
    .stTextInput>div>div>input { background-color: #0a0a0a; color: #00FF00; border: 1px solid #00FF00; text-align: center; font-family: monospace; }
    .stButton>button { width: 100%; background-color: transparent; color: #00FF00; font-weight: bold; border: 2px solid #00FF00; height: 50px; font-size: 18px; transition: 0.3s; }
    .stButton>button:hover { background-color: #00FF00; color: black; box-shadow: 0 0 20px #00FF00; }
    .result-box { border: 2px dashed #00FF00; padding: 20px; margin-top: 20px; background: #050505; text-align: center; }
    .team-vs { color: white; font-size: 20px; font-weight: bold; margin-bottom: 10px; }
    .score-final { font-size: 80px; color: #00FF00; font-family: 'Impact', sans-serif; text-shadow: 0 0 20px #00FF00; }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<h1 class="main-header">💉 TEAM ID INJECTOR V4.0</h1>', unsafe_allow_html=True)

# --- دالة فك التشفير ---
def decode_team_data(encoded_id):
    try:
        # يفك التشفير ويتوقع النص بالشكل: "Name:Power"
        decoded_bytes = base64.b64decode(encoded_id)
        decoded_str = decoded_bytes.decode('utf-8')
        name, power = decoded_str.split(':')
        return name, int(power)
    except:
        return None, None

# --- الواجهة ---
col1, col2 = st.columns(2)
with col1:
    id_home = st.text_input("HOME TEAM ID:", placeholder="Paste ID 1")
with col2:
    id_away = st.text_input("AWAY TEAM ID:", placeholder="Paste ID 2")

if st.button("INJECT & ANALYZE"):
    if id_home and id_away:
        # فك تشفير البيانات
        name1, power1 = decode_team_data(id_home)
        name2, power2 = decode_team_data(id_away)

        if name1 and name2:
            # محاكاة العملية (Animation)
            with st.status("SYSTEM PROCESS...", expanded=True) as status:
                st.write(f"🔓 Decrypting ID 1: {name1} detected...")
                time.sleep(0.8)
                st.write(f"🔓 Decrypting ID 2: {name2} detected...")
                time.sleep(0.8)
                st.write("⚔️ Calculating Attack/Defense Vectors...")
                time.sleep(1)
                status.update(label="INJECTION SUCCESSFUL", state="complete")

            # خوارزمية النتيجة بناءً على "القوة" الموجودة في الـ ID
            # القوة هي رقم من 0 إلى 5 يحدد كم هدفاً سيسجل الفريق تقريباً
            score1 = power1
            score2 = power2
            
            # إضافة تغيير طفيف لعدم جعل النتيجة ثابتة جداً (اختياري)
            # score1 = max(0, power1 + random.choice([-1, 0, 1])) 

            st.markdown(f"""
                <div class="result-box">
                    <div class="team-vs">{name1} <span style="color:#00FF00">VS</span> {name2}</div>
                    <div style="color: #888; font-size: 12px;">SCRIPT OUTPUT: EXACT SCORE</div>
                    <div class="score-final">{score1} - {score2}</div>
                    <div style="margin-top: 10px; color: #00FF00;">CONFIDENCE: 99.9%</div>
                </div>
            """, unsafe_allow_html=True)
            st.balloons()
        else:
            st.error("❌ ERROR: Corrupted IDs! Check input.")
    else:
        st.warning("⚠️ WAITING FOR DATA INJECTION...")
        
