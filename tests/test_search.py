from pages.home_page import HomePage
from pages.search_page import SearchPage
import pytest


@pytest.mark.usefixtures("setup_and_teardown")
class TestSearch:
    def test_search_for_a_valid_product(self):
        home_pg = HomePage(self.driver)
        home_pg.click_on_store_button()
        home_pg.enter_product_into_search_box("Galaxy S22")
        home_pg.click_on_search_button()
        search_pg = SearchPage(self.driver)
        assert search_pg.display_status_of_valid_product()
        
    def test_search_for_an_invalid_product(self):
        home_pg = HomePage(self.driver)
        home_pg.click_on_store_button()
        home_pg.enter_product_into_search_box("Galaxy S23")
        home_pg.click_on_search_button()
        expected_text = "There is no product that matches the search criteria."
        search_pg = SearchPage(self.driver)
        assert search_pg.retrieve_invalid_product_message().__eq__(expected_text)
    
    def test_search_without_entering_any_product(self):
        home_pg = HomePage(self.driver)
        home_pg.click_on_store_button()
        home_pg.enter_product_into_search_box(" ")
        home_pg.click_on_search_button()
        expected_text = "There is no product that matches the search criteria."
        search_pg = SearchPage(self.driver)
        assert search_pg.retrieve_invalid_product_message().__eq__(expected_text)
