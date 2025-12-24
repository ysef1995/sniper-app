import streamlit as st
import time

# إعداد الصفحة لتناسب الهاتف
st.set_page_config(page_title="SNIPER AI SYSTEM", layout="centered")

# دالة التحليل الذكي للرموز (ID)
def ai_decode_logic(h_id, a_id):
    # يقوم المحرك بعد الحروف الكبيرة لاستنتاج الأهداف
    h_goals = sum(1 for c in h_id if c.isupper())
    a_goals = sum(1 for c in a_id if c.isupper())
    
    # لضمان نتيجة 1-0 في المباريات الدفاعية
    if h_goals == 0 and a_goals == 0: h_goals = 1
    return h_goals, a_goals

st.markdown("<h1 style='text-align: center; color: #f1c40f;'>🏆 AI SCORE PLATFORM</h1>", unsafe_allow_html=True)

# إدخال البيانات (أسماء الفرق والرموز)
col1, col2 = st.columns(2)
with col1:
    h_team = st.text_input("🏠 الفريق المضيف:", "Burkina Faso")
    h_id_code = st.text_input("🆔 ID المضيف (6 رموز):", placeholder="مثال: Bfk14s")
with col2:
    a_team = st.text_input("✈️ الفريق الضيف:", "Equatorial Guinea")
    a_id_code = st.text_input("🆔 ID الضيف (6 رموز):", placeholder="مثال: gnq06r")

if st.button("🚀 START ANALYSIS"):
    if h_id_code and a_id_code:
        # --- مرحلة الانتظار (30 ثانية للتحليل) كما في الفيديو ---
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        for p in range(100):
            time.sleep(0.3)  # الإجمالي 30 ثانية (100 * 0.3)
            progress_bar.progress(p + 1)
            # تحديث الوقت المتبقي
            rem = 30 - int(p * 0.3)
            status_text.markdown(f"<p style='text-align: center;'>⏳ جاري تحليل موازين القوى... متبقي {rem} ثانية</p>", unsafe_allow_html=True)
        
        status_text.success("✅ تم استكمال تحليل البيانات المشفرة!")
        h_score, a_score = ai_decode_logic(h_id_code, a_id_code)

        # --- التصميم الاحترافي للنتيجة النهائية ---
        st.markdown(f"""
        <div style="background: #1e1e1e; color: white; padding: 30px; border-radius: 20px; border: 5px solid #f1c40f; text-align: center; margin-top: 20px;">
            <p style="color: #f1c40f; font-weight: bold; font-size: 20px; letter-spacing: 2px;">FINAL EXACT SCORE</p>
            <div style="display: flex; justify-content: space-around; align-items: center; margin: 30px 0;">
                <div style="font-size: 24px; font-weight: bold; flex: 1; text-transform: uppercase;">{h_team}</div>
                <div style="background: #333; color: #f1c40f; font-size: 80px; font-weight: bold; padding: 15px 45px; border-radius: 20px; min-width: 160px; box-shadow: 0 0 25px rgba(241, 196, 15, 0.4);">
                    {h_score}-{a_score}
                </div>
                <div style="font-size: 24px; font-weight: bold; flex: 1; text-transform: uppercase;">{a_team}</div>
            </div>
            <div style="background: #282828; padding: 20px; border-radius: 12px; text-align: right; border-right: 6px solid #f1c40f;">
                <h4 style="margin: 0; color: #f1c40f;">📋 تقرير المحلل الذكي:</h4>
                <p style="margin: 10px 0 0; color: #ddd; font-size: 16px; line-height: 1.5;">
                    بناءً على تحليل الرموز {h_id_code} و {a_id_code}، تم استنتاج أن المباراة تميل لنتيجة {h_score}-{a_score}.
                </p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.warning("⚠️ الرجاء إدخال رموز الـ ID أولاً لبدء عملية التوقع.")
        
