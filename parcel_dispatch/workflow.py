"""Reserve a shipment from a warehouse order."""

from .reservations import reserve_shipment


def schedule_order(order):
    return reserve_shipment(order["id"], destination=order["destination"], carrier=order["carrier"])
