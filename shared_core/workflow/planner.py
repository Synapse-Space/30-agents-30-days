from .model import WorkflowStep 


class WorkflowPlanner:
    def build(self, fields):
        steps=[]
        for index,field in enumerate(fields):
            steps.append(WorkflowStep(
                     id=index + 1,

                    name=f"Fill {field}",

                    action="input",

                    payload={

                        "field": field

                    },
            ))
        
         steps.append(

            WorkflowStep(

                id=len(steps) + 1,

                name="Submit Form",

                action="submit",

            )

        )

        return steps
