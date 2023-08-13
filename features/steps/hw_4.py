# from behave import given, when, then
# from selenium.webdriver.common.by import By
#
# # BEST_SELLERS_BTN = (By.CSS_SELECTOR, "[href='/gp/bestsellers/?ref_=nav_cs_bestsellers']")
# LINKS_11 = (By.CSS_SELECTOR, '.issue-card-wrapper')
# HELP_TOPICS = (By. CSS_SELECTOR, '.help-topics')
#
# #******************************* Problem 1 **********************************
#
# @given('Open Amazon page')
# def open_amazon(context):
#     context.driver.get('https://www.amazon.com/')
#
#
# @then('Click on Best Seller')
# def click_on_best_seller(context):
#     context.driver.find_element(By.CSS_SELECTOR, "[href='/gp/bestsellers/?ref_=nav_cs_bestsellers']").click()
#
#
# @then('Verify Best Sellers link')
# def verify_best_seller_link(context):
#     expected_result = 'Best Sellers'
#     actual_result = context.driver.find_element(By.CSS_SELECTOR, "[href='/Best-Sellers/zgbs/ref=zg_bs_tab']").text
#     assert expected_result == actual_result, f'Error, expected {expected_result} did not match actual {actual_result}'
#     print('Test Passed')
#
#
# @then('Verify New Releases')
# def verify_new_releases_link(context):
#     expected_result = 'New Releases'
#     actual_result = context.driver.find_element(By.CSS_SELECTOR, "[href='/gp/new-releases/ref=zg_bs_tab']").text
#     assert expected_result == actual_result, f'Error, expected {expected_result} did not match actual {actual_result}'
#     print('Test Passed')
#
#
# @then('Movers & Shakers')
# def verify_movers_shakers_link(context):
#     expected_result = 'Movers & Shakers'
#     actual_result = context.driver.find_element(By.CSS_SELECTOR, "[href='/gp/movers-and-shakers/ref=zg_bs_tab']").text
#     assert expected_result == actual_result, f'Error, expected {expected_result} did not match actual {actual_result}'
#     print('Test Passed')
#
#
# @then('Most Wished For')
# def verify_wished_for_link(context):
#     expected_result = 'Most Wished For'
#     actual_result = context.driver.find_element(By.CSS_SELECTOR, "[href='/gp/most-wished-for/ref=zg_bs_tab']").text
#     assert expected_result == actual_result, f'Error, expected {expected_result} did not match actual {actual_result}'
#     print('Test Passed')
#
#
# @then('Gift Ideas')
# def verify_gift_ideas_link(context):
#     expected_result = 'Gift Ideas'
#     actual_result = context.driver.find_element(By.CSS_SELECTOR, "[href='/gp/most-gifted/ref=zg_bs_tab']").text
#     assert expected_result == actual_result, f'Error, expected {expected_result} did not match actual {actual_result}'
#     print('Test Passed')
#
# #******************************* Problem 3 **********************************
#
# @given('Open Customer Service')
# def open_customer_service(context):
#     context.driver.get('https://www.amazon.com/gp/help/customer/display.html')
#
#
# @then('Verify Welcome to Amazon Customer Service')
# def verify_welcome(context):
#     expected_result = 'Welcome to Amazon Customer Service'
#     actual_result = context.driver.find_element(By.CSS_SELECTOR, "h1.fs-heading.bolded").text
#     assert expected_result == actual_result, f'Error, expected {expected_result} did not match actual {actual_result}'
#     print('Test Passed')
#
#
# @then('Verify 11 boxes of links')
# def verify_11_links(context):
#     context.driver.find_element(*LINKS_11)
#     links = context.driver.find_elements(*LINKS_11)
#     assert len(links) > 1
#     print(f'Expected at least 2 links, but got {len(links)}')
#
#
# @then('Verify Search our help library')
# def verify_help_library(context):
#     expected_result = 'Search our help library'
#     actual_result = context.driver.find_element(By.CSS_SELECTOR, "h2.fs-heading.bolded").text
#     assert expected_result == actual_result, f'Error, expected {expected_result} did not match actual {actual_result}'
#     print('Test Passed')
#
#
# @then('Verify Search Bar')
# def verify_search_bar(context):
#     context.driver.find_element(By.ID, 'hubHelpSearchInput')
#     print('Test Passed')
#
#
# #**** I would need help on grabbing the correct element link for All help topics because there are two elements
# # that are the same code for the link****
#
# # @then('Verify All help topics')
# # def verify_all_help_topics(context):
# #     expected_result = 'All help topics'
# #     actual_result = context.driver.find_element(By.CSS_SELECTOR, "h2.fs-heading.bolded").text
# #     assert expected_result == actual_result, f'Error, expected {expected_result} did not match actual {actual_result}'
# #     print('Test Passed')
#
#
# @then('Verify All Drop Down Topics')
# def verify_help_topics(context):
#     context.driver.find_element(*HELP_TOPICS)
#     links = context.driver.find_elements(*HELP_TOPICS)
#     assert len(links) > 1
#     print(f'Expected at least 2 links, but got {len(links)}')
#     print('Test Passed')
#
#
#
