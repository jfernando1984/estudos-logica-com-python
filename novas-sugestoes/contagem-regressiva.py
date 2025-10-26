import sys
import select
import termios
import tty
import time
from typing import Optional

def parse_duration(s: str) -> Optional[float]:
    s = s.strip()
    if not s:
        return None
    # aceita formatos: SS ou MM:SS ou HH:MM:SS
    parts = s.split(":")
    try:
        parts = [int(p) for p in parts]
    except ValueError:
        return None
    if len(parts) == 1:
        return float(parts[0])
    if len(parts) == 2:
        return float(parts[0] * 60 + parts[1])
    if len(parts) == 3:
        return float(parts[0] * 3600 + parts[1] * 60 + parts[2])
    return None

def format_time(seconds: float) -> str:
    if seconds < 0:
        seconds = 0.0
    secs = int(seconds)
    hrs, rem = divmod(secs, 3600)
    mins, sec = divmod(rem, 60)
    frac = seconds - int(seconds)
    return f"{int(hrs):02d}:{int(mins):02d}:{int(sec):02d}{frac:+.2f}"[:11].replace("+", ".")

def main():
    # obter duração por argumento ou entrada interativa
    duration = None
    if len(sys.argv) > 1:
        duration = parse_duration(sys.argv[1])
        if duration is None:
            print("Formato inválido. Use SS ou MM:SS ou HH:MM:SS")
            return
    else:
        user = input("Duração (SS ou MM:SS ou HH:MM:SS): ").strip()
        duration = parse_duration(user)
        if duration is None:
            print("Formato inválido. Saindo.")
            return

    fd = sys.stdin.fileno()
    old_attrs = termios.tcgetattr(fd)
    tty.setcbreak(fd)

    remaining = float(duration)
    original = float(duration)
    running = False
    last_tick = time.monotonic()

    print("Timer — p: play/pause | r: reset | q: quit")
    try:
        while True:
            now = time.monotonic()
            if running:
                elapsed = now - last_tick
                remaining -= elapsed
            last_tick = now

            # exibir
            sys.stdout.write("\r" + format_time(remaining) + " ")
            sys.stdout.flush()

            if remaining <= 0:
                sys.stdout.write("\nTempo esgotado!\a\n")
                sys.stdout.flush()
                break

            r, _, _ = select.select([sys.stdin], [], [], 0.1)
            if r:
                ch = sys.stdin.read(1)
                if ch.lower() == "p":  # play / pause
                    running = not running
                elif ch.lower() == "r":  # reset
                    remaining = float(original)
                    running = False
                    last_tick = time.monotonic()
                    sys.stdout.write("\nReset\n")
                elif ch.lower() == "q":
                    sys.stdout.write("\nQuit\n")
                    break
    except KeyboardInterrupt:
        sys.stdout.write("\nInterrompido\n")
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_attrs)

if __name__ == "__main__":
    main()