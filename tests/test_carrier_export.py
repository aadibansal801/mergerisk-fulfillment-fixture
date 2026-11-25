import json
import unittest

from parcel_dispatch.manifests import carrier_manifest


class CarrierExportTests(unittest.TestCase):
    def test_exports_the_carrier_manifest_as_json(self):
        actual = json.loads(carrier_manifest("ROUTE 2", ["P-8", "P-2"]))
        self.assertEqual(actual, {"route_id": "ROUTE 2", "parcel_count": 2, "parcel_ids": ["P-2", "P-8"]})
