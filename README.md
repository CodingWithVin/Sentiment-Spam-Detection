## Analysis and Observations


When tested on the full training and test data, 
the Naive Bayes model showed that positive accuracy was consistently higher than negative accuracy, 
reflecting the frequency and strength of words associated with positive sentiment. 
Specifically, the model achieved a positive accuracy of 0.9604, a negative accuracy of 0.7080, 
and an overall total accuracy of 0.9105. Words like “great,” “love,” and “amazing” appeared often in positive reviews, 
giving them strong influence in the models' probability calculations. 
This pattern illustrates how repetition of enthusiastic language can change  a model trained on simple word counts. 
Overall, the results suggest that the model can catch the general tone effectively but struggles with nuance, 
because it relies entirely on how frequently certain words appear rather than on context or sentence structure. 
This is especially important as the same words that contribute to a positive review appear in a negative one.
For instance, the review “a brilliant performance but predictable plot” was misclassified as negative because the word “predictable”
carries a strong negative association that overpowered the positive influence of “brilliant.” Similarly, “slow and boring but loved the 
soundtrack” was incorrectly labeled as positive, driven largely by the overwhelming weight of the word “loved.” 
These mistakes reveal the core limitation of the Naive Bayes approach: it assumes each word acts independently, 
ignoring contrast and negation. Without awareness of context, a single word can change an entire prediction. 

While the program performs well at capturing frequently occurring spam-related keywords
it struggles with nuance, negation, and mixed intent, which are common in legitimate emails
