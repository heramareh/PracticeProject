Feature: Compute add
  In order to play with Lettuce
  As beginners
  We'll implement add

  Scenario: Add of 0
    Given I have the number 1,2
    When I compute its add
    Then I see the number 3

  Scenario: Add of 1
    Given I have the number -1,-2
    When I compute its add
    Then I see the number -3

  Scenario: Add of 2
    Given I have the number 0,-1
    When I compute its add
    Then I see the number -1

  Scenario: Add of 3
    Given I have the number -1,1
    When I compute its add
    Then I see the number 0
