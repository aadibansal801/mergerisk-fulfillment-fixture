import unittest

from parcel_dispatch.labels import print_pick_batch


class BulkLabelTests(unittest.TestCase):
    def test_formats_one_print_line_per_order(self):
        actual = print_pick_batch([{ "id": "o-14", "aisle": "r3"}, { "id": "o-22", "aisle": "r4"}])
        self.assertEqual(actual, "R3 / O-14\nR4 / O-22")
