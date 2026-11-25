"""Render short human-readable labels for warehouse bins."""


def render_pick_label(order_id, aisle):
    return f"{aisle.upper()} / {order_id.upper()}"


def label_heading(route_id):
    return f"Pick list for {route_id}"


def label_footer(count):
    return f"{count} parcels ready"
