import streamlit as st
import math
import time

st.set_page_config(page_title="SNIPER V123.0 - AUTO FLEX", layout="wide")

def poisson_calc(k, lmbda):
    if lmbda <= 0: lmbda = 0.01
    return (lmbda**k * math.exp(-lmbda)) / math.factorial(k)

st.title("🛡️ محرك التحليل المرن (Auto-Flex Logic)")

# --- مدخلات البيانات ---
col_h, col_a = st.columns(2)
with col_h:
    h_name = st.text_input("🏠 الفريق المضيف:", "Nigeria")
    h_id = st.text_input("🆔 بصمة المضيف:", "NGA-92xV5zP_Str88")
with col_a:
    a_name = st.text_input("✈️ الفريق الضيف:", "Tanzania")
    a_id = st.text_input("🆔 بصمة الضيف:", "TAN-41kM3tL_Low62")

if st.button("🚀 تشغيل المحلل الذكي"):
    with st.spinner('⏳ جاري تفكيك الرموز وتحديد احتمالات الاختراق...'):
        time.sleep(1)

    # دالة التفكيك والتحليل المرن
    def analyze_flex(id_text, role="h"):
        # استخراج الأرقام
        nums = [int(s) for s in "".join((c if c.isdigit() else " ") for c in id_text).split()]
        atk = nums[-1] if role == "h" else nums[0]
        dfns = nums[0] if role == "h" else nums[-1]
        
        # البحث عن رموز المرونة (الاختراق)
        flex_factor = 1.0
        if any(key in id_text for key in ["kM", "Spd", "Str", "xV"]):
            flex_factor = 1.4  # منح مرونة هجومية آلية
        return atk, dfns, flex_factor

    h_atk, h_def, h_flex = analyze_flex(h_id, "h")
    a_atk, a_def, a_flex = analyze_flex(a_id, "a")

    # --- معادلة التصادم المرن (Flex-Clash Equation) ---
    # أهداف المضيف: هجومه ضد دفاع الضيف مع معامل المرونة الخاص به
    h_mu = ((h_atk / a_def) * 1.5) * h_flex
    
    # أهداف الضيف: هجومه ضد دفاع المضيف مع معامل المرونة (لمنع الـ 0 الدائم)
    # هنا يتم كسر الجمود: معامل المرونة يضمن وجود فرصة هدف حتى لو الأرقام ضعيفة
    a_mu = ((a_atk / h_def) * 1.1) * a_flex

    # حساب مصفوفة 0-0 إلى 5-5
    outcomes = []
    for h in range(6):
        for a in range(6):
            p = poisson_calc(h, h_mu) * poisson_calc(a, a_mu)
            outcomes.append({'s': f"{h}-{a}", 'p': p, 'h': h, 'a': a})
    
    outcomes.sort(key=lambda x: x['p'], reverse=True)
    final = outcomes[0]

    # --- العرض الاحترافي للطباعة ---
    st.markdown(f"""
    <div style="background-color: #ffffff; padding: 45px; border: 12px solid #1e1e1e; border-radius: 20px; text-align: center; color: #1e1e1e;">
        <h2 style="color: #666; font-weight: bold; margin-bottom: 20px;">التحليل الرمزي للمواجهة</h2>
        <div style="display: flex; justify-content: space-around; align-items: center; margin-bottom: 30px;">
            <h1 style="font-size: 50px; flex: 1;">{h_name}</h1>
            <div style="background: #1e1e1e; color: #f1c40f; padding: 25px 50px; border-radius: 15px; font-size: 85px; font-weight: bold; flex: 0.5;">
                {final['s']}
            </div>
            <h1 style="font-size: 50px; flex: 1;">{a_name}</h1>
        </div>
        <div style="background: #fdfdfd; padding: 15px; border-radius: 10px; border: 2px dashed #ddd;">
             <p style="font-size: 18px; color: #2ecc71; font-weight: bold; margin: 0;">✅ ميزان مرن: تم احتساب قوة الاختراق الرمزي آلياً</p>
             <p style="font-size: 14px; color: #7f8c8d;">ID Check: {h_id} vs {a_id}</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ملخص الأسواق
    st.markdown("---")
    st.subheader("📋 ملخص الأسواق المطبوع:")
    c1, c2, c3 = st.columns(3)
    c1.info(f"🏆 التوقع: {'1' if final['h'] > final['a'] else ('2' if final['a'] > final['h'] else 'X')}")
    c2.warning(f"📈 الأهداف: {'OVER 2.5' if (final['h']+final['a']) >= 2.5 else 'UNDER 2.5'}")
    c3.success(f"⚽ BTTS: {'YES' if final['a'] > 0 else 'NO'}")
    
