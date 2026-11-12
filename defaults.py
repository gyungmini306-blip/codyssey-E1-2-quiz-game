from quiz import Quiz


def create_default_quizzes():
    """파이썬 기초 문제 다섯 개를 생성합니다."""
    return [
        Quiz('input()이 반환하는 값의 기본 자료형은?', ['str', 'int', 'bool', 'list'], 1),
        Quiz('range(1, 5)에서 마지막으로 나오는 정수는?', ['3', '4', '5', '6'], 2),
        Quiz('함수에서 호출한 곳으로 값을 보내는 키워드는?', ['break', 'print', 'return', 'continue'], 3),
        Quiz('Python에서 객체를 생성할 때 초기 속성을 설정하는 메서드는?', ['print', 'input', 'append', '__init__'], 4),
        Quiz('딕셔너리에서 값을 찾을 때 사용하는 것은?', ['키', '들여쓰기', '반복 횟수', '파일 확장자'], 1),
    ]
