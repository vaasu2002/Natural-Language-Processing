# **Quora Insincere Questions Classification**
## Detect toxic content to improve online conversations

An insincere question is defined as a question intended to make a statement rather than look for helpful answers. Some characteristics that can signify that a question is insincere:

**   Has a non-neutral tone
- Has an exaggerated tone to underscore a point about a group of people
- Is rhetorical and meant to imply a statement about a group of people
*  Is disparaging or inflammatory
- Suggests a discriminatory idea against a protected class of people, or seeks confirmation of a stereotype
- Makes disparaging attacks/insults against a specific person or group of people
- Based on an outlandish premise about a group of people
- Disparages against a characteristic that is not fixable and not measurable
*  Isn't grounded in reality
- Based on false information, or contains absurd assumptions
*  Uses sexual content (incest, bestiality, pedophilia) for shock value, and not to seek genuine answers


The training data includes the question that was asked, and whether it was identified as insincere (target = 1). The ground-truth labels contain some amount of noise: they are not guaranteed to be perfect.

Note that the distribution of questions in the dataset should not be taken to be representative of the distribution of questions asked on Quora. This is, in part, because of the combination of sampling procedures and sanitization measures that have been applied to the final dataset.




![alt text](https://github.com/vaasu2002/Natural-Language-Processing/blob/main/Transfer%20Learning/Projects/Quora%20Insincere%20Questions%20Classification/images/final_accuracy_matrics.png)
