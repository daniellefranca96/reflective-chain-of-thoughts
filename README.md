# reflective-chain-of-thoughts

Demo in: https://rcot-ui.fly.dev

Reflective Chain Of Thoughts (RCoT) is an attempt to combine the iterativeness of the CoT prompt with the deeper level of reflection of the ToT.

This method involves a deep step-by-step analysis, where we consider various perspectives and decide the best way forward at each step. We continue this process until we reach a satisfactory conclusion. The overall goal is to think critically, analyze the problem, evaluate options, make decisions, and assess our progress regularly.

To summarize the steps:

1.Starting  a new interaction: here we make a summary of all previous paths decided.

2.CoT - Step-by-step Analysis: Begin thinking about the first step to approach the goal.

3.ToT - Expanding Thoughts: Consider different perspectives and potential paths related to this first step.

4.Deciding the Path: Decide the most promising path based on the different approaches.

5.Progress Check: Evaluate if the decision brings us closer to the goal.

6.Goal Achievement Check:  This step is to evaluate if the expected result has been achieved. If not, you continue refining and developing your ideas.

7.Loop Back: Based on the progress check, return to the CoT and repeat the process, adjusting as necessary.

<p align="center">
  <img  src="https://github.com/daniellefranca96/reflective-chain-of-thoughts/assets/134293046/41a41b27-db75-4818-849a-4cc1016ab801">
</p>

## Optional Parameters:
Below are some optional parameters that can be added to any prompt to increase it's success. All parameters should be put below EXPECTED RESULT SECTION.  

- MAX NUMBER OF LOOPS: (default: as much  as needed). \[In case a number is put by the user we must adjusts the plan to get to expect result in this limitation\]  
- RESOURCES AVALIBALE:  (default: unlimited, min: ) \[List the available resources that can be utilized by the language model that that apply to all steps, anything generated in prompts must not exceed this resources\]  

## Running
The promptS files contains the versions of the method, it was tested on GPT3 and GPT4. To run it, copy the template, fill your GOAL and EXPECTED RESULTS and run it in a LLM.  

VERSIONS:  
prompt-v1: optimized for deep analysis of the goal, mode free thinking, it can never reach an end like ToT.  
prompt-v2: optimized for return of results and reaching conclusion, more flat thinking.  

## React Adapted Prompt
Following bellow and adaptation of the React Framework used today in autonomous agents to implement the method:   

YoutubeSearch: useful for when you need to search a video on youtube  
Shell: useful for when you need use to computer shell    

Use the following format:    

Goal: the input goal you must achieve  
Thought: Let's start thinking step-by-step to approach the goal. What's the first step or aspect we should consider?  
Expand Thoughts: Let's explore different perspectives and potential paths related to the first step. Could you please suggest and briefly describe different ways we could approach this?  
Deciding Path: Considering the different approaches you've described, which one seems the most promising or optimal to you? Please justify your choice.  
Action: the action to take, should be one of [YoutubeSearch, Shell]   
Action Input: the input to the action  
Observation: the result of the action  
Progress Check: Having chosen a path, let's check our progress. Are we closer to your goal from the decision made in the previous step? If not, what's missing or what should be adjusted?  
... (this Thought/Expand Thoughts/Decide Path/Action/Action Input/Observation/Progress Check can repeat N times)  
Thought: I now know the final answer  
Final Answer: the final answer to the original input question  

## TODO

- [ ] Run in others LLMs  
  - [X] Vicuna
  - [x] LLAMA2
  - [x] Bard
  - [ ] OpenAssistant (oasst)
  - [x] Claude
  - [ ] LLAMA
  - [x] MPT
  - [x] Sabia
    
  - [ ] Falcon
- [x] Create Autonomous Version 
- [X] Create prompt optional parameters: max number of loops and resources avaliable.
  
## Feedback & Contribution
Any feedback or contribution to improve the method is welcome.
