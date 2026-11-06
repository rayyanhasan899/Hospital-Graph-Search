# Validation and limitations

## Observed locally — 6 November 2026

Python 3.14.7 ran the standard-library test suite successfully:

```powershell
python -m unittest discover -s tests -v
```

One parameterized test method checks all **36 start/goal pairs**, for each of GBFS and A*. It verifies reachability and returned path costs; A* costs match an independent exhaustive-path reference on this supplied graph. This is not a proof for arbitrary graphs or inadmissible heuristics.

The UI environment was installed with Streamlit 1.67.0, but Windows Application Control blocked native pandas dependencies during a shared smoke-test run before this app's UI checks could execute. Interactive Streamlit behavior is therefore not reported as passing. No system security settings were changed. The original algorithm and UI source remain unchanged.
