import streamlit as st
import math
import time

st.set_page_config(page_title="SNIPER V121.0 - LOGIC ONLY", layout="wide")

def poisson_calc(k, lmbda):
    if lmbda <= 0: lmbda = 0.01
    return (lmbda**k * math.exp(-lmbda)) / math.factorial(k)

st.title("⚖️ المحلل المنطقي الصارم (Strict Numerical Decoder)")

# --- مدخلات الرموز والأسماء ---
col_h, col_a = st.columns(2)
with col_h:
    h_name = st.text_input("🏠 فريق المضيف:", "Nigeria")
    h_id = st.text_input("🆔 بصمة المضيف:", "NGA-92xV5zP_Str88")
with col_a:
    a_name = st.text_input("✈️ فريق الضيف:", "Tanzania")
    a_id = st.text_input("🆔 بصمة الضيف:", "TAN-41kM3tL_Low62")

if st.button("🚀 استخراج النتيجة المنطقية"):
    with st.spinner('⏳ جاري حساب التوازن الرقمي بين الرموز...'):
        time.sleep(1)

    # دالة استخراج القيم الرقمية بدقة
    def get_digits(text):
        nums = [int(s) for s in "".join((c if c.isdigit() else " ") for c in text).split()]
        return nums if nums else [50]

    # تحليل القيم
    h_vals = get_digits(h_id)
    a_vals = get_digits(a_id)
    
    # تحديد الهجوم والدفاع بناءً على مكان الرقم في الـ ID
    h_atk = h_vals[-1] if len(h_vals) > 0 else 50 # الرقم الأخير غالباً هو القوة (Str88)
    h_def = h_vals[0] if len(h_vals) > 0 else 50  # الرقم الأول هو الصلابة (92xV)
    
    a_atk = a_vals[0] if len(a_vals) > 0 else 40  # للضيف الرقم الأول هجومي (41kM)
    a_def = a_vals[-1] if len(a_vals) > 0 else 40 # الرقم الأخير دفاعي (Low62)

    # --- ميزان القوى الرياضي ---
    # القوة الصافية للمضيف = (هجومه - دفاع خصمه)
    h_net = (h_atk - a_def) 
    # القوة الصافية للضيف = (هجومه - دفاع خصمه)
    a_net = (a_atk - h_def)

    # تحويل القوة لـ أهداف (Lambda)
    h_mu = max(0.1, (h_net / 20) + 1.0)
    a_mu = max(0.1, (a_net / 30) + 0.5)

    # حساب مصفوفة 0-0 إلى 5-5
    results = []
    for h in range(6):
        for a in range(6):
            p = poisson_calc(h, h_mu) * poisson_calc(a, a_mu)
            results.append({'s': f"{h}-{a}", 'p': p, 'h': h, 'a': a})
    
    results.sort(key=lambda x: x['p'], reverse=True)
    final = results[0]

    # --- عرض النتيجة بأسلوب الطباعة ---
    st.markdown(f"""
    <div style="background-color: #ffffff; padding: 40px; border: 12px solid #1e1e1e; border-radius: 20px; text-align: center; color: #1e1e1e;">
        <h2 style="color: #666; font-weight: bold;">التحليل الرمزي للمواجهة</h2>
        <div style="display: flex; justify-content: space-around; align-items: center; margin: 30px 0;">
            <h1 style="font-size: 55px; flex: 1;">{h_name}</h1>
            <div style="background: #1e1e1e; color: #f1c40f; padding: 20px 45px; border-radius: 12px; font-size: 85px; font-weight: bold; flex: 0.6;">
                {final['s']}
            </div>
            <h1 style="font-size: 55px; flex: 1;">{a_name}</h1>
        </div>
        <div style="background: #f8f9fa; padding: 15px; border-radius: 10px; border: 1px solid #ddd;">
             <p style="font-size: 18px; margin: 0;">📊 <b>ميزان القوى:</b> {h_atk} هجوم ضد {a_def} دفاع | {a_atk} هجوم ضد {h_def} دفاع</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # الأسواق
    st.markdown("---")
    st.subheader("📋 ملخص الأسواق المطبوع:")
    c1, c2, c3 = st.columns(3)
    c1.info(f"🏆 التوقع: {'1' if final['h'] > final['a'] else ('2' if final['a'] > final['h'] else 'X')}")
    c2.warning(f"📈 الأهداف: {'OVER 2.5' if (final['h']+final['a']) >= 2.5 else 'UNDER 2.5'}")
    c3.success(f"⚽ BTTS: {'YES' if final['a'] > 0 else 'NO'}")
    
