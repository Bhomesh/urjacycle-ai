# ⚡ UrjaCycle AI (ऊर्जा चक्र)
### Circular Waste Segregation, Rooftop Solar Yield & EV Grid Peak Shifting on AWS

[![License: MIT](https://img.shields.io/badge/License-MIT-amber.svg)](LICENSE)
[![Hackathon](https://img.shields.io/badge/Bharat%20Builds%20Tour-WeMakeDevs%20x%20AWS-orange.svg)](https://www.wemakedevs.org/aws/env)
[![Track](https://img.shields.io/badge/Track-03%20Waste%20and%20Energy-amber.svg)](https://www.wemakedevs.org/aws/env#tracks)
[![Lead Architect](https://img.shields.io/badge/Lead%20Architect-Bhomesh%20Razdan-purple.svg)](https://github.com/Bhomesh)

---

## Overview
**UrjaCycle AI** is a circular economy and clean energy transition platform built on AWS for the **Bharat Builds Tour: Environmental Hacks**.

It addresses municipal waste and urban energy grid challenges:
1. **Source Waste Classification & Informal Recycler Protection:** AI categorizes waste into Wet, Dry, and Hazardous E-Waste, with transparent fair-trade scrap pricing.
2. **Rooftop Solar PV Yield & Payback:** Photovoltaic yield modeling ($E = A \cdot r \cdot H \cdot PR$) to estimate kilowatt-hours and financial payback.
3. **EV Midday Solar Load Shifter:** Time-of-Use tariffs offering a 67% discount during solar peak production (11 AM - 3 PM).
4. **AWS Cedar Zero-Trust Authorization:** Decouples permissions between citizens, informal recyclers, and grid operators.

---

## Quickstart (Zero Dependencies)
```bash
git clone https://github.com/Bhomesh/urjacycle-ai.git
cd urjacycle-ai

# Run test suite
python3 -m unittest discover tests

# Launch web command center
python3 -m src.server 8082
```
Open **[http://localhost:8082](http://localhost:8082)**.

---

## Architecture & AWS Stack
* **AWS Open Source:** AWS Cedar (RBAC), AWS SAM CLI, LocalStack, AWS Finch.
* **AWS Cloud Services:** AWS Lambda, Amazon API Gateway, Amazon DynamoDB, Amazon EventBridge, Amazon Bedrock.

---

## Author
* **Lead Architect:** **Bhomesh Razdan** (`bhomeshrazdan@gmail.com`)
