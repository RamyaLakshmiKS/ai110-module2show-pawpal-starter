"""
PawPal+ — logic layer
All backend classes live here. UI (app.py) imports from this module.
"""

from typing import NamedTuple

# Maps priority label to sort order (lower number = higher priority).
PRIORITY_RANK = {"high": 0, "medium": 1, "low": 2}


class SkippedTask(NamedTuple):
    """A task that did not make it into the daily plan, with a reason."""
    task: "Task"
    reason: str


class Task:
    """A single pet care activity."""

    def __init__(self, title: str, duration_minutes: int, priority: str,
                 category: str = "", notes: str = ""):
        if priority not in PRIORITY_RANK:
            raise ValueError(f"priority must be one of {list(PRIORITY_RANK)}; got {priority!r}")
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

    def __init__(self, name: str, available_minutes: int,
                 pet: Pet = None, preferences: dict = None):
        self.name = name
        self.available_minutes = available_minutes
        self.pet = pet
        self.preferences = preferences or {}


class Scheduler:
    """Selects and orders tasks to fit the owner's constraints."""

    def __init__(self, owner: Owner, tasks: list[Task]):
        self.owner = owner
        self.tasks = tasks

    def build_plan(self) -> "DailyPlan":
        """Run the scheduling algorithm and return a DailyPlan.

        Uses a local `remaining_minutes` counter (starting from
        owner.available_minutes) so the owner's stored value is never
        mutated and multiple plans can be built from the same owner.
        """
        pass

    def _sort_by_priority(self, tasks: list[Task]) -> list[Task]:
        """Return tasks sorted from highest to lowest priority."""
        pass

    def _fits_in_time(self, task: Task, remaining_minutes: int) -> bool:
        """Return True if task duration fits within remaining_minutes."""
        pass


class DailyPlan:
    """The finalized schedule produced by the Scheduler."""

    def __init__(self, scheduled_tasks: list[Task], skipped_tasks: list[SkippedTask]):
        self.scheduled_tasks = scheduled_tasks
        self.skipped_tasks = skipped_tasks              # list of SkippedTask(task, reason)
        self.total_duration_minutes = sum(
            t.duration_minutes for t in scheduled_tasks
        )

    def display(self) -> str:
        """Return a formatted string of the scheduled tasks for the UI."""
        pass

    def explain(self) -> str:
        """Return a narrative explaining why tasks were included or skipped."""
        pass
