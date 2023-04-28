def generate_hashtag(s):
    if not s:
        return False
    
    # Split the string into words and capitalize the first letter of each word
    words = [word.capitalize() for word in s.split()]
    
    # Combine the words with a hashtag and check if the result is within 140 characters
    hashtag = "#" + "".join(words)
    if len(hashtag) > 140:
        return False
    
    return hashtag
