"""Reserve several orders selected by a warehouse operator."""

from .reservations import reserve_shipment


def reserve_dispatch_batch(orders):
    return [reserve_shipment(order["id"], destination=order["destination"]) for order in orders]
