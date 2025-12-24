import streamlit as st
import math
import time

# إعداد واجهة البرنامج
st.set_page_config(page_title="SNIPER V128.0 - FINAL MASTER", layout="wide")

def poisson_calc(k, lmbda):
    if lmbda <= 0: lmbda = 0.01
    return (lmbda**k * math.exp(-lmbda)) / math.factorial(k)

st.title("🎯 المحلل الرمزي الشامل (The Ultimate Analyst)")

# --- 1. مدخلات البيانات ---
col_h, col_a = st.columns(2)
with col_h:
    h_name = st.text_input("🏠 الفريق المضيف:", "Nigeria")
    h_id = st.text_input("🆔 بصمة المضيف:", "NGA-82yV_Str91")
with col_a:
    a_name = st.text_input("✈️ الفريق الضيف:", "Tanzania")
    a_id = st.text_input("🆔 بصمة الضيف:", "TAN-62kM_Res72")

if st.button("🚀 تحليل المواجهة بالمنطق الموحد"):
    with st.spinner('⏳ جاري تفكيك الرموز وتحليل ميزان القوى...'):
        time.sleep(1.5)

    # دالة استخراج البيانات (المواقع المتقاطعة)
    def get_match_data(id_text, role):
        nums = [int(s) for s in "".join((c if c.isdigit() else " ") for c in id_text).split()]
        atk = nums[-1] if role == "h" else nums[0]
        dfns = nums[0] if role == "h" else nums[-1]
        has_flex = any(k in id_text for k in ["kM", "Spd", "Str"])
        return atk, dfns, has_flex

    h_atk, h_def, h_flex = get_match_data(h_id, "h")
    a_atk, a_def, a_flex = get_match_data(a_id, "a")

    # --- 2. وحدة التحليل النصي الذكي ---
    comments = []
    # تحليل المضيف
    if h_atk > 88: comments.append(f"✅ **هجوم كاسح:** {h_name} يمتلك قوة ضاربة ({h_atk}) قادرة على تمزيق التكتلات.")
    elif h_atk > 70: comments.append(f"✅ **هجوم منظم:** {h_name} يمتلك فاعلية جيدة أمام المرمى.")
    
    # تحليل الدفاع والاختراق
    if a_flex:
        comments.append(f"⚠️ **تحذير اختراق:** تم رصد رمز (kM/Spd) للضيف، مما يفتح ثغرة لهدف مباغت.")
    else:
        comments.append(f"🛡️ **ثبات دفاعي:** لا توجد مؤشرات اختراق واضحة للضيف، المباراة تميل لـ Clean Sheet.")

    # --- 3. معادلة السكور (المحرك الديناميكي) ---
    # حساب أهداف المضيف بناءً على الفجوة
    gap_h = h_atk - a_def
    if gap_h >= 30: h_mu = 3.3   # يوجه لـ 3 أهداف (مثل تونس)
    elif gap_h >= 12: h_mu = 2.2 # يوجه لـ 2 أهداف (مثل نيجيريا)
    else: h_mu = 1.1            # يوجه لـ 1 هدف (مثل الكونغو)

    # حساب أهداف الضيف (منع التصفير التلقائي)
    gap_a = a_atk - h_def
    a_mu = (a_atk / h_def) * 1.3
    if a_flex and gap_a > -50: 
        a_mu = max(a_mu, 0.96) # ضمان هدف 2-1 أو 3-1
    else: 
        a_mu = min(a_mu, 0.3)  # ضمان 1-0 أو 3-0

    # حساب مصفوفة الاحتمالات
    results = []
    for h in range(6):
        for a in range(6):
            p = poisson_calc(h, h_mu) * poisson_calc(a, a_mu)
            results.append({'s': f"{h}-{a}", 'p': p, 'h': h, 'a': a})
    results.sort(key=lambda x: x['p'], reverse=True)
    final = results[0]

    # --- 4. العرض النهائي للطباعة ---
    st.markdown(f"""
    <div style="background-color: #ffffff; padding: 40px; border: 12px solid #1e1e1e; border-radius: 20px; color: #1e1e1e;">
        <h2 style="text-align: center; color: #1e1e1e; font-weight: bold;">📊 تقرير المحلل الفني الشامل</h2>
        <div style="background: #fdf2d0; padding: 20px; border-radius: 12px; margin: 20px 0; border-right: 8px solid #f1c40f;">
            <h4 style="margin-top:0;">🔍 رؤية المحرك:</h4>
            {"<p style='margin-bottom:5px;'>" + "</p><p style='margin-bottom:5px;'>".join(comments) + "</p>"}
        </div>
        <div style="display: flex; justify-content: space-around; align-items: center; margin: 30px 0;">
            <h1 style="font-size: 45px; flex: 1; text-align: center;">{h_name}</h1>
            <div style="background: #1e1e1e; color: #f1c40f; padding: 20px 45px; border-radius: 15px; font-size: 80px; font-weight: bold; flex: 0.6; text-align: center;">
                {final['s']}
            </div>
            <h1 style="font-size: 45px; flex: 1; text-align: center;">{a_name}</h1>
        </div>
        <p style="text-align: center; color: #7f8c8d; font-size: 14px;">بصمة المواجهة المتقاطعة: {h_id} VS {a_id}</p>
    </div>
    """, unsafe_allow_html=True)

    # ملخص الأسواق
    st.markdown("---")
    st.subheader("📋 ملخص الأسواق المعتمد:")
    c1, c2, c3 = st.columns(3)
    c1.info(f"🏆 الفوز: {'المضيف (1)' if final['h'] > final['a'] else 'X2'}")
    c2.warning(f"📈 الأهداف: {'OVER 2.5' if (final['h']+final['a']) >= 2.5 else 'UNDER 2.5'}")
    c3.success(f"⚽ BTTS: {'YES' if final['a'] > 0 else 'NO'}")
    
