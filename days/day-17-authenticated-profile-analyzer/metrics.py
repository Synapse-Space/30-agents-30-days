from profile_models import ProfileReport


class MetricsAnalyzer:

    def analyze(
        self,
        profile: ProfileReport,
    ):

        stats = profile.statistics

        metrics = []

        if stats.connections >= 500:

            metrics.append(
                "Strong professional network."
            )

        if stats.posts >= 50:

            metrics.append(
                "Consistent content creator."
            )

        if stats.followers > stats.connections:

            metrics.append(
                "Follower growth exceeds direct connections."
            )

        return metrics