from pydantic import BaseModel, Field
from typing import Optional

class BudgetInput(BaseModel):
    annual_salary: float = Field(..., gt=0)
    monthly_debt: float = Field(default=0, ge=0)
    location: Optional[str] = None

class BudgetResult(BaseModel):
    gross_monthly_income: float
    estimated_taxes: float
    net_monthly_income: float
    max_rent_30_percent: float
    recommended_rent: float
    comfortable_rent: float
    disposable_after_max_rent: float
    disposable_after_recommended: float
    debt_to_income_ratio: float
    rent_to_income_ratio: float
    financial_health_score: str
