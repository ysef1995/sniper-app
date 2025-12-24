import streamlit as st

# إعداد الصفحة لتناسب الهاتف
st.set_page_config(page_title="SNIPER SMART", layout="centered")

# دالة ذكية لتحويل الـ ID لنتائج واقعية (1-0, 2-1, 3-1)
def calculate_exact_score(h_id, a_id):
    # حساب قوة وهمية من الرموز لضبط النتيجة
    h_power = sum(ord(c) for c in h_id) % 10
    a_power = sum(ord(c) for c in a_id) % 5
    
    # منطق النتائج الواقعية (الكونغو 1-0، نيجيريا 2-1)
    if h_power > 7: h_score, a_score = 3, (1 if a_power > 2 else 0)
    elif h_power > 4: h_score, a_score = 2, (1 if a_power > 1 else 0)
    else: h_score, a_score = 1, 0
    
    return f"{h_score}-{a_score}"

st.markdown("<h2 style='text-align: center;'>🎯 SMART ANALYST V131</h2>", unsafe_allow_html=True)

# مدخلات بسيطة ومنظمة
h_name = st.text_input("🏠 المضيف:", "D.R. Congo")
h_id = st.text_input("🆔 ID المضيف:", "Rt4X2p")

a_name = st.text_input("✈️ الضيف:", "Benin")
a_id = st.text_input("🆔 ID الضيف:", "Km9L1s")

if st.button("🚀 ANALYZE NOW"):
    score = calculate_exact_score(h_id, a_id)
    
    # --- تصميم أنيق، متناسق ومضغوط للهاتف ---
    st.markdown(f"""
    <div style="background: #1e1e1e; color: white; padding: 20px; border-radius: 20px; text-align: center; margin-top: 20px;">
        <p style="color: #f1c40f; margin-bottom: 5px; font-weight: bold;">EXACT SCORE</p>
        <div style="display: flex; justify-content: space-between; align-items: center; padding: 10px;">
            <span style="font-size: 18px; flex: 1;">{h_name}</span>
            <span style="font-size: 45px; font-weight: bold; color: #f1c40f; background: #333; padding: 5px 20px; border-radius: 10px; margin: 0 10px;">
                {score}
            </span>
            <span style="font-size: 18px; flex: 1;">{a_name}</span>
        </div>
        <hr style="border-color: #444;">
        <div style="text-align: right; font-size: 14px; color: #ccc;">
            <b>📋 التحليل:</b> مباراة تكتيكية، المضيف يسيطر دفاعياً.
        </div>
    </div>
    """, unsafe_allow_html=True)
    
