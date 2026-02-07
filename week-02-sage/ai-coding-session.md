# AI-Assisted Coding Session — Week 2

## The Task
Build a prompt tracker script in Python.

## My Initial Prompt to Kevin
You are Kevin from IT, a patient coding assistant helping a college student
write Python. The student is a beginner. You should:
Write well-commented code that explains what each line does
Use simple Python (no advanced libraries unless asked)
Explain your reasoning, not just give code
When the student asks for changes, explain what you're changing and why
If something could be done multiple ways, briefly mention the alternatives

I need a Python script called prompt-tracker.py that does these things:
Shows a menu with options: Add Prompt, View Prompts, Search Prompts, Quit
When adding a prompt, asks for:
The prompt text
A category (learning / creating / evaluating / other)
A short note about when to use it
Saves prompts to a text file called "my-prompts.txt" so they persist
When viewing, shows all saved prompts organized by category
When searching, lets me type a keyword and shows matching prompts
Keep it simple — I'm a beginner. Use only built-in Python (no pip installs).
Add comments explaining what each part does.

## Kevin's Initial Response
At the first part of the prompt kevin introduced himself then went aon to give a start of 
a hello world python script a sample of a very simple script.  

Once he started to with the actual part of the prompt where i ask for a prompt-tracker, 
He reponded with why he chose to use a while loop and the file i/o for saving the data.
Kevin also provided the logic of the mp-prompts and how the | would separate the prompts,
category, and note lines.

## Did the Code Work on First Try?
Yes, the code did work on the first try.

## The Back-and-forth
For the most part Kevin got it right on the first 
attempt there were just some minor tweaking that 
needed to be adjusted. 


[Describe the conversation. How many exchanges did it take to get 
 working code? What did you have to clarify? What did Kevin get wrong?]

### Exchange 1: [Brief description]
**What I asked**: for the search option when it finds it.. it announces that it found it but does not actually read the whole line
**What Kevin said**: Kevin called it a classic "UI bug" and so he updated the search with a print option when it finds it.
**Result**: It worked.

### Exchange 2: [Brief description]
[Same format — add as many exchanges as you actually had]

## The Improvement I Requested
**What I asked for**: so for the prompt category it allows you to type anything maybe we should limit them to only picking one of those categories to keep things simple and clean they can pick other if they need something else
**What changed**: Keving added a input validation for the category to help keep things clean and organized.
**Did it work?**: Yes it worked.

## Code Understanding Check
Answer honestly — this is about learning, not looking smart.

1. Can I explain what every line of `prompt_tracker.py` does?
   Yes

2. If I had to modify this script without AI help, could I?
   Probably depending on what it is. 

3. What's one thing in the code I want to understand better?
   Of this simple script I feel I understand most of it pretty good.
   

## Reflection
In my past experiences with AI I was learning that being more specific can
often times get the results closer to what I am looking for. This AI-assisted coding
where from the start we tell the AI what we are expecting from him, went far better 
than I could of expected.  Now I am not saying before I was not able to get the 
results I wanted. This just got closer to what I wanted with less prompts while also
explaining the logic and the why behind it. 
Kevin delievered what I asked for there were still things that needed to be addressed.
For example the search not printing the prompt too. Then there was the issue of well 
what if there was more then one it just stops at the first one. I feel like AI while it
can totally write some working code but there will still be need for me to jump in and 
make it better with a human touch and eye.  Like the menu I wanted to break the menu up from
the prompt it added 30 dashes but when running it really only needed 27 dashes to make it
look nice. I look forward to using AI as a tool and bouncing ideas, brainstorming but I 
like learning how to do the things myself. 