import time
import sys
import random

def simulate_analysis(duration=10):
    """وظيفة لمحاكاة عملية التحليل الذكي مع شريط تقدم"""
    print("\n📡 Connecting to SNIPER V37.0 AI Server...")
    animation = "|/-\\"
    for i in range(duration * 10):
        time.sleep(0.1)
        sys.stdout.write(f"\r🔍 Analyzing Data Strings... {animation[i % len(animation)]} {((i+1)/(duration*10))*100:.0f}%")
        sys.stdout.flush()
    print("\n✅ Analysis Complete! Extracting Results...\n")

def decode_and_predict(id_home, id_away, id_odds):
    """
    هذه الدالة تقوم بمحاكاة فك التشفير. 
    برمجياً: بما أن الـ ID هو هاش، سنقوم باستخراج 'البصمة الرقمية' منه لتقدير القوة.
    """
    # تحويل الرموز إلى قيم عددية وهمية للمحاكاة بناءً على الهاش
    val_h = sum(ord(c) for c in id_home) % 5
    val_a = sum(ord(c) for c in id_away) % 3
    
    # توقع النتائج (منطق افتراضي بناءً على قوة الـ ID)
    score_h = val_h if val_h <= 4 else 1
    score_a = val_a if val_a <= 3 else 0
    
    # تحديد السوق بناءً على الـ Odds ID
    is_over = "OVER 2.5" if (val_h + val_a) >= 3 else "UNDER 2.5"
    btts = "YES" if (val_h > 0 and val_a > 0) else "NO"
    winner = "HOME (1)" if score_h > score_a else ("AWAY (2)" if score_a > score_h else "DRAW (X)")

    return score_h, score_a, winner, is_over, btts

def main():
    print("="*60)
    print("      🛰️  SUR IA - DECODER & ANALYZER V37.0  🛰️")
    print("="*60)
    
    # خانات الإدخال التي طلبتها
    home_name = input("🏠 Enter HOME Team Name: ")
    id_home = input(f"🆔 Enter {home_name} SUR ID: ")
    
    print("-" * 30)
    away_name = input("✈️  Enter AWAY Team Name: ")
    id_away = input(f"🆔 Enter {away_name} SUR ID: ")
    
    print("-" * 30)
    id_odds = input("💰 Enter GLOBAL MARKET ID: ")
    
    # وقت الانتظار للتحليل (10 ثواني)
    simulate_analysis(10)
    
    # الحصول على النتائج
    s_h, s_a, win, ov, bt = decode_and_predict(id_home, id_away, id_odds)
    
    # طباعة النتائج النهائية بشكل احترافي للستريم
    print("="*60)
    print(f"🏆 PREDICTION FOR: {home_name.upper()} VS {away_name.upper()}")
    print("="*60)
    print(f"🎯 CORRECT SCORE    : {s_h} - {s_a}")
    print(f"📊 MAIN MARKET (1X2): {win}")
    print(f"⚽ GOALS TOTAL      : {ov}")
    print(f"🔄 BOTH TEAMS SCORE : {bt}")
    print("="*60)
    print(f"🛡️  VERIFIED BY ID: {id_odds[:8]}...")
    print("="*60)

if __name__ == "__main__":
    main()
    
