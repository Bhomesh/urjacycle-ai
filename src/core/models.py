"""
UrjaCycle AI - Core Models
Author: Bhomesh Razdan (Lead Architect)
Event: Bharat Builds Tour - Environmental Hacks (Track 03: Waste and Energy)
"""

from dataclasses import dataclass, asdict
from typing import List, Dict, Optional, Any
from enum import Enum
import time

class WasteCategory(str, Enum):
    BIODEGRADABLE_WET = "Wet Organic"
    RECYCLABLE_DRY = "Dry Recyclable"
    HAZARDOUS_EWASTE = "Hazardous E-Waste"
    DOMESTIC_HAZARDOUS = "Domestic Sanitary"

@dataclass
class WasteClassificationResult:
    item_name: str
    category: WasteCategory
    confidence_score: float
    disposal_bin_color: str           # "Green", "Blue", "Red", "Yellow"
    informal_recycler_value_inr: float # Fair value per kg to prevent informal exploitation
    carbon_offset_kg_co2: float
    handling_instructions: str

    def to_dict(self) -> Dict[str, Any]:
        d = asdict(self)
        d['category'] = self.category.value
        return d

@dataclass
class SolarYieldEstimate:
    rooftop_area_sqm: float
    usable_solar_area_sqm: float
    pv_system_capacity_kw: float
    annual_generation_kwh: float
    annual_savings_inr: float
    co2_mitigated_metric_tons: float
    estimated_capex_inr: float
    simple_payback_years: float

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

@dataclass
class EVChargingSlot:
    slot_id: str
    station_id: str
    station_name: str
    hour_window: str                  # e.g., "11:00 - 13:00"
    tariff_inr_per_kwh: float
    is_solar_super_offpeak: bool      # true during midday solar surplus
    green_energy_pct: float
    co2_saving_pct: float

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)
