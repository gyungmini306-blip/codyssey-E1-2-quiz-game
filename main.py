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


class QuizGame:
    def show_menu(self):
        print("\n=== 코디세이 E1-1 · E1-2 복습 퀴즈 ===")
        print("1. 퀴즈 풀기\n2. 퀴즈 추가\n3. 퀴즈 목록\n4. 점수 확인\n5. 종료")

    def run(self):
        try:
            while True:
                self.show_menu()
                choice = read_number("선택: ", 1, 5)
                if choice == 5:
                    print("퀴즈 게임을 종료합니다.")
                    break
                print("이 기능은 개발 중입니다.")
        except (KeyboardInterrupt, EOFError):
            print("\n입력이 중단되어 안전하게 종료합니다.")


if __name__ == "__main__":
    QuizGame().run()
