# MetaCharacters 

1. (*) -> Any number of occurrences(including 0 occurrences)

2. (+) -> One or more occurrences

3. {} -> Indicate the number of occurrences of a preceding regex to match

4. () -> Enclose a group of Regex

5. \ -> Used to drop the special meaning of characters following it.

6. [] -> Represent a character class

7. ^ -> Matches the Beginning

8. $ -> Matches the end

9. . -> Matches any character except newline

10. | -> Means OR (matches with any of the characters spearated by it)

11. ? -> Matches Zero or One Occurrence


# Special Sequence in Regex

- Special Sequence does not match for the actual character in the string instead it tells the specific location in the search string where the match must occur 

- It makes it easier to write commonly used patterns 

1. \A --> Matches if the string begins with the given character.

2. \b --> Matches if the word begins or ends with the given character. \b(begins) will check for the beginning of the word and (string)\b will check for the ending of the word

3. \B --> It is the opposte of the \b i.e the string should not start or end with the given regex

4. \d --> matches any decimal digit, this is equivalent to the set class (0-9)

5. \D --> matches any non-digit character , this is equivalent the the set class (^0-9)

6. \s --> Matches any whitespace character

7. \S --> Matches any non-whitespace character

8. \w --> Matches any alphanumeric character , this is equivalent to the set class(a-zA-Z0-9)

9. \W --> matches any non-alphanumeric character 

10. \Z --> Mathes if the string ends with the given regex.


# Regex Sets 

- A set is a set of characters inside a pair of square brackets [ ] with a special meaning 


1. [atx] --> Returns a match where one of the specified characters(a,t,x) are present 

2. [a-x] --> Returns a match for any lower case character, alphabatically between a and h 

3. [^atx] --> Retruns a match for any character Except  a,t and x

4. [0123] --> Returns a match where any of specified digits (0,1,2,3) are present 

5. [0-9] --> Returns a match for any digit between 0 and 9

6. [0-7][0-9] --> Returns a match for any two digit number from 00 and 79

7. [a-zA-Z] --> Returns a match for any character alphabatically between a and z , and Upper case 

8. [+] --> in sets +,*,..,{},|,$,() has no special meaning , so [+] means 



