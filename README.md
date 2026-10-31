# endpoint-compliance-scorer

Score each endpoint's compliance (patching, antivirus, encryption, firewall, recent check-in) out of 100 and list the worst first, so remediation starts where it matters.

## How to run

```sh
python3 main.py endpoints.csv
```

## Example output

```
pc2: 40/100 NON-COMPLIANT
pc1: 100/100 COMPLIANT
1/2 endpoint(s) non-compliant.
```

Standard library only. Run the tests with `python3 -m unittest discover`.
