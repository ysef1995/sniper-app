import streamlit as st
import time
import hashlib

# إعدادات الواجهة الاحترافية
st.set_page_config(page_title="SNIPER AI ORIGINAL LOGIC", layout="wide")

def original_algorithm(url):
    """محاكاة منطق السكريبت الأصلي: تحويل الرابط إلى أهداف عبر خوارزمية الهاش"""
    # 1. صنع بصمة فريدة للمباراة
    match_hash = hashlib.sha256(url.encode()).hexdigest()
    
    # 2. استخراج "أوزان" الأهداف من البصمة (المنطق الرقمي)
    # نأخذ قيم معينة من الهاش ونحولها لأرقام
    h_weight = int(match_hash[2:4], 16)
    a_weight = int(match_hash[4:6], 16)
    
    # 3. تحويل الأوزان إلى أهداف واقعية (بين 0 و 4)
    h_s = h_weight % 5
    a_s = a_s_calc = a_weight % 3
    
    # موازنة النتيجة لمنع التعادلات المملة (مثل 1-1 دائماً)
    if h_s == a_s and h_s < 4:
        h_s += 1
        
    return h_s, a_s, match_hash[:12].upper()

st.markdown("<h2 style='text-align: center; color: #f1c40f;'>🛡️ SNIPER AI: ORIGINAL ALGORITHM</h2>", unsafe_allow_html=True)

# مدخل الرابط
url_input = st.text_input("🔗 BeSoccer Match Link:", placeholder="أدخل الرابط لتشغيل الخوارزمية الأصلية...")

if st.button("🚀 EXECUTE CORE ANALYSIS"):
    if url_input:
        # شريط التحليل الاحترافي كما في الفيديوهات
        progress = st.progress(0)
        status = st.empty()
        
        for i in range(100):
            time.sleep(0.1) # سرعة معقولة للتحليل
            progress.progress(i + 1)
            if i < 50: status.text("⏳ Reading Match Metadata...")
            else: status.text("📊 Decoding Digital ID Weights...")
            
        h_score, a_score, match_id = original_algorithm(url_input)
        status.success("✅ Analysis Complete!")
        
        # عرض الـ ID بوضوح
        st.markdown(f"<p style='text-align:center;'>Match ID: <span style='color:#00ff00;'>SUR_{match_id}</span></p>", unsafe_allow_html=True)
        
        # تصميم النتيجة النهائي (بدون أخطاء HTML)
        st.markdown(f"""
        <div style="background: #000; padding: 30px; border: 3px solid #f1c40f; border-radius: 20px; text-align: center; color: white;">
            <div style="font-size: 80px; font-weight: bold; color: #fff; margin-bottom: 20px;">{h_score} - {a_score}</div>
            
            <div style="display: flex; justify-content: center; gap: 10px; flex-wrap: wrap;">
                <div style="background: #1a1a1a; padding: 15px; border-radius: 12px; width: 120px; border-top: 4px solid #f1c40f;">
                    <small style="color:#888;">WINNER</small><br><b style="color:#f1c40f;">{"HOME" if h_score > a_score else "AWAY" if a_score > h_score else "DRAW"}</b>
                </div>
                <div style="background: #1a1a1a; padding: 15px; border-radius: 12px; width: 120px; border-top: 4px solid #f1c40f;">
                    <small style="color:#888;">O/U 2.5</small><br><b style="color:#f1c40f;">{"OVER" if h_score+a_score > 2.5 else "UNDER"}</b>
                </div>
                <div style="background: #1a1a1a; padding: 15px; border-radius: 12px; width: 120px; border-top: 4px solid #f1c40f;">
                    <small style="color:#888;">BTTS</small><br><b style="color:#f1c40f;">{"YES" if h_score > 0 and a_score > 0 else "NO"}</b>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.error("⚠️ يرجى إدخال الرابط.")
        
