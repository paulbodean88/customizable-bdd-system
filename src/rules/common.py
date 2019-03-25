def open_url(driver):
    driver.get_driver().get('https://www.openstreetmap.org')


def close_test(driver):
    driver.get_driver().close()
