import unittest

from parcel_dispatch.labels import render_pick_label
from parcel_dispatch.manifests import manifest_filename, manifest_summary
from parcel_dispatch.workflow import schedule_order


class DispatchTests(unittest.TestCase):
    def test_manifest_sorts_parcels_and_names_the_export(self):
        self.assertEqual(manifest_summary("ROUTE 2", ["P-8", "P-2"])["parcel_ids"], ["P-2", "P-8"])
        self.assertEqual(manifest_filename("ROUTE 2"), "manifest-route-2.json")

    def test_order_gets_a_reservation(self):
        reservation = schedule_order({"id": "O-14", "destination": "BLR", "carrier": "parcelco"})
        self.assertEqual(reservation["destination"], "BLR")
        self.assertEqual(reservation["state"], "reserved")

    def test_label_normalizes_the_printed_order(self):
        self.assertEqual(render_pick_label("o-14", "r3"), "R3 / O-14")
