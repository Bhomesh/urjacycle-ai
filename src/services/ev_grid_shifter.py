"""
UrjaCycle AI - EV Smart Charging & Solar Peak Load Shifting Engine
Author: Bhomesh Razdan (Lead Architect)
"""

from typing import List, Dict, Any
from ..core.models import EVChargingSlot

class EVGridShifterEngine:
    """Incentivizes EV charging during solar generation surplus to protect grid stability."""

    def __init__(self):
        self._slots: List[EVChargingSlot] = [
            EVChargingSlot("SLOT-01", "ST-DTU-01", "DTU North Campus Fast Hub", "01:00 - 05:00", 5.5, False, 25.0, 15.0),
            EVChargingSlot("SLOT-02", "ST-DTU-01", "DTU North Campus Fast Hub", "08:00 - 11:00", 8.0, False, 45.0, 30.0),
            EVChargingSlot("SLOT-03", "ST-DTU-01", "DTU North Campus Fast Hub", "11:00 - 14:00", 3.8, True, 92.0, 85.0), # Solar Midday Super Off-Peak!
            EVChargingSlot("SLOT-04", "ST-DTU-01", "DTU North Campus Fast Hub", "14:00 - 17:00", 4.2, True, 85.0, 78.0),
            EVChargingSlot("SLOT-05", "ST-DTU-01", "DTU North Campus Fast Hub", "18:00 - 22:00", 11.5, False, 12.0, 0.0), # Evening Coal Peak (Expensive)
        ]

    def get_all_slots(self) -> List[EVChargingSlot]:
        return self._slots

    def recommend_best_charging_window(self, battery_kwh_needed: float = 30.0) -> Dict[str, Any]:
        """Recommends slot with lowest tariff and highest renewable fraction."""
        solar_slots = [s for s in self._slots if s.is_solar_super_offpeak]
        best_slot = min(solar_slots, key=lambda s: s.tariff_inr_per_kwh) if solar_slots else self._slots[0]
        
        peak_slot = max(self._slots, key=lambda s: s.tariff_inr_per_kwh)
        
        cost_optimized = round(best_slot.tariff_inr_per_kwh * battery_kwh_needed, 2)
        cost_peak = round(peak_slot.tariff_inr_per_kwh * battery_kwh_needed, 2)
        savings = round(cost_peak - cost_optimized, 2)

        return {
            "recommended_slot": best_slot.to_dict(),
            "battery_kwh_needed": battery_kwh_needed,
            "cost_in_solar_window_inr": cost_optimized,
            "cost_in_peak_window_inr": cost_peak,
            "savings_inr": savings,
            "savings_pct": round((savings / cost_peak) * 100, 1),
            "clean_energy_share_pct": best_slot.green_energy_pct,
            "grid_impact": "Prevents DISCOM thermal transformer overloading by soaking up local rooftop solar surplus."
        }
