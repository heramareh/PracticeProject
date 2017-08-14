Feature: Compute add
  In order to play with Lettuce
  As beginners
  We'll implement add

  Scenario: Add of 0
    Given I have the numbers -1,1
    When I compute its add
    Then I see the number 0

  Scenario: Add of 1
    Given I have the numbers 12,9
    When I compute its add
    Then I see the number 21