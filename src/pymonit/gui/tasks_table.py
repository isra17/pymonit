from textual.reactive import reactive
from textual.widgets import DataTable

from pymonit.mon.threads import ThreadInfo

class TasksTable(DataTable):
    threads: reactive[dict[int, ThreadInfo]] = reactive(dict)

    def on_mount(self) -> None:
        self.add_columns("TID", "Name", "Frame")

    def watch_threads(self, threads: dict[int, ThreadInfo]) -> None:
        added_rows = threads.keys() - self.rows.keys()
        removed_rows = self.rows.keys() - threads.keys()

        for key in added_rows:
            tinfo = threads[key]
            self.add_row(tinfo.tid, tinfo.name, tinfo.current_frame)

        for key in removed_rows:
            self.remove_row(key)


