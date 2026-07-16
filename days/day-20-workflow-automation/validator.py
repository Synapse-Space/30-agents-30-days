class FormValidator:

    def validate(

        self,

        page,

    ):

        popup = page.locator(

            ".error,.validation-error"

        )

        if popup.count():

            raise ValueError(

                "Validation failed."

            )

        return True