# ...existing code...
import sys
import select
import termios
import tty
import time

def format_time(t: float) -> str:
    mins, secs = divmod(t, 60)
    hours, mins = divmod(mins, 60)
    return f"{int(hours):02d}:{int(mins):02d}:{secs:05.2f}"

def main():
    # ...existing code...
    fd = sys.stdin.fileno()
    old_attrs = termios.tcgetattr(fd)
    tty.setcbreak(fd)
    running = False
    start = 0.0
    elapsed = 0.0
    laps = []

    print("Cronômetro — Enter: start/stop | l: lap | r: reset | q: quit")
    try:
        while True:
            if running:
                current = time.perf_counter() - start + elapsed
            else:
                current = elapsed

            sys.stdout.write("\r" + format_time(current))
            sys.stdout.flush()

            r, _, _ = select.select([sys.stdin], [], [], 0.1)
            if r:
                ch = sys.stdin.read(1)
                if ch in ("\n", "\r"):  # Enter para start/stop (aceita \n ou \r)
                    if not running:
                        start = time.perf_counter()
                        running = True
                    else:
                        elapsed = time.perf_counter() - start + elapsed
                        running = False
                elif ch.lower() == "l":  # lap
                    laps.append(current)
                    sys.stdout.write("\n")
                    print(f"Lap {len(laps)}: {format_time(current)}")
                elif ch.lower() == "r":  # reset
                    running = False
                    start = 0.0
                    elapsed = 0.0
                    laps.clear()
                    sys.stdout.write("\nReset\n")
                elif ch.lower() == "q":  # quit
                    sys.stdout.write("\nQuit\n")
                    break
    except KeyboardInterrupt:
        sys.stdout.write("\nInterrompido\n")
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_attrs)

if __name__ == "__main__":
    main()
# ...existing code...