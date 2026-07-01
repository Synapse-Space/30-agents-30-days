from pathlib import Path 

class SafetyValidator:
    PROTECTED={
        ".git",
        ".env",
        "venv",
        "__pycache__",
    }

    @staticmethod
    def validate(path:Path):
        for part in path.parts:
            if part in SafetyValidator.PROTECTED:
                raise PermissionError(f"Protected directory access: {part}")
        return True