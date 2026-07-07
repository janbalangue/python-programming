'''
Author: Jay Balangue
Date: 2026-07-07
Module: 1
Lab: Algorithms

----------
PSEUDOCODE
----------

FUNCTION CreateSavingsGoal(UserID, AccountID, TargetAmount, TargetDate)
    IF the user already has a savings goal for the same AccountID
        DISPLAY "You already have a savings goal for this account."
        RETURN
    ELSE IF TargetAmount <= 0
        DISPLAY "Target amount must be greater than zero."
        RETURN
    ELSE IF TargetDate is in the past
        DISPLAY "Target date must be in the future."
        RETURN
    END IF
    CREATE a new savings goal with the provided details
    STORE the savings goal in the database
END FUNCTION

FUNCTION UpdateSavingsProgress(UserID, AccountID, SavingsGoal, AmountSaved)
    RETRIEVE the goal matching (UserID, AccountID, SavingsGoal)
    IF no match found
        DISPLAY "Savings goal not found."
        RETURN
    END IF
    UPDATE goal.AmountSaved += AmountSaved
END FUNCTION

FUNCTION RetrieveSavingsGoalStatus(UserID)
    IF the user has no savings goals
        DISPLAY "No savings goals found."
    ELSE
        FOR each savings goal of the user
            RETRIEVE the user's account, current savings goal and progress
            DISPLAY the savings goal status to the user
            IF the savings goal is met
                DISPLAY "Congratulations! You have met your savings goal."
            ELSE
                DISPLAY "You have not met your savings goal yet."
        END FOR
    END IF 
END FUNCTION

# User gets a notification if the target date is 7 days from today and the savings goal is not met.
FUNCTION NotifyUserIfGoalDateApproaching(UserID)
    FOR each savings goal of the user
        RETRIEVE the user's current savings goal and TargetDate
        IF the TargetDate is 7 days from now AND the savings progress is less than the TargetAmount
            SEND a notification to the user about the approaching goal date and insufficient savings
        END IF
    END FOR

END FUNCTION

START
    PROMPT user for the UserID
    DO WHILE Next Action is not Quit
        CALL NotifyUserIfGoalDateApproaching(UserID)
        PROMPT user for their Next Action (Create Goal, Update Progress, Retrieve Status, Quit)
        IF Next Action is Create Goal
            PROMPT user for AccountID, TargetAmount and TargetDate
            CALL CreateSavingsGoal(UserID, AccountID, TargetAmount, TargetDate)
        ELSE IF Next Action is Update Progress
            PROMPT user for AccountID, SavingsGoal and AmountSaved
            CALL UpdateSavingsProgress(UserID, AccountID, SavingsGoal, AmountSaved)
        ELSE IF Next Action is Retrieve Status
            CALL RetrieveSavingsGoalStatus(UserID)
        ELSE
            DISPLAY "Invalid action. Please try again."  
        END IF     
    END WHILE
END
'''