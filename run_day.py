# adventOfCode/run_day.py
from __future__ import annotations

import importlib
import os
import sys
from pathlib import Path


def file_to_module(workspace_root: Path, file_path: Path) -> str:
    """
    Convert:
      <root>/adventOfCode/2025/day08.py
    into:
      adventOfCode.2025.day08
    """
    rel = file_path.relative_to(workspace_root)
    if rel.suffix != ".py":
        raise ValueError(f"Not a .py file: {rel}")
    parts = list(rel.with_suffix("").parts)  # remove ".py"
    return ".".join(parts)


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python -m adventOfCode.run_day <path-to-dayXX.py>")
        sys.exit(2)

    # VS Code will pass an absolute path for ${file}
    file_path = Path(sys.argv[1]).resolve()

    # Assume workspace root is the current working directory
    workspace_root = Path(os.getcwd()).resolve()

    # Ensure workspace root is on sys.path so "adventOfCode.*" imports work
    if str(workspace_root) not in sys.path:
        sys.path.insert(0, str(workspace_root))

    module_name = file_to_module(workspace_root, file_path)

    # Import the module (this makes relative imports inside it work)
    mod = importlib.import_module(module_name)

    # Optional convention: if the module has main(), call it
    if hasattr(mod, "main") and callable(getattr(mod, "main")):
        mod.main()


if __name__ == "__main__":
    main()
