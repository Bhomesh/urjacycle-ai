"""
UrjaCycle AI - AWS Lambda Handlers
Author: Bhomesh Razdan (Lead Architect)
"""

import json
from typing import Dict, Any
from .services.waste_classifier import WasteClassifierEngine
from .services.solar_engine import SolarYieldEngine
from .services.ev_grid_shifter import EVGridShifterEngine
from .services.cedar_auth import CedarPolicyEngine

waste_classifier = WasteClassifierEngine()
solar_engine = SolarYieldEngine()
ev_shifter = EVGridShifterEngine()
cedar_engine = CedarPolicyEngine()

def build_response(status_code: int, body: Any) -> Dict[str, Any]:
    return {
        "statusCode": status_code,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET,POST,OPTIONS",
            "Access-Control-Allow-Headers": "Content-Type,Authorization"
        },
        "body": json.dumps(body)
    }

def handler_classify_waste(event: Dict[str, Any], context: Any = None) -> Dict[str, Any]:
    params = event.get("queryStringParameters") or {}
    item = params.get("item", "lithium_battery")
    res = waste_classifier.classify_item(item)
    return build_response(200, res.to_dict())

def handler_calculate_solar(event: Dict[str, Any], context: Any = None) -> Dict[str, Any]:
    params = event.get("queryStringParameters") or {}
    try:
        roof = float(params.get("roof_sqm", 250.0))
        tariff = float(params.get("tariff_inr", 8.5))
    except ValueError:
        return build_response(400, {"error": "Invalid numerical parameters"})

    res = solar_engine.calculate_yield(roof, tariff_inr=tariff)
    return build_response(200, res.to_dict())

def handler_get_ev_slots(event: Dict[str, Any], context: Any = None) -> Dict[str, Any]:
    slots = [s.to_dict() for s in ev_shifter.get_all_slots()]
    rec = ev_shifter.recommend_best_charging_window(35.0)
    return build_response(200, {
        "slots": slots,
        "optimization": rec
    })

def handler_cedar_auth(event: Dict[str, Any], context: Any = None) -> Dict[str, Any]:
    try:
        body = json.loads(event.get("body", "{}"))
        role = body.get("role", "Citizen")
        action = body.get("action", "Action::ClassifyWaste")
        res = body.get("resource", "WasteCatalog")
    except Exception:
        return build_response(400, {"error": "Invalid JSON body"})

    allowed, reason = cedar_engine.is_authorized(role, action, res)
    return build_response(200, {
        "principal_role": role,
        "action": action,
        "resource": res,
        "decision": "ALLOW" if allowed else "DENY",
        "reason": reason
    })
