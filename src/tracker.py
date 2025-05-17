from rich import print
from rich.prompt import Confirm, Prompt
import json
from datetime import date
from storage import save_log

def run_daily_check():
    print("\n[b]Día de disciplina:[/b]")

    wake_up = Confirm.ask("¿Te levantaste a la hora prometida?")
    exercised = Confirm.ask("¿Hiciste ejercicio?")
    ate_clean = Confirm.ask("¿Comiste pollo, arroz y huevo (y solo eso)?")
    note = Prompt.ask("¿Comentario motivacional o autoflagelante?")

    today = str(date.today())
    entry = {
        "wake_up": wake_up,
        "exercised": exercised,
        "ate_clean": ate_clean,
        "note": note
    }

    save_log(today, entry)
    print("[green]✔ Registro guardado. ¡Un paso más hacia la grandeza![/green]")
