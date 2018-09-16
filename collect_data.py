import time
from fuzzywuzzy import fuzz
import twitter_tokenizer

#### Topics that will be collected.
# topics = ['#happy', '#fun'] TODO rewrite as a test
topics = ['#sports', '#politics', '#technology', '#food', '#music']

ignore_doc = 'Just added myself to the http://wefollow.com twitter directory under: #'


class TagCollection:
    
    def __init__(self, hashtag, no_of_tags, filename, threshold):
        """
        hashtag - string, tags you want to collect
        no_of_tags - positive int, max number of tags you want to collect
        filename - string
        threshold - int, in the range [0,100] for fuzz.ratio
        """
        assert no_of_tags > 0, 'tags must be a positive integer'  
        
        self.hashtag = hashtag
        self.no_of_tags = no_of_tags
        self.filename = filename
         
        self.threshold = 75
      
            
    def extract(self):     
        """extract the messages containing the specified hashtag"""
        
        timestamp_char, user_char, msg_char = ('T', 'U', 'W')
        tok = twitter_tokenizer.Tokenizer(preserve_case=False)
        hashtag_counter = 0
        first_charcter = 0
        
        txtfile = open(self.filename, "w+")
        with open("/home/ubuntu/vol1/4th_year_project/mhkmodes/tweets2009-06.txt") as tweets:

            for idx, doc in enumerate(tweets):
            
                is_msg = (msg_char == doc[first_charcter])
                if is_msg:
                    
                    # skip document
                    if self.is_similar(ignore_doc, doc):
                        continue
                    
                    tokenized_doc = tok.tokenize(doc)
                    
                    if hashtag in tokenized_doc:
                        txtfile.write(doc)
                        hashtag_counter += 1
                        
                if self.is_enough_tags(hashtag_counter):
                    break
            
            txtfile.close()

    
    def is_exists(self, filename, hashtag):
        # check file name exists 
        if not filename:
            filename = "{}.txt".format(hashtag)

    def is_similar(self, doc1, doc2):
        return fuzz.ratio(doc1, doc2) >= self.threshold
    
    def is_enough_tags(self, hashtag_counter):
        return hashtag_counter >= self.no_of_tags
        

if __name__ == '__main__':
    
    start_program = time.time()
    no_of_tags = 2
    threshold = 75
    
    for hashtag in topics:
        
        start_extract = time.time()
        
        filename = hashtag + '_' + str(no_of_tags) + '.txt'
        
        messages = TagCollection(hashtag, no_of_tags, filename, threshold)
        messages.extract()
        
        print("{}: Finished collecting messages and took {}".format(filename , start_extract-time.time()))
        
    print("Program collect_data finished which took {}".format(start_program - time.time()))