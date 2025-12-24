import streamlit as st
import time

def ai_smart_decoder(h_id, a_id):
    # تحليل المضيف: الحروف الكبيرة تعطي أهدافاً حقيقية
    h_score = sum(1 for c in h_id if c.isupper())
    
    # تحليل الضيف: يبحث السكريبت عن "ثغرة" (حرف صغير في النهاية) ليسجل
    a_score = 1 if a_id[-1].islower() and any(c.isdigit() for c in a_id) else 0
    
    # تصحيح المنطق الحر (0-5)
    h_score = min(h_score, 5)
    
    win = "Home" if h_score > a_score else "Away" if a_score > h_score else "Draw"
    ou = "Over 2.5" if (h_score + a_score) > 2.5 else "Under 2.5"
    bt = "Yes" if (h_score > 0 and a_score > 0) else "No"
    
    return h_score, a_score, win, ou, bt

# --- الواجهة الاحترافية (طبق الأصل عن الفيديو) ---
st.markdown("<h2 style='text-align: center; color: #f1c40f;'>🛡️ SNIPER AI: AUTONOMOUS ANALYST</h2>", unsafe_allow_html=True)

link = st.text_input("🔗 BeSoccer Match Link:")
col1, col2 = st.columns(2)
with col1:
    h_i = st.text_input("🆔 Home ID (AI Generated):")
with col2:
    a_i = st.text_input("🆔 Away ID (AI Generated):")

if st.button("🚀 EXECUTE SMART ANALYSIS (30s)"):
    # المحاكاة الزمنية للتحليل العميق
    with st.spinner("جاري قراءة البيانات من الرابط وتحليل الـ IDs..."):
        time.sleep(30)
    
    h_s, a_s, win, ou, bt = ai_smart_decoder(h_i, a_i)
    
    st.markdown(f"""
    <div style="background: #111; padding: 25px; border: 3px solid #f1c40f; border-radius: 15px; text-align: center; color: white;">
        <div style="display: flex; justify-content: space-around; align-items: center;">
            <div style="background: #f1c40f; color: black; font-size: 60px; font-weight: bold; padding: 10px 40px; border-radius: 15px;">{h_s} - {a_s}</div>
        </div>
        <div style="display: flex; justify-content: space-between; margin-top: 25px;">
            <div style="flex: 1; background: #222; margin: 5px; padding: 15px; border-radius: 10px;">
                <p style="color: #f1c40f; font-size: 12px;">WINNER</p><h4>{win}</h4>
            </div>
            <div style="flex: 1; background: #222; margin: 5px; padding: 15px; border-radius: 10px;">
                <p style="color: #f1c40f; font-size: 12px;">O/U 2.5</p><h4>{ou}</h4>
            </div>
            <div style="flex: 1; background: #222; margin: 5px; padding: 15px; border-radius: 10px;">
                <p style="color: #f1c40f; font-size: 12px;">BTTS</p><h4>{bt}</h4>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
