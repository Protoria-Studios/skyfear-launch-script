import os, sys, subprocess

VAR_NAME = "OPENSSL_ia32cap"
VAR_VALUE = "~0x200000200000000"
GAME_EXE = "SKYFEAR.exe"

def game_exists(path):
    return os.path.isfile(path)

def launch_game(path):
    env = os.environ.copy()
    env[VAR_NAME] = VAR_VALUE
    try:
        subprocess.run([path], env=env)
    except Exception as e:
        print("Error launching game:", e)

def main():
    print("Skyfear Launcher\n")
    print("Source code: https://github.com/Protoria-Studios/skyfear-launch-script\n")
    game_path = os.path.join(os.getcwd(), GAME_EXE)

    if not game_exists(game_path):
        print("Game not found.")
        return

    if os.environ.get(VAR_NAME) != VAR_VALUE:
        print(f"Setting env var {VAR_NAME}...")
        os.environ[VAR_NAME] = VAR_VALUE

    print("Launching game...")
    launch_game(game_path)

if __name__ == "__main__":
    main()
