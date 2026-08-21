from pathlib import Path

from src.benchmark import run


def test_benchmark_generates_results() -> None:
    """Smoke test."""

    output_file = Path("outputs/results.csv")

    if output_file.exists():
        output_file.unlink()

    run()

    assert output_file.exists()
