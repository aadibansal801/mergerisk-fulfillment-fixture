"""Render short human-readable labels for warehouse bins."""


def format_pick_label(order_id, aisle):
    return f"{aisle.upper()} / {order_id.upper()}"


def label_heading(route_id):
    return f"Pick list for {route_id}"


def label_footer(count):
    return f"{count} parcels ready"


def print_pick_batch(orders):
    lines = []
    for order in orders:
        lines.append(format_pick_label(order["id"], order["aisle"]))
    return "\n".join(lines)
