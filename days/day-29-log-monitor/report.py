def build_summary(metrics):

    return f"""
Events Processed

{metrics['events']}

Alerts Generated

{metrics['alerts']}
"""