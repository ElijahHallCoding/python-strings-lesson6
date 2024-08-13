# List of reviews
reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "poor quality product. Wouldn't recommend it to anyone.", # Had to keep 'poor' in lowercase form to accomplish the capitalization.
    "The product was average. Nothing extraordinary about it."
    ]

# List of Keywords
keywords = ["good", "excellent", "bad", "poor", "average"]

# Task 1: Keyword Highlighter
for review in reviews:
    for keyword in keywords:
        # Replace keyword with uppercase
        review = review.replace(keyword, keyword.upper())
    #Print the review
    print(review,"\n")


# Task 2
reviews = [
    "This product is really good. I'm impressed with its quality, A truly amazing experience!",
    "The performance of this product is excellent. Highly recommended! So many great things to say about this product.",
    "I had a bad experience with this product. It didn't meed my expectations.",
    "The product was average. Nothing extraordinary about it. Honestly its really subpar.",
    "This device is truly awesome.",
    "What an superb system installed on this device.",
    "This is just terrible, a truly awful experience!",
    "What a fantastic presentation to regain my confidence in this product! Yesterday's presentation was pretty disappointing.",
    "This product is horrible! I will not be spending my money here again!"
]

# Defining words
positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

# Function to count positive and negative words
def sentiment_tally(reviews):
    #Counters
    total_positive = 0
    total_negative = 0

    #Loop through the review
    for review in reviews:
        #Began counters for each review
        positive_count = 0
        negative_count = 0

        # Split the review 
        words = review.split()

        # Loop through each word in the review
        for word in words:
            # Remove punctuation from the word and convert it to lowercase
            clean_word = ""
            for char in word:
                if char.isalpha():
                    clean_word += char.lower()

            # Check if the cleaned is in the list
            if clean_word in positive_words:
                positive_count += 1
            elif clean_word in negative_words:
                negative_count += 1

        # Print the results
        print(f"Review: '{review}'")
        print(f"Positive words: {positive_count}, Negative words: {negative_count}\n")

# Call the function
sentiment_tally(reviews)

# Task 3
# Same review 
reviews = [ 
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "poor quality product. Wouldn't recommend it to anyone.", # Had to keep 'poor' in lowercase form to accomplish the capitalization.
    "The product was average. Nothing extraordinary about it."
    ]

# Review summary function
def summarize_reviews(reviews):
    for review in reviews:
        # Check length of review
        if len(review) <= 30:
            summary = review 
        else:
            # Take first 30 characters from the review 
            cut_off_point = 30

            
            if review[cut_off_point] != ' ':

                # Find the last space within the first 30 characters to avoid cutting the word
                while cut_off_point > 0 and review[cut_off_point] != ' ':
                    cut_off_point -= 1

                # Create the summary 
                summary = review[:cut_off_point] + '..'
            
            # Print the summary
            print("Review Summary:", summary)


summarize_reviews(reviews)
