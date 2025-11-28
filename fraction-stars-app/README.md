# 분수 스타 게임 (fraction-stars-app)

간단한 초등학교 3학년용 분수 학습 Streamlit 앱입니다. 학생들이 색이 칠해진 별(🌟)의 개수를 전체 별 수로 나타내는 분수를 입력하며 분수의 의미를 익힙니다.

## 포함된 파일
- `app.py` — 메인 Streamlit 앱 (한국어 UI)

## 실행 요구사항
- Python 3.8+
- 의존성: `streamlit` (루트의 `requirements.txt`에 포함)

### 로컬에서 실행하기
1. 이 저장소를 로컬로 복제하거나 Codespaces/Dev Container에서 열기
2. (권장) 가상환경을 만들고 활성화한 뒤 의존성 설치:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

3. 앱 실행:

```bash
streamlit run fraction-stars-app/app.py
```

웹 브라우저가 열리면 한국어 UI로 된 쉬운 분수 문제를 풀 수 있습니다.

### Streamlit Cloud(앱 배포)
1. 이 저장소를 GitHub에 푸시합니다.
2. Streamlit Community Cloud에서 새 앱을 생성하고, 리포지토리와 `fraction-stars-app/app.py` 경로를 지정합니다.
3. 배포 버튼을 누르면 앱이 공개되어 학생들이 접근할 수 있습니다.

-## 사용 방법 (학생용)
- 시작하기 버튼을 눌러 문제를 만듭니다.
- 화면에 보이는 별을 보고 `a/b` 형태로 분수를 입력하세요.
  - `a` = 빛나는 별(🌟) 개수
  - `b` = 전체 별(🌟 + ⭐) 개수
- 정답이면 축하 메시지가 나오고 즉시 새로운 문제가 생성됩니다.
- 오답이면 “틀렸어요! 다시 시도해보세요.” 라는 메시지가 나오며 같은 문제가 유지됩니다.

### 통분(약분) 허용
- 예: 문제의 정답이 `2/4`인 경우 사용자가 `1/2`로 입력하면 정답으로 처리합니다. 입력한 분수와 정답 분수를 최대공약수로 약분해 비교합니다.

## 노트
- 앱은 Streamlit의 `st.session_state`를 이용해 문제 상태와 정답 여부를 관리합니다.
- UI는 초등학생이 사용하기 쉽도록 단순하고 큰 이모지로 구성되어 있습니다.

행복한 수업시간 되세요! 🌟
