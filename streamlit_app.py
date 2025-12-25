import customtkinter as ctk
import cloudscraper
import threading
import time

# إعدادات الواجهة
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

class SofaPredictor(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("SOFASCORE REAL-DATA IA")
        self.geometry("600x500")
        self.scraper = cloudscraper.create_scraper() # لتجاوز الحماية

        # التصميم (UI)
        self.label_title = ctk.CTkLabel(self, text="SOFASCORE IA ANALYZER", font=("Arial", 26, "bold"), text_color="#00FF00")
        self.label_title.pack(pady=20)

        self.entry_id = ctk.CTkEntry(self, placeholder_text="Enter SofaScore Match ID...", width=350, height=45)
        self.entry_id.pack(pady=10)

        self.btn_analyze = ctk.CTkButton(self, text="RUN IA ANALYSIS", command=self.start_analysis, fg_color="#1B5E20", height=40)
        self.btn_analyze.pack(pady=15)

        self.info_label = ctk.CTkLabel(self, text="Enter ID to start", font=("Arial", 14))
        self.info_label.pack(pady=10)

        self.progress = ctk.CTkProgressBar(self, width=400)
        self.progress.set(0)
        self.progress.pack(pady=10)

        self.result_box = ctk.CTkFrame(self, fg_color="#0a0a0a", border_width=2, border_color="#00FF00")
        self.result_box.pack(pady=20, padx=20, fill="both", expand=True)

        self.final_score = ctk.CTkLabel(self.result_box, text="SCORE: --", font=("Arial", 40, "bold"), text_color="#00FF00")
        self.final_score.pack(pady=20)

    def start_analysis(self):
        m_id = self.entry_id.get()
        if not m_id: return
        threading.Thread(target=self.fetch_and_analyze, args=(m_id,)).start()

    def fetch_and_analyze(self, match_id):
        try:
            self.btn_analyze.configure(state="disabled")
            self.progress.set(0.3)
            self.info_label.configure(text="Connecting to SofaScore Servers...")
            
            # جلب بيانات المباراة الحقيقية
            api_url = f"https://api.sofascore.com/api/v1/event/{match_id}"
            response = self.scraper.get(api_url)
            data = response.json()

            # استخراج أسماء الفرق
            home_team = data['event']['homeTeam']['name']
            away_team = data['event']['awayTeam']['name']
            
            self.progress.set(0.6)
            self.info_label.configure(text=f"Analyzing: {home_team} vs {away_team}")
            time.sleep(2) # للواقعية في البث

            # خوارزمية بسيطة تعتمد على الـ ID لتوليد نتيجة منطقية (Score Exact)
            # ملاحظة: يمكنك تطوير هذه المعادلة بناءً على رتبة الفريق (Ranking)
            home_rank = data['event']['homeTeam'].get('ranking', 5)
            away_rank = data['event']['awayTeam'].get('ranking', 5)
            
            # منطق التوقع
            if home_rank < away_rank:
                pred = "2 - 1"
            elif home_rank > away_rank:
                pred = "0 - 1"
            else:
                pred = "1 - 1"

            self.progress.set(1.0)
            self.final_score.configure(text=f"SCORE: {pred}")
            self.info_label.configure(text=f"Match: {home_team} vs {away_team}", text_color="#00FF00")
            
        except Exception as e:
            self.info_label.configure(text="Error: Invalid ID or Connection Issue", text_color="red")
        finally:
            self.btn_analyze.configure(state="normal")

if __name__ == "__main__":
    app = SofaPredictor()
    app.mainloop()
    
