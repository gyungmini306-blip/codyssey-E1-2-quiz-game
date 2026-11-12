import contextlib
import io
import platform
import statistics
import tempfile
import tracemalloc
from pathlib import Path
from time import perf_counter

from main import QuizGame
from quiz import Quiz


def measure(action):
    samples = []
    for _ in range(10):
        start = perf_counter()
        action()
        samples.append((perf_counter() - start) * 1000)
    return f"{statistics.median(samples):.3f} ms"


def main():
    with tempfile.TemporaryDirectory(dir=Path(__file__).resolve().parent) as folder:
        path = Path(folder) / "state.json"
        with contextlib.redirect_stdout(io.StringIO()):
            game = QuizGame(path)
            game.quizzes = [
                Quiz(f"연습 퀴즈 {i}", ["가", "나", "다", "라"], 1)
                for i in range(1000)
            ]

            def save():
                if not game.save_state():
                    raise RuntimeError("Benchmark save failed")

            save()
            save_time = measure(save)
            load_time = measure(lambda: QuizGame(path))
            search_time = measure(
                lambda: next(q for q in game.quizzes if q.question == "연습 퀴즈 999")
            )
            tracemalloc.start()
            try:
                loaded = QuizGame(path)
                assert len(loaded.quizzes) == 1000
                _, peak = tracemalloc.get_traced_memory()
            finally:
                tracemalloc.stop()
        print(f"환경: {platform.system()}, Python {platform.python_version()}")
        print(f"로드 중앙값 | {load_time}")
        print(f"저장 중앙값 (백업 포함) | {save_time}")
        print(f"마지막 제목 선형 탐색 중앙값 | {search_time}")
        print(f"로드 중 Python 할당 피크 | {peak / 1024:.1f} KiB")
        print(f"JSON 파일 크기 | {path.stat().st_size / 1024:.1f} KiB")


if __name__ == "__main__":
    main()
