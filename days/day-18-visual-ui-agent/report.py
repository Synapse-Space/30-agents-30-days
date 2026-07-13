def explain(

    element,

):

    return f"""

Target

{element.label}

Type

{element.element_type}

Confidence

{element.confidence}

Bounding Box

{element.bounding_box}

Explain why this element matches
the user's request.
"""