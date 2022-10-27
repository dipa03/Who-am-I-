print("Hello, welcome to my game. Let's see how well you know me!")
print('All lowercase, please!')

ans = input ('Ready to play? (yes/no): ')
score = 0
total_q = 6

if ans.lower() == 'yes':
    ans = input ('1. What is my favorite programming language? ')
    if ans.lower() == 'python':
        score += 1
        print('Correct')
    else:
        print('Incorrect')

    ans = input ('2. What state was I born in? ')
    if ans.lower() == 'alabama':
        score += 1
        print('Correct')
    else:
        print('Incorrect')

    ans = input ('3. What is my favorite anime? ')
    if ans.lower() == 'dragon ball' or ans.lower() == 'attack on titan' or ans.lower() == 'soul eater':
        score += 1
        print('Correct')
    else:
        print('Incorrect')
    
    ans = input ('4. What is my favorite console? ')
    if ans.lower() == 'nintendo switch' or ans.lower() == 'wii' or ans.lower() == 'ps5':
        score += 1
        print('Correct')
    else:
        print('Incorrect')
    
    ans = input ('5. What is my favorite activity? ')
    if ans.lower() == 'listening to music' or ans.lower() == 'roller skating' or ans.lower() == 'baking':
        score += 1
        print('Correct')
    else:
        print('Incorrect')

    ans = input ('6. What genre of music is my favorite? ')
    if ans.lower() == 'rock':
        score += 1
        print('Correct')
    else:
        print('Incorrect')

else:
    print('Boo on you.')

print('Thank you for playing, you got', str(score), "questions correct. ")

percentage = score/total_q * 100

print("Here's your mark!: " + str(percentage))

if score < 3:
    print ("Let's get to know each other!")
else:
    print("We're pratically besties!")


print ('Thanks for playing. Goodbye!')