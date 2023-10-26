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


## Example sentence


## How it works



|         | Joe | is  | curious | about | cars |
|---------|-----|-----|---------|-------|------|
| Joe     | X   | 0.1 | 0.4     | 0.2   | 0.3  |
| is      | X   | X   | 0.1     | 0.3   | 0.1  |
| curious | X   | X   | X       | 0.4   | 0.2  |
| about   | X   | X   | X       | X     | 0.4  |
| cars    | X   | X   | X       | X     | X    | 


## Constructor parameters


## Roadmap

TODOS:

1. Write a readme with description, usage instructions and an example. Add a short description on Github and tags.
2. Publish library on PIP
3. Add language models other than BERT and instructions for other users to user their own models.
4. Use spaCy sentencizer to segment large documents into sentences

