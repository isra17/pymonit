from textual.app import App, ComposeResult
from textual.containers import ScrollableContainer
from textual.widgets import Button, Footer, Header, Static

from pymonit.gui.tasks_table import TasksTable
from pymonit.mon.monitor import Monitor

class PyMonitApp(App):

    BINDINGS = [
        ("q", "quit", "Quit")
    ]

    def __init__(self):
        self.monitor = Monitor()
        super().__init__()

    def on_mount(self) -> None:
        self.set_interval(1 / 60, self.update_monitor)

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield ScrollableContainer(TasksTable())

    def update_monitor(self):
        self.monitor.update()

        tasks_table = self.query_one(TasksTable)
        tasks_table.threads = self.monitor.threads


