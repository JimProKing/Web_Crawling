# 네이버플러스 스토어 쇼핑 트렌드 리포트 자동화 프로젝트

Playwright로 네이버플러스 스토어 베스트 상품을 카테고리 + 연령/성별별로 필터링해서  
인기 상품 이미지를 자동 캡처하고, python-docx로 예쁜 워드 리포트를 만드는 실습 프로젝트입니다.

> 2025년 기준 네이버플러스 스토어는 직접 URL 접속을 차단하므로  
> 반드시 **네이버 메인 → "스토어" 클릭 → 새 탭 우회 접속** 방식이 필요합니다.

## 폴더 및 파일 구조

| 파일명                     | 역할 설명                                                                 |
|---------------------------|--------------------------------------------------------------------------|
| `step_1_1.py`             | `output` 폴더 자동 생성                                                   |
| `step_1_2.py`             | 핵심! 네이버 메인 → 스토어 새 탭 우회 접속 함수 (`run_playwright`)         |
| `step_1_2_inspector.py`   | `with sync_playwright()` 버전 (참고용)                                    |
| `step_1_3.py`             | 베스트상품 탭으로 이동                                                    |
| `step_2_1.py`             | 카테고리 선택 + 세부 옵션(연령/성별) 선택 함수                             |
| `step_2_2.py`             | 현재 페이지의 상품 이미지 캡처 → `step_2_2.json`에 경로 저장               |
| `step_2_3.py`             | 위 기능들을 하나로 묶은 `fetch_trends_by_filter()` 함수                   |
| `step_3_1.py`             | python-docx로 제목 + 날짜 넣은 문서 초기화                                 |
| `step_3_2.py`             | 핵심! 수집한 이미지를 5열 표로 삽입해서 완성된 리포트 생성                 |
| `step_3_2_table.py`       | python-docx 표 기본 예제 (참고용)                                         |
| `step_x.py`               | 완성 예제 (현재 `add_table` 함수 없어서 실행 안 됨)                        |
| `output/`                 | 자동 생성 폴더 → 이미지 파일 + 완성된 `.docx` 파일 들어감                  |

## 실행 전 준비 (필수)

```bash
# 가상환경 생성 및 활성화
python -m venv .venv
source .venv/bin/activate        # Mac/Linux
# .venv\Scripts\activate         # Windows
```
# 필요 패키지 설치
pip install playwright python-docx

# 브라우저 설치 (한 번만)
playwright install chromium
단계별 실행 순서
Bashpython step_1_1.py      # output 폴더 생성
python step_1_2.py      # 스토어 접속 테스트
python step_1_3.py      # 베스트상품 이동
python step_2_1.py      # 카테고리/옵션 선택 테스트
python step_2_2.py      # 이미지 캡처 → step_2_2.json 생성
python step_2_3.py      # 통합 수집 실행
python step_3_1.py      # 제목 테스트 → step_3_1.docx 생성
python step_3_2.py      # 최종 리포트 완성 → step_3_2.docx 생성 (핵심!)
여러 카테고리 한 번에 리포트 만들기 (step_3_2.py 수정 예시)
Pythondoc = init_docx()
add_table(doc, "패션의류", "20대 여성")
add_table(doc, "패션잡화", "30대 남성")
add_table(doc, "화장품/미용", "40대 여성")
doc.save(OUT_DIR / "쇼핑트렌드_종합리포트.docx")
주의사항

pip install docx (X) → 반드시 pip install python-docx (O)
page.pause() 실행 시 터미널에 > 프롬프트가 뜨면 여기서 locator 테스트 가능
이미지 경로는 output/step_2_2.json에 저장됨
네이버플러스 스토어는 직접 URL 접속 불가
