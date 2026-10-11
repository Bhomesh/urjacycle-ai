"""
UrjaCycle AI - Rooftop Solar Photovoltaic Yield & Economic Engine
Standard Formula: E = A * r * H * PR
Author: Bhomesh Razdan (Lead Architect)
"""

from ..core.models import SolarYieldEstimate

class SolarYieldEngine:
    """Calculates rooftop solar capacity, generation, savings and carbon mitigation."""

    def calculate_yield(self, rooftop_area_sqm: float, avg_daily_irradiance_kwh: float = 5.3, tariff_inr: float = 8.5) -> SolarYieldEstimate:
        # Usable rooftop area: 70% (30% reserved for parapet shading, stairs, maintenance)
        usable_area = round(rooftop_area_sqm * 0.70, 1)
        
        # Standard: ~10 sqm required for 1 kWp capacity
        kw_capacity = round(usable_area / 10.0, 2)
        
        # Photovoltaic Yield: E = A * r * H * PR
        # r = 0.20 (20% panel efficiency), PR = 0.78
        annual_kwh = round(usable_area * 0.20 * (avg_daily_irradiance_kwh * 365.0) * 0.78, 1)
        
        annual_savings = round(annual_kwh * tariff_inr, 2)
        
        # Grid emission factor for India (Central Electricity Authority): 0.82 kg CO2 / kWh
        co2_mitigated_tons = round((annual_kwh * 0.82) / 1000.0, 2)
        
        # Benchmark Rooftop Solar Capex in India: ~₹48,000 per kW (post-PM Surya Ghar subsidy)
        estimated_capex = round(kw_capacity * 48000.0, 2)
        
        payback_years = round(estimated_capex / annual_savings, 1) if annual_savings > 0 else 0.0

        return SolarYieldEstimate(
            rooftop_area_sqm=rooftop_area_sqm,
            usable_solar_area_sqm=usable_area,
            pv_system_capacity_kw=kw_capacity,
            annual_generation_kwh=annual_kwh,
            annual_savings_inr=annual_savings,
            co2_mitigated_metric_tons=co2_mitigated_tons,
            estimated_capex_inr=estimated_capex,
            simple_payback_years=payback_years
        )
