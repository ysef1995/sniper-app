import streamlit as st
import base64
import time

# --- محرك التوقعات الإحصائي المطور ---
def statistical_engine(home_raw, away_raw):
    try:
        # فك التشفير واستخراج البيانات (الاسم:الهجوم:الدفاع)
        h_name, h_atk, h_def = base64.b64decode(home_raw).decode('utf-8').split(':')
        a_name, a_atk, a_def = base64.b64decode(away_raw).decode('utf-8').split(':')
        
        # تحويل القيم إلى أرقام
        h_atk, h_def = int(h_atk), int(h_def)
        a_atk, a_def = int(a_atk), int(a_def)

        # --- المعادلة الرياضية المحدثة ---
        # تم تصغير القاسم (Divisor) لزيادة حساسية تسجيل الأهداف
        # الفارق مقسوم على 12 ليعطي نتائج واقعية (1-3 أهداف)
        home_goals = max(0, (h_atk - a_def) // 12)
        away_goals = max(0, (a_atk - h_def) // 15)

        # إضافة "لمسة عشوائية منطقية" إذا كان الهجوم متقارباً جداً مع الدفاع
        if h_atk > a_def and home_goals == 0: home_goals = 1
        if a_atk > h_def and away_goals == 0: away_goals = 1

        return h_name, a_name, int(home_goals), int(away_goals)
    except Exception as e:
        return None, None, None, None

# --- إعدادات واجهة المستخدم ---
st.set_page_config(page_title="Pro Stats Predictor", page_icon="⚽", layout="centered")

st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #ffffff; }
    .stTextInput>div>div>input { background-color: #262730; color: #00ff00; border-color: #4b4b4b; }
    .stButton>button { width: 100%; background-color: #ff4b4b; color: white; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.title("🎯 Statistical Prediction Engine")
st.subheader("تحليل القوة الهجومية والدفاعية")
st.write("---")

# خانات إدخال الـ IDs
col1, col2 = st.columns(2)
with col1:
    home_id = st.text_input("HOME TEAM STATS ID", placeholder="Paste Code Here...")
with col2:
    away_id = st.text_input("AWAY TEAM STATS ID", placeholder="Paste Code Here...")

if st.button("CALCULATE PREDICTION"):
    if home_id and away_id:
        h_n, a_n, h_g, a_g = statistical_engine(home_id, away_id)
        
        if h_n:
            with st.spinner('جاري معالجة البيانات الإحصائية...'):
                time.sleep(1.5)
            
            # عرض النتيجة بشكل احترافي
            st.markdown(f"<h2 style='text-align: center;'>{h_n}  {h_g} - {a_g}  {a_n}</h2>", unsafe_allow_html=True)
            
            # تفاصيل إضافية للتحليل
            st.info(f"التحليل: قوة هجوم {h_n} واجهت دفاع {a_n} مما أدى لتوقع {h_g} أهداف.")
        else:
            st.error("خطأ في قراءة الأكواد! تأكد من نسخ الكود بشكل صحيح.")
    else:
        st.warning("يرجى إدخال الأكواد أولاً.")
        
