import streamlit as st
import math
import time

# --- إعدادات الواجهة ---
st.set_page_config(page_title="SNIPER V72.0 DOMINANCE", page_icon="🚜", layout="wide")

# --- منطق سكريبت V37.0 الأصلي (الخاص بك) ---
def poisson_probability(k, lmbda):
    return (lmbda**k * math.exp(-lmbda)) / math.factorial(k)

def calculate_overall_rating(xg, xga, ppg):
    return (xg * 30) - (xga * 15) + (ppg * 20)

def calculate_total_form_factor(ppg, form_string):
    form_factor = 1.0
    try:
        w, d, l = map(int, form_string.split('-'))
        form_factor += (w * 0.02) - (l * 0.02)
    except: pass
    combined_factor = (form_factor * (ppg / 1.5))
    return max(0.85, min(1.15, combined_factor))

def apply_dominance_logic(home_xg, away_xg, home_rating, away_rating):
    diff = home_rating - away_rating
    if diff > 30.0: return home_xg, away_xg * 0.60, f"🚜 هيمنة {home_rating:.1f}"
    elif diff < -30.0: return home_xg * 0.60, away_xg, f"🚜 هيمنة {away_rating:.1f}"
    return home_xg, away_xg, "⚖️ مباراة متكافئة"

# --- واجهة المستخدم (الـ 4 خانات + المدخلات اليدوية) ---
st.title("🚜 SNIPER V72.0 - نظام الهيمنة المطور")

# القسم الأول: البيانات الأساسية والـ IDs
col_names, col_ids = st.columns(2)
with col_names:
    h_team = st.text_input("🏠 الفريق المضيف:", "Tunisie")
    a_team = st.text_input("✈️ الفريق الضيف:", "Ouganda")
with col_ids:
    h_id = st.text_input("🆔 ID المضيف:", "101")
    a_id = st.text_input("🆔 ID الضيف:", "102")

st.markdown("---")

# القسم الثاني: إحصائيات سكريبت V37.0
st.subheader("📊 بيانات القوة (V37.0 Stats)")
c1, c2 = st.columns(2)
with c1:
    st.markdown(f"**إحصائيات {h_team}**")
    h_xg = st.number_input("xG (Home):", value=1.8)
    h_xga = st.number_input("xGA (Home):", value=1.1)
    h_ppg = st.number_input("PPG (Home):", value=2.1)
    h_form = st.text_input("Form (W-D-L) M:", "4-1-0")

with c2:
    st.markdown(f"**إحصائيات {a_team}**")
    a_xg = st.number_input("xG (Away):", value=0.9)
    a_xga = st.number_input("xGA (Away):", value=1.7)
    a_ppg = st.number_input("PPG (Away):", value=0.8)
    a_form = st.text_input("Form (W-D-L) A:", "1-1-3")

st.markdown("---")

# القسم الثالث: الأودز اليدوية لجميع الأسواق
st.subheader("💰 أودز الأسواق (Manual Odds)")
o1, o2, o3 = st.columns(3)
with o1:
    odd_h = st.number_input(f"Odd Win {h_team}:", value=1.45)
    odd_d = st.number_input("Odd Draw:", value=4.20)
    odd_a = st.number_input(f"Odd Win {a_team}:", value=7.80)
with o2:
    odd_o25 = st.number_input("Odd Over 2.5:", value=1.85)
    odd_u25 = st.number_input("Odd Under 2.5:", value=1.95)
with o3:
    odd_by = st.number_input("Odd BTTS Yes:", value=2.10)
    odd_bn = st.number_input("Odd BTTS No:", value=1.75)

if st.button("🚀 تشغيل محرك الهيمنة (30 ثانية)"):
    status = st.empty()
    bar = st.progress(0)
    
    # محاكاة تحليل السكريبت
    for i in range(1, 101):
        status.info(f"🚜 جاري معالجة منطق الهيمنة... {i}%")
        time.sleep(0.3)
        bar.progress(i)

    # 1. حساب التصنيفات
    h_rate = calculate_overall_rating(h_xg, h_xga, h_ppg)
    a_rate = calculate_overall_rating(a_xg, a_xga, a_ppg)
    
    # 2. تعديل xG المبدئي (من سكريبتك)
    final_h = h_xg * (a_xga / 1.3) * calculate_total_form_factor(h_ppg, h_form)
    final_a = a_xg * (h_xga / 1.3) * calculate_total_form_factor(a_ppg, a_form)
    
    # 3. 🔥 تطبيق منطق الهيمنة V37.0 🔥
    final_h, final_a, dom_msg = apply_dominance_logic(final_h, final_a, h_rate, a_rate)

    # 4. حساب الاحتمالات (Poisson)
    wh, dr, wa, o25, bt = 0, 0, 0, 0, 0
    scores = []
    for h in range(6):
        for a in range(6):
            p = poisson_probability(h, final_h) * poisson_probability(a, final_a)
            if h > a: wh += p
            elif a > h: wa += p
            else: dr += p
            if h+a >= 3: o25 += p
            if h>=1 and a>=1: bt += p
            scores.append({'s': f"{h}-{a}", 'p': p})
    
    scores.sort(key=lambda x: x['p'], reverse=True)
    top = scores[0]

    # --- عرض النتائج النهائية ---
    st.success(f"✅ تم التحليل: {dom_msg}")
    
    # النتيجة الكبيرة
    st.markdown(f"<h1 style='text-align: center; font-size: 60px; color: #f1c40f;'>{h_team} {top['s']} {a_team}</h1>", unsafe_allow_html=True)
    
    st.markdown("---")
    # جدول القيم (Value) بناءً على أودزك اليدوية
    st.subheader("💎 تحليل القيمة (Value Analysis)")
    v1, v2, v3 = st.columns(3)
    with v1:
        st.metric(f"قيمة فوز {h_team}", round(wh * odd_h, 2))
        st.metric("قيمة التعادل", round(dr * odd_d, 2))
    with v2:
        st.metric("قيمة Over 2.5", round(o25 * odd_o25, 2))
        st.metric("قيمة BTTS Yes", round(bt * odd_by, 2))
    with v3:
        st.metric("تقييم القوة", f"{h_rate:.1f} vs {a_rate:.1f}")
        st.write("⭐⭐⭐⭐" if wh > 0.6 else "⭐⭐⭐")
        
