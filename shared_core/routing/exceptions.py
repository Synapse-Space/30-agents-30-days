
class RoutingException(Exception):
    """Base routing exception."""


class RouteNotFoundException(RoutingException):
    """Raised when no matching route exists."""


class InvalidRouteException(RoutingException):
    """Raised for invalid route configuration."""