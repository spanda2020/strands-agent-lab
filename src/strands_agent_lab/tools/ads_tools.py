from pathlib import Path

import pandas as pd
from strands import tool

from strands_agent_lab.schemas.campaign import CampaignMetrics


DATA_FILE = (
    Path(__file__).resolve().parents[3]
    / "data"
    / "ads.csv"
)


def load_campaign_metrics(campaign_id: str) -> CampaignMetrics:
    """Load and aggregate metrics for a campaign."""

    df = pd.read_csv(DATA_FILE)

    campaign = df[df["campaign_id"] == campaign_id]

    if campaign.empty:
        raise ValueError(f"Campaign {campaign_id} not found")

    return CampaignMetrics(
        campaign_id=campaign_id,
        impressions=int(campaign["impressions"].sum()),
        clicks=int(campaign["clicks"].sum()),
        spend=float(campaign["spend"].sum()),
        conversions=int(campaign["conversions"].sum()),
        revenue=float(campaign["revenue"].sum()),
    )


@tool
def get_campaign_metrics(campaign_id: str) -> CampaignMetrics:
    """
    Get aggregated advertising performance metrics
    for a specific campaign ID.
    """

    return load_campaign_metrics(campaign_id)