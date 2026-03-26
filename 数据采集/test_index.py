# coding:utf-8

from qdata.baidu_index import (
    get_feed_index,
    get_news_index,
    get_search_index,
    get_live_search_index
)
from qdata.baidu_index.common import check_keywords_exists
from qdata.baidu_login import get_cookie_by_qr_login

keywords_list = [['发烧']]
cookies = """BAIDUID=88F7189C2E54F020FBE472212F3904FB:FG=1; BAIDUID_BFESS=88F7189C2E54F020FBE472212F3904FB:FG=1; BDUSS=FPTGhKWm5jWWh6bHhVQS0tU1pGYlJpWFN2NFZzVWNKMnR3TldmQ1F2Wm41TVpsSVFBQUFBJCQAAAAAAAAAAAEAAACEMmMHx-XQxMGw5PQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGdXn2VnV59lan; BDUSS_BFESS=FPTGhKWm5jWWh6bHhVQS0tU1pGYlJpWFN2NFZzVWNKMnR3TldmQ1F2Wm41TVpsSVFBQUFBJCQAAAAAAAAAAAEAAACEMmMHx-XQxMGw5PQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGdXn2VnV59lan; BIDUPSID=88F7189C2E54F020FBE472212F3904FB; PSTM=1704941416; bdindexid=hqhojdab89uuk55ifgudbpfb56; PTOKEN=c226d4dfeb024bde9dbf605bb0389859; PTOKEN_BFESS=c226d4dfeb024bde9dbf605bb0389859; STOKEN=91725077498ea5313307cf4a100ef183c2184bd79d3b87087a011ed5ab96bc58; STOKEN_BFESS=91725077498ea5313307cf4a100ef183c2184bd79d3b87087a011ed5ab96bc58; UBI=fi_PncwhpxZ%7ETaJcxf-5dfX0bUpE0U5NpvC; UBI_BFESS=fi_PncwhpxZ%7ETaJcxf-5dfX0bUpE0U5NpvC; __yjs_st=2_YWQ0MjRmNjMwNmZmYTk1OTgzMmNmZWEzYzk0Njc2MTc1ZDMyMmNiZGUyMmI5ZWQxOGJmNjNlNGNhNjg0MTY0YmZiN2QxMDZhZDA4MTYzMWNmMjUzNTI5ZDkxZjdiOTM5MDYzNDIxOWI3YjIzZmQ0NmYyNmFiMTNiY2NjOGE1NmQ3YjQ5ODJkMTdmYTJkYmEwMTYzNjczOTVhZDg4ODkxZmY5YTI4MDY4MGJmMzNkZTgzZTk2ZmEyMmRjMDk4ZTA4XzdfZTk1M2ExOTU="""

def test_get_search_index():
    """获取搜索指数"""
    for index in get_search_index(
            keywords_list=keywords_list,
            start_date='2023-01-01',
            end_date='2024-01-10',
            cookies=cookies
    ):
        print(index)



if __name__ == "__main__":
    # print(get_cookie_by_qr_login())
    test_get_search_index()
