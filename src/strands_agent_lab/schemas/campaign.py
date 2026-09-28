from pydantic import BaseModel


from pydantic import BaseModel


class CampaignMetrics(BaseModel):
    campaign_id: str
    impressions: int
    clicks: int
    spend: float
    conversions: int
    revenue: float

    ctr: float
    cpc: float
    conversion_rate: float
    roas: float




class CampaignAnalysis(BaseModel):
    campaign_id: str
    summary: str