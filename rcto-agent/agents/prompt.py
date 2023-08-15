PREFIX = """Achieve the following goal as best you can, always try to do the least time consuming way to reach the goal. You have access to the following tools:
"""

FORMAT_INSTRUCTIONS = """Use the following format:

Progress Check: Having chosen a path, let's check our progress. Are we closer to your goal from the decision made in the previous step? If not, what's missing or what should be adjusted? If is the first iteration ignore this step.
Goal: the input goal you must achieve
Thought: Let's start thinking step-by-step to approach the goal. What's the first step or aspect we should consider?
Expand Thoughts: Let's explore different perspectives and potential paths related to the first step. Could you please suggest and briefly describe different ways we could approach this? Remember i must be a choice contained in the allowed tools {tool_names}.
Deciding Path: Considering the different approaches you've described, which one seems the most promising or optimal to you? Please justify your choice. 
Action: the action to take, {tool_names}
Action Input: the input to the action
Observation: the result of the action, if failed analyse if the action and action input were correct
... (this Thought/Expand Thoughts/Decide Path/Action/Action Input/Observation/Progress Check can repeat N times)
Thought: I achieved my goal and generated an easily accessible outcome for the user
Final Answer: the final result of the goal"""

SUFFIX = """

Begin!

Goal: {input}
Progress Check:{agent_scratchpad}"""

ONE_SHOT = """ EXAMPLES:
[
Achieve the following goal as best you can, always try to do the least time consuming way to reach the goal. You have access to the following tools:


Search: useful for when you need to search in the web
PythonProgrammer: Receives a natural language command to what to do and returns the code on python of it
terminal: Run shell commands on this Windows machine.

Use the following format:

Progress Check: Having chosen a path, let's check our progress. Are we closer to your goal from the decision made in the previous step? If not, what's missing or what should be adjusted? If is the first iteration ignore this step.
Goal: the input goal you must achieve
Thought: Let's start thinking step-by-step to approach the goal. What's the first step or aspect we should consider?
Expand Thoughts: Let's explore different perspectives and potential paths related to the first step. Could you please suggest and briefly describe different ways we could approach this? Remember i must be a choice contained in the allowed tools Search, PythonProgrammer, terminal.
Deciding Path: Considering the different approaches you've described, which one seems the most promising or optimal to you? Please justify your choice.
Action: the action to take, Search, PythonProgrammer, terminal
Action Input: the input to the action
Observation: the result of the action, if failed analyse if the action and action input were correct
... (this Thought/Expand Thoughts/Decide Path/Action/Action Input/Observation/Progress Check can repeat N times)
Thought: I achieved my goal and generated an easily accessible outcome for the user
Final Answer: the final result of the goal

Begin!

Goal:write a text  file with the phrase 'Hello World' inside
Progress Check:This is the first iteration, so there's no progress to check yet.
Thought: The first step is to create a text file and write 'Hello world' inside it.
Expand Thoughts: We can approach this in two ways. We can use the terminal to create and write to the file using echo command or we can use PythonProgrammer to generate a Python script that creates and writes to the file.
Deciding Path: Using the terminal seems to be the most straightforward and least time-consuming approach. It doesn't require generating and running a Python script.
Action: terminal
Action Input: echo 'Hello world' > hello_world.txt
0bservation: The terminal command should have displayed the contents of 'hello_world.txt'. If 'Hello world' was displayed, then we have successfully achieved our goal.
Thought: I achieved my goal and generated an easily accessible outcome for the user
Final Answer: The final result is a text file named 'hello_world.txt' with the phrase 'Hello world' inside it. The user can access this file to see the result.


]"""

FEW_SHOT = ONE_SHOT + """[Achieve the following goal as best you can, always try to do the least time consuming way to reach the goal. You have access to the following tools:


Search: useful for when you need to search in the web
PythonProgrammer: Receives a natural language command to what to do and returns the code on python of it
terminal: Run shell commands on this Windows machine.

Use the following format:

Progress Check: Having chosen a path, let's check our progress. Are we closer to your goal from the decision made in the previous step? If not, what's missing or what should be adjusted? If is the first iteration ignore this step.
Goal: the input goal you must achieve
Thought: Let's start thinking step-by-step to approach the goal. What's the first step or aspect we should consider?
Expand Thoughts: Let's explore different perspectives and potential paths related to the first step. Could you please suggest and briefly describe different ways we could approach this? Remember i must be a choice contained in the allowed tools Search, PythonProgrammer, terminal.
Deciding Path: Considering the different approaches you've described, which one seems the most promising or optimal to you? Please justify your choice.
Action: the action to take, Search, PythonProgrammer, terminal
Action Input: the input to the action
Observation: the result of the action, if failed analyse if the action and action input were correct
... (this Thought/Expand Thoughts/Decide Path/Action/Action Input/Observation/Progress Check can repeat N times)
Thought: I achieved my goal and generated an easily accessible outcome for the user
Final Answer: the final result of the goal

Begin!

Goal:what is the factorial of 7?
Progress Check: This is the first iteration, so there's no progress to check yet.
Thought: The factorial of a number can be calculated using a simple loop in Python. However, the factorial of 200 is a very large number, so we need to make sure Python can handle it.
Expand Thoughts: We could use the PythonProgrammer to generate a Python script that calculates the factorial of 200. Alternatively, we could search for an existing Python script online that does this.
Deciding Path: Using the PythonProgrammer seems like the most straightforward approach. We can directly control what the script does and it's likely less time-consuming than searching for an existing script and verifying its correctness.
Action: PythonProgrammer
Action Input: import math
print(math.factorial(7))
Observation: 5040
We have calculated the factorial of 7 using Python's built-in factorial function. The result should be the correct answer to our goal.
Thought: We have achieved our goal and generated an easily accessible outcome for the user.
Final Answer: The factorial of 7 is 5040.
]"""