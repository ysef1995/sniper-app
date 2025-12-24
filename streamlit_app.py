import math
import hashlib
import os

# --- وظائف التشفير الخاصة بالستريم ---
def generate_match_id(team_name, xg, ppg, rating):
    # إنشاء بصمة فريدة بناءً على قوة الفريق لتبدو احترافية
    raw_data = f"{team_name}{xg}{ppg}{rating}"
    return hashlib.md5(raw_data.encode()).hexdigest()[:12].upper()

def generate_market_id(win1, over, btts):
    # تشفير الأسواق الرئيسية الثلاثة
    raw_market = f"{win1}{over}{btts}"
    return "MARKET-" + hashlib.sha1(raw_market.encode()).hexdigest()[:10].upper()

# --- منطق الـ Sniper V37 (الذي أرفقته أنت) ---
def poisson_probability(k, lmbda):
    return (lmbda**k * math.exp(-lmbda)) / math.factorial(k)

def calculate_overall_rating(xg, xga, ppg):
    return (xg * 30) - (xga * 15) + (ppg * 20)

def main():
    # 1. إدخال البيانات يدوياً
    print("\n" + "═"*60)
    print("      🚀 INITIALIZING ID MATCH SUR IA GENERATOR 🚀")
    print("═"*60)
    
    home_name = input("🏠 Home Team Name: ")
    away_name = input("✈️  Away Team Name: ")
    
    print("\n📊 Enter Statistics for " + home_name)
    h_xg = float(input("   xG: "))
    h_xga = float(input("   xGA: "))
    h_ppg = float(input("   PPG: "))
    
    print("\n📊 Enter Statistics for " + away_name)
    a_xg = float(input("   xG: "))
    a_xga = float(input("   xGA: "))
    a_ppg = float(input("   PPG: "))
    
    print("\n💰 Enter Market Odds:")
    odd_1 = float(input("   Odd Win 1: "))
    odd_over = float(input("   Odd Over 2.5: "))
    odd_btts = float(input("   Odd BTTS Yes: "))

    # 2. المعالجة الحسابية (V37 Logic)
    h_rating = calculate_overall_rating(h_xg, h_xga, h_ppg)
    a_rating = calculate_overall_rating(a_xg, a_xga, a_ppg)
    
    # 3. توليد الرموز المشفرة للستريم
    id_home = generate_match_id(home_name, h_xg, h_ppg, h_rating)
    id_away = generate_match_id(away_name, a_xg, a_ppg, a_rating)
    id_market = generate_market_id(odd_1, odd_over, odd_btts)

    # 4. طباعة النتيجة النهائية (التنسيق الذهبي للستريم)
    os.system('cls' if os.name == 'nt' else 'clear') # تنظيف الشاشة لعرض النتيجة فقط
    print("\n\n")
    print(" " * 10 + "🛡️  SYSTEM DATA DECODED SUCCESSFULLY  🛡️")
    print("═" * 60)
    
    # عرض الفريق الأول
    print(f"  [TEAM A] {home_name.upper()}")
    print(f"  ID MATCH SUR IA: {id_home}")
    print("─" * 60)
    
    # عرض الفريق الثاني
    print(f"  [TEAM B] {away_name.upper()}")
    print(f"  ID MATCH SUR IA: {id_away}")
    print("═" * 60)
    
    # عرض ID السوق الشامل
    print(f"  📊 GLOBAL MARKET MASTER ID:")
    print(f"  {id_market}")
    print("═" * 60)
    print(" " * 15 + "🛰️  READY FOR BROADCAST")
    print("\n\n")

if __name__ == "__main__":
    main()
    
