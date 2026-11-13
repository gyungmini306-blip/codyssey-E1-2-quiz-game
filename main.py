from quizgame import QuizGame


if __name__ == "__main__":
    try:
        QuizGame().run()
    except (KeyboardInterrupt, EOFError):
        print("\n프로그램 시작 또는 저장 중 입력이 중단되어 종료합니다.")
