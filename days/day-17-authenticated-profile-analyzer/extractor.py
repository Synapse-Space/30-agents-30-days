
from playwright.sync_api import Page

from profile_models import (
    ProfileSummary,
    ProfileStatistics,
    ProfileReport,
)


class ProfileExtractor:

    def extract(
        self,
        page: Page,
    ) -> ProfileReport:

        name = page.locator(".profile-name").inner_text()

        headline = page.locator(".profile-headline").inner_text()

        location = page.locator(".profile-location").inner_text()

        followers = int(
            page.locator(".followers").inner_text()
        )

        connections = int(
            page.locator(".connections").inner_text()
        )

        posts = int(
            page.locator(".posts").inner_text()
        )

        return ProfileReport(

            summary=ProfileSummary(

                name=name,

                headline=headline,

                location=location,

            ),

            statistics=ProfileStatistics(

                followers=followers,

                connections=connections,

                posts=posts,

            ),

        )