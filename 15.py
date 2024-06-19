import csv

Tweets = 'covid19_tweets.csv'  # Change this to the path of your CSV file

try:
    with open(Tweets, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
except FileNotFoundError:
    print(f"The file {Tweets} does not exist.")
except UnicodeDecodeError:
    print(f"Error decoding the file {Tweets}. Try using a different encoding.")
