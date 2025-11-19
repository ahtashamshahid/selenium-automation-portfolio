def test_search_example(driver):
    driver.get("https://the-internet.herokuapp.com/")
    assert "Welcome" in driver.title or driver.find_element("tag name", "h1")
