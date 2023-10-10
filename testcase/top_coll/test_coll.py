'''
@filename: /test_coll
@time: 2023/10/7 16:07
'''
import pytest
from commons.utils.readYaml import load_yaml

from page_object.topcollPage import TopcollPage
from commons.utils.log import get_logger

logger = get_logger()


class TestTopcoll():

    @pytest.fixture(autouse=True)
    def setup(self,driver) -> None:
        self.driver = driver
        self.topcoll_page = TopcollPage(self.driver)

    def teardown(self) -> None:
        pass


    def test_topcoll(self,driver):
        self.topcoll_page.open_topcoll()

    # @pytest.mark.parametrize('keyword',load_yaml('data/top_coll/coll_name.yaml'))
    # def test_search_coll(self,driver,keyword):
    def test_search_coll(self,driver):
        # logger.info(keyword)
        # topcoll_page.search_coll(keyword['keywords'])
        self.topcoll_page.search_coll()

    def test_hover_marketCap(self,driver):
        self.topcoll_page.hover_marketCap()
