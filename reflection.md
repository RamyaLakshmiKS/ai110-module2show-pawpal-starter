# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

**Three core user actions:**

1. **Enter owner and pet information** — The user provides basic details about themselves and their pet (e.g., pet name, species/breed, owner's available time per day, and any care preferences). This context constrains what the scheduler can realistically plan.

2. **Add and manage care tasks** — The user creates, edits, or removes pet care tasks such as walks, feeding, medication, grooming, and enrichment activities. Each task has at minimum a duration (how long it takes) and a priority (how critical it is), so the scheduler can make informed decisions about what to include when time is limited.

3. **Generate and view a daily plan** — The user triggers the scheduler to produce a daily care plan. The app selects and orders tasks based on available time, priorities, and preferences, then displays the resulting schedule along with an explanation of why certain tasks were included or excluded.

The initial UML includes five classes arranged around a central `Scheduler`:

- **`Task`** — represents a single pet care activity. Holds the task name, how long it takes (`duration_minutes`), its `priority` (high/medium/low), a `category` (walk, feeding, medication, etc.), and optional notes. Responsible only for describing itself — it has no scheduling logic.

- **`Pet`** — holds descriptive information about the animal: name, species, breed, and age. Its only responsibility is to provide a readable summary of the pet. Age and species are stored because they could influence which tasks are relevant (e.g., a senior dog may need shorter walks).

- **`Owner`** — represents the person using the app. Stores their name, how many minutes they have available today, and any care preferences. Also holds a reference to their `Pet`. Responsible for answering whether a given task fits within the time they have left.

- **`Scheduler`** — the core logic class. Takes an `Owner` and a list of `Task` objects, then decides which tasks to include in the day's plan based on available time and priority. Internally sorts tasks by priority and checks each one against remaining time before committing it to the plan.

- **`DailyPlan`** — the output produced by `Scheduler`. Holds the final ordered list of scheduled tasks, a list of skipped tasks with reasons, and the total time committed. Responsible for formatting the plan for display and generating a plain-language explanation of the scheduling decisions.

**b. Design changes**

After reviewing the initial skeleton, four problems were identified and fixed before implementing any logic:

1. **`pet` moved into `Owner.__init__`** — The original skeleton set `self.pet = None` as a bare attribute with no way to pass a `Pet` at construction time. This made it easy to forget to assign the pet after creating an owner. Adding `pet` as an optional constructor parameter makes the relationship explicit and keeps object creation self-contained.

2. **Removed `Owner.has_time_for(task)`** — This method duplicated the time-check logic already present in `Scheduler._fits_in_time`. The key difference is that `Owner.available_minutes` is the full-day budget (never decremented), while the scheduler needs a shrinking `remaining_minutes` counter as tasks are added. Keeping both would produce inconsistent results. The check now lives exclusively in `Scheduler`, and `build_plan` will use a local `remaining_minutes` variable so the owner's stored value is never mutated.

3. **Added `PRIORITY_RANK` constant and validation** — Priority was stored as a raw string (`"high"` / `"medium"` / `"low"`) with no enforcement. A typo like `"High"` or `"urgent"` would pass through silently and break `_sort_by_priority`. A module-level `PRIORITY_RANK` dict (`{"high": 0, "medium": 1, "low": 2}`) now serves as both the sort key and the validation whitelist — `Task.__init__` raises `ValueError` if the priority isn't in it.

4. **Replaced `list[tuple]` with `SkippedTask` named tuple** — `skipped_tasks` was typed as `list[tuple]` with the structure `(task, reason)` documented only in a comment. Nothing prevented the fields from being swapped or extended inconsistently. A `SkippedTask(task, reason)` named tuple makes the structure explicit, self-documenting, and accessible by name rather than index.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
