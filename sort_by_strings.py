def sort_by_strings(s, t):
    """
      sample input: "cats" "atzc"
      sample output: "catz"
      assumption(s) => 1. s does not have repeating letters
      2. s and t are all lowercased
      3. Overall, the goodwill of the person running my code that they will be nice. (have mercy plox)
      4. Person running my code likes notes. If not, then apologies QQ.
      
    """
    copy_of_t = t # don't want to modify stuff
    result = '' # result string set up
    for char in s: # iterate through each character in the first string
        number_of_occurences = copy_of_t.count(char) # find the number of times it occurs in t
        result += char * number_of_occurences # put it that many times into our result
        copy_of_t = copy_of_t.replace(char, '') # change the character to an empty string so we don't count it again
    return result + copy_of_t # add the remaining characters in the copy of t to our result

print(sort_by_strings("cats", "atzc"))
