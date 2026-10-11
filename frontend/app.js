lucide.createIcons();

document.addEventListener('DOMContentLoaded', () => {
  document.getElementById('btn-classify').addEventListener('click', async () => {
    const item = document.getElementById('waste-input').value;
    try {
      const res = await fetch(`/api/waste/classify?item=${encodeURIComponent(item)}`);
      const data = await res.json();
      document.getElementById('waste-result').innerHTML = `
        <div>Item: <span class="text-white">${data.item_name}</span></div>
        <div>Category: <span class="text-amber-400 font-bold">${data.category}</span></div>
        <div>Bin Color: <span class="text-red-400">${data.disposal_bin_color}</span></div>
        <div>Informal Scrap Bounty: <span class="text-emerald-400 font-bold">₹${data.informal_recycler_value_inr} / kg</span></div>
        <div>CO₂ Offset: <span class="text-cyan-400">${data.carbon_offset_kg_co2} kg CO₂</span></div>
        <div class="text-slate-400 mt-2">${data.handling_instructions}</div>
      `;
    } catch (e) {
      console.log(e);
    }
  });

  document.getElementById('btn-calc-solar').addEventListener('click', async () => {
    const area = document.getElementById('solar-area').value;
    try {
      const res = await fetch(`/api/solar/calculate?roof_sqm=${area}`);
      const data = await res.json();
      document.getElementById('solar-result').innerHTML = `
        <div>System Capacity: <span class="text-emerald-400 font-bold">${data.pv_system_capacity_kw} kWp</span></div>
        <div>Annual Generation: <span class="text-cyan-400">${data.annual_generation_kwh.toLocaleString()} kWh/yr</span></div>
        <div>Annual Savings: <span class="text-emerald-400 font-bold">₹${data.annual_savings_inr.toLocaleString()} / year</span></div>
        <div>CO₂ Mitigated: <span class="text-blue-400">${data.co2_mitigated_metric_tons} Metric Tons/yr</span></div>
        <div>Estimated Capex: <span class="text-slate-300">₹${data.estimated_capex_inr.toLocaleString()}</span></div>
        <div>Simple Payback: <span class="text-amber-400 font-bold">${data.simple_payback_years} Years</span></div>
      `;
    } catch (e) {
      console.log(e);
    }
  });
});
