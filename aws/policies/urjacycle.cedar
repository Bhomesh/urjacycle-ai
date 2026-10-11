// UrjaCycle AI - AWS Cedar Policies
// Author: Bhomesh Razdan (Lead Architect)

permit (
    principal in UrjaCycle::Role::"Citizen",
    action in [
        UrjaCycle::Action::"ClassifyWaste",
        UrjaCycle::Action::"CalculateSolarYield",
        UrjaCycle::Action::"BookEVSlot",
        UrjaCycle::Action::"LogRecycling"
    ],
    resource
);

permit (
    principal in UrjaCycle::Role::"InformalRecycler",
    action in [
        UrjaCycle::Action::"ClaimEWasteBounty",
        UrjaCycle::Action::"RedeemScrapCredits"
    ],
    resource is UrjaCycle::Resource::"EWasteManifest"
);

permit (
    principal in UrjaCycle::Role::"DiscomOfficer",
    action in [
        UrjaCycle::Action::"AdjustEVTimeOfUseTariff",
        UrjaCycle::Action::"ApproveSolarGridInterconnection"
    ],
    resource
);

permit (
    principal in UrjaCycle::Role::"Admin",
    action,
    resource
);
