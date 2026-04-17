@sample2-feature
Feature: SAMPLE2

        Scenario: SAMPLE TEST FAIL (test intended to fail)
            Given New Acrom session
             Then Page "Home" is diplayed
             When Page select menu "Restaurant Solutions"
             Then Page select menu "CyberSecurity"
             Then Page contains menu "Restaurant Software"
             Then Page contains text "Restaurant Kiosk"
		