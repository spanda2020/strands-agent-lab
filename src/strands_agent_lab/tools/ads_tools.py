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

    # Aggregate base metrics
    impressions = int(campaign["impressions"].sum())
    clicks = int(campaign["clicks"].sum())
    spend = float(campaign["spend"].sum())
    conversions = int(campaign["conversions"].sum())
    revenue = float(campaign["revenue"].sum())

    # Calculate derived metrics
    ctr = (clicks / impressions * 100) if impressions else 0.0
    cpc = (spend / clicks) if clicks else 0.0
    conversion_rate = (conversions / clicks * 100) if clicks else 0.0
    roas = (revenue / spend) if spend else 0.0

    return CampaignMetrics(
        campaign_id=campaign_id,
        impressions=impressions,
        clicks=clicks,
        spend=spend,
        conversions=conversions,
        revenue=revenue,
        ctr=ctr,
        cpc=cpc,
        conversion_rate=conversion_rate,
        roas=roas,
    )


@tool
def get_campaign_metrics(campaign_id: str) -> CampaignMetrics:
    """
    Get aggregated advertising performance metrics
    for a specific campaign ID.
    """

    return load_campaign_metrics(campaign_id)