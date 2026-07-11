
from profile_models import ProfileReport


def build_prompt(
    profile: ProfileReport,
    metrics,
):

    return f"""
Profile

Name:
{profile.summary.name}

Headline:
{profile.summary.headline}

Location:
{profile.summary.location}

Followers:
{profile.statistics.followers}

Connections:
{profile.statistics.connections}

Posts:
{profile.statistics.posts}

Detected Insights

{chr(10).join(metrics)}

Provide a concise profile analysis.
"""