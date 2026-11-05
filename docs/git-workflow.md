# E1-2 GitHub 업로드 및 복제 실습

실습일: 2026-11-06

## 저장소

- E1-1: https://github.com/gyungmini306-blip/codyssey-E1-1-dev-workstation
- E1-2: https://github.com/gyungmini306-blip/codyssey-E1-2-quiz-game
- E1-2 제목: 코디세이 E1-2 — Python 콘솔 퀴즈 게임

## 초기 업로드

원본 프로젝트 디렉터리에서 실행했습니다.

```text
git remote add origin https://github.com/gyungmini306-blip/codyssey-E1-2-quiz-game.git
git push -u origin main
branch 'main' set up to track 'origin/main'.
 * [new branch]      main -> main

git push origin feature/play
 * [new branch]      feature/play -> feature/play
```

`feature/play`의 퀴즈 풀기 기능은 로컬 개발 시 이미 main에 병합했습니다.
`git log --oneline --graph --all`로 분기와 병합을 확인할 수 있습니다.

## clone 및 복제본 변경

별도 작업 디렉터리에 복제했습니다.

```text
git clone https://github.com/gyungmini306-blip/codyssey-E1-2-quiz-game.git work/codyssey-quiz-clone
Cloning into 'work/codyssey-quiz-clone'...
```

복제본 README에 다음 문장을 추가하고, 제출 체크리스트와 이 실습 기록을 작성했습니다.

```text
복제 저장소에서 변경 후 원본으로 pull 실습 완료.
```

복제본에서 변경사항을 커밋하고 업로드한 뒤 원본에서 가져오는 순서는 다음과 같습니다.
복제본의 커밋 번호는 `2a723ea`이며, 원본에서 다음 pull 결과를 확인했습니다.

```shell
git add README.md docs/git-workflow.md
git commit -m "Docs: 복제 저장소에서 GitHub 실습 기록 추가"
git push
# 원본 프로젝트 디렉터리에서
git pull --ff-only
```

```text
From https://github.com/gyungmini306-blip/codyssey-E1-2-quiz-game
   140dcb9..2a723ea  main -> origin/main
Updating 140dcb9..2a723ea
Fast-forward
 README.md            |  8 ++++---
 docs/git-workflow.md | 65 ++++++++++++++++++++++++++++++++++++++++++++++++++++
 2 files changed, 70 insertions(+), 3 deletions(-)
 create mode 100644 docs/git-workflow.md
```

원본에서 `git log -1 --oneline`로 `2a723ea` 커밋을 확인하고,
README에 실습 문장이 반영된 것을 확인했습니다.

## 자동 검증

```text
python -m unittest -v
Ran 6 tests
OK
```

빈 입력·문자·범위 밖 숫자, 추가한 문제와 최고 점수의 재실행 후 유지,
손상된 파일 복구, 입력 중단 후 저장, 읽기·쓰기 실패를 검증했습니다.

환경 및 실행 결과와 Git 그래프의 실제 화면 캡처는 별도로 수집해야 합니다.
