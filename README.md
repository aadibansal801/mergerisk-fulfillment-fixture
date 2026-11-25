# Fulfillment merge fixture

A small fictional fulfillment service for composing carrier manifests, reserving shipments and printing dispatch labels. It uses Python's standard library and synthetic order IDs.

## Try it in MergeRisk

Paste `https://github.com/aadibansal801/mergerisk-fulfillment-fixture` into the [hosted beta](https://mergerisk-beta.onrender.com/), then enter the target and source names from one case. Each parent passes its own test suite. All four pairs merge cleanly in Git.

### Carrier export loses its JSON import

- Target `shipping/trim-imports`
- Source `shipping/carrier-export`
- Expected `MR-PY-IMPORT-001` and a verified patch that restores the original import. The combined export test fails with `NameError` before repair.

### Batch booking omits a new required carrier

- Target `dispatch/require-carrier`
- Source `dispatch/batch-booking`
- Expected `MR-PY-SIG-002`. The combined batch booking test fails with `TypeError`. Choosing a carrier requires a product decision.

### Bulk label printing calls the old formatter name

- Target `labels/rename-formatter`
- Source `labels/bulk-printing`
- Expected `MR-PY-RENAME-001`. The combined test fails with `NameError`. Review the rename before applying it.

### Clean control

- Target `shipping/trim-imports`
- Source `dispatch/require-carrier`
- Expected no merge-introduced findings. The combined tests pass.

## Run the tests locally

```sh
python -m unittest discover -s tests -v
```
