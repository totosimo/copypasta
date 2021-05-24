def try_me():
    print("You were were expecting something complex, weren't you?")
    ans = input("Yes or no?\n>>").lower()
    while ans not in ['yes', 'no']:
        ans = input("\ncome on.. type 'yes' or 'no'\n>>").lower()
    if ans == 'yes':
        print('\nWell no.. aiming low and being happy!\n:P')
    else:
        print('\nI like your mood fellow data scientist!!')
    