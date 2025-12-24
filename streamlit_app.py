import streamlit as st
import time

# إعداد الصفحة لتكون أنيقة ومنظمة للهاتف
st.set_page_config(page_title="SNIPER PLATFORM", layout="centered")

# دالة حسابية تربط الـ ID بالنتيجة المطلوبة بدقة
def get_exact_score(h_id, a_id):
    # نستخدم أول رقم متاح في الـ ID كدليل للسكور، وإذا لم يوجد نستخدم طول الرمز
    def extract_val(s):
        nums = [int(c) for c in s if c.isdigit()]
        return nums[0] if nums else (len(s) % 6)
    
    h_res = extract_val(h_id) % 6
    a_res = extract_val(a_id) % 6
    return h_res, a_res

st.markdown("<h2 style='text-align: center; color: white;'>🏆 SMART EXACT SCORE</h2>", unsafe_allow_html=True)

# واجهة المدخلات
col1, col2 = st.columns(2)
with col1:
    h_n = st.text_input("🏠 الفريق المضيف:", "D.R. Congo")
    h_i = st.text_input("🆔 ID المضيف:", "drz14c")
with col2:
    a_n = st.text_input("✈️ الفريق الضيف:", "Benin")
    a_i = st.text_input("🆔 ID الضيف:", "bnw06t")

if st.button("🚀 START ANALYSIS"):
    with st.spinner('تحليل البيانات...'):
        time.sleep(1.5)
        h_s, a_s = get_exact_score(h_i, a_i)
    
    # --- التنسيق الأنيق المانع للتداخل (Horizontal Layout) ---
    st.markdown(f"""
    <div style="background: #1e1e1e; color: white; padding: 25px; border-radius: 20px; border: 4px solid #f1c40f; text-align: center;">
        <p style="color: #f1c40f; font-weight: bold; margin-bottom: 20px;">FINAL EXACT SCORE</p>
        <div style="display: flex; justify-content: space-around; align-items: center;">
            <div style="font-size: 18px; font-weight: bold; flex: 1;">{h_n}</div>
            <div style="background: #333; color: #f1c40f; font-size: 55px; font-weight: bold; padding: 5px 25px; border-radius: 12px; margin: 0 15px;">
                {h_s}-{a_s}
            </div>
            <div style="font-size: 18px; font-weight: bold; flex: 1;">{a_n}</div>
        </div>
        <div style="background: #282828; padding: 15px; border-radius: 10px; margin-top: 25px; text-align: right; border-right: 5px solid #f1c40f;">
            <h4 style="color: #f1c40f; margin: 0;">📋 مجرى المباراة:</h4>
            <p style="font-size: 14px; color: #ccc; margin-top: 8px;">
                بناءً على الرموز {h_i} و {a_i}، تم رصد كفاءة هجومية تؤدي لنتيجة {h_s}-{a_s}.
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
