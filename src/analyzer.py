import json
from pathlib import Path

DATA_PATH = Path("data/log.json")

INSULTS = [
    "¿Eso fue todo? Estás más blando que puré de nubes.",
    "That’s it? You’re softer than cloud mash.",
    "Ni una ameba sería tan inconstante.",
    "Not even an amoeba would be this wishy-washy.",
    "¿Querés resultados con esa disciplina de trapo mojado?",
    "You want results with that wet-noodle discipline of yours?",
    "Sos la alarma que suena y nunca se levanta.",
    "You’re the alarm that rings but never gets up.",
]

MOTIVATIONS = [
    "Estás forjando el acero, un día a la vez.",
    "You’re forging steel, one day at a time.",
    "Buen trabajo, aún no sos un dios, pero vas camino.",
    "Good work—you’re not a god yet, but you’re on your way.",
    "Seguí así y no vas a necesitar motivación, vas a serla.",
    "Keep this up, and you won’t need motivation—you’ll be motivation.",
    "Te falta forja, pero hay fuego en vos.",
    "You still need tempering, but there’s fire in you.",
]


def load_data():
    with open(DATA_PATH) as f:
        return json.load(f)


def analyze(data):
    total_days = len(data)
    keys = ["wake_up", "exercise", "eating"]
    results = {k: 0 for k in keys}
    notes_written = 0

    for day in data.values():
        for k in keys:
            if day.get(k):
                results[k] += 1
        if day.get("note"):
            notes_written += 1

    print("\n📊 Discipline Summary:\n")
    for k in keys:
        pct = (results[k] / total_days) * 100
        label = {
            "wake_up": "⏰ Wake-up time",
            "exercise": "🏋️ Workout done",
            "eating": "🍗 Ate like a warrior",
        }[k]
        print(f"{label}: {results[k]}/{total_days} ✅ ({pct:.0f}%)")

    print(f"🧾 Notes written: {notes_written}/{total_days} ✅")

    overall_pct = (
        sum(results.values()) + (notes_written if notes_written else 0)
    ) / (total_days * 4) * 100

    print(f"\n🔥 Overall: {overall_pct:.0f}%")

    if overall_pct >= 60:
        print(f"💬 {random_choice(MOTIVATIONS)}")
    else:
        print(f"💀 {random_choice(INSULTS)}")


def random_choice(lst):
    import random
    return random.choice(lst)
