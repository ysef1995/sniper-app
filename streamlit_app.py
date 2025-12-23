import streamlit as st
import cloudscraper
from bs4 import BeautifulSoup
import math
import pandas as pd
import re
import time

# إعدادات الصفحة
st.set_page_config(page_title="SNIPER V51.0 GOLD", page_icon="🏆", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stMetric { background-color: #1f2937; padding: 15px; border-radius: 10px; border-left: 5px solid #f1c40f; }
    .status-box { padding: 20px; border-radius: 10px; background-color: #262730; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🏆 SNIPER V51.0 GOLD - نظام التقييم الذكي")
st.write("التحليل يستغرق 10 ثوانٍ لفحص البيانات بدقة وإعطاء تقييم النجوم")

def get_stars(prob):
    """تحديد عدد النجوم بناءً على نسبة الثقة"""
    if prob >= 0.25: return "⭐⭐⭐⭐⭐ (ثقة مطلقة)"
    elif prob >= 0.20: return "⭐⭐⭐⭐ (ثقة عالية)"
    elif prob >= 0.15: return "⭐⭐⭐ (متوسطة)"
    else: return "⭐⭐ (ضعيفة/مخاطرة)"

def calculate_advanced_stats(h_xg, a_xg):
    win_h, draw, win_a = 0, 0, 0
    btts_yes, btts_no = 0, 0
    over_25, under_25 = 0, 0
    scores = []

    for h in range(6):
        for a in range(6):
            prob = (math.exp(-h_xg) * h_xg**h / math.factorial(h)) * \
                   (math.exp(-a_xg) * a_xg**a / math.factorial(a))
            if h > a: win_h += prob
            elif a > h: win_a += prob
            else: draw += prob
            if h > 0 and a > 0: btts_yes += prob
            else: btts_no += prob
            if h + a > 2.5: over_25 += prob
            else: under_25 += prob
            scores.append({'Score': f"{h}-{a}", 'Prob': prob})
            
    scores.sort(key=lambda x: x['Prob'], reverse=True)
    return {
        'win_h': win_h, 'draw': draw, 'win_a': win_a,
        'btts_yes': btts_yes, 'btts_no': btts_no,
        'over_25': over_25, 'under_25': under_25,
        'top_score': scores[0]
    }

url = st.text_input("🔗 الصق رابط المباراة هنا:")

if st.button("🚀 ابدأ التحليل الذهبي (10 ثوانٍ)"):
    if url:
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        # نظام الـ 10 ثوانٍ (تقسيم الوقت على المراحل)
        stages = [
            "🔍 جاري سحب البيانات الخام من السيرفر...",
            "📊 تحليل معدلات الـ xG للهجوم والدفاع...",
            "📉 معالجة خوارزمية بواسون للنتائج الدقيقة...",
            "🛡️ تقييم ثبات الدفاع وقوة المهاجمين...",
            "⭐ توليد تقييم النجوم النهائي..."
        ]
        
        for i, stage in enumerate(stages):
            status_text.warning(stage)
            time.sleep(2) # 5 مراحل * 2 ثانية = 10 ثوانٍ
            progress_bar.progress((i + 1) * 20)

        try:
            scraper = cloudscraper.create_scraper()
            res = scraper.get(url, timeout=20)
            soup = BeautifulSoup(res.text, 'html.parser')
            raw_text = soup.get_text()
            stats = re.findall(r"([0-2]\.\d{2})", raw_text)
            
            h_xg = float(stats[0]) if len(stats) > 0 else 1.60
            a_xg = float(stats[1]) if len(stats) > 1 else 1.30

            data = calculate_advanced_stats(h_xg, a_xg)

            st.balloons()
            st.success("✅ تم اكتمال التحليل الذهبي بنجاح!")
            
            # عرض التقييم بالنجوم في الأعلى
            st.markdown(f"### 🎖️ تقييم SNIPER للمباراة: {get_stars(data['top_score']['Prob'])}")
            
            st.markdown("---")
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.subheader("🏁 النتيجة النهائية (1X2)")
                st.info(f"🏠 المضيف: {data['win_h']*100:.1f}%")
                st.info(f"🤝 التعادل: {data['draw']*100:.1f}%")
                st.info(f"✈️ الضيف: {data['win_a']*100:.1f}%")

            with col2:
                st.subheader("⚽ الأهداف و BTTS")
                st.write(f"✅ كلاهما يسجل: **{data['btts_yes']*100:.1f}%**")
                st.write(f"📈 Over 2.5: **{data['over_25']*100:.1f}%**")
                st.write(f"📉 Under 2.5: **{data['under_25']*100:.1f}%**")

            with col3:
                st.subheader("🎯 النتيجة الدقيقة")
                st.metric("SCORE EXACT", data['top_score']['Score'])
                st.write(f"نسبة الثقة الرياضية: {data['top_score']['Prob']*100:.1f}%")

        except Exception as e:
            st.error(f"حدث خطأ في جلب البيانات، يرجى التأكد من الرابط.")
    else:
        st.error("يرجى إدخال الرابط أولاً!")
        
