# Havina

Havina is a Python library that can generate knowledge graphs triplets from an input text. Its implementation
is based on the paper "[Language models are open knowledge graphs](https://arxiv.org/abs/2010.11967)" with some
tweaks to improve performance. Most notably, instead of summing the attention scores of each word in a relation,
I am calculating their mean. 

The reasoning behind this change is that a simple sum of scores favors longer relations even if the extra words
do not carry any relevant meaning.

It can be used to evaluate the language comprehension of AI models or as a tool to extract triplets from text 
and build knowledge graphs.

---
## How to use it

---



## Example sentence

---


## How it works

---

The last layer of a transformer based language model, like BERT, outputs attention matrices for all its attention heads.
We calcualte the average of all the matrices to operate the algorithm. If we are looking for head-tail relationships
with tokens from left to right, we would have a matrix like the following. We disregard
the attention scores from below the diagonal because they represent a word-to-word relationship from right to left. We
utilize such an average of matrices for the beam-search algorithm.

We assume that each attention score represent the probability of two words been related in the sentence.
We show below an example of the beam-search input for the sentence "Joe is curious about cars".

|         | Joe | is  | curious | about | cars |
|---------|-----|-----|---------|-------|------|
| Joe     | X   | 0.1 | 0.4     | 0.2   | 0.3  |
| is      | X   | X   | 0.1     | 0.3   | 0.1  |
| curious | X   | X   | X       | 0.4   | 0.2  |
| about   | X   | X   | X       | X     | 0.4  |
| cars    | X   | X   | X       | X     | X    | 


We utilize spaCy to determine the noun chunks and link them to form head-tail pairs. One possible
head-tail pair for this example would be "(Joe, cars)". Taking "Joe" as the first word, we traverse
the first line of the matrix forming candidate relationships. "is", "curious", "about" are all candidates.

The beam-search only passes for its next iteration the top-k candidates, based on their average attention scores.
If k is one, the only candidate for the second iteration is "curious" with a score of 0.4.

We now traverse the third line in the matrix, looking for possible next tokens given "curious".
"curious about" is the only possibility here because "cars" belongs to the tail chunk. "curious" about
has a score of `(0.4+0.4)/2=0.4`.

The relationship we found for the head-tail pair "(Joe, cars)" is "curious about", so the triplet
looks like `(Joe, curious about, cars)`.

In a later stage, we remove prepositions for the relations and uncapitalize, so the final triplet is `(joe, curious, cars)`.

## Constructor parameters


## Roadmap

TODOS:

1. Write a readme with description, usage instructions and an example. Add a short description on Github and tags.
2. Publish library on PIP
3. Add language models other than BERT and instructions for other users to user their own models.
4. Use spaCy sentencizer to segment large documents into sentences

