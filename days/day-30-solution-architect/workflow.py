from monitor import WorkflowMonitor
from recovery import RecoveryManager

class EnterpriseWorkflow:
    def __init__(self, supervisor):
        self.supervisor=supervisor
        self.monitor=WorkflowMonitor()
        self.recovery=RecoveryManager()

    async def run(self,objective):

        try:

            return await self.supervisor.execute(
                objective
            )

        except Exception as exc:

            await self.recovery.repair(
                exc
            )