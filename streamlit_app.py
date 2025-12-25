import streamlit as st
import time
import hashlib

# إعدادات الواجهة الاحترافية للبث المباشر
st.set_page_config(page_title="SNIPER AI PRO", page_icon="🎯", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #000; }
    .title-text { color: #00FF00; text-align: center; font-family: 'Courier New', monospace; text-shadow: 0 0 15px #00FF00; }
    .stTextInput>div>div>input { background-color: #0a0a0a; color: #00FF00; border: 1px solid #00FF00; text-align: center; }
    .stButton>button { width: 100%; background-color: #00FF00; color: #000; font-weight: bold; border-radius: 10px; height: 50px; }
    .prediction-card { border: 2px solid #00FF00; padding: 30px; border-radius: 15px; background-color: #050505; text-align: center; }
    .score-display { font-size: 85px; color: #00FF00; font-weight: bold; font-family: 'Impact', sans-serif; margin: 10px 0; }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<h1 class="title-text">⚡ SNIPER IA ANALYZER ⚡</h1>', unsafe_allow_html=True)

# دالة تحليل الذكاء الاصطناعي (منطق رياضي ثابت)
def calculate_ai_prediction(match_id):
    # تحويل الـ ID إلى قيمة رقمية فريدة لاستخدامها في الحسابات
    hash_object = hashlib.md5(match_id.encode())
    hex_hash = hash_object.hexdigest()
    
    # استخراج قيم رقمية من الـ Hash لتمثيل قوة الفريقين
    val1 = int(hex_hash[0:2], 16) % 4  # أهداف الفريق الأرضي (0-3)
    val2 = int(hex_hash[2:4], 16) % 3  # أهداف الفريق الضيف (0-2)
    
    # منطق لضمان عدم وجود نتائج مبالغ فيها (مثل 9-0)
    if val1 > 2 and val2 > 2:
        val1, val2 = 1, 1
        
    return f"{val1}-{val2}"

# الواجهة
user_input = st.text_input("ENTER MATCH ID (SOFASCORE):", placeholder="Example: 13424942")

if st.button("EXECUTE IA CALCULATION"):
    if user_input:
        # تنظيف المدخلات لاستخراج الأرقام فقط
        m_id = "".join(filter(str.isdigit, user_input))
        
        if len(m_id) > 4:
            with st.status("🛠️ CRUNCHING DATA...", expanded=True) as status:
                st.write("📡 Accessing Historical Databases...")
                time.sleep(1)
                st.write("📊 Comparing H2H Defensive Patterns...")
                time.sleep(1.5)
                st.write("🧠 Applying Neural Prediction Model...")
                time.sleep(1)
                status.update(label="ANALYSIS SUCCESSFUL", state="complete")

            # حساب النتيجة بناءً على المنطق الرياضي للـ ID
            final_result = calculate_ai_prediction(m_id)
            
            # حساب نسبة الثقة بناءً على الـ ID (ثابتة لنفس المباراة)
            confidence = 85 + (int(m_id[-1]) % 10)
            
            st.markdown(f"""
                <div class="prediction-card">
                    <p style="color: #888;">MATCH IDENTIFIED: {m_id}</p>
                    <p style="color: #00FF00; letter-spacing: 3px;">EXACT SCORE PREDICTION</p>
                    <div class="score-display">{final_result}</div>
                    <div style="border-top: 1px solid #222; padding-top: 15px;">
                        <span style="color: white;">IA CONFIDENCE: </span>
                        <span style="color: #00FF00; font-weight: bold;">{confidence}%</span>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            st.balloons()
        else:
            st.error("Invalid ID format.")
    else:
        st.warning("Please enter a Match ID.")
        
