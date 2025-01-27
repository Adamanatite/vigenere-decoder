ENGLISH_IC = 0.0686
ALPHABET = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]


def vigenere_encrypt(plaintext, key):
    
    plaintext = plaintext.strip().replace(" ", "").replace("\n", "").upper()
    key = key.upper()
    
    ciphertext_chars = []
    for i, char in enumerate(plaintext):
        char_index = (ALPHABET.index(key[i%len(key)]) + ALPHABET.index(char)) % len(ALPHABET)
        ciphertext_chars += ALPHABET[char_index]
    return "".join(ciphertext_chars)

def get_frequencies(text):
    
    frequencies = {}

    for char in text:
        frequencies[char] = frequencies.get(char, 0) + 1
    return frequencies


def ic(frequencies):
    total_length = 0
    top_sum = 0

    for char in ALPHABET:
        f_i = frequencies.get(char, 0)
        top_sum += f_i * (f_i - 1)
        total_length += f_i
    return top_sum / (total_length * (total_length - 1))




def get_ic(ciphertext, n):
    total_ic = 0

    for i in range(n):
        split = ciphertext[i::n]
        frequencies = get_frequencies(split)
        total_ic += ic(frequencies)

    return total_ic / n


def main(ciphertext, guesses):
    
    ciphertext = ciphertext.replace(" ", "").strip().replace("\n", "").upper()

    best_guess = 0
    best_ic = 99999

    for guess in guesses:
        current_ic = get_ic(ciphertext, guess)
        ic_diff = abs(current_ic - ENGLISH_IC)
        print(guess, ic_diff)
        if ic_diff < best_ic:
            best_ic = ic_diff
            best_guess = guess

    return best_guess, best_ic 


ciphertext = vigenere_encrypt("""
                              True nervous very very dreadfully nervous I had been and am but why will you say that I am mad The disease had sharpened my senses not destroyed not dulled them Above all was the sense of hearing acute I heard all things in the heaven and in the earth I heard many things in hell How then am I mad Hearken and observe how healthily how calmly I can tell you the whole story

It is impossible to say how first the idea entered my brain but once conceived it haunted me day and night Object there was none Passion there was none Icls loved the old man He had never wronged me He had never given me insult For his gold I had no desire I think it was his eye yes it was this One of his eyes resembled that of a vulture a pale blue eye with a film over it Whenever it fell upon me my blood ran cold and so by degrees very gradually I made up my mind to take the life of the old man and thus rid myself of the eye forever

Now this is the point You fancy me mad Madmen know nothing But you should have seen me You should have seen how wisely I proceeded with what caution with what foresight with what dissimulation I went to work I was never kinder to the old man than during the whole week before I killed him And every night about midnight I turned the latch of his door and opened it oh so gently And then when I had made an opening sufficient for my head I put in a dark lantern all closed closed so that no light shone out and then I thrust in my head Oh you would have laughed to see how cunningly I thrust it in I moved it slowly very very slowly so that I might not disturb the old mans sleep It took me an hour to place my whole head within the opening so far that I could see him as he lay upon his bed Ha would a madman have been so wise as this And then when my head was well in the room I undid the lantern cautiously oh so cautiously cautiously for the hinges creaked I undid it just so much that a single thin ray fell upon the vulture eye And this I did for seven long nights every night just at midnight but I found the eye always closed and so it was impossible to do the work for it was not the old man who vexed me but his Evil Eye And every morning when the day broke I went boldly into the chamber and spoke courageously to him calling him by name in a hearty tone and inquiring how he had passed the night So you see he would have been a very profound old man indeed to suspect that every night just at twelve I looked in upon him while he slept

Upon the eighth night I was more than usually cautious in opening the door A watchs minute hand moves more quickly than did mine Never before that night had I felt the extent of my own powers of my sagacity I could scarcely contain my feelings of triumph To think that there I was opening the door little by little and he not even to dream of my secret deeds or thoughts I fairly chuckled at the idea and perhaps he heard me for he moved on the bed suddenly as if startled Now you may think that I drew back but no His room was as black as pitch with the thick darkness for the shutters were close fastened through fear of robbers and so I knew that he could not see the opening of the door and I kept pushing it on steadily steadily

I had my head in and was about to open the lantern when my thumb slipped upon the tin fastening and the old man sprang up in the bed crying out Whos there

I kept quite still and said nothing For a whole hour I did not move a muscle and in the meantime I did not hear him lie down He was still sitting up in the bed listening just as I have done night after night hearkening to the death watches in the wall

Presently I heard a slight groan and I knew it was the groan of mortal terror It was not a groan of pain or of grief oh no it was the low stifled sound that arises from the bottom of the soul when overcharged with awe I knew the sound well Many a night just at midnight when all the world slept it has welled up from my own bosom deepening with its dreadful echo the terrors that distracted me I say I knew it well I knew what the old man felt and pitied him although I chuckled at heart I knew that he had been lying awake ever since the first slight noise when he had turned in the bed His fears had been ever since growing upon him He had been trying to fancy them causeless but could not He had been saying to himself It is nothing but the wind in the chimney it is only a mouse crossing the floor or it is merely a cricket which has made a single chirp Yes he has been trying to comfort himself with these suppositions but he had found all in vain All in vain because Death in approaching him had stalked with his black shadow before him and enveloped the victim And it was the mournful influence of the unperceived shadow that caused him to feel although he neither saw nor heard to feel the presence of my head within the room

When I had waited a long time very patiently without hearing him lie down I resolved to open a little a very very little crevice in the lantern So I opened it you cannot imagine how stealthily stealthily until at length a single dim ray like the thread of the spider shot from out the crevice and fell upon the vulture eye

It was open wide wide open and I grew furious as I gazed upon it I saw it with perfect distinctness all a dull blue with a hideous veil over it that chilled the very marrow in my bones but I could see nothing else of the old mans face or person for I had directed the ray as if by instinct precisely upon the damned spot

And now have I not told you that what you mistake for madness is but over acuteness of the senses now I say there came to my ears a low dull quick sound such as a watch makes when enveloped in cotton I knew that sound well too It was the beating of the old mans heart It increased my fury as the beating of a drum stimulates the soldier into courage

But even yet I refrained and kept still I scarcely breathed I held the lantern motionless I tried how steadily I could maintain the ray upon the eye Meantime the hellish tattoo of the heart increased It grew quicker and quicker and louder and louder every instant The old mans terror must have been extreme It grew louder I say louder every moment do you mark me well I have told you that I am nervous so I am And now at the dead hour of the night amid the dreadful silence of that old house so strange a noise as this excited me to uncontrollable terror Yet for some minutes longer I refrained and stood still But the beating grew louder louder I thought the heart must burst And now a new anxiety seized me the sound would be heard by a neighbor The old mans hour had come With a loud yell I threw open the lantern and leaped into the room He shrieked once once only In an instant I dragged him to the floor and pulled the heavy bed over him I then smiled gaily to find the deed so far done But for many minutes the heart beat on with a muffled sound This however did not vex me it would not be heard through the wall At length it ceased The old man was dead I removed the bed and examined the corpse Yes he was stone stone dead I placed my hand upon the heart and held it there many minutes There was no pulsation He was stone dead His eye would trouble me no more

If still you think me mad you will think so no longer when I describe the wise precautions I took for the concealment of the body The night waned and I worked hastily but in silence First of all I dismembered the corpse I cut off the head and the arms and the 
legs""", "LEMONS")

guesses = [2,3,4,5,6,7,8,9]

predicted_n, ic_diff = main(ciphertext, guesses)
print("Most likely key length:", predicted_n)
print("IC score difference:", ic_diff)