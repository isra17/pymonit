import inspect
import sys
import typing as t
from dataclasses import dataclass
import threading

@dataclass
class ThreadInfo:
    tid: int | None
    ident: int | None
    name: str
    daemon: bool
    current_frame: str
    obj: threading.Thread

def collect_threads_info() -> t.Iterator[ThreadInfo]:
    for thread in threading.enumerate():
        if not thread.ident:
            continue

        stack = sys._current_frames()[thread.ident]
        func = stack.f_code.co_name
        module = inspect.getmodule(stack).__name__

        yield ThreadInfo(
            tid=thread.native_id,
            ident=thread.ident,
            name=thread.name,
            daemon=thread.daemon,
            current_frame=f"{module}.{func}",
            obj=thread,
        )
