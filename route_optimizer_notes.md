# Route Optimizer — Data Model Sketch

## The Problem
Given a set of cities in SE Asia, find the lowest-cost (or fastest, or lowest-carbon)
route that visits all cities once and returns to start — a Travelling Salesman / VRP problem.

## Cities (8 nodes)
1. Bangkok (BKK)
2. Ho Chi Minh City (HCMC)
3. Singapore (SIN)
4. Kuala Lumpur (KL)
5. Jakarta (JKT)
6. Manila (MNL)
7. Yangon (RGN)
8. Phnom Penh (PNH)

## Edges (connections between cities)
Each edge needs THREE weights:
- cost_usd: estimated freight cost per TEU
- transit_days: time to traverse this leg
- co2_kg: estimated carbon emissions per TEU

## Transport Modes
- road: Thailand/Vietnam/Cambodia/Myanmar corridors
- sea: all island connections (Singapore, Jakarta, Manila)
- rail: limited — Bangkok–KL–Singapore corridor only

## What the user controls
- Which cities to include (subset of 8)
- Weight: how much to prioritise cost vs speed (slider 0–100%)
- Which modes are allowed

## Output
- Ordered list of cities (the route)
- Total cost, total transit days, total CO2
- Folium map with route drawn

## Questions to resolve in Day 2–3 code
- Do we use OR-Tools VRP or implement Nearest Neighbor manually first?
  → Start with Nearest Neighbor (simpler), add 2-opt improvement, compare
- How do we handle sea vs road mode differences in the distance matrix?
  → Two separate matrices, user selects allowed modes