from playwright.sync_api import Page

from step_1_2 import run_playwright  # 이전에 작성한 모듈을 불러옵니다.


def goto_best_goods(page: Page):
    # 인스펙터 창에서 복사한 코드 붙여넣기
    page.get_by_role("link", name="베스트 NONE").click()
    page.get_by_role("link", name="베스트상품").click()
    # page.get_by_role("textbox", name="검색어 입력").click()
    # page.get_by_role("textbox", name="검색어 입력").fill("패딩")
    # page.get_by_role("textbox", name="검색어 입력").press("Enter")
    # page.get_by_role("textbox", name="검색어 입력").fill("패딩")
    # page.get_by_role("textbox", name="검색어 입력").press("Enter")
    # with page.expect_popup() as page2_info:
    #     page.get_by_role("link", name="광고 [디스커버리] 여성 켈리 구스다운 미드패딩 (").click()
    # page2 = page2_info.value

if __name__ == "__main__":
    play, browser, page = run_playwright(slow_mo=1000)
    goto_best_goods(page)  # 베스트상품 페이지로 이동
    page.pause()  # 인스ㄴ펙터 실행

    browser.close()
    play.stop()
