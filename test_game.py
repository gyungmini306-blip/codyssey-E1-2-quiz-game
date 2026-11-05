import contextlib
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from main import QuizGame, read_number


class GameTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory(dir=Path(__file__).resolve().parent)
        self.addCleanup(self.directory.cleanup)
        self.path = Path(self.directory.name) / "state.json"
        self.output = io.StringIO()
        self.capture = contextlib.redirect_stdout(self.output)
        self.capture.__enter__()
        self.addCleanup(self.capture.__exit__, None, None, None)

    def test_invalid_numbers_retry_and_trim_spaces(self):
        with patch("builtins.input", side_effect=["", "abc", "0", "9", " 2 "]):
            self.assertEqual(read_number("", 1, 5), 2)

    def test_add_and_score_survive_restart(self):
        game = QuizGame(self.path)
        with patch("builtins.input", side_effect=["", "새 문제", "가", "나", "다", "라", "x", "5", "2"]):
            game.add_quiz()
        with patch("builtins.input", side_effect=["1", "2", "3", "4", "1", "2"]):
            self.assertEqual(game.play(), 100)
        restored = QuizGame(self.path)
        self.assertEqual(len(restored.quizzes), 6)
        self.assertEqual(restored.quizzes[-1].question, "새 문제")
        self.assertEqual(restored.best_score, 100)
        with patch("builtins.input", return_value="3"):
            restored.play()
        self.assertEqual(QuizGame(self.path).best_score, 100)

    def test_corrupt_and_invalid_schema_restore_defaults(self):
        cases = ["{broken", "[]", '{"quizzes": [], "best_score": true}',
                 '{"quizzes": [], "best_score": 101}',
                 '{"quizzes": [{}], "best_score": null}']
        for content in cases:
            with self.subTest(content=content):
                self.path.write_text(content, encoding="utf-8")
                game = QuizGame(self.path)
                self.assertEqual(len(game.quizzes), 5)
                self.assertIsNone(game.best_score)
                self.assertTrue(game.save_state())
                json.loads(self.path.read_text(encoding="utf-8"))

    def test_empty_quizzes_and_zero_score_are_valid(self):
        self.path.write_text('{"quizzes": [], "best_score": 0}', encoding="utf-8")
        game = QuizGame(self.path)
        self.assertEqual(game.quizzes, [])
        self.assertEqual(game.best_score, 0)
        self.assertIsNone(game.play())
        game.list_quizzes()
        game.show_score()

    def test_interruption_does_not_add_partial_quiz_and_saves(self):
        for interrupt in (KeyboardInterrupt, EOFError):
            with self.subTest(interrupt=interrupt):
                game = QuizGame(self.path)
                with patch("builtins.input", side_effect=["2", "미완성 문제", interrupt()]):
                    game.run()
                restored = QuizGame(self.path)
                self.assertEqual(len(restored.quizzes), 5)
                self.assertIsNone(restored.best_score)

    def test_file_access_failures_are_reported(self):
        game = QuizGame(self.path)
        with patch.object(Path, "open", side_effect=PermissionError):
            game.load_state()
            self.assertFalse(game.save_state())
        self.assertIn("저장에 실패", self.output.getvalue())


if __name__ == "__main__":
    unittest.main()
