def build_summary(state):
    return f"""Reflection completed.
    Iterations:
    {state.get('iteration', 0)}
    Final Score:
    {state.get('score', 0.0)}

    Explain why the graph stopped.
    """