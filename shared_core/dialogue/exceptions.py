class DialogueException(
    Exception
):
    """Base dialogue exception."""


class RoutingException(
    DialogueException
):
    """Unable to route message."""