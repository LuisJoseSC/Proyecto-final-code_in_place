import subprocess
import sys
sys.stdout.reconfigure(encoding='utf-8')
sys.stdin.reconfigure(encoding='utf-8')

def call_local_llm(prompt):
    try:
        result = subprocess.run(
            ["ollama", "run", "glm-4.6:cloud", prompt],
            capture_output=True
        )
        return result.stdout.decode('utf-8', errors='ignore').strip()
    except Exception:
        return "Ollama no está disponible. Instálalo y agrega glm-4.6:cloud."

def main():
    print("Proyecto Final - Code in Place")
    print("Por Luis Jose Sanchez")
    print("Chat con IA open source")
    print("Modelo: glm-4.6:cloud")
    while True:
        try:
            user_input = input("Tú: ").strip()
        except (KeyboardInterrupt, EOFError):
            sys.exit(0)
        if user_input.lower() == "salir":
            print("Programa finalizado.")
            break
        response = call_local_llm(user_input)
        print(f"Modelo: {response}")


if __name__ == "__main__":
    main()
