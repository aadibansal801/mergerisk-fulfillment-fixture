"""Create in-memory shipment reservations for the dispatch queue."""


def reserve_shipment(order_id, *, destination, carrier):
    if not order_id or not destination or not carrier:
        raise ValueError("Order ID, destination and carrier are required")
    return {"order_id": order_id, "destination": destination, "carrier": carrier, "state": "reserved"}
