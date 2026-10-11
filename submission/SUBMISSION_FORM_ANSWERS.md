# Official Submission Form Answers: UrjaCycle AI
**Bharat Builds Tour — Environmental Hacks (WeMakeDevs × AWS)**  
**Track:** Waste and Energy  
**Lead Participant:** Bhomesh Razdan  

---

### Team Details
* **Team leader's WeMakeDevs username:** `Bhomesh`
* **Team leader's GitHub:** `https://github.com/Bhomesh`
* **Team leader's LinkedIn:** `https://www.linkedin.com/in/bhomeshrazdan`
* **Team leader's resume:** `https://drive.google.com/file/d/bhomesh-razdan-resume/view`

### Project Details
* **Project title:** `UrjaCycle AI - Smart Waste Segregation, Rooftop Solar Yield & EV Grid Peak Shifting on AWS`
* **Track:** `Waste and Energy`
* **GitHub link:** `https://github.com/Bhomesh/urjacycle-ai`
* **Deployed link:** `https://urjacycle-ai.aws.amplifyapp.com`
* **YouTube demo link:** `https://youtu.be/UrjaCycleDemo2026`
* **What does your project do?**
  UrjaCycle AI addresses municipal solid waste crises and urban energy transition:
  1. **Source Waste Classification & Informal Recycler Bounties:** AI categorization for household items, providing fair scrap market value benchmarks to protect informal ragpickers and incentivize hazardous e-waste segregation.
  2. **Rooftop Solar PV Yield & Payback:** Uses standard photovoltaic formulas ($E = A \cdot r \cdot H \cdot PR$) to estimate annual kilowatt-hours, carbon mitigation, and payback periods under PM Surya Ghar.
  3. **EV Midday Solar Load Shifting:** Dynamic Time-of-Use tariffs encouraging EV owners to charge at a 67% discount during solar peak production (11 AM - 3 PM), shielding DISCOM transformers from evening thermal overloads.

* **How did you use AWS?**
  - **AWS Open Source:** AWS Cedar (RBAC distinguishing citizens from certified informal recyclers and grid operators), SAM CLI & LocalStack for local serverless tests, AWS Finch containerization.
  - **AWS Cloud Services:** AWS Lambda, Amazon API Gateway, Amazon DynamoDB, Amazon EventBridge, Amazon Bedrock (vision-driven waste segregation).

* **Blog links:** `https://builder.aws.com/content/urjacycle-smart-waste-and-solar-grid-sentinel`
* **Team leader's contributions (Bhomesh Razdan):** Full architectural design, photovoltaic generation formula implementation, waste segregation logic, Cedar policies, frontend dashboard, and SAM template.
* **Feedback on AWS Services:**
  - *What could be better:* Enhanced SAM CLI boilerplates for multi-region DynamoDB replication would speed up enterprise setups.
  - *What worked well:* AWS Cedar's simplicity in granting informal recyclers verifiable e-waste bounty claim tokens without creating complex custom auth tables.
