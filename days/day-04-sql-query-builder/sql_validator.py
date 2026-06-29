import re


class SQLValidator:

    BLOCKED_KEYWORDS = [
        "INSERT",
        "UPDATE",
        "DELETE",
        "DROP",
        "ALTER",
        "CREATE",
        "TRUNCATE",
        "REPLACE",
        "MERGE",
        "GRANT",
        "REVOKE",
        "PRAGMA",
        "ATTACH",
        "DETACH",
    ]

    @classmethod
    def validate(cls, sql: str):

        sql = sql.strip()

        if not sql:
            raise ValueError("Empty SQL generated.")

        if ";" in sql[:-1]:
            raise ValueError("Multiple SQL statements detected.")

        if not re.match(
            r"^\s*SELECT",
            sql,
            re.IGNORECASE,
        ):
            raise ValueError(
                "Only SELECT queries are allowed."
            )

        upper_sql = sql.upper()

        for keyword in cls.BLOCKED_KEYWORDS:

            if keyword in upper_sql:
                raise ValueError(
                    f"Blocked SQL keyword detected: {keyword}"
                )

        return sql