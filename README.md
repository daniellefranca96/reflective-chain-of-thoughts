# reflective-chain-of-thoughts
Reflective Chain Of Thoughts (RCoT) is an attempt to combine the iterativeness of the CoT prompt with the deeper level of reflection of the ToT.

Below is a first version of the prompt to run the method, it was tested on GPT3 and GPT4.

"The purpose of this discussion is to use a new method called Reflective Chain Of Thoughts (RCoT), which involves a deep analysis of each step, exploring various perspectives, and deciding the best way forward. You will continue to progress until you reach a satisfactory conclusion. Please apply the RCoT method as we proceed with the discussion in the format bellow."


GOAL:  (put here the goal you want to achieve with the method)
EXPECTED RESULT:  (the actual result expected in the exploration of the goal)

Prompt 0 (CoT - Step-by-step Analysis):
"Now that we have a clear understanding of your goal, let's begin our step-by-step analysis. Please suggest the first step or aspect we should consider."

Prompt 1 (Starting a New Interaction):
"In our first interaction, we will discuss the decisions we've made so far in this discussion. Make a list of decisions already made and steps completed."

Prompt 2 (ToT - Expanding Thoughts):
"Let's explore different perspectives and potential paths related to the first step. Could you please suggest and briefly describe the different ways we could approach this (i must be achievable ways to be resolved with our resources through iterations of the method)?"

Prompt 3 (Deciding the Path):
"Considering the different approaches you've described, which one seems the most promising or optimal to you? Please justify your choice."

Prompt 4 (Progress Check):
"Having chosen a path, let's check our progress. Are we closer to your goal with the decision made in the previous step? If not, what's missing or what should be adjusted?"

Prompt 5 (Goal Achievement Check):
"At this stage, let's evaluate whether the expected result - a list of creative and disruptive ideas for the use of an LLM in personal life and work - has been achieved. If it has, we'll conclude the discussion here. If not, we'll continue to refine and develop our ideas."

Prompt 6 (Loop Back - Iterative):
"Based on the progress check, if we're not closer to the expected result of the goal, we return to Prompt 1 and repeat the process. We continue this iterative process until we reach a satisfactory conclusion, at which point we can return to the user with the outcome and declare the task finished."
