def build_summary(state):
    return f"""Reflection completed.
    Iterations:
    {state.iteration}
    Final Score:
    {state.score}

    Explain why the graph stopped.
    """