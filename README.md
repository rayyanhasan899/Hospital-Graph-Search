# Hospital Graph Search Lab

A small academic lab visualizing **Greedy Best-First Search (GBFS)** and **A*** over a six-node directed hospital supply graph. The Streamlit interface lets you select start/goal nodes and displays the returned path and weighted cost with NetworkX and Matplotlib.

## Run locally

```powershell
python -m venv .venv
.venv\Scripts\python -m pip install -r requirements.txt
.venv\Scripts\python -m streamlit run app.py
```

On Ubuntu use `.venv/bin/python` instead. Choose the initial node, destination, and algorithm, then select **Run Search**. Edges are directed: a reverse journey is not necessarily reachable.

## Implementation

- `searchAlgos.py`: graph, coordinates, Euclidean heuristic, priority queues, and path reconstruction.
- `app.py`: controls and graph rendering.
- The notebook preserves the associated lab work.

GBFS prioritizes estimated distance to the goal; A* combines travelled cost with the heuristic. The supplied coordinates and weights are teaching data. Some Euclidean distances exceed corresponding edge costs, so a general optimality guarantee is not asserted. See [validation notes](docs/VALIDATION.md) for checks on this specific graph.

This is an algorithms lab, not a real hospital routing system. No deployment, real medical use, or AI-model training is claimed. The original tracked `__pycache__` is retained; new bytecode/build artifacts are ignored.

Academic lab work by Syed Muhammad Rayyan Hassan.
