import streamlit as st
import base64
import time
import random

# --- محرك التوقعات الذكي المطور ---
def statistical_engine(home_raw, away_raw):
    try:
        h_name, h_atk, h_def = base64.b64decode(home_raw).decode('utf-8').split(':')
        a_name, a_atk, a_def = base64.b64decode(away_raw).decode('utf-8').split(':')
        
        h_atk, h_def = int(h_atk), int(h_def)
        a_atk, a_def = int(a_atk), int(a_def)

        # --- المنطق الجديد لمنع خلل الـ 0-0 ---
        # 1. حساب الفارق الأساسي
        h_diff = h_atk - a_def
        a_diff = a_atk - h_def

        # 2. معادلة الأهداف مع "عامل المبادرة" (+10 للأرض و +5 للضيف)
        # القاسم أصبح 10 بدلاً من 12 و 15 لزيادة الحساسية
        home_goals = max(0, (h_diff + 10) // 10)
        away_goals = max(0, (a_diff + 5) // 12)

        # 3. محاكاة "الواقعية": إذا كان الهجوم قوياً جداً والدفاع ضعيف، نمنح فرصة لهدف إضافي
        if h_diff > 20: home_goals += random.randint(0, 1)
        if a_diff > 15: away_goals += random.randint(0, 1)

        return h_name, a_name, int(home_goals), int(away_goals)
    except:
        return None, None, None, None

# --- واجهة المستخدم ---
st.set_page_config(page_title="Smart Score Predictor", layout="centered")

st.title("⚽ Smart Football Predictor v2.0")
st.info("تم تحديث المعادلات لتجنب النتائج الصفرية غير الواقعية")

col1, col2 = st.columns(2)
with col1:
    home_id = st.text_input("HOME TEAM ID")
with col2:
    away_id = st.text_input("AWAY TEAM ID")

if st.button("RUN ANALYSIS"):
    if home_id and away_id:
        h_n, a_n, h_g, a_g = statistical_engine(home_id, away_id)
        if h_n:
            st.markdown(f"<h1 style='text-align: center;'>{h_n} {h_g} - {a_g} {a_n}</h1>", unsafe_allow_html=True)
            if h_g > a_g: st.success(f"توقعات بفوز {h_n}")
            elif a_g > h_g: st.success(f"توقعات بفوز {a_n}")
            else: st.warning("توقعات بنتيجة متعادلة")
        else:
            st.error("Invalid Code!")
            
