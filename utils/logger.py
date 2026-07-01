from datetime import datetime
from pathlib import Path


LOG_DIR = Path("logs")
LOG_FILE = LOG_DIR / "regression.log"


def log(message):
    LOG_DIR.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    final_message = f"[{timestamp}] {message}"

    print(final_message)

    with open(LOG_FILE, "a", encoding="utf-8") as file:
        file.write(final_message + "\n")