from heapq import heappop, heappush
from typing import Any


# ---------- Data Structures (Plain Classes) ----------
class Agent:
    def __init__(self, agent_id: int,
                 start: tuple[int, int],
                 goal: tuple[int, int]):
        self.id = agent_id
        self.start = start
        self.goal = goal


class Conflict:
    def __init__(
        self,
        agent1: int,
        agent2: int,
        time: int,
        conflict_type: str,
        position: tuple[int, int],
    ):
        self.agent1 = agent1
        self.agent2 = agent2
        self.time = time
        # 'vertex' or 'edge'
        self.type = conflict_type
        self.position = position


class Node:
    def __init__(
        self,
        solution: dict[int, list[tuple[int, int]]],
        constraints: list[tuple[int, int]] | None = None,
        conflicts: list[Conflict] | None = None,
        chosen_conflict: Conflict | None = None,
        cost: int = 0,
    ) -> None:
        self.solution = solution  # dict agent_id -> list of positions
        self.constraints = (
            constraints if constraints is not None else []
        )  # (higher, lower)
        self.conflicts = conflicts if conflicts is not None else []
        self.chosen_conflict = chosen_conflict
        self.cost = cost

    # For heap ordering: we compare by cost, and use a counter to break ties.
    def __lt__(self, other: Any) -> Any:
        if self.cost != other.cost:
            return self.cost < other.cost
        # If costs equal, use an arbitrary tie-breaker
        # (e.g., id) to avoid comparing lists
        # We'll assign a counter externally, but here we fall back to id(self)
        return id(self) < id(other)


# ---------- Low‑Level Helper Functions (Placeholders) ----------
def find_single_agent_path(agent: Agent, env: Any) -> list[tuple[int, int]]:
    """
    Shortest path for one agent ignoring others.
    Placeholder: returns a simple Manhattan path.
    Replace with real A*.
    """
    path = [agent.start]
    x, y = agent.start
    ## entrer le path 
    gx, gy = agent.goal
    while (x, y) != (gx, gy):
        if x < gx:
            x += 1
        elif x > gx:
            x -= 1
        elif y < gy:
            y += 1
        elif y > gy:
            y -= 1
        path.append((x, y))
    return path


def find_all_conflicts(node: Node) -> list[Conflict]:
    """
    Detect all vertex/edge conflicts among agents' paths.
    Placeholder: returns empty list.
    Replace with full conflict detection.
    """
    return []


def choose_conflict(node: Node) -> Conflict | None:
    """
    Pick one conflict, e.g., earliest time.
    Placeholder: returns first conflict or None.
    """
    if node.conflicts:
        return node.conflicts[0]
    return None


def get_path_cost(node: Node) -> int:
    """Sum of path lengths (number of moves)."""
    total = 0
    for path in node.solution.values():
        total += len(path) - 1
    return total


def generate_path(node: Node) -> bool:
    """
    Plan paths respecting priority constraints in node.constraints.
    Placeholder: assumes all paths are already valid.
    Replace with a real priority‑based planner.
    """
    # In a real implementation,
    # you would sort agents by priority (topological order)
    # and plan each one while treating higher‑priority paths as obstacles.
    return True


def run_cbs(
    agent1: int, agent2: int,
    current_solution: dict[int, list[tuple[int, int]]]
) -> tuple[list[tuple[int, int]], list[tuple[int, int]]] | None:
    """
    Solve the two‑agent subproblem with CBS.
    Placeholder: returns original paths (assumes no conflict).
    """
    return current_solution[agent1], current_solution[agent2]


# ---------- Main PBS‑CC Class ----------
class PBSCC:
    def __init__(self, agents: list[Agent], env: Any):
        self.agents = agents
        self.env = env
        # for tie‑breaking in heap
        self.counter = 0

    def solve(self) -> dict[int, list[tuple[int, int]]] | None:
        """
        Run the high‑level PBS‑CC algorithm
        and return a conflict‑free solution,
        or None if no solution is found.
        """
        # 1. Build root node
        root_solution = {}
        for agent in self.agents:
            root_solution[agent.id] = find_single_agent_path(agent, self.env)

        root = Node(solution=root_solution)
        root.conflicts = find_all_conflicts(root)
        root.chosen_conflict = choose_conflict(root)
        root.cost = get_path_cost(root)

        # Priority queue (min‑heap)
        open_list: list[Any] = []
        self._push_node(open_list, root)

        while open_list:
            # self.print_open_list(open_list)
            _, _, current = heappop(open_list)

            # If no conflicts, success
            if not current.conflicts:
                return current.solution

            # Get the chosen conflict
            conflict = current.chosen_conflict
            if conflict is None:
                return None  # shouldn't happen

            a1 = conflict.agent1
            a2 = conflict.agent2

            # Create two child nodes with opposite priority orderings
            left_child = Node(
                solution=current.solution.copy(),
                # a1 > a2
                constraints=current.constraints + [(a1, a2)],
            )
            right_child = Node(
                solution=current.solution.copy(),
                # a2 > a1
                constraints=current.constraints + [(a2, a1)],
            )

            left_ok = generate_path(left_child)
            right_ok = generate_path(right_child)

            if left_ok:
                left_child.conflicts = find_all_conflicts(left_child)
                left_child.chosen_conflict = choose_conflict(left_child)
                left_child.cost = get_path_cost(left_child)
                self._push_node(open_list, left_child)

            if right_ok:
                right_child.conflicts = find_all_conflicts(right_child)
                right_child.chosen_conflict = choose_conflict(right_child)
                right_child.cost = get_path_cost(right_child)
                self._push_node(open_list, right_child)

            # Fallback to CBS only when both children fail
            # and open_list becomes empty
            if (not left_ok) and (not right_ok) and (not open_list):
                cbs_result = run_cbs(a1, a2, current.solution)
                if cbs_result is not None:
                    new_path_a1, new_path_a2 = cbs_result
                    cbs_node = Node(
                        solution=current.solution.copy(),
                        constraints=current.constraints.copy(),
                    )
                    cbs_node.solution[a1] = new_path_a1
                    cbs_node.solution[a2] = new_path_a2
                    cbs_node.conflicts = find_all_conflicts(cbs_node)
                    cbs_node.chosen_conflict = choose_conflict(cbs_node)
                    cbs_node.cost = get_path_cost(cbs_node)
                    self._push_node(open_list, cbs_node)

        # No solution found
        return None

    def print_open_list(self, open_list):
        if not open_list:
            print("OPEN is empty.")
            return
        sorted_items = sorted(open_list, key=lambda x: (x[0], x[1]))
        print(f"\nOPEN list ({len(sorted_items)} nodes):")
        for i, (cost, cnt, node) in enumerate(sorted_items):
            print(f"# {i+1}: cost={cost}, count={cnt}, "
                  f"conflicts={len(node.conflicts)}, "
                  f"constraints={node.constraints}")
        print()

    def _push_node(self, heap, node):
        """Push node onto heap with a unique counter."""
        heappush(heap, (node.cost, self.counter, node))
        self.counter += 1


# ---------- Example Usage ----------
if __name__ == "__main__":
    agents = [
        Agent(0, (0, 0), (2, 3)),
        Agent(1, (1, 2), (2, 2)),
    ]
    env = None  # replace with your environment

    solver = PBSCC(agents, env)
    solution = solver.solve()
    if solution:
        print("Solution found:")
        for agent_id, path in solution.items():
            print(f"Agent {agent_id}: {path}")
    else:
        print("No solution found.")
