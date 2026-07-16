class WorkflowRecovery:

    def retry(

        self,

        step,

        retries=2,

    ):

        for attempt in range(retries):

            print(

                f"Retry {attempt+1}: {step.name}"

            )

        return False