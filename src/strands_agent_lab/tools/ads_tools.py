from pathlib import Path

import pandas as pd
from strands import tool

DATA_FILE = (
    Path(__file__).resolve().parents[3]
    / "data"
    / "ads.csv"
)


@tool
def get_campaign_metrics(campaign_id: str) -> dict:
    """
    Get aggregated advertising performance metrics for a campaign.

    Use this tool when performance data is needed for a
    specific campaign ID.
    """

    df = pd.read_csv(DATA_FILE)

    campaign = df[df["campaign_id"] == campaign_id]

    if campaign.empty:
        return {
            "error": f"Campaign {campaign_id} not found"
        }

    impressions = int(campaign["impressions"].sum())
    clicks = int(campaign["clicks"].sum())
    spend = float(campaign["spend"].sum())
    conversions = int(campaign["conversions"].sum())
    revenue = float(campaign["revenue"].sum())

    return {
        "campaign_id": campaign_id,
        "impressions": impressions,
        "clicks": clicks,
        "spend": spend,
        "conversions": conversions,
        "revenue": revenue,
    }