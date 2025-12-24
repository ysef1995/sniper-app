import hashlib
import time

def generate_id(team_data):
    # دمج البيانات لإنشاء بصمة فريدة (PPG, xG, Form)
    raw_str = f"{team_data['name']}{team_data['ppg']}{team_data['xg']}{team_data['form']}"
    return hashlib.md5(raw_str.encode()).hexdigest()[:12].upper()

def generate_odds_id(odds_data):
    # تشفير شامل لأسواق 1X2, O/U 2.5, BTTS
    raw_odds = f"{odds_data['1x2']}{odds_data['ou25']}{odds_data['btts']}"
    return "ODDS-" + hashlib.sha1(raw_odds.encode()).hexdigest()[:10].upper()

def display_stream_dashboard(home_team, away_team, odds):
    # توليد الرموز
    home_id = generate_id(home_team)
    away_id = generate_id(away_team)
    market_id = generate_odds_id(odds)

    # التنسيق النهائي الذي سيظهر للمشاهدين (التنسيق الذهبي)
    print("\n" + " " * 10 + "🚀 SYSTEM MATCH SUR IA ACTIVATED 🚀")
    print("═" * 60)
    
    # عرض الفريق الأول
    print(f"  [HOME] {home_team['name'].upper()}")
    print(f"  ID MATCH SUR IA: {home_id}")
    print("─" * 60)
    
    # عرض الفريق الثاني
    print(f"  [AWAY] {away_team['name'].upper()}")
    print(f"  ID MATCH SUR IA: {away_id}")
    print("═" * 60)
    
    # عرض الـ ID الخاص بجميع الأسواق في الأسفل
    print(f"  📊 GLOBAL MARKET ID (1X2, O/U, BTTS):")
    print(f"  {market_id}")
    print("═" * 60)
    print(" " * 12 + "READY FOR PREDICTION ANALYSIS")

# --- إدخال البيانات (مثال لمباراة الجزائر والسودان) ---
home = {
    "name": "Algeria",
    "ppg": 2.45,
    "xg": 1.88,
    "form": "WWWDW"
}

away = {
    "name": "Sudan",
    "ppg": 0.92,
    "xg": 0.74,
    "form": "LDLLW"
}

# أسواق 1X2، الأهداف، وتسجيل الطرفين
current_odds = {
    "1x2": [1.42, 4.15, 8.20],
    "ou25": "UNDER",
    "btts": "NO"
}

# تشغيل العرض
display_stream_dashboard(home, away, current_odds)
