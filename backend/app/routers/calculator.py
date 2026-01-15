from fastapi import APIRouter
from app.schemas import BudgetInput, BudgetResult

router = APIRouter()

def estimate_taxes(annual_salary: float) -> float:
    if annual_salary <= 40000:
        return annual_salary * 0.20
    elif annual_salary <= 80000:
        return annual_salary * 0.25
    elif annual_salary <= 150000:
        return annual_salary * 0.30
    else:
        return annual_salary * 0.35

@router.post("/budget", response_model=BudgetResult)
async def calculate_budget(budget_input: BudgetInput):
    annual_salary = budget_input.annual_salary
    monthly_debt = budget_input.monthly_debt

    gross_monthly = annual_salary / 12
    annual_taxes = estimate_taxes(annual_salary)
    monthly_taxes = annual_taxes / 12
    net_monthly = gross_monthly - monthly_taxes

    max_rent_30 = gross_monthly * 0.30
    comfortable_rent = gross_monthly * 0.25

    debt_to_income = (monthly_debt / gross_monthly) * 100 if gross_monthly > 0 else 0

    if debt_to_income > 20:
        recommended_rent = gross_monthly * 0.25
    elif debt_to_income > 10:
        recommended_rent = gross_monthly * 0.27
    else:
        recommended_rent = max_rent_30

    recommended_rent = max(recommended_rent - monthly_debt * 0.5, comfortable_rent * 0.8)

    disposable_max = net_monthly - max_rent_30 - monthly_debt
    disposable_recommended = net_monthly - recommended_rent - monthly_debt
    rent_to_income = (recommended_rent / gross_monthly) * 100 if gross_monthly > 0 else 0

    total_obligations = recommended_rent + monthly_debt
    obligation_ratio = (total_obligations / gross_monthly) * 100 if gross_monthly > 0 else 100

    if obligation_ratio <= 40:
        health_score = "healthy"
    elif obligation_ratio <= 50:
        health_score = "moderate"
    else:
        health_score = "stretched"

    return BudgetResult(
        gross_monthly_income=round(gross_monthly, 2),
        estimated_taxes=round(monthly_taxes, 2),
        net_monthly_income=round(net_monthly, 2),
        max_rent_30_percent=round(max_rent_30, 2),
        recommended_rent=round(recommended_rent, 2),
        comfortable_rent=round(comfortable_rent, 2),
        disposable_after_max_rent=round(disposable_max, 2),
        disposable_after_recommended=round(disposable_recommended, 2),
        debt_to_income_ratio=round(debt_to_income, 2),
        rent_to_income_ratio=round(rent_to_income, 2),
        financial_health_score=health_score,
    )
