import hashlib
import math

def calculate_poisson_probability(lmbda, x):
    """حساب احتمالية تسجيل عدد معين من الأهداف"""
    return (exp(-lmbda) * (lmbda**x)) / math.factorial(x)

def generate_sur_ia_dashboard(team_h, team_a, xG_h, xG_a, ppg_h, ppg_a, form_h, form_a, odds):
    # 1. توقع النتيجة الدقيقة (Correct Score) بناءً على الـ xG
    score_h = round(xG_h)
    score_a = round(xG_a)
    
    # 2. تحليل الأسواق (Market Analysis)
    # سوق 1x2
    main_market = "1" if xG_h > xG_a + 0.5 else ("2" if xG_a > xG_h + 0.5 else "X")
    
    # سوق Over/Under 2.5
    total_expected_goals = xG_h + xG_a
    ou_25 = "Over 2.5" if total_expected_goals > 2.5 else "Under 2.5"
    
    # سوق BTTS (كلا الفريقين يسجل)
    btts = "YES" if xG_h > 0.8 and xG_a > 0.8 else "NO"

    # 3. توليد الـ IDs المشفرة (التنسيق الذهبي)
    def create_id(name, ppg, xg, form):
        base = f"{name[:2].upper()}-{int(ppg*100)}-{int(xg*100)}-{form[:3].upper()}"
        return f"{base}-{hashlib.md5(base.encode()).hexdigest()[:4].upper()}"

    home_id = create_id(team_h, ppg_h, xG_h, form_h)
    away_id = create_id(team_a, ppg_a, xG_a, form_a)

    # طباعة المخرجات الاحترافية
    print(f"\n{'='*45}")
    print(f"🏆 MATCH SUR IA - PRO DASHBOARD 🏆")
    print(f"{'='*45}")
    print(f"🏟️ MATCH: {team_h} VS {team_a}")
    print(f"🎯 AI PREDICTED SCORE: {score_h} - {score_a}")
    print(f"{'-'*45}")
    print(f"📊 TEAM IDs:")
    print(f"ID_HOME: {home_id}")
    print(f"ID_AWAY: {away_id}")
    print(f"{'-'*45}")
    print(f"💰 STRATEGY & MARKETS:")
    print(f"▣ Market 1X2: {main_market}")
    print(f"▣ Goals O/U: {ou_25} ({total_expected_goals:.2f})")
    print(f"▣ BTTS:       {btts}")
    print(f"▣ Market ID:  M-{hashlib.md5(str(odds).encode()).hexdigest()[:6].upper()}")
    print(f"{'='*45}\n")

# مثال للتشغيل (بيانات مباراة الجزائر والسودان)
generate_sur_ia_dashboard(
    "Algeria", "Sudan", 
    xG_h=2.10, xG_a=0.45, 
    ppg_h=2.4, ppg_a=0.9, 
    form_h="WWWDW", form_a="LLDLW",
    odds=[1.40, 4.50, 8.00]
)
