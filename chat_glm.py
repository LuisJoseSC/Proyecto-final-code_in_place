import subprocess
import sys
import time
sys.stdout.reconfigure(encoding='utf-8')
sys.stdin.reconfigure(encoding='utf-8')

MODEL_NAME = "deepseek-v3.1:671b-cloud"


def slow_print(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")
    sys.stdout.flush()

def call_local_llm(prompt):
    try:
        result = subprocess.run(
            ["ollama", "run", MODEL_NAME, prompt],
            capture_output=True,
            text=True,
            encoding="utf-8",
        )
        return result.stdout.strip()
    except Exception:
        return "Ollama no está disponible. Instálalo y agrega glm-4.6:cloud."


def main():
    slow_print("Proyecto Final - Code in Place")
    slow_print("Por Luis Jose Sanchez")
    slow_print("Chat con IA open source")
    slow_print(f"Modelo: {MODEL_NAME}")
    while True:
        try:
            user_input = input("Tú: ").strip()
        except (KeyboardInterrupt, EOFError):
            sys.exit(0)
        if user_input.lower() == "salir":
            slow_print("Programa finalizado.")
            break
        response = call_local_llm(user_input)
        slow_print(f"Modelo: {response}")


if __name__ == "__main__":
    main()
