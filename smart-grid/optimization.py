"""
optimization.py
Smart Grid Power Allocation Engine
"""

ZONE_PRIORITY = {
    "Zone A": 3,
    "Zone B": 2,
    "Zone C": 1
}

UNDERSERVE_THRESHOLD = 0.80


def optimize_grid(zone_demands, available_supply):

    total_demand = sum(zone_demands.values())
    remaining_supply = available_supply

    allocations = {}
    alerts = []

    # Sort zones by priority
    sorted_zones = sorted(
        zone_demands.items(),
        key=lambda x: ZONE_PRIORITY.get(x[0], 0),
        reverse=True
    )

    # Allocate power
    for zone, demand in sorted_zones:

        allocated = min(demand, remaining_supply)

        allocations[zone] = round(allocated, 2)

        remaining_supply -= allocated

        if remaining_supply < 0:
            remaining_supply = 0

    total_allocated = sum(allocations.values())

    # Efficiency
    if total_demand > 0:
        efficiency_after = round(
            (total_allocated / total_demand) * 100,
            1
        )
    else:
        efficiency_after = 0

    # Alerts
    for zone, demand in zone_demands.items():

        allocated = allocations.get(zone, 0)

        if demand > 0:
            served_ratio = allocated / demand
        else:
            served_ratio = 1

        if served_ratio < UNDERSERVE_THRESHOLD:

            deficit = round(demand - allocated, 2)

            alerts.append(
                f"{zone} power deficit: {deficit} MW"
            )

    # Status
    if not alerts:
        status = "Balanced"
    elif efficiency_after >= 85:
        status = "Constrained"
    else:
        status = "Critical Overload"

    # Zone details
    zone_details = []

    for zone, demand in zone_demands.items():

        allocated = allocations.get(zone, 0)

        served_pct = (
            round((allocated / demand) * 100, 1)
            if demand > 0 else 100
        )

        zone_details.append({
            "zone": zone,
            "priority": ZONE_PRIORITY.get(zone, 0),
            "demand_mw": round(demand, 2),
            "allocated_mw": round(allocated, 2),
            "served_pct": served_pct
        })

    return {
        "allocations": allocations,
        "total_demand": round(total_demand, 2),
        "available_supply": round(available_supply, 2),
        "total_allocated": round(total_allocated, 2),
        "efficiency_after": efficiency_after,
        "status": status,
        "alerts": alerts,
        "zone_details": zone_details
    }


if __name__ == "__main__":

    sample_demands = {
        "Zone A": 420,
        "Zone B": 280,
        "Zone C": 610
    }

    sample_supply = 1000

    result = optimize_grid(
        sample_demands,
        sample_supply
    )

    print("\nSMART GRID OPTIMIZATION RESULT\n")

    print("Status:", result["status"])
    print("Efficiency:", result["efficiency_after"], "%")

    print("\nAllocations:")
    for zone, power in result["allocations"].items():
        print(zone, ":", power, "MW")

    if result["alerts"]:
        print("\nAlerts:")
        for alert in result["alerts"]:
            print("-", alert)