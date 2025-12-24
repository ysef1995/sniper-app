import streamlit as st
import math
import time

st.set_page_config(page_title="SNIPER V125.0 - DYNAMIC GAP", layout="wide")

def poisson_calc(k, lmbda):
    if lmbda <= 0: lmbda = 0.01
    return (lmbda**k * math.exp(-lmbda)) / math.factorial(k)

st.title("⚖️ محلل الفجوة الرقمية (Dynamic Delta Logic)")

# --- 1. إدخال البيانات ---
col_h, col_a = st.columns(2)
with col_h:
    h_name = st.text_input("🏠 الفريق المضيف:", "Tunisia")
    h_id = st.text_input("🆔 بصمة المضيف:", "TUN-94xV_Dom95") # مثال لقوة كاسحة
with col_a:
    a_name = st.text_input("✈️ الفريق الضيف:", "Opponent")
    a_id = st.text_input("🆔 بصمة الضيف:", "OPP-45kM_Low55") # دفاع ضعيف

if st.button("🚀 تحليل الفجوة واستخراج السكور"):
    with st.spinner('⏳ جاري قياس "مسافة" التفوق بين الفريقين...'):
        time.sleep(1)

    # دالة استخراج الأرقام والرموز
    def parse_id(id_text, pos):
        nums = [int(s) for s in "".join((c if c.isdigit() else " ") for c in id_text).split()]
        val_atk = nums[-1] if pos == "h" else nums[0]
        val_def = nums[0] if pos == "h" else nums[-1]
        has_break = any(k in id_text for k in ["kM", "Spd", "Str"])
        return val_atk, val_def, has_break

    h_atk, h_def, h_has_break = parse_id(h_id, "h")
    a_atk, a_def, a_has_break = parse_id(a_id, "a")

    # --- منطق الفجوة الديناميكي (The Delta Logic) ---
    
    # 1. حساب أهداف المضيف بناءً على "حجم الفارق"
    delta_h = h_atk - a_def # الفارق بين هجوم المضيف ودفاع الضيف
    
    if delta_h >= 35:     # فارق ضخم (اكتساح مثل تونس)
        h_lambda = 3.1    # يوجه لـ 3 أهداف
    elif delta_h >= 20:   # فارق متوسط (مثل نيجيريا)
        h_lambda = 2.1    # يوجه لـ 2 أهداف
    elif delta_h >= 5:    # مباراة متكافئة
        h_lambda = 1.2    # يوجه لـ 1 هدف
    else:                 # المضيف أضعف
        h_lambda = 0.8

    # 2. حساب أهداف الضيف (منطق الاختراق)
    delta_a = a_atk - h_def
    
    # إذا كان هناك رمز اختراق (kM) والفارق ليس كارثياً
    if a_has_break and delta_a > -50: 
        a_lambda = 0.95 # يضمن هدفاً واحداً (الـ 2-1 أو 3-1)
    else:
        a_lambda = 0.2  # يضمن شباك نظيفة (3-0 أو 2-0)

    # حساب الاحتمالات
    results = []
    for h in range(6):
        for a in range(6):
            p = poisson_calc(h, h_lambda) * poisson_calc(a, a_lambda)
            results.append({'s': f"{h}-{a}", 'p': p, 'h': h, 'a': a})
    
    results.sort(key=lambda x: x['p'], reverse=True)
    final = results[0]

    # --- تصميم الطباعة ---
    st.markdown(f"""
    <div style="background-color: #ffffff; padding: 45px; border: 12px solid #1e1e1e; border-radius: 20px; text-align: center; color: #1e1e1e;">
        <h2 style="color: #666; font-weight: bold;">التحليل الديناميكي للمباراة</h2>
        <div style="display: flex; justify-content: space-around; align-items: center; margin: 30px 0;">
            <h1 style="font-size: 50px;">{h_name}</h1>
            <div style="background: #1e1e1e; color: #f1c40f; padding: 20px 50px; border-radius: 15px; font-size: 85px; font-weight: bold;">
                {final['s']}
            </div>
            <h1 style="font-size: 50px;">{a_name}</h1>
        </div>
        <div style="text-align: left; background: #f0f0f0; padding: 15px; border-radius: 10px;">
            <p style="margin: 5px;">📏 <b>فارق القوة للمضيف:</b> {delta_h} نقطة (يستوجب {int(h_lambda)} أهداف)</p>
            <p style="margin: 5px;">⚔️ <b>حالة الضيف:</b> {'اختراق ناجح' if final['a']>0 else 'دفاع محكم'}</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # الأسواق
    st.markdown("---")
    st.subheader("📋 ملخص الأسواق:")
    c1, c2, c3 = st.columns(3)
    c1.info(f"🏆 الفوز: {'1' if final['h'] > final['a'] else 'X2'}")
    c2.warning(f"📈 الأهداف: {'OVER 2.5' if (final['h']+final['a']) >= 2.5 else 'UNDER 2.5'}")
    c3.success(f"⚽ BTTS: {'YES' if final['a'] > 0 else 'NO'}")
    
