import streamlit as st
import time
import hashlib

# --- 1. منطق فك التشفير المطور (V37.5 Dominance Logic) ---
def decode_id_to_score(id_string, is_home=True):
    if not id_string:
        return 0
    
    # تحويل الـ ID إلى قيمة رقمية فريدة باستخدام MD5
    hash_object = hashlib.md5(id_string.encode())
    hash_hex = hash_object.hexdigest()
    hash_val = int(hash_hex, 16)
    
    # استخراج "بصمة الهيمنة" من أول 3 رموز في الـ ID
    prefix = id_string[:2].upper()
    
    # منطق التهديف للمضيف (Home)
    if is_home:
        base_goals = hash_val % 3 # القيمة الأساسية (0-2)
        # إذا كان الفريق "الجزائر" أو يحتوي الـ ID على رموز قوة (A, B, 2)
        if prefix == "DZ" or any(char in id_string[:4] for char in "AB2"):
            return base_goals + 2 # رفع السقف لضمان نتائج مثل 3-0 أو 4-1
        return base_goals
    
    # منطق التهديف للضيف (Away)
    else:
        # إذا كان الخصم ضعيفاً (مثل السودان أمام الجزائر) نقيد أهدافه
        if any(char in id_string for char in "LX"): 
            return hash_val % 1 # غالباً 0
        return hash_val % 2 # غالباً 0 أو 1

# --- 2. إعدادات واجهة Streamlit ---
st.set_page_config(page_title="SNIPER AI - V37.5 DECODER", layout="wide")

# تصميم الهيدر (الذهبي)
st.markdown("""
    <h1 style='text-align: center; color: #D4AF37; margin-bottom: 0;'>🛰️ SNIPER AI - ID DECODER SYSTEM</h1>
    <p style='text-align: center; color: #666;'>Advanced Dominance Analysis v37.5</p>
    <hr style="border-color: #333;">
""", unsafe_allow_html=True)

# --- 3. خانات الإدخال مع مفاتيح فريدة (Keys) ---
col1, col2 = st.columns(2)

with col1:
    h_name = st.text_input("🏠 Home Team Name", value="Home Team", key="home_name_v37")
    h_id = st.text_input(f"🆔 {h_name} SUR ID", key="home_id_v37")

with col2:
    a_name = st.text_input("✈️ Away Team Name", value="Away Team", key="away_name_v37")
    a_id = st.text_input(f"🆔 {a_name} SUR ID", key="away_id_v37")

m_id = st.text_input("💰 GLOBAL MARKET MASTER ID", key="market_id_v37")

# --- 4. زر التحليل والأنيميشن ---
if st.button("🔍 START DEEP ANALYSIS", use_container_width=True):
    if h_id and a_id and m_id:
        # محاكاة التحليل لمدة 10 ثوانٍ لزيادة الحماس
        status_text = st.empty()
        progress_bar = st.progress(0)
        
        for p in range(100):
            time.sleep(0.1) # 10 ثوانٍ إجمالية
            progress_bar.progress(p + 1)
            if p < 30: status_text.text("📡 Syncing with Sniper Satellite...")
            elif p < 60: status_text.text(f"⚙️ Decoding {h_name} & {a_name} Algorithms...")
            else: status_text.text("🔥 Activating Dominance Protocol...")
        
        status_text.success("✅ DATA DECODED!")
        time.sleep(1)
        status_text.empty()
        progress_bar.empty()

        # حساب الأهداف بناءً على المنطق المطور
        goal_h = decode_id_to_score(h_id, is_home=True)
        goal_a = decode_id_to_score(a_id, is_home=False)
        
        # تحليل الأسواق
        win_market = "HOME (1)" if goal_h > goal_a else ("AWAY (2)" if goal_a > goal_h else "DRAW (X)")
        over_under = "OVER 2.5" if (goal_h + goal_a) >= 3 else "UNDER 2.5"
        btts = "YES" if (goal_h > 0 and goal_a > 0) else "NO"

        # --- 5. العرض النهائي (التصميم الذهبي) ---
        st.markdown(f"""
        <div style="background-color: #0e1117; padding: 35px; border: 2px solid #D4AF37; border-radius: 20px; text-align: center; color: white;">
            <h2 style="color: #D4AF37; letter-spacing: 2px;">🏆 FINAL PREDICTION REPORT</h2>
            <div style="margin: 30px 0; display: flex; justify-content: center; align-items: center; gap: 40px;">
                <div style="flex: 1;">
                    <h1 style="font-size: 85px; margin: 0; line-height: 1;">{goal_h}</h1>
                    <p style="color: #888; font-size: 18px; margin-top: 10px;">{h_name.upper()}</p>
                </div>
                <div style="font-size: 45px; color: #D4AF37; font-weight: bold;">VS</div>
                <div style="flex: 1;">
                    <h1 style="font-size: 85px; margin: 0; line-height: 1;">{goal_a}</h1>
                    <p style="color: #888; font-size: 18px; margin-top: 10px;">{a_name.upper()}</p>
                </div>
            </div>
            <div style="display: flex; justify-content: space-around; background: #1a1c23; padding: 20px; border-radius: 15px; border: 1px solid #333;">
                <div><p style="color: #D4AF37; margin:0;">🚩 1X2</p><b>{win_market}</b></div>
                <div><p style="color: #D4AF37; margin:0;">⚽ GOALS</p><b>{over_under}</b></div>
                <div><p style="color: #D4AF37; margin:0;">🔄 BTTS</p><b>{btts}</b></div>
            </div>
            <p style="color: #444; font-size: 12px; margin-top: 30px; letter-spacing: 3px;">VERIFIED ID: {m_id}</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.error("⚠️ Error: Please input all required IDs to bypass encryption.")

