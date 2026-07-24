import traceback
import traceback 
from .models import ErrorContext

class ErrorAnalyzer:
    def analyze(self, exception: Exception) -> ErrorContext:
        return ErrorContext(
            exception_type=type(exception).__name__,
            message=str(exception),
            traceback=traceback.format_exc()
        )