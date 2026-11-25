"""Create in-memory shipment reservations for the dispatch queue."""


def reserve_shipment(order_id, *, destination):
    if not order_id or not destination:
        raise ValueError("Order ID and destination are required")
    return {"order_id": order_id, "destination": destination, "state": "reserved"}
