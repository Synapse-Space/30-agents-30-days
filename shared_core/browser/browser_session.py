
from .playwright_client import PlaywrightClient
from .auth import AuthenticationManager


class BrowserSession:

    def __init__(

        self,

        headless=True,

        storage_state="storage_state.json",

    ):

        self.client = PlaywrightClient(headless)

        self.auth = AuthenticationManager(

            storage_state

        )

        self.browser = None

        self.context = None

        self.page = None

    def __enter__(self):

        self.browser = self.client.start()

        self.context = self.auth.new_context(

            self.browser

        )

        self.page = self.context.new_page()

        return self.page

    def __exit__(

        self,

        exc_type,

        exc,

        tb,

    ):

        self.auth.save_context(

            self.context

        )

        self.context.close()

        self.client.stop()