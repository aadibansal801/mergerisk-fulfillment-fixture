import unittest

from parcel_dispatch.batch import reserve_dispatch_batch


class DispatchBatchTests(unittest.TestCase):
    def test_reserves_each_order_in_the_original_sequence(self):
        reservations = reserve_dispatch_batch([
            {"id": "O-14", "destination": "BLR"},
            {"id": "O-22", "destination": "DEL"},
        ])
        self.assertEqual([item["order_id"] for item in reservations], ["O-14", "O-22"])
