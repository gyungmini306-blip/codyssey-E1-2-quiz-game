from quiz import Quiz


def create_default_quizzes():
    """E1-1 세 문제와 E1-2 두 문제를 새 객체로 생성합니다."""
    return [
        Quiz(
            "[E1-1] 리눅스 터미널에서 현재 작업 디렉터리의 경로를 확인하는 명령은?",
            ["pwd", "mkdir", "cp", "mv"],
            1,
        ),
        Quiz(
            "[E1-1] docker run -p 8080:80에서 호스트의 접속 포트는?",
            ["80", "8080", "8000", "443"],
            2,
        ),
        Quiz(
            "[E1-1] Docker 볼륨을 사용하면 어떤 효과를 얻을 수 있나요?",
            ["이미지가 자동 업데이트된다", "Git 커밋이 생성된다",
             "컨테이너를 삭제해도 볼륨을 삭제하지 않으면 데이터를 유지할 수 있다",
             "모든 포트가 자동으로 공개된다"],
            3,
        ),
        Quiz(
            "[E1-2] Python에서 객체를 생성할 때 초기 속성을 설정하는 메서드는?",
            ["print", "input", "append", "__init__"],
            4,
        ),
        Quiz(
            "[E1-2] 원격 저장소를 새로운 로컬 디렉터리에 복제하는 Git 명령은?",
            ["git clone", "git add", "git commit", "git status"],
            1,
        ),
    ]
