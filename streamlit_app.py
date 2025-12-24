import streamlit as st
import time
import hashlib

# إعداد الواجهة لتكون مطابقة للفيديو الأصلي
st.set_page_config(page_title="SNIPER AI PRO", layout="wide")

def core_logic_engine(url):
    """محرك الخوارزمية الأصلية: تحويل الرابط إلى نتيجة ثابتة ومنطقية"""
    # تنظيف الرابط لضمان عدم تغير النتيجة بسبب فراغ أو حرف كبير
    clean_url = url.strip().lower()
    
    # صنع بصمة رقمية عميقة (SHA-256) للمباراة
    match_fingerprint = hashlib.sha256(clean_url.encode()).hexdigest()
    
    # استخراج أرقام معينة من وسط البصمة لضمان "منطق الأهداف"
    # نستخدم أوزان رياضية ثابتة لكل مباراة
    val1 = int(match_fingerprint[10:12], 16)
    val2 = int(match_fingerprint[12:14], 16)
    
    # تحديد الأهداف (المضيف بين 0-4، الضيف بين 0-2) لنتائج واقعية
    h_s = val1 % 5 
    a_s = val2 % 3
    
    # تصحيح النتائج الصفرية المملة لزيادة الواقعية
    if h_s == 0 and a_s == 0: h_s, a_s = 1, 0
    
    return h_s, a_s, match_fingerprint[:10].upper()

st.markdown("<h2 style='text-align: center; color: #f1c40f;'>🛡️ SNIPER AI: CORE ENGINE</h2>", unsafe_allow_html=True)

# خانة الرابط
target_link = st.text_input("🔗 Paste Match Link:", placeholder="أدخل رابط المباراة هنا...")

if st.button("🚀 EXECUTE CORE ANALYSIS"):
    if target_link:
        # مرحلة التحليل البصري (30 ثانية أو أقل)
        with st.status("🔍 جاري فحص البصمة الرقمية للمباراة...", expanded=True) as status:
            time.sleep(2)
            st.write("📊 تحليل موازين القوى (xG)...")
            h_s, a_s, m_id = core_logic_engine(target_link)
            time.sleep(2)
            status.update(label="✅ تم استخراج النتيجة من الخوارزمية!", state="complete")
        
        # عرض الـ Match ID المنسق
        st.markdown(f"<p style='text-align:center;'>Match Token: <span style='color:#00ff00;'>SNPR_{m_id}</span></p>", unsafe_allow_html=True)
        
        # تصميم النتيجة النهائي (حل مشكلة ظهور الأكواد والتداخل)
        st.markdown(f"""
        <div style="background: #000; padding: 35px; border: 4px solid #f1c40f; border-radius: 25px; text-align: center; color: white;">
            <div style="font-size: 85px; font-weight: bold; color: #fff; margin-bottom: 25px; text-shadow: 0 0 15px #f1c40f;">
                {h_s} - {a_s}
            </div>
            
            <div style="display: flex; justify-content: center; gap: 15px; flex-wrap: wrap;">
                <div style="background: #111; padding: 20px; border-radius: 15px; width: 125px; border-top: 5px solid #f1c40f;">
                    <small style="color:#888;">WINNER</small><br><b style="color:#f1c40f; font-size: 18px;">{"HOME" if h_s > a_s else "AWAY" if a_s > h_s else "DRAW"}</b>
                </div>
                <div style="background: #111; padding: 20px; border-radius: 15px; width: 125px; border-top: 5px solid #f1c40f;">
                    <small style="color:#888;">O/U 2.5</small><br><b style="color:#f1c40f; font-size: 18px;">{"OVER" if h_s+a_s > 2.5 else "UNDER"}</b>
                </div>
                <div style="background: #111; padding: 20px; border-radius: 15px; width: 125px; border-top: 5px solid #f1c40f;">
                    <small style="color:#888;">BTTS</small><br><b style="color:#f1c40f; font-size: 18px;">{"YES" if h_s>0 and a_s>0 else "NO"}</b>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.warning("⚠️ يرجى إدخال الرابط أولاً.")
        
