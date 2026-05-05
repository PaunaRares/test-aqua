@e2e-branch
Feature: Branch specific deterministic result

  @branch-fail
  Scenario: Should fail on e2e-fail branch
    Given Sample step fail
@e2e-branch
Feature: Branch specific deterministic result

  @branch-pass
  Scenario: Should pass on e2e-pass branch
    Given Sample step pass
