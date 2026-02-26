# AGENTS.md

## Cursor Cloud specific instructions

### Overview
BusNetPy is a Python library for Chinese public transit (bus) network analysis. It scrapes bus route data from AMap API and 8684.cn, builds geospatial datasets, constructs graph-based network models (Space-L and Space-P), computes transit metrics, and visualizes results.

### Package structure
All source code lives in `BusNetPynew/`. There is no `setup.py` or `pyproject.toml`; the package is imported directly from the workspace root via `import BusNetPynew` or `from BusNetPynew import <module>`.

### Running and testing
- **Import test**: `python3 -c "import BusNetPynew; print(BusNetPynew.__all__)"`
- **Lint**: `flake8 BusNetPynew/ --max-line-length=150 --exclude=BusNetPynew/citycode.py,BusNetPynew/ChineseAdminiDivisionsDict.py`
- **Tests**: `python3 -m pytest tests/ -v` (34 unit tests covering coordinate conversion, cycle detection, utils, Space-L/Space-P network, route planning, imports)

### Key caveats
- Data collection features (`buspider.buspi.businfo()`) require AMap API keys (`key`, `key_fwd`, `jscode`). Without these keys, data scraping will not work, but all offline analysis (network construction, metrics, route planning, visualization) can be exercised with synthetic or pre-collected CSV data.
- The `conversion_geo.py` module has an unqualified import (`from ChineseAdminiDivisionsDict import ...`) that only works when run from inside `BusNetPynew/` directory. This module is commented out in `buspider.py` and is not part of the standard import chain.
- `matplotlib` requires a non-interactive backend (`Agg`) in headless environments: `import matplotlib; matplotlib.use('Agg')`.
- Dependencies are declared in `requirements.txt` at the repo root.
