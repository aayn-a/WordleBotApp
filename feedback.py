def getFeedback(guess, target):
    feedback = ["gray"] * 5
    targetC = {}

    for char in target:
        targetC[char] = targetC.get(char, 0) + 1
    
    #Greens
    for i in range(5):
        if guess.strip()[i] == target.strip()[i]:
            feedback[i] = "green"
            targetC[guess[i]] -= 1
    
    for i in range(5):
        if feedback[i] == "gray" and guess[i] in targetC and targetC[guess[i]] > 0:
            feedback[i] = "yellow"
            targetC[guess[i]] -= 1

    return feedback

