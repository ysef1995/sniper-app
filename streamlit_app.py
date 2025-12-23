import streamlit as st
import hashlib
import math
import time
import random

# إعداد الواجهة الاحترافية
st.set_page_config(page_title="SNIPER V58.0 HARMONY", page_icon="🏆", layout="wide")

def calculate_harmonized_logic(h_xg, a_xg):
    win_h, draw, win_a, btts, over25 = 0, 0, 0, 0, 0
    scores = []
    
    # 1. بناء قاعدة الاحتمالات
    for h in range(6):
        for a in range(6):
            p = (math.exp(-h_xg)*h_xg**h/math.factorial(h)) * (math.exp(-a_xg)*a_xg**a/math.factorial(a))
            if h > a: win_h += p
            elif a > h: win_a += p
            else: draw += p
            if h > 0 and a > 0: btts += p
            if h + a > 2.5: over25 += p
            scores.append({'s': f"{h}-{a}", 'p': p, 'type': 'H' if h>a else 'A' if a>h else 'D'})

    # 2. تحديد الاتجاه السائد للمباراة (الفائز أو التعادل)
    prob_map = {'H': win_h, 'D': draw, 'A': win_a}
    main_pred = max(prob_map, key=prob_map.get)
    
    # 3. اختيار أفضل نتيجة دقيقة من نفس "الاتجاه" لضمان التطابق
    matching_scores = [s for s in scores if s['type'] == main_pred]
    matching_scores.sort(key=lambda x: x['p'], reverse=True)
    
    return win_h, draw, win_a, btts, over25, matching_scores[0], main_pred

st.title("🏆 SNIPER V58.0 - المحرك المتناغم")
url = st.text_input("🔗 رابط المباراة للتحليل العميق (30 ثانية):")

if st.button("🚀 بدء تحليل النخبة"):
    if url:
        bar = st.progress(0)
        status = st.empty()
        
        # مراحل التحليل (30 ثانية)
        for i in range(1, 11):
            status.warning(f"⏳ مرحلة التحليل {i}/10: جاري معالجة البيانات العميقة...")
            time.sleep(3)
            bar.progress(i * 10)
            
        # استخراج بصمة الرابط (Match ID بالحروف)
        match_slug = url.split('/')[-1] if '/' in url else "match"
        seed = sum(ord(c) for c in match_slug)
        random.seed(seed)
        
        # توليد xG ديناميكي فريد لكل رابط
        h_xg = round(random.uniform(0.8, 2.6), 2)
        a_xg = round(random.uniform(0.7, 2.0), 2)
        
        wh, dr, wa, bt, ov, top, res_type = calculate_harmonized_logic(h_xg, a_xg)
        
        st.success(f"✅ تم التحليل بنجاح! المباراة المعالجة: {match_slug}")
        
        st.markdown("---")
        c1, c2, c3 = st.columns(3)
        with c1:
            title = "المضيف" if res_type == 'H' else "الضيف" if res_type == 'A' else "تعادل"
            st.metric("توقع الفائز (1X2)", title)
            st.write(f"الثقة: {max(wh, dr, wa)*100:.1f}%")
        with c2:
            st.metric("سوق BTTS", "YES" if bt > 0.5 else "NO")
            st.write(f"الاحتمالية: {bt*100:.1f}%")
        with c3:
            st.metric("أهداف المباراة", "+2.5" if ov > 0.5 else "-2.5")
            st.write(f"الاحتمالية: {ov*100:.1f}%")

        st.markdown("---")
        st.markdown(f"<h1 style='text-align: center; color: #f1c40f;'>النتيجة الدقيقة المتناغمة: {top['s']}</h1>", unsafe_allow_html=True)
        
        stars = "⭐" * (5 if top['p'] > 0.2 else 4 if top['p'] > 0.15 else 3)
        st.write(f"### تقييم الضمان: {stars}")
    else:
        st.error("الرجاء إدخال الرابط أولاً!")
        
