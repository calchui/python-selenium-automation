# Created by edc_p at 8/29/2023
Feature: Verify Empty Cart

  Scenario: Verify Text in Cart
      Given Open Amazon page
      When Click Cart Icon
      Then Verify Amazon Cart is Empty Text