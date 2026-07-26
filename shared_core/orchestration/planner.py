from abc import ABC, abstractmethod


class WorkflowPlanner(ABC):

    @abstractmethod
    def plan(
        self,
        objective: str,
    ):
        """
        Convert a goal into
        executable tasks.
        """