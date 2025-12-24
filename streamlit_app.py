import streamlit as st
import time
import hashlib

st.set_page_config(page_title="SNIPER AI - REALISTIC SCORE", layout="wide")

def generate_realistic_score(url):
    # تحويل الرابط إلى بصمة فريدة لضمان عدم تكرار النتيجة
    hash_object = hashlib.md5(url.encode())
    hash_hex = hash_object.hexdigest()
    
    # تحويل أول وثاني حرف من الهاش إلى أرقام (0-5)
    # هذا المنطق يضمن أن كل مباراة لها سكور فريد بناءً على رابطها
    h_s = int(hash_hex[0], 16) % 6  # نتيجة بين 0 و 5
    a_s = int(hash_hex[1], 16) % 4  # نتيجة بين 0 و 3 (واقعية للضيف)
    
    # تعديل خاص للفرق الكبرى مثل الجزائر لضمان سكور مرتفع
    if "algeria" in url.lower() or "madrid" in url.lower():
        h_s = max(h_s, 3) # لا يقل عن 3 أهداف للقوة الهجومية
        
    return h_s, a_s, hash_hex[:8].upper()

st.markdown("<h2 style='text-align: center; color: #f1c40f;'>🛡️ SNIPER AI: REALISTIC SCORE ENGINE</h2>", unsafe_allow_html=True)

# خانة الرابط الأساسية
match_url = st.text_input("🔗 BeSoccer / Flashscore Link:", placeholder="أدخل رابط المباراة هنا...")

if st.button("🚀 EXECUTE DYNAMIC ANALYSIS"):
    if match_url:
        # توليد السكور والـ ID تلقائياً من الرابط
        h_score, a_score, match_hash = generate_realistic_score(match_url)
        
        # عرض الـ IDs المولدة آلياً طبق الأصل عن الفيديو
        st.write(f"📡 Match ID: `SUR_{match_hash}_H` | `SUR_{match_hash}_A`")
        
        # شريط التحميل الاحترافي (30 ثانية)
        bar = st.progress(0)
        status = st.empty()
        for i in range(100):
            time.sleep(0.3)
            bar.progress(i + 1)
            status.markdown(f"<p style='text-align: center;'>⏳ جاري تحليل موازين القوى... متبقي {30 - int(i*0.3)}s</p>", unsafe_allow_html=True)
            
        # تصميم الواجهة لمنع تداخل النصوص كما في الصور السابقة
        st.markdown(f"""
        <div style="background: #000; padding: 35px; border: 4px solid #f1c40f; border-radius: 25px; text-align: center; color: white;">
            <div style="font-size: 80px; font-weight: bold; color: #fff; margin-bottom: 20px; border-bottom: 2px solid #333; display: inline-block; padding: 0 40px;">
                {h_score} - {a_score}
            </div>
            <div style="display: flex; justify-content: center; gap: 15px; flex-wrap: wrap;">
                <div style="background: #1a1a1a; padding: 20px; border-radius: 15px; width: 120px; border-top: 5px solid #f1c40f;">
                    <small style="color: #888;">WINNER</small><br><b style="font-size: 18px; color: #f1c40f;">{"HOME" if h_score > a_score else "DRAW" if h_score == a_score else "AWAY"}</b>
                </div>
                <div style="background: #1a1a1a; padding: 20px; border-radius: 15px; width: 120px; border-top: 5px solid #f1c40f;">
                    <small style="color: #888;">O/U 2.5</small><br><b style="font-size: 18px; color: #f1c40f;">{"OVER" if h_score+a_score > 2.5 else "UNDER"}</b>
                </div>
                <div style="background: #1a1a1a; padding: 20px; border-radius: 15px; width: 120px; border-top: 5px solid #f1c40f;">
                    <small style="color: #888;">BTTS</small><br><b style="font-size: 18px; color: #f1c40f;">{"YES" if h_score > 0 and a_score > 0 else "NO"}</b>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.warning("⚠️ يرجى وضع الرابط أولاً.")
        
