import sys
from tracker import run_daily_check
from analyzer import analyze, load_data

if __name__ == "__main__":
    print("🔥 Bienvenido a la Ley de los 7 Días 🔥")
   
    run_daily_check()
    
    if "--summary" in sys.argv:
        data = load_data()
        analyze(data)
