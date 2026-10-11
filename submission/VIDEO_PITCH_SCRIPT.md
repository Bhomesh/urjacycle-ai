# 3-Minute Video Pitch Script: UrjaCycle AI
**Speaker:** Bhomesh Razdan (Lead Architect)  
**Track:** 03 Waste and Energy | Bharat Builds Tour (WeMakeDevs x AWS)  

### [0:00 - 0:35] The Problem
"Hello judges! I am Bhomesh Razdan. In India's cities, landfills like Ghazipur are overflowing with unsegregated toxic trash, while informal waste pickers work without fair scrap pricing. At the same time, as millions switch to electric vehicles, uncoordinated evening charging threatens to collapse local electrical transformers. We built **UrjaCycle AI** to close the loop on urban waste and power."

### [0:35 - 1:30] Live Walkthrough & Innovation
"UrjaCycle does three things:
1. **AI Waste Classification & Recycler Bounties:** When a user logs an item like a discarded lithium battery or phone PCB, our engine instantly categorizes it into hazardous e-waste, prescribes safety precautions, and calculates fair market scrap value (₹180/kg to ₹450/kg), preventing middleman exploitation of informal ragpickers.
2. **Rooftop Solar Yield Sizing:** Using standard solar irradiance equations ($E = A \cdot r \cdot H \cdot PR$), our dashboard calculates that a 250 m² rooftop generates 52.8 MWh annually, saving ₹4.48 Lakhs with a 1.9-year payback.
3. **EV Midday Load Shifter:** We dynamically discount EV charging tariffs by 67% (down to ₹3.80/kWh) during solar peak hours (11 AM - 3 PM), encouraging drivers to charge on clean solar energy rather than dirty coal evening grids."

### [1:30 - 2:30] AWS Architecture
"UrjaCycle runs on AWS:
- AWS Lambda and API Gateway for zero-idle microservices.
- Amazon DynamoDB for waste manifests and solar audit logs.
- AWS Cedar for declarative authorization: verified informal recyclers can claim e-waste bounties, while DISCOM engineers manage grid tariffs.
- Packaged with AWS Finch and tested locally on AWS SAM CLI."

### [2:30 - 3:00] Conclusion
"UrjaCycle creates a cleaner, self-powering city where waste has value and clean energy is optimized. Thank you!"
