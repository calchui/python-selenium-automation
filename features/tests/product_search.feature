Feature: Test Scenarios for Search functionality

  Scenario: User can search for a product
    Given Open Google page
    When Input Car into search field
    And Click on searnav-search-submit-buttonch icon
    Then Product results for Car are shown