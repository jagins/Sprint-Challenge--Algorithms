'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    #base case if there's no more words to process
    if len(word) == 0:
        return 0
    #break down the string to 2 elements and compare if they're == 'th'
    if word[0:2] == 'th':
        #calls the function again with moving the index pointer to the next element
        #add 1 to the end for the counter since it bubbles back up
        return count_th(word[1:]) + 1 
    return count_th(word[1:])
