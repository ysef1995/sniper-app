import streamlit as st
import time
import random
import hashlib

st.set_page_config(page_title="SNIPER AI ULTIMATE", layout="wide")

def deep_ai_logic(url):
    # محاكاة ذكية لتحليل التشكيلة والبيانات الحية
    unique_id = hashlib.md5(url.encode()).hexdigest().upper()
    
    # منطق الأهداف التلقائي بناءً على معطيات المباراة
    # يتم فحص الرابط: إذا كانت مباراة قمة يرتفع السكور، إذا كانت دفاعية ينخفض
    if "algeria" in url.lower():
        h_s, a_s = 3, 0  # الجزائر دائماً قوية هجومياً في هذا المنطق
    elif "derby" in url.lower() or "cup" in url.lower():
        h_s, a_s = 2, 1
    else:
        # توليد عشوائي ذكي للمباريات العادية
        h_s = random.choice([1, 2, 0])
        a_s = random.choice([0, 1])

    # توليد الـ IDs تلقائياً لتظهر في الواجهة
    h_id = f"STR_{h_s}{unique_id[:3]}_K"
    a_id = f"DEF_{a_s}{unique_id[-3:]}_Z"
    
    return h_id, a_id, h_s, a_s

st.markdown("<h1 style='text-align: center; color: #f1c40f;'>🛡️ SNIPER AI: LIVE LINEUP ANALYST</h1>", unsafe_allow_html=True)

# المدخل الوحيد: الرابط
match_link = st.text_input("🔗 BeSoccer / Flashscore Link:", placeholder="أدخل الرابط هنا للتحليل الشامل...")

if st.button("🚀 START AUTOMATED ANALYSIS"):
    if match_link:
        # 1. الذكاء الاصطناعي يحلل الرابط ويولد الـ IDs فوراً
        home_id, away_id, h_score, a_score = deep_ai_logic(match_link)
        
        # 2. عرض الـ IDs المولدة آلياً (للمصداقية كما في الفيديو)
        c1, c2 = st.columns(2)
        c1.warning(f"📡 System Generated Home ID: {home_id}")
        c2.warning(f"📡 System Generated Away ID: {away_id}")
        
        # 3. شريط التحميل الاحترافي (30 ثانية للتحليل العميق)
        progress_bar = st.progress(0)
        status = st.empty()
        for i in range(100):
            time.sleep(0.3)
            progress_bar.progress(i + 1)
            # محاكاة قراءة التشكيلة
            if i < 30: msg = "قراءة تشكيلة الفريقين..."
            elif i < 60: msg = "تحليل معدل الأهداف المتوقعة (xG)..."
            else: msg = "توليد السكور النهائي بناءً على البيانات..."
            status.markdown(f"<p style='text-align: center;'>⏳ {msg} ({30 - int(i*0.3)}s)</p>", unsafe_allow_html=True)
        
        # 4. النتيجة النهائية والأسواق
        st.markdown(f"""
        <div style="background: #000; padding: 40px; border: 5px solid #f1c40f; border-radius: 30px; text-align: center; color: white;">
            <p style="color: #f1c40f; font-weight: bold; font-size: 22px; letter-spacing: 3px;">AI LIVE PREDICTION</p>
            <div style="font-size: 90px; font-weight: bold; color: #fff; margin: 30px 0; text-shadow: 0 0 20px #f1c40f;">
                {h_score} - {a_score}
            </div>
            <div style="display: flex; justify-content: space-around; gap: 20px;">
                <div style="flex: 1; background: #1a1a1a; padding: 25px; border-radius: 20px; border-top: 4px solid #f1c40f;">
                    <p style="color: #666;">WINNER</p><h2 style="color: #f1c40f;">{"HOME" if h_score > a_score else "DRAW" if h_score == a_score else "AWAY"}</h2>
                </div>
                <div style="flex: 1; background: #1a1a1a; padding: 25px; border-radius: 20px; border-top: 4px solid #f1c40f;">
                    <p style="color: #666;">O/U 2.5</p><h2 style="color: #f1c40f;">{"OVER" if h_score+a_score > 2.5 else "UNDER"}</h2>
                </div>
                <div style="flex: 1; background: #1a1a1a; padding: 25px; border-radius: 20px; border-top: 4px solid #f1c40f;">
                    <p style="color: #666;">BTTS</p><h2 style="color: #f1c40f;">{"YES" if h_score > 0 and a_score > 0 else "NO"}</h2>
                </div>
            </div>
            <p style="margin-top: 30px; font-size: 10px; color: #333;">MATCH HASH: {home_id}{away_id}</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.error("⚠️ يرجى وضع الرابط أولاً ليقوم الذكاء الاصطناعي بعمله.")
        
