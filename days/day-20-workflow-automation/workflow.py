class WorkflowController:
    def run(self, queue, executor, validator, page):
        while not queue.empty():
            step=queue.next()
            executor.execute(page, step)

            validator.validate(page)
            