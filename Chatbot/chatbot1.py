file = open("stop-words.txt")
stopwords = file.readlines()

def filterWords(input):
    splitString = input.split(" ")
    
    # Create an array to hold valid, filtered words.
    filteredWords = [];
    
    # Loop over the array of submitted words.
    for word in splitString:
        
        # Check if the current word is valid (not a stop word).
        isStopWord = False
        for line in stopwords:
            stopWord = line.strip("\n");
            
            # If this word matches the current stop word, it is a stop word.
            if word == stopWord:
                isStopWord = True
                break
        
        # If this word is NOT a stop word, add it to the valid, filtered words.
        if isStopWord == False:
            filteredWords.append(word)
    
    # Return the filtered words.
    return filteredWords

def isNumber(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

# Extract the first number from an array of words.
def getNumber(words):
    # Loop over the words.
    for word in words:
        # If this word is a number then return it.
        if isNumber(word):
            return int(word)
    
    # No number was found, return False to indicate failure.
    return False

# Ask for the user's age.
def askAge():
    ageWords = filterWords(raw_input("How old are you? "))

    return getNumber(ageWords)

# Ask question.
nameWords = filterWords(raw_input("Hello there, what's your name? "))

print "Hi " + " ".join(nameWords) + ", let's talk!"

# Ask for age until it's been given.
age = askAge()
while age == False:
    print "You didn't tell me your age :("
    age = askAge()

if age < 20:
    print "Oh you must still be at school?"
else:
    print "You oldie!"

print "Do you want to ask me something? Perhaps, ask about the weather or how I'm feeling..."

while True:
    input = raw_input("")

    if input.find("?") > -1:
        # Find the answer.
        filteredWords = filterWords(input.replace("?", ""))
        if "weather" in filteredWords:
            print "It's going to rain."
        elif "feeling" in filteredWords:
            print "I'm feeling sad :("
        else:
            print "I'm sorry, I didn't understand that question."        
    else:
        print "You don't want to ask me anything...nothing at all?"