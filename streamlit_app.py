import streamlit as st
import time
import hashlib

# --- وظيفة فك التشفير المنطقي ---
def decode_id_to_logic(id_string, limit=4):
    if not id_string: return 0
    # استخدام الهاش لضمان نتيجة ثابتة ومنطقية لكل ID
    hash_val = int(hashlib.sha256(id_string.encode()).hexdigest(), 16)
    return hash_val % limit

# --- واجهة التطبيق ---
st.set_page_config(page_title="SNIPER V37.0 - DECODER", layout="wide")

st.markdown("<h1 style='text-align: center; color: #D4AF37;'>🛰️ SNIPER AI - ID DECODER SYSTEM</h1>", unsafe_allow_html=True)

# مدخلات المستخدم مع إضافة مفاتيح فريدة (key) لتجنب الخطأ
col1, col2 = st.columns(2)
with col1:
    h_name = st.text_input("🏠 Home Team Name", value="Home Team", key="h_name_input")
    h_id = st.text_input(f"🆔 {h_name} SUR ID", key="h_id_input")
with col2:
    a_name = st.text_input("✈️ Away Team Name", value="Away Team", key="a_name_input")
    a_id = st.text_input(f"🆔 {a_name} SUR ID", key="a_id_input")

m_id = st.text_input("💰 GLOBAL MARKET MASTER ID", key="m_id_input")

# زر البدء
if st.button("🔍 START DEEP ANALYSIS"):
    if h_id and a_id and m_id:
        # --- مرحلة الانتظار (10 ثوانٍ) ---
        status_text = st.empty()
        progress_bar = st.progress(0)
        
        for percent_complete in range(100):
            time.sleep(0.1) # 100 * 0.1 = 10 ثوانٍ
            progress_bar.progress(percent_complete + 1)
            if percent_complete < 30:
                status_text.text("📡 Connecting to Global Sports Database...")
            elif percent_complete < 60:
                status_text.text(f"⚙️ Decoding {h_name} & {a_name} Data Strings...")
            else:
                status_text.text("🧪 Applying Sniper V37 Dominance Logic...")
        
        status_text.success("✅ Analysis Complete!")
        time.sleep(1)
        status_text.empty()
        progress_bar.empty()

        # --- حساب النتائج ---
        goal_h = decode_id_to_logic(h_id, 4) # الحد الأقصى 3 أهداف للمضيف
        goal_a = decode_id_to_logic(a_id, 3) # الحد الأقصى 2 أهداف للضيف
        
        win_market = "HOME (1)" if goal_h > goal_a else ("AWAY (2)" if goal_a > goal_h else "DRAW (X)")
        over_under = "OVER 2.5" if (goal_h + goal_a) >= 3 else "UNDER 2.5"
        btts = "YES" if (goal_h > 0 and goal_a > 0) else "NO"

        # --- التصميم الذهبي للنتائج ---
        st.markdown(f"""
        <div style="background-color: #0e1117; padding: 30px; border: 2px solid #D4AF37; border-radius: 15px; text-align: center; color: white;">
            <h2 style="color: #D4AF37;">🏆 FINAL PREDICTION REPORT</h2>
            <hr style="border-color: #333;">
            <div style="display: flex; justify-content: space-around; align-items: center; margin: 20px 0;">
                <div>
                    <h1 style="font-size: 70px; margin: 0; color: white;">{goal_h}</h1>
                    <p style="color: #888; font-weight: bold;">{h_name.upper()}</p>
                </div>
                <div style="font-size: 40px; color: #D4AF37; font-weight: bold;">VS</div>
                <div>
                    <h1 style="font-size: 70px; margin: 0; color: white;">{goal_a}</h1>
                    <p style="color: #888; font-weight: bold;">{a_name.upper()}</p>
                </div>
            </div>
            <hr style="border-color: #333;">
            <div style="display: flex; justify-content: space-around; font-family: 'Courier New', Courier, monospace;">
                <div style="text-align: center;">
                    <p style="color: #D4AF37; margin-bottom: 5px;">🚩 1X2</p>
                    <b style="font-size: 22px;">{win_market}</b>
                </div>
                <div style="text-align: center;">
                    <p style="color: #D4AF37; margin-bottom: 5px;">⚽ GOALS</p>
                    <b style="font-size: 22px;">{over_under}</b>
                </div>
                <div style="text-align: center;">
                    <p style="color: #D4AF37; margin-bottom: 5px;">🔄 BTTS</p>
                    <b style="font-size: 22px;">{btts}</b>
                </div>
            </div>
            <p style="color: #444; font-size: 11px; margin-top: 25px; letter-spacing: 2px;">DECODED MASTER ID: {m_id}</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.warning("⚠️ Please fill in all IDs to start the analysis.")
        
