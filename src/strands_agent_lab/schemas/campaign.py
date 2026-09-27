from pydantic import BaseModel


class CampaignMetrics(BaseModel):
    campaign_id: str
    impressions: int
    clicks: int
    spend: float
    conversions: int
    revenue: float