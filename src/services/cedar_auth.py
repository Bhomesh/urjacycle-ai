"""
UrjaCycle AI - AWS Cedar Policy Authorization Engine
Author: Bhomesh Razdan (Lead Architect)
"""

from typing import Dict, Any, Tuple

class CedarPolicyEngine:
    def __init__(self):
        self.policies = [
            {
                "id": "policy::permit_citizen_actions",
                "effect": "permit",
                "principal_roles": ["Citizen", "InformalRecycler", "DiscomOfficer", "Admin"],
                "actions": ["Action::ClassifyWaste", "Action::CalculateSolarYield", "Action::BookEVSlot", "Action::LogRecycling"],
                "resource_types": ["WasteCatalog", "SolarRooftop", "EVStation"]
            },
            {
                "id": "policy::permit_informal_recycler",
                "effect": "permit",
                "principal_roles": ["InformalRecycler", "Admin"],
                "actions": ["Action::ClaimEWasteBounty", "Action::RedeemScrapCredits"],
                "resource_types": ["EWasteManifest"]
            },
            {
                "id": "policy::permit_discom_grid_operator",
                "effect": "permit",
                "principal_roles": ["DiscomOfficer", "Admin"],
                "actions": ["Action::AdjustEVTimeOfUseTariff", "Action::ApproveSolarGridInterconnection"],
                "resource_types": ["GridTariff", "NetMeteringAgreement"]
            }
        ]

    def is_authorized(self, principal_role: str, action: str, resource_type: str, context: Dict[str, Any] = None) -> Tuple[bool, str]:
        for policy in self.policies:
            if (policy["effect"] == "permit" and
                principal_role in policy["principal_roles"] and
                action in policy["actions"] and
                resource_type in policy["resource_types"]):
                return True, f"PERMIT by {policy['id']}"
                
        return False, f"DENY: Unauthorized action {action} by {principal_role} on {resource_type}"
