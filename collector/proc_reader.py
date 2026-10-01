from pathlib import Path

PROC = Path("/proc")


def read_process(pid):
    try:
        stat = (PROC / str(pid) / "stat").read_text()
        end = stat.rfind(")")
        fields = stat[end + 2:].split()

        status = (PROC / str(pid) / "status").read_text()
        memory_kb = 0

        for line in status.splitlines():
            if line.startswith("VmRSS:"):
                memory_kb = int(line.split()[1])
                break

        return {
            "pid": pid,
            "name": stat[stat.find("(") + 1:end],
            "ppid": int(fields[1]),
            "state": fields[0],
            "cpu_ticks": int(fields[11]) + int(fields[12]),
            "memory_bytes": memory_kb * 1024,
        }

    except (OSError, ValueError, IndexError):
        return None


def list_processes():
    for entry in PROC.iterdir():
        if entry.name.isdigit():
            process = read_process(int(entry.name))
            if process is not None:
                yield process


if __name__ == "__main__":
    for process in list_processes():
        print(process)