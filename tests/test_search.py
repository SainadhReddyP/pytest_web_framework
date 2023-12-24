from pages.home_page import HomePage
import pytest


@pytest.mark.usefixtures("setup_and_teardown")
class TestSearch:
    def test_search_for_a_valid_product(self):
        home_pg = HomePage(self.driver)
        home_pg.click_on_store_button()
        search_pg = home_pg.search_for_a_product("Galaxy S22")
        assert search_pg.display_status_of_valid_product()
        
    def test_search_for_an_invalid_product(self):
        home_pg = HomePage(self.driver)
        home_pg.click_on_store_button()
        search_pg = home_pg.search_for_a_product("Galaxy S23")
        expected_text = "There is no product that matches the search criteria."
        assert search_pg.retrieve_invalid_product_message().__eq__(expected_text)
    
    def test_search_without_entering_any_product(self):
        home_pg = HomePage(self.driver)
        home_pg.click_on_store_button()
        search_pg = home_pg.search_for_a_product(" ")
        expected_text = "There is no product that matches the search criteria."
        assert search_pg.retrieve_invalid_product_message().__eq__(expected_text)
