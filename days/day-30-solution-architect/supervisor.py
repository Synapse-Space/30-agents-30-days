import asyncio 


class EnterpriseSupervisor:
    def __init__(self, planner,registry):
        self.planner = planner
        
        self.registry=registry

    async def execute(self,objective):
        tasks=self.planner.plan(objective)
        completed={}
        while tasks:
            ready=[task for task in tasks
            if all(
                dependency in completed 
                for dependency in task.dependencies
            )
            ]
            await asyncio.gather(
                 *[
                    self.run(task)
                    for task in ready
                ]
            )
            for task in ready:
                completed[task.name]=True 
                tasks.remove(task)

        return completed
    
    async def run(self, task):
        print(f"Executing {task.name}")

        await asyncio.sleep(1)