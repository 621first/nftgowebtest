'''
@filename: /test_coll
@time: 2023/10/7 16:07
'''
import pytest
from commons.utils.readYaml import load_yaml

from page.topcollPage import TopcollPage


class TestTopcoll():
    def test_topcoll(self,driver):
        topcoll_page = TopcollPage(driver)
        topcoll_page.open_topcoll()

    @pytest.mark.parametrize('keyword',load_yaml('data/top_coll/coll_name.yaml'))
    def test_search_coll(self,driver,keyword):
        topcoll_page = TopcollPage(driver)
        topcoll_page.search_coll(keyword['keywords'])