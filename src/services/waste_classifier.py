"""
UrjaCycle AI - Intelligent Waste Classification & Informal Recycler Value Engine
Author: Bhomesh Razdan (Lead Architect)
"""

from typing import Dict, Any, List
from ..core.models import WasteCategory, WasteClassificationResult

ITEM_DATABASE = {
    "lithium_battery": {
        "category": WasteCategory.HAZARDOUS_EWASTE,
        "bin": "Black/Red E-Waste Bin",
        "value_per_kg": 180.0,
        "co2_offset": 3.8,
        "instruction": "Do not puncture. Tape terminals. Schedule certified informal recycler pickup."
    },
    "smartphone_pcb": {
        "category": WasteCategory.HAZARDOUS_EWASTE,
        "bin": "Black/Red E-Waste Bin",
        "value_per_kg": 450.0,
        "co2_offset": 8.5,
        "instruction": "Contains precious metals (gold, palladium, copper). Direct to authorized smelter."
    },
    "pet_plastic_bottle": {
        "category": WasteCategory.RECYCLABLE_DRY,
        "bin": "Blue Dry Bin",
        "value_per_kg": 28.0,
        "co2_offset": 1.4,
        "instruction": "Empty liquid, rinse, and compress flat to optimize storage density."
    },
    "cardboard_carton": {
        "category": WasteCategory.RECYCLABLE_DRY,
        "bin": "Blue Dry Bin",
        "value_per_kg": 14.0,
        "co2_offset": 0.9,
        "instruction": "Remove tape and keep dry for clean paper pulping."
    },
    "food_scraps": {
        "category": WasteCategory.BIODEGRADABLE_WET,
        "bin": "Green Wet Bin",
        "value_per_kg": 2.0,
        "co2_offset": 0.5,
        "instruction": "Ideal for residential composting or municipal biomethanation (CBG) digestors."
    },
    "aluminum_can": {
        "category": WasteCategory.RECYCLABLE_DRY,
        "bin": "Blue Dry Bin",
        "value_per_kg": 110.0,
        "co2_offset": 9.1,
        "instruction": "95% energy savings over virgin bauxite smelting. Rinse and crush."
    }
}

class WasteClassifierEngine:
    """Classifies waste items and computes fair trade scrap values for informal kabadiwallas."""

    def classify_item(self, item_name: str) -> WasteClassificationResult:
        key = item_name.strip().lower().replace(" ", "_")
        matched = ITEM_DATABASE.get(key)

        if not matched:
            # Fuzzy heuristic default
            if any(k in key for k in ["battery", "laptop", "phone", "circuit", "cable", "electronic", "wire"]):
                cat = WasteCategory.HAZARDOUS_EWASTE
                bin_color = "Black/Red E-Waste Bin"
                val = 140.0
                co2 = 4.2
                instr = "Contains heavy metals. Deliver to authorized E-waste collection hub."
            elif any(k in key for k in ["plastic", "paper", "can", "glass", "box", "metal", "bottle"]):
                cat = WasteCategory.RECYCLABLE_DRY
                bin_color = "Blue Dry Bin"
                val = 22.0
                co2 = 1.2
                instr = "Clean, dry, and segregate from organic waste."
            else:
                cat = WasteCategory.BIODEGRADABLE_WET
                bin_color = "Green Wet Bin"
                val = 3.0
                co2 = 0.4
                instr = "Organic wet waste suitable for composting."
            
            return WasteClassificationResult(
                item_name=item_name,
                category=cat,
                confidence_score=0.88,
                disposal_bin_color=bin_color,
                informal_recycler_value_inr=val,
                carbon_offset_kg_co2=co2,
                handling_instructions=instr
            )

        return WasteClassificationResult(
            item_name=item_name,
            category=matched["category"],
            confidence_score=0.97,
            disposal_bin_color=matched["bin"],
            informal_recycler_value_inr=matched["value_per_kg"],
            carbon_offset_kg_co2=matched["co2_offset"],
            handling_instructions=matched["instruction"]
        )
