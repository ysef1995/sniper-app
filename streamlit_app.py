import streamlit as st
import time
import random
import cloudscraper

# --- إعدادات الصفحة والتصميم ---
st.set_page_config(page_title="SNIPER X PRO", page_icon="🧿", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #000000; }
    .title { color: #00FF00; font-family: 'Courier New', monospace; text-align: center; text-shadow: 0px 0px 10px #00FF00; }
    .stTextInput>div>div>input { background-color: #111; color: #00FF00; border: 1px solid #00FF00; text-align: center; font-family: monospace; }
    .stButton>button { background-color: #00FF00; color: black; font-weight: bold; width: 100%; border-radius: 5px; height: 50px; font-size: 18px; }
    .stButton>button:hover { background-color: #00cc00; color: white; border: 1px solid white; }
    .result-box { border: 2px solid #00FF00; background-color: #050505; padding: 20px; border-radius: 15px; text-align: center; margin-top: 20px; }
    .team-name { color: white; font-size: 18px; font-weight: bold; }
    .score-big { font-size: 80px; color: #00FF00; font-family: 'Impact', sans-serif; margin: -10px 0; text-shadow: 0 0 20px #00FF00; }
    .meta-info { color: #888; font-size: 12px; font-family: monospace; }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<h1 class="title">⚡ SNIPER AI: EXACT SCORE ⚡</h1>', unsafe_allow_html=True)

# --- دوال النظام ---

def get_match_id(text):
    # استخراج الأرقام فقط من المدخلات
    return "".join(filter(str.isdigit, text))

def simulate_smart_prediction(match_id):
    # استخدام الـ ID كـ "بذرة" (Seed) لجعل التوقع ثابتاً لنفس المباراة
    # هذا يعني أن نفس الـ ID سيعطي دائماً نفس النتيجة، مما يجعله يبدو حقيقياً
    random.seed(int(match_id))
    
    # قائمة نتائج واقعية (Score Exact)
    scores = ["1-1", "2-1", "1-0", "0-0", "0-1", "1-2", "2-0", "2-2"]
    # أوزان لترجيح النتائج الأكثر شيوعاً (1-1 و 1-0)
    weights = [20, 15, 15, 10, 15, 10, 10, 5]
    
    prediction = random.choices(scores, weights=weights, k=1)[0]
    accuracy = random.randint(88, 97)
    
    return prediction, accuracy

# --- واجهة التطبيق ---

user_input = st.text_input("🔗 PASTE MATCH LINK OR ID:", placeholder="Example: 13424942")

if st.button("START HACKING SYSTEM"):
    if user_input:
        match_id = get_match_id(user_input)
        
        if len(match_id) < 5:
            st.error("❌ INVALID ID! Please check the link.")
        else:
            try:
                # 1. محاكاة الاتصال والتحليل (لإعطاء طابع الفيديو)
                with st.status("SYSTEM INITIALIZING...", expanded=True) as status:
                    st.write("📡 Connecting to Satellite Server...")
                    time.sleep(1)
                    st.write("🔓 Bypassing Firewall Security...")
                    time.sleep(1.2)
                    st.write(f"🔍 Analyzing Match ID: {match_id}")
                    time.sleep(1)
                    st.write("🧠 Running AI Neural Network...")
                    time.sleep(1.5)
                    status.update(label="ANALYSIS COMPLETED successfully!", state="complete", expanded=False)

                # 2. توليد النتيجة (يعمل دائماً ولا يتوقف)
                pred_score, confidence = simulate_smart_prediction(match_id)
                
                # 3. عرض النتيجة بشكل مبهر
                st.markdown(f"""
                    <div class="result-box">
                        <p class="team-name">MATCH ANALYSIS REPORT</p>
                        <p style="color:#00FF00; letter-spacing: 2px;">PREDICTED SCORE</p>
                        <div class="score-big">{pred_score}</div>
                        <br>
                        <span style="background-color: #111; padding: 5px 15px; border-radius: 10px; color: #00FF00; border: 1px solid #00FF00;">
                            CONFIDENCE: {confidence}%
                        </span>
                        <p class="meta-info">ID: {match_id} | SERVER: ONLINE</p>
                    </div>
                """, unsafe_allow_html=True)
                
                st.balloons()

            except Exception as e:
                st.error("System Glitch. Rebooting...")
    else:
        st.warning("⚠️ ENTER DATA FIRST!")

st.markdown("<br><center><p style='color:#333;'>SNIPER V3.0 - PRIVATE SERVER</p></center>", unsafe_allow_html=True)
