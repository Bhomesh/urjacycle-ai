# Building UrjaCycle: Circular Waste & Rooftop Solar Grid Balancer on AWS
**Author:** Bhomesh Razdan | Bharat Builds Tour: Environmental Hacks (Track 03: Waste & Energy)

## Overview
Indian cities generate over 150,000 tonnes of municipal solid waste every day, while landfills like Ghazipur stand as towering environmental hazards. Concurrently, rapid EV adoption is threatening to overload local distribution transformers unless charging is aligned with renewable generation.

**UrjaCycle AI** is an intelligent serverless application on AWS solving both challenges:
1. **Source Waste Classification & Informal Recycler Protection:** Uses AI to identify recyclable and hazardous e-waste, publishing fair scrap market value benchmarks for informal waste pickers.
2. **Rooftop Solar Photovoltaic Yield Modeling ($E = A \cdot r \cdot H \cdot PR$):** Accurately computes rooftop potential, annual generation, and financial payback.
3. **EV Time-of-Use Grid Shifter:** Incentivizes daytime solar EV charging with 67% tariff discounts, absorbing midday solar surplus and protecting grid transformers.
4. **AWS Cedar Authorization:** Enforces Zero-Trust role policies between citizens, certified informal recyclers, and DISCOM grid operators.

Architected on AWS SAM CLI with Lambda, DynamoDB, and Bedrock, UrjaCycle proves the viability of circular energy and waste systems.
