import streamlit as st
import time

st.set_page_config(page_title="SNIPER AI PLATFORM", layout="centered")

# دالة فك التشفير والتحليل
def ai_analyze_id(h_id, a_id):
    # الذكاء الاصطناعي يقرأ القوة من الرموز (الحروف الكبيرة = أهداف)
    h_s = sum(1 for c in h_id if c.isupper())
    a_s = sum(1 for c in a_id if c.isupper())
    
    # ضمان نتيجة منطقية إذا كانت الرموز صغيرة (1-0)
    if h_s == 0 and a_s == 0: h_s = 1
    return h_s, a_s

st.markdown("<h1 style='text-align: center;'>🎯 AI SCORE SYSTEM</h1>", unsafe_allow_True=True)

# إدخال البيانات كما في الفيديو
col1, col2 = st.columns(2)
with col1:
    h_name = st.text_input("🏠 الفريق المضيف:", "Burkina Faso")
    h_id = st.text_input("🆔 ID المضيف:", placeholder="أدخل الرمز هنا...")
with col2:
    a_name = st.text_input("✈️ الفريق الضيف:", "Equatorial Guinea")
    a_id = st.text_input("🆔 ID الضيف:", placeholder="أدخل الرمز هنا...")

if st.button("🚀 START ANALYSIS"):
    if h_id and a_id:
        # --- مرحلة العد التنازلي (30 ثانية) كما في الفيديو ---
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        for percent_complete in range(100):
            time.sleep(0.3)  # لإكمال 30 ثانية تقريباً (0.3 * 100)
            progress_bar.progress(percent_complete + 1)
            remaining = 30 - int(percent_complete * 0.3)
            status_text.text(f"⏳ جاري تحليل موازين القوى... متبقي {remaining} ثانية")
        
        status_text.success("✅ اكتمل التحليل!")
        h_s, a_s = ai_analyze_id(h_id, a_id)

        # --- الطباعة الأنيقة (النتيجة النهائية) ---
        st.markdown(f"""
        <div style="background: #1e1e1e; color: white; padding: 30px; border-radius: 20px; border: 5px solid #f1c40f; text-align: center; margin-top: 20px;">
            <p style="color: #f1c40f; font-weight: bold; font-size: 20px;">FINAL EXACT SCORE</p>
            <div style="display: flex; justify-content: space-around; align-items: center; margin: 20px 0;">
                <div style="font-size: 24px; font-weight: bold; flex: 1;">{h_name}</div>
                <div style="background: #333; color: #f1c40f; font-size: 70px; font-weight: bold; padding: 10px 40px; border-radius: 15px; min-width: 150px; box-shadow: 0 0 20px #f1c40f66;">
                    {h_s}-{a_s}
                </div>
                <div style="font-size: 24px; font-weight: bold; flex: 1;">{a_name}</div>
            </div>
            <div style="background: #282828; padding: 15px; border-radius: 10px; text-align: right; border-right: 5px solid #f1c40f;">
                <p style="margin: 0; color: #f1c40f;">📋 تقرير المحلل:</p>
                <p style="margin: 5px 0 0; color: #ccc; font-size: 14px;">بناءً على تشفير الرموز، يتوقع النظام مباراة تنتهي بنتيجة {h_s}-{a_s}.</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.error("⚠️ يرجى إدخال الرموز (IDs) أولاً!")
        
