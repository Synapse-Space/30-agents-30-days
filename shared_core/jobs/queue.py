class JobQueue:

    def publish(

        self,

        job,

    ):

        raise NotImplementedError

    def consume(self):

        raise NotImplementedError