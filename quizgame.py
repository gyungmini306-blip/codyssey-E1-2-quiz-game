import json
import random
from pathlib import Path

from defaults import create_default_quizzes
from quiz import Quiz


def read_number(prompt, minimum, maximum):
    """유효한 범위의 정수를 입력할 때까지 다시 묻습니다."""
    while True:
        value = input(prompt).strip()
        if not value:
            print("입력이 비어 있습니다. 숫자를 입력하세요.")
            continue
        try:
            number = int(value)
        except ValueError:
            print("숫자로 입력하세요.")
            continue
        if minimum <= number <= maximum:
            return number
        print(f"{minimum}~{maximum} 사이의 숫자를 입력하세요.")


def read_text(prompt):
    while True:
        text = input(prompt).strip()
        if text:
            return text
        print("빈 내용은 등록할 수 없습니다. 다시 입력하세요.")


class QuizGame:
    def __init__(self, state_path=None):
        self.state_path = (
            Path(state_path) if state_path is not None
            else Path(__file__).resolve().parent / "state.json"
        )
        self.quizzes = create_default_quizzes()
        self.best_score = None
        self.backup_path = self.state_path.with_suffix(self.state_path.suffix + ".bak")
        self.load_state()

    def decode_state(self, content):
        data = json.loads(content)
        if not isinstance(data, dict):
            raise ValueError("저장 데이터는 딕셔너리여야 합니다.")

        items = data.get("quizzes")
        if not isinstance(items, list):
            raise ValueError("quizzes는 목록이어야 합니다.")

        quizzes = []
        for item in items:
            if not isinstance(item, dict):
                raise ValueError("퀴즈 항목은 객체여야 합니다.")
            quizzes.append(Quiz(item.get("question"), item.get("choices"), item.get("answer")))
        if "best_score" not in data:
            raise ValueError("최고 점수 항목이 없습니다.")
        best_score = data["best_score"]
        if best_score is not None:
            if type(best_score) not in (int, float):
                raise ValueError("최고 점수는 숫자여야 합니다.")
            if not 0 <= best_score <= 100:
                raise ValueError("최고 점수는 0~100이어야 합니다.")

        return quizzes, best_score

    def load_state(self):
        for path in (self.state_path, self.backup_path):
            try:
                quizzes, score = self.decode_state(path.read_text(encoding="utf-8"))
            except FileNotFoundError:
                continue
            except (ValueError, RecursionError, OSError):
                print(f"저장 파일을 사용할 수 없습니다: {path.name}")
                continue
            self.quizzes, self.best_score = quizzes, score
            if path == self.backup_path:
                print("백업에서 데이터를 복원했습니다. 다음 저장 시 state.json에 반영합니다.")
            else:
                print(f"저장된 데이터를 불러왔습니다. (퀴즈 {len(quizzes)}개)")
            return
        print("사용 가능한 저장 파일이 없어 기본 퀴즈로 시작합니다.")

    def backup_current_state(self):
        try:
            content = self.state_path.read_text(encoding="utf-8")
            self.decode_state(content)
        except (FileNotFoundError, ValueError, RecursionError):
            return
        temporary = self.backup_path.with_suffix(".bak.tmp")
        temporary.write_text(content, encoding="utf-8")
        temporary.replace(self.backup_path)

    def save_state(self):
        quizzes = []
        for quiz in self.quizzes:
            quizzes.append(quiz.to_dict())

        data = {
            "quizzes": quizzes,
            "best_score": self.best_score,
        }
        temporary_path = self.state_path.with_name(self.state_path.name + ".tmp")
        try:
            with temporary_path.open("w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=2, allow_nan=False)
                file.write("\n")
            self.backup_current_state()
            temporary_path.replace(self.state_path)
            return True
        except (OSError, ValueError):
            print("파일 저장에 실패했습니다. 폴더 권한과 저장 공간을 확인하세요.")
            return False

    def show_menu(self):
        print("\n=== 코디세이 E1-2 · 파이썬 기초 퀴즈 ===")
        print("1. 퀴즈 풀기\n2. 퀴즈 추가\n3. 퀴즈 목록\n4. 점수 확인\n5. 종료")

    def show_score(self):
        if self.best_score is None:
            print("아직 완료한 게임이 없습니다. 퀴즈를 먼저 풀어 보세요.")
        else:
            print(f"최고 점수: {self.best_score:g}점 (100점 만점)")

    def list_quizzes(self):
        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
            return
        print(f"\n등록된 퀴즈 목록 (총 {len(self.quizzes)}개)")
        for number, quiz in enumerate(self.quizzes, start=1):
            print(f"[{number}] {quiz.question}")

    def add_quiz(self):
        print("\n새 퀴즈를 등록합니다.")
        question = read_text("문제: ")
        choices = []
        for number in range(1, 5):
            choices.append(read_text(f"선택지 {number}: "))
        answer = read_number("정답 번호 (1~4): ", 1, 4)
        self.quizzes.append(Quiz(question, choices, answer))
        print("퀴즈가 추가되었습니다.")
        self.save_state()

    def play(self):
        if not self.quizzes:
            print("등록된 퀴즈가 없습니다. 먼저 퀴즈를 추가하세요.")
            return
        correct = 0
        questions = self.quizzes.copy()
        random.shuffle(questions)
        total = len(questions)
        print(f"\n퀴즈를 무작위 순서로 출제합니다. (총 {total}문제)")
        for number, quiz in enumerate(questions, start=1):
            print(f"\n[문제 {number}/{total}]")
            quiz.display()
            answer = read_number("정답 번호 (1~4): ", 1, 4)
            if quiz.is_correct(answer):
                print("정답입니다!")
                correct += 1
            else:
                print(f"오답입니다. 정답: {quiz.answer}. {quiz.choices[quiz.answer - 1]}")
        score = round(correct / total * 100, 2)
        print(f"\n결과: {total}문제 중 {correct}문제 정답! ({score:g}점)")
        if self.best_score is None or score > self.best_score:
            self.best_score = score
            print("새로운 최고 점수입니다!")
        self.save_state()
        return score

    def run(self):
        try:
            while True:
                self.show_menu()
                choice = read_number("선택: ", 1, 5)
                if choice == 5:
                    print("퀴즈 게임을 종료합니다.")
                    break
                elif choice == 1:
                    self.play()
                elif choice == 2:
                    self.add_quiz()
                elif choice == 3:
                    self.list_quizzes()
                elif choice == 4:
                    self.show_score()
        except (KeyboardInterrupt, EOFError):
            print("\n입력이 중단되어 안전하게 종료합니다.")
        finally:
            if self.save_state():
                print("데이터를 저장했습니다.")
