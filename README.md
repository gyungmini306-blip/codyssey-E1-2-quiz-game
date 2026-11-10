# 코디세이 E1-2 — Python 콘솔 퀴즈 게임
## 현재 로컬 작업 위치

이 과제의 현재 작업 폴더는 `C:\Users\gyung\codyssey\e1-2`입니다.
PowerShell에서 아래 명령으로 이동한 뒤 이 문서의 실습 명령을 실행합니다.

```powershell
cd C:\Users\gyung\codyssey\e1-2
```


코디세이 입학연수 E1-2 「컴퓨터에게 명령 내리는 말(파이썬) 처음 배우기」 과제입니다.
E1-1과 E1-2에서 학습한 내용을 복습하는 Python 콘솔 퀴즈 게임입니다.

- GitHub 저장소: [codyssey-E1-2-quiz-game](https://github.com/gyungmini306-blip/codyssey-E1-2-quiz-game)
- 이전 과제: [E1-1 개발 워크스테이션](https://github.com/gyungmini306-blip/codyssey-E1-1-dev-workstation)

## 주제 선정 이유

개발 환경 구성과 Python·Git 개념을 문제로 풀며 복습하고, 이해가 부족한 부분을 확인하기 위해 선택했습니다.

## 개발 환경

- Python 3.10 이상
- Python 표준 라이브러리만 사용
- 실제 확인 환경: Windows / PowerShell / Python 3.13.3 / Git 2.52.0.windows.1

## 실행 방법

프로젝트 폴더에서 다음 명령을 실행합니다.

```shell
python main.py
```

Windows에서 `python` 명령이 없다면 `py main.py`를 사용합니다.
외부 패키지 설치는 필요하지 않습니다.

## 기능 목록

1. 퀴즈 풀기: 전체 문제를 무작위 순서로 출제하고 정오답과 최종 점수를 표시합니다.
2. 퀴즈 추가: 문제, 선택지 4개, 정답 번호 1~4를 입력하여 등록합니다.
3. 퀴즈 목록: 등록된 문제의 제목을 확인합니다.
4. 점수 확인: 완료한 게임의 최고 점수를 확인합니다.
5. 종료: 데이터를 저장하고 종료합니다.

숫자 입력은 앞뒤 공백을 제거하며, 빈 입력·문자·범위 밖 숫자는 다시 입력받습니다.
문제와 선택지는 빈 내용을 등록할 수 없습니다.
Ctrl+C 또는 입력 스트림 종료 시 안내 후 저장을 시도합니다.
입력 도중 중단된 새 문제는 등록하지 않으며, 미완료 게임은 점수에 반영하지 않습니다.

## 기본 문제

- E1-1: 현재 경로 확인 명령, Docker 포트 매핑, 볼륨의 데이터 유지
- E1-2: `__init__`의 역할, `git clone`의 역할

기본 문제는 총 5개입니다. 내용을 직접 검토하고 본인이 이해한 표현으로 수정할 수 있습니다.

## 보너스 과제: 랜덤 출제

게임을 시작할 때마다 Python 표준 라이브러리 `random`의 `shuffle()`로 문제 순서를 섞습니다.
`self.quizzes.copy()`로 만든 목록을 섞으므로 퀴즈 목록과 저장 파일의 등록 순서는 유지합니다.
선택지와 정답 번호는 바뀌지 않으며, 모든 문제를 한 번씩 출제합니다.
무작위이므로 이전 게임과 같은 순서가 나올 수도 있습니다.

## 직접 체험하기

프로젝트 폴더에서 `python main.py`를 실행한 다음 아래 순서로 확인합니다.

1. `3`: 기본 퀴즈 5개 목록 확인
2. `4`: 아직 완료한 게임이 없다는 안내 확인 (첫 실행 기준)
3. `1`: 1~4 중 정답 번호를 입력하여 전체 문제 풀이 및 결과 확인
4. `1`: 다시 풀며 랜덤 출제 확인
5. `2`: 자신이 만든 문제, 선택지 4개, 정답 번호 입력
6. `3`: 추가한 문제가 목록에 나타나는지 확인
7. `5`: 종료 후 다시 `python main.py` 실행
8. `3`, `4`: 추가한 문제와 최고 점수가 유지되는지 확인

메뉴에 `abc`, 빈 입력, `9`를 입력하면 재입력 안내도 확인할 수 있습니다.

## 이 과제에서 배울 내용

| 학습 내용 | 이 프로젝트에서 확인할 부분 |
|---|---|
| 변수와 자료형 | 문제 문자열, 선택지 목록, 정답 정수, 정답 여부 bool, JSON용 dict |
| 조건문과 반복문 | 메뉴의 if/elif, 재입력의 while, 문제 출제의 for |
| 함수와 반환값 | `read_number()`가 검증한 숫자를 반환하는 흐름 |
| 클래스와 객체 | `Quiz`는 개별 문제, `QuizGame`은 게임 전체를 관리. `__init__`은 초기 속성을 설정하고 `self`는 해당 객체를 가리킴 |
| 파일과 예외 처리 | JSON 저장/불러오기, 파일 손상과 입력 중단 시 try/except |
| Git과 GitHub | 기능별 커밋, 브랜치 병합, 원격 push, clone 및 pull |
| 랜덤과 목록 복사 | `shuffle()`은 목록을 직접 변경하므로 원본을 보존하려면 복사본 사용 |

스스로 설명해 볼 질문: 왜 `while`과 `for`를 다르게 썼을까? 왜 클래스를 두 개로 나눴을까?
왜 종료 후에도 문제가 남아 있을까? `random.shuffle()`의 반환값을 변수에 넣으면 왜 안 될까?

## 파일 구조

```text
e1-2/
├── main.py          # QuizGame, 입력 처리, 메뉴, 진행, 저장/불러오기
├── quiz.py          # Quiz: 개별 문제 검증, 출력, 정답 확인
├── defaults.py      # 기본 퀴즈 5개 생성
├── test_game.py     # 표준 unittest를 사용한 동작 검증
├── docs/            # 최종 확인, 콘솔 실행 결과, Git 실습 기록
├── README.md
├── .gitignore
└── state.json       # 실행 후 자동 생성되는 개인 데이터
```

## 데이터 파일

`state.json`은 현재 터미널 위치와 관계없이 `main.py`와 같은 프로젝트 루트에 저장합니다.
UTF-8 인코딩을 사용하며, 한글은 그대로 기록합니다.

```json
{
  "quizzes": [
    {
      "question": "리눅스에서 현재 작업 경로를 확인하는 명령은?",
      "choices": ["pwd", "mkdir", "cp", "mv"],
      "answer": 1
    }
  ],
  "best_score": null
}
```

- `quizzes`: 문제 목록. 빈 목록도 허용합니다.
- `question`: 비어 있지 않은 문제 문자열
- `choices`: 비어 있지 않은 선택지 문자열 4개
- `answer`: 1~4의 정수
- `best_score`: 미플레이 시 `null`, 플레이 후 0~100의 최고 점수

점수는 `정답 수 / 전체 문제 수 × 100`이며 소수 둘째 자리까지 반올림합니다.
문제가 추가되어도 백분율로 비교합니다. 0점으로 완료한 게임은 미플레이와 구분합니다.

파일이 없으면 기본 퀴즈로 시작합니다. JSON 문법 또는 데이터 구조가 잘못되면
안내 후 기본 퀴즈와 미플레이 상태로 초기화합니다. 이후 저장 시 초기화된 내용으로 덮어씁니다.
읽기·쓰기 권한 오류는 안내 메시지로 처리합니다. 저장 실패 시 재실행 후 데이터 유지는 보장되지 않습니다.
저장 중 원본 손상을 줄이기 위해 임시 파일에 쓴 후 `state.json`을 교체합니다.

`state.json`과 임시 저장 파일은 개인 실행 데이터이므로 Git에서 제외합니다.
새로 복제한 저장소에서도 기본 문제 5개로 시작할 수 있습니다.

## 검증 방법

```shell
python -m unittest -v
```

자동 검증 항목: 잘못된 숫자 입력, 퀴즈 추가 및 최고 점수의 재실행 후 유지,
낮은 점수로 최고 점수를 덮어쓰지 않음, 파일 손상 복구, 빈 문제 목록,
Ctrl+C·EOF 중단 후 저장, 읽기·쓰기 오류 처리, 랜덤 출제 시 전체 문제 1회 출제 및 등록 순서 보존.

실제 실행에서도 메뉴 → 목록 → 추가 → 퀴즈 풀기 → 점수 확인 → 종료 → 재실행 순으로 확인합니다.

최종 확인 결과: 자동 검증 7개 통과, 실제 콘솔 프로그램의 추가·플레이·점수·재실행·EOF·손상 복구 확인.
점검은 별도 복사본에서 수행하여 사용자 실행 데이터를 바꾸지 않았습니다.

- [최종 요구사항 확인 기록](docs/final-review.md)
- [실제 콘솔 실행 결과](docs/console-verification.txt)
- [Git 개발 이력 텍스트](docs/git-history.txt)

## Git 개발 기록

기능별 커밋을 남겼으며, 퀴즈 풀기는 `feature/play` 브랜치에서 개발한 뒤
`main`으로 `--no-ff` 병합하여 분기와 병합이 그래프에 표시되도록 했습니다.

```shell
git log --oneline --graph --all
```

## GitHub 연결 및 복제 실습 방법

아래는 이 프로젝트의 GitHub 연결 및 복제 실습 명령입니다.

1. GitHub에서 `codyssey-E1-2-quiz-game`이라는 빈 저장소를 만듭니다. README, .gitignore, 라이선스를 자동 생성하지 않습니다.
2. 이 프로젝트 폴더에서 원격 저장소에 연결하고 업로드합니다.

```shell
git remote add origin https://github.com/gyungmini306-blip/codyssey-E1-2-quiz-game.git
git push -u origin main
git push origin feature/play
```

3. 프로젝트의 상위 폴더로 이동하여 별도 디렉터리에 복제합니다.

```shell
cd ..
git clone https://github.com/gyungmini306-blip/codyssey-E1-2-quiz-game.git codyssey-quiz-clone
cd codyssey-quiz-clone
```

4. 복제한 폴더의 README 맨 아래에 `복제 저장소에서 변경 후 원본으로 pull 실습 완료.`를 추가하고 저장합니다.

```shell
git add README.md
git commit -m "Docs: 복제 저장소 변경 실습 기록 추가"
git push
cd ../e1-2
git pull
```

5. 원본 README에 추가한 문장이 나타나는지 확인합니다.
명령 입력과 출력 결과를 캡처하여 clone과 pull 실습 증거로 남깁니다.
실제 수행 결과는 [GitHub 업로드 및 복제 실습 기록](docs/git-workflow.md)에 정리합니다.

## 제출 체크리스트

- [x] GitHub 저장소 업로드 및 URL 확인
- [x] 필수 프로그램 기능과 보너스 랜덤 출제 검증
- [x] 실제 실행 및 데이터 유지·오류 처리 결과를 텍스트로 기록
- [x] VS Code, Python 버전, Git 설정 등 개발 환경 스크린샷
- [ ] 퀴즈 추가, 목록, 플레이, 점수 확인 실행 스크린샷
- [x] 종료 후 재실행하여 데이터 유지 확인 (자동 검증 및 실제 프로세스 실행)
- [x] `git log --oneline --graph --all` 결과 스크린샷 (실제 출력을 VS Code에서 열어 촬영)
- [x] GitHub 저장소 clone → 변경 → commit → push → 원본 pull 실습
- [ ] 코드의 입력 처리, 클래스, 저장 흐름을 직접 설명할 수 있는지 확인

스크린샷을 `docs/screenshots/`에 저장한 경우 README에 상대 경로 링크를 추가합니다.
토큰과 비밀번호는 캡처하지 않습니다.
개발 환경과 Git 이력 이미지를 확보했습니다. 퀴즈 실행 이미지와 본인 학습 확인은 아직 미완료입니다.

복제 저장소에서 변경 후 원본으로 pull 실습 완료.

## 스크린샷 증거

### 개발 환경

사용자가 촬영한 실제 Python·Git 버전 및 사용자 설정 화면입니다.

![Python 및 Git 환경](docs/screenshots/environment.png)

사용자가 촬영한 VS Code 소스 제어 및 프로젝트 이력 화면입니다.

![VS Code 개발 환경](docs/screenshots/vscode-git.png)

### Git 이력

실제 `git log --oneline --graph --all` 출력을 [텍스트 파일](docs/git-graph.txt)로 저장하고 VS Code에서 열어 촬영했습니다. 터미널 화면을 재구성한 이미지가 아닙니다.

![실제 Git 그래프 출력을 표시한 VS Code](docs/screenshots/git-graph.png)

### 퀴즈 실행

추가·목록·플레이·점수 확인의 실제 실행 스크린샷은 아직 수집하지 않았습니다.
