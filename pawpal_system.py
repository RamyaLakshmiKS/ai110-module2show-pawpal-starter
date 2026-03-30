"""
PawPal+ — logic layer
All backend classes live here. UI (app.py) imports from this module.
"""


class Task:
    """A single pet care activity."""

    def __init__(self, title: str, duration_minutes: int, priority: str,
                 category: str = "", notes: str = ""):
        self.title = title
        self.duration_minutes = duration_minutes
        self.priority = priority          # "high" | "medium" | "low"
        self.category = category          # e.g. "walk", "feeding", "medication"
        self.notes = notes

    def is_high_priority(self) -> bool:
        """Return True if this task has high priority."""
        pass

    def __repr__(self) -> str:
        pass


class Pet:
    """Information about the animal being cared for."""

    def __init__(self, name: str, species: str, breed: str = "", age: int = 0):
        self.name = name
        self.species = species
        self.breed = breed
        self.age = age

    def summary(self) -> str:
        """Return a human-readable description of the pet."""
        pass


class Owner:
    """The person using the app, along with their time constraints and preferences."""

    def __init__(self, name: str, available_minutes: int, preferences: dict = None):
        self.name = name
        self.available_minutes = available_minutes
        self.preferences = preferences or {}
        self.pet: Pet = None

    def has_time_for(self, task: Task) -> bool:
        """Return True if the task duration fits within available time."""
        pass


class Scheduler:
    """Selects and orders tasks to fit the owner's constraints."""

    def __init__(self, owner: Owner, tasks: list[Task]):
        self.owner = owner
        self.tasks = tasks

    def build_plan(self) -> "DailyPlan":
        """Run the scheduling algorithm and return a DailyPlan."""
        pass

    def _sort_by_priority(self, tasks: list[Task]) -> list[Task]:
        """Return tasks sorted from highest to lowest priority."""
        pass

    def _fits_in_time(self, task: Task, remaining_minutes: int) -> bool:
        """Return True if task duration fits within remaining_minutes."""
        pass


class DailyPlan:
    """The finalized schedule produced by the Scheduler."""

    def __init__(self, scheduled_tasks: list[Task], skipped_tasks: list[tuple]):
        self.scheduled_tasks = scheduled_tasks          # tasks that made the cut
        self.skipped_tasks = skipped_tasks              # list of (task, reason) tuples
        self.total_duration_minutes = sum(
            t.duration_minutes for t in scheduled_tasks
        )

    def display(self) -> str:
        """Return a formatted string of the scheduled tasks for the UI."""
        pass

    def explain(self) -> str:
        """Return a narrative explaining why tasks were included or skipped."""
        pass
