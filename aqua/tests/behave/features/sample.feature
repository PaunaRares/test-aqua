@sample-feature
Feature: SAMPLE Feature

        @sample1
        Scenario: Sample Scenario #1
            Given New Acrom session
             Then Page "Home" is diplayed
              And Page contains menu "Why Acrom"
             When Page select menu "Why Acrom"
             Then Page "Why Acrom" is diplayed
		
        @sample2
        Scenario: Sample Scenario #2
            Given New Acrom session
             Then Page "Home" is diplayed
              And Page contains menu "Why Acrom"
             When Page select menu "Why Acrom"
             Then Page "Why Acrom" is diplayed

        @long-test
        Scenario: Long Test (30s)
            Given New Acrom session
             Then Page "Home" is diplayed
              And Sleep "30" seconds
              And Page contains menu "Why Acrom"
             When Page select menu "Why Acrom"
             Then Page "Why Acrom" is diplayed