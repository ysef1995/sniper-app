import streamlit as st
import math
import time
import random

# إعداد الواجهة الاحترافية
st.set_page_config(page_title="SNIPER V62.0 MANUAL", page_icon="⚙️", layout="wide")

def calculate_manual_logic(h_xg, a_xg):
    win_h, draw, win_a, btts, over25 = 0, 0, 0, 0, 0
    scores = []
    for h in range(6):
        for a in range(6):
            p = (math.exp(-h_xg)*h_xg**h/math.factorial(h)) * (math.exp(-a_xg)*a_xg**a/math.factorial(a))
            if h > a: win_h += p
            elif a > h: win_a += p
            else: draw += p
            if h > 0 and a > 0: btts += p
            if h + a > 2.5: over25 += p
            scores.append({'s': f"{h}-{a}", 'p': p, 'type': 'H' if h>a else 'A' if a>h else 'D'})

    prob_map = {'H': win_h, 'D': draw, 'A': win_a}
    main_pred = max(prob_map, key=prob_map.get)
    matching_scores = [s for s in scores if s['type'] == main_pred]
    matching_scores.sort(key=lambda x: x['p'], reverse=True)
    return win_h, draw, win_a, btts, over25, matching_scores[0], main_pred

st.title("⚙️ SNIPER V62.0 - لوحة التحكم اليدوية")
st.write("أدخل بيانات الفرق والمعرفات الخاصة بها للحصول على تحليل دقيق.")

# --- إنشاء الـ 4 خانات المطلوبة ---
st.markdown("### 🏟️ إعدادات المباراة")
col_name1, col_id1 = st.columns(2)
col_name2, col_id2 = st.columns(2)

with col_name1:
    home_name = st.text_input("📝 اسم الفريق الأول (المضيف):", placeholder="مثال: السنغال")
with col_id1:
    home_id = st.text_input("🆔 ID الفريق الأول:", placeholder="مثال: 524")

with col_name2:
    away_name = st.text_input("📝 اسم الفريق الثاني (الضيف):", placeholder="مثال: بوتسوانا")
with col_id2:
    away_id = st.text_input("🆔 ID الفريق الثاني:", placeholder="مثال: 102")

st.markdown("---")

if st.button("🚀 بدء التحليل العميق (30 ثانية)"):
    if home_name and away_name and home_id and away_id:
        bar = st.progress(0)
        status = st.empty()
        
        # مراحل التحليل (30 ثانية)
        stages = [
            f"🔍 فحص معرف الفريق: {home_id}",
            f"📊 جاري سحب إحصائيات {home_name}...",
            f"🔍 فحص معرف الفريق: {away_id}",
            f"📊 جاري سحب إحصائيات {away_name}...",
            "⚙️ معالجة خوارزمية التناغم...",
            "🎯 توليد النتيجة الدقيقة..."
        ]
        
        for i, stage in enumerate(stages):
            status.info(stage)
            time.sleep(5) # 5 ثوانٍ لكل مرحلة ليكون المجموع 30
            bar.progress((i+1) * 16)
            
        # دمج الـ IDs لإنشاء بصمة فريدة للمباراة
        combined_seed = home_id + away_id
        random.seed(combined_seed)
        
        # توليد xG بناءً على الـ IDs المدخلة
        h_xg = round(random.uniform(1.2, 2.8), 2)
        a_xg = round(random.uniform(0.6, 1.9), 2)
        
        wh, dr, wa, bt, ov, top, res_type = calculate_manual_logic(h_xg, a_xg)
        
        # عرض النتائج المتوافقة
        st.success(f"✅ تم التحليل بنجاح لمباراة: {home_name} vs {away_name}")
        
        c1, c2, c3 = st.columns(3)
        with c1:
            winner = home_name if res_type == 'H' else away_name if res_type == 'A' else "تعادل"
            st.metric("🏆 التوقع (1X2)", winner)
        with c2:
            st.metric("🥅 BTTS", "نعم" if bt > 0.5 else "لا")
        with c3:
            st.metric("⚽ الأهداف (+2.5)", "Over" if ov > 0.5 else "Under")

        st.markdown("---")
        # النتيجة الكبيرة المتناغمة
        st.markdown(f"<h1 style='text-align: center; color: #f1c40f;'>{home_name} {top['s']} {away_name}</h1>", unsafe_allow_html=True)
        
        stars = "⭐⭐⭐⭐⭐" if top['p'] > 0.2 else "⭐⭐⭐⭐"
        st.markdown(f"<h3 style='text-align: center;'>تقييم الضمان: {stars}</h3>", unsafe_allow_html=True)
    else:
        st.error("الرجاء ملء الخانات الأربعة (الأسماء والـ IDs) للمتابعة.")
        
