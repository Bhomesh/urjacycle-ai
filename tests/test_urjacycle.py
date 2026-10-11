"""
Unit Tests for UrjaCycle AI - All Engines & Handlers
Author: Bhomesh Razdan (Lead Architect)
"""

import unittest
from src.services.waste_classifier import WasteClassifierEngine
from src.services.solar_engine import SolarYieldEngine
from src.services.ev_grid_shifter import EVGridShifterEngine
from src.services.cedar_auth import CedarPolicyEngine
from src.core.models import WasteCategory
from src.lambda_handlers import (
    handler_classify_waste,
    handler_calculate_solar,
    handler_get_ev_slots,
    handler_cedar_auth
)

class TestUrjaCycle(unittest.TestCase):

    def test_waste_classifier(self):
        eng = WasteClassifierEngine()
        res = eng.classify_item("lithium_battery")
        self.assertEqual(res.category, WasteCategory.HAZARDOUS_EWASTE)
        self.assertEqual(res.informal_recycler_value_inr, 180.0)

        res2 = eng.classify_item("plastic water bottle")
        self.assertEqual(res2.category, WasteCategory.RECYCLABLE_DRY)

    def test_solar_yield_formula(self):
        eng = SolarYieldEngine()
        # 100 sqm roof -> usable 70 sqm -> 7 kW capacity -> annual ~21,120 kWh
        y = eng.calculate_yield(100.0)
        self.assertEqual(y.usable_solar_area_sqm, 70.0)
        self.assertEqual(y.pv_system_capacity_kw, 7.0)
        self.assertGreater(y.annual_generation_kwh, 15000.0)
        self.assertGreater(y.annual_savings_inr, 100000.0)
        self.assertTrue(1.0 < y.simple_payback_years < 6.0)

    def test_ev_grid_shifter(self):
        eng = EVGridShifterEngine()
        rec = eng.recommend_best_charging_window(40.0)
        self.assertIn("recommended_slot", rec)
        self.assertTrue(rec["savings_pct"] > 50.0)
        self.assertTrue(rec["recommended_slot"]["is_solar_super_offpeak"])

    def test_cedar_authorization(self):
        eng = CedarPolicyEngine()
        allowed, _ = eng.is_authorized("Citizen", "Action::ClassifyWaste", "WasteCatalog")
        self.assertTrue(allowed)

        allowed_scrap, _ = eng.is_authorized("InformalRecycler", "Action::ClaimEWasteBounty", "EWasteManifest")
        self.assertTrue(allowed_scrap)

        denied, _ = eng.is_authorized("Citizen", "Action::ClaimEWasteBounty", "EWasteManifest")
        self.assertFalse(denied)

    def test_lambda_handlers(self):
        res = handler_classify_waste({"httpMethod": "GET", "queryStringParameters": {"item": "cardboard"}})
        self.assertEqual(res["statusCode"], 200)

        res2 = handler_calculate_solar({"httpMethod": "GET", "queryStringParameters": {"roof_sqm": "200"}})
        self.assertEqual(res2["statusCode"], 200)

if __name__ == "__main__":
    unittest.main()
