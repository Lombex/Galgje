Hangman = [ "Paal", "Touw", "Hoofd", "Lichaam", "Linker been", "Rechter been", "Rechter arm", "Linker arm"];
HangmanIndex = -1;

GuessedList = [];

print("Kies een woord die u wil gebruiken.");
GetWoord = input("Woord: ");

print("Het woord bestaat uit", len(GetWoord),"letters");
LetterList = list(GetWoord);

# Speler heeft 8 pogingen
AttemptIndex = 8;
GeradenWoord = 0;
while True:
    GetChar = input("Geef een letter: ");  
    if GetChar in GuessedList:
        print ("Deze Letter heeft u al geraden!")
    else: 
        if GetChar in LetterList:
            CharUsedCount = GetWoord.count(GetChar);
            for x in range(CharUsedCount):
                GuessedList += GetChar;
            GeradenWoord += CharUsedCount;
            if GeradenWoord == len(GetWoord):
                print("Je hebt gewonnen! het woord was:", GetWoord);
                break;   
            print(GetChar, "Zat er", CharUsedCount, "keer in!");            
        else:
            if AttemptIndex < 1:
                print("Game Over!");
                break;
            else:
                HangmanIndex += 1;
                print("Fout! Je hebt nog", AttemptIndex,"Levens\nHangman: ", Hangman[HangmanIndex]);
                AttemptIndex -= 1;