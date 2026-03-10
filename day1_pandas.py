import pandas as pd
import pandas as pd

# ── CREATE A SAMPLE SUPPLY CHAIN DATASET ──────────────────────────────
data = {
    "origin": ["Bangkok", "Singapore", "Jakarta", "HCMC", "Bangkok", "KL", "Manila", "Singapore"],
    "destination": ["Singapore", "KL", "Singapore", "Bangkok", "Jakarta", "Singapore", "HCMC", "Jakarta"],
    "mode": ["road", "road", "sea", "road", "sea", "road", "sea", "sea"],
    "cost_usd": [450, 280, 620, 310, 890, 195, 740, 510],
    "transit_days": [2, 1, 4, 3, 5, 1, 6, 3],
    "volume_teu": [12, 8, 25, 15, 30, 6, 18, 22],
}

df = pd.DataFrame(data)
print("── Raw Data ──")
print(df)
print()

# ── EXERCISE 1: Sort by cost ───────────────────────────────────────────
print("── Cheapest Routes ──")
print(df.sort_values("cost_usd").head(3))
print()

# ── EXERCISE 2: Filter to sea routes only ─────────────────────────────
print("── Sea Routes Only ──")
sea_routes = df[df["mode"] == "sea"]
print(sea_routes)
print()

# ── EXERCISE 3: Average cost by transport mode ────────────────────────
print("── Avg Cost by Mode ──")
print(df.groupby("mode")["cost_usd"].mean())
print()

# ── EXERCISE 4: Add a cost-per-day column ─────────────────────────────
df["cost_per_day"] = df["cost_usd"] / df["transit_days"]
print("── Cost Efficiency (lower = better) ──")
print(df[["origin", "destination", "mode", "cost_per_day"]].sort_values("cost_per_day"))
print()

# ── EXERCISE 5: Total volume by origin city ───────────────────────────
print("── Volume by Origin ──")
print(df.groupby("origin")["volume_teu"].sum().sort_values(ascending=False))
df["cost_per_day_calc"] = df["cost_usd"] / df["transit_days"]
print("── Cost per Day for Each Route ──")
print(df[["origin", "destination", "mode", "cost_usd", "transit_days", "cost_per_day_calc"]])
