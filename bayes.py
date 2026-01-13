def get_file_counts(file_name):
    word_list = {}
    with open(file_name, "r", encoding="utf-8") as file:
       for line in file:
          x = line.split()
          for i in x:
             if i in word_list:
                word_list[i]+=1
             else:
                word_list[i] = 1
    return word_list

def counts_to_probs(dictionary,number):
    for key, value in dictionary.items():
       dictionary[key] = value/number
    return dictionary
              
def train_model(file_name):
   counts = get_file_counts(file_name)
   with open(file_name, "r") as file:
      num_lines = len(file.readlines())
   return counts_to_probs(counts, num_lines)

def get_probability(dict_prob,review):
   chance = 1
   for word in review.lower().split():
      if word not in dict_prob: # if word in review isn't in list of words
         chance*=0.00009
      else:
         chance*=dict_prob[word]
   return chance
      
def classify(review,pos_model,neg_model):
   pos_prob = get_probability(pos_model,review)
   neg_prob = get_probability(neg_model,review)
   if pos_prob > neg_prob:
      return "positive"
   elif pos_prob < neg_prob:
      return "negative"
   else:
      return "positive"
   
def sentiment_analyzer(pos_file,neg_file):
   pos_model = train_model(pos_file)
   neg_model = train_model(neg_file)
   print("Blank line terminates.")
   review = input("Enter a sentence: ")
   sentiment = classify(review,pos_model,neg_model)
   while review != "":
      sentiment = classify(review,pos_model,neg_model)
      print(sentiment)
      review = input("Enter a sentence: ")

def get_accuracy(pos_test,neg_test,pos_training,neg_training):
   # confirming pos accuracy
   pos_model = train_model(pos_training)
   neg_model = train_model(neg_training)
   pos_total = 0
   pos_correct = 0
   with open(pos_test, "r", encoding="utf-8") as file:
      for line in file:
         review = line.strip()
         if review == "":
               continue
         pos_total += 1
         prediction = classify(review, pos_model, neg_model)
         if prediction == "positive":
               pos_correct += 1
   # confirming negativ accuracy            
   neg_total = 0
   neg_correct = 0
   with open(neg_test, "r", encoding="utf-8") as file:
      for line in file:
         review = line.strip()
         if review == "":
              continue 
         neg_total += 1
         prediction = classify(review, pos_model, neg_model)
         if prediction == "negative":
               neg_correct += 1
   # overall findings            
   total = pos_total + neg_total
   total_correct = pos_correct + neg_correct

   pos_acc = (pos_correct / pos_total)
   neg_acc = (neg_correct / neg_total)
   total_acc = (total_correct / total)

   print("Positive accuracy:", pos_acc)
   print("Negative accuracy:", neg_acc)
   print("Total accuracy:", total_acc)

