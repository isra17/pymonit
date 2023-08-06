from dataclasses import dataclass

from pymonit.mon.threads import ThreadInfo, collect_threads_info


@dataclass
class Monitor:
    threads: dict[int, ThreadInfo]

    def __init__(self):
        self.threads = {}

    def update(self) -> None:
        self.threads = {
            t.tid: t
            for t in collect_threads_info()
        }

if __name__ == "__main__":
    m = Monitor()
    m.update()
    print(m)

