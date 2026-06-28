from pydantic import ValidationError

class Validator:
    @staticmethod
    def validate(data, schema):
        try:
            return schema.model_validate(data)

        except ValidationError as exc:

            raise ValueError(
                str(exc)
            ) from exc