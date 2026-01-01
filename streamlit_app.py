import streamlit as st
import base64

def advanced_statistical_engine(home_raw, away_raw):
    try:
        h_name, h_atk, h_def = base64.b64decode(home_raw).decode('utf-8').split(':')
        a_name, a_atk, a_def = base64.b64decode(away_raw).decode('utf-8').split(':')
        
        # تحويل البيانات (الهجوم والدفاع يجب أن يكون بين 0 و 100)
        ha, hd = int(h_atk), int(h_def)
        aa, ad = int(a_atk), int(a_def)

        # --- المنطق الاحترافي الجديد ---
        # حساب قوة التسجيل (قوة الهجوم مقابل قوة دفاع الخصم)
        home_score_power = (ha * (100 - ad)) / 1000
        away_score_power = (aa * (100 - hd)) / 1000

        # تحويل القوة إلى أهداف منطقية (0-4 أهداف)
        h_goals = int(home_score_power // 1.5)
        a_goals = int(away_score_power // 1.8) # الضيف دائماً أصعب في التسجيل

        # إضافة ميزة "الحد الأدنى" للمباريات التنافسية
        if ha > ad and h_goals == 0: h_goals = 1
        if aa > hd and a_goals == 0: a_goals = 1

        return h_name, a_name, h_goals, a_goals
    except:
        return None, None, None, None

# واجهة Streamlit بسيطة
st.title("🏆 Pro Match Predictor v3.0")
h_id = st.text_input("Home ID")
a_id = st.text_input("Away ID")

if st.button("Predict"):
    res = advanced_statistical_engine(h_id, a_id)
    if res[0]:
        st.header(f"{res[0]} {res[2]} - {res[3]} {res[1]}")
        
