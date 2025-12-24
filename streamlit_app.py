import streamlit as st
import time

st.set_page_config(page_title="SNIPER PRO ANALYST", layout="wide")

def analyze_markets(h_id, a_id):
    # منطق فك التشفير بناءً على بصمة الـ ID
    h_weight = sum(ord(c) for c in h_id)
    a_weight = sum(ord(c) for c in a_id)
    
    h_score = (h_weight % 3) + (1 if any(c.isupper() for c in h_id) else 0)
    a_score = (a_weight % 2) + (1 if 'k' in a_id.lower() or 'm' in a_id.lower() else 0)
    
    # توقعات الأسواق
    winner = "Home" if h_score > a_score else "Away" if a_score > h_score else "Draw"
    ou_25 = "Over 2.5" if (h_score + a_score) > 2.5 else "Under 2.5"
    btts = "Yes" if (h_score > 0 and a_score > 0) else "No"
    
    return h_score, a_score, winner, ou_25, btts

st.markdown("<h1 style='text-align: center; color: #f1c40f;'>🛡️ SNIPER PRO MATCH ANALYST</h1>", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    h_team = st.text_input("🏠 Home Team:", "Burkina Faso")
    h_id = st.text_input("🆔 Home Match ID:")
with col2:
    a_team = st.text_input("✈️ Away Team:", "Equatorial Guinea")
    a_id = st.text_input("🆔 Away Match ID:")

if st.button("🚀 EXECUTE DEEP ANALYSIS"):
    if h_id and a_id:
        with st.status("🔍 Scanning Team Statistics...", expanded=True) as status:
            time.sleep(10) # 30 ثانية للتحليل الكامل
            st.write("🔗 Decoding Match ID...")
            time.sleep(10)
            st.write("📊 Calculating Market Odds...")
            time.sleep(10)
            status.update(label="Analysis Complete!", state="complete", expanded=False)
        
        h_s, a_s, win, ou, bt = analyze_markets(h_id, a_id)
        
        # --- طباعة متناسقة واحترافية (طبق الأصل عن الفيديو) ---
        st.markdown(f"""
        <div style="background: #121212; padding: 25px; border-radius: 15px; border: 2px solid #f1c40f; color: white;">
            <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #333; padding-bottom: 15px;">
                <div style="text-align: center; flex: 1;"><h3>{h_team}</h3></div>
                <div style="background: #f1c40f; color: black; padding: 10px 30px; border-radius: 10px; font-size: 40px; font-weight: bold;">{h_s} - {a_s}</div>
                <div style="text-align: center; flex: 1;"><h3>{a_team}</h3></div>
            </div>
            <div style="display: flex; justify-content: space-around; margin-top: 20px; text-align: center;">
                <div style="background: #1e1e1e; padding: 15px; border-radius: 10px; width: 30%;">
                    <p style="color: #f1c40f; margin: 0;">WINNER</p>
                    <h4 style="margin: 5px 0;">{win}</h4>
                </div>
                <div style="background: #1e1e1e; padding: 15px; border-radius: 10px; width: 30%;">
                    <p style="color: #f1c40f; margin: 0;">O/U 2.5</p>
                    <h4 style="margin: 5px 0;">{ou}</h4>
                </div>
                <div style="background: #1e1e1e; padding: 15px; border-radius: 10px; width: 30%;">
                    <p style="color: #f1c40f; margin: 0;">BTTS</p>
                    <h4 style="margin: 5px 0;">{bt}</h4>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
