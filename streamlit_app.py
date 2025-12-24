import streamlit as st
import math

def poisson_calc(k, lmbda):
    if lmbda <= 0: lmbda = 0.01
    return (lmbda**k * math.exp(-lmbda)) / math.factorial(k)

st.title("🎯 المحلل الدقيق (Precision Logic V129)")

# مدخلات الرموز
h_id = st.text_input("🆔 بصمة المضيف:", "RDC-88yV_Str75")
a_id = st.text_input("🆔 بصمة الضيف:", "BEN-35Low_Res82")

if st.button("🚀 استخراج السكور الحقيقي"):
    # دالة استخراج الأرقام
    def parse(id_t, pos):
        n = [int(s) for s in "".join((c if c.isdigit() else " ") for c in id_t).split()]
        return (n[-1], n[0]) if pos == "h" else (n[0], n[-1])

    h_atk, h_def = parse(h_id, "h")
    a_atk, a_def = parse(a_id, "a")

    # --- ميزان القوى المنضبط (The Precision Balance) ---
    # أهداف المضيف: تم تقليل المعامل ليكون 1.1 لضمان الواقعية
    gap_h = h_atk / a_def
    h_mu = gap_h * 1.1 
    
    # أهداف الضيف: تعتمد كلياً على وجود رمز الاختراق kM وقوة الهجوم
    if "kM" in a_id and a_atk > 45:
        a_mu = (a_atk / h_def) * 1.2
        a_mu = max(a_mu, 0.75) # يمنح هدفاً واحداً فقط في المباريات المفتوحة
    else:
        a_mu = 0.15 # يضمن صفر للضيف في المباريات المغلقة مثل الكونغو

    # حساب الاحتمالات
    res = []
    for h in range(5):
        for a in range(5):
            p = poisson_calc(h, h_mu) * poisson_calc(a, a_mu)
            res.append({'s': f"{h}-{a}", 'p': p, 'h': h, 'a': a})
    
    res.sort(key=lambda x: x['p'], reverse=True)
    final = res[0]

    st.success(f"النتيجة المتوقعة: {final['s']}")
    
