"""Prepare outbound parcel manifests for warehouse staff."""

import json


def manifest_summary(route_id, parcel_ids):
    return {
        "route_id": route_id,
        "parcel_count": len(parcel_ids),
        "parcel_ids": sorted(parcel_ids),
    }


def manifest_filename(route_id):
    return f"manifest-{route_id.lower().replace(' ', '-')}.json"
