
def build_reasoning(
    element,
):

    return f"""
Selected Target

Label:
{element.label}

Type:
{element.element_type}

Confidence:
{element.confidence}

Explain briefly why this target best satisfies the user's request.
"""