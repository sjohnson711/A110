# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
  1. The number of attempts did not did not decrement after the first guess/str on line 42
  2. The new game button functionality is not working correctly
  3. The game difficulty is not correlating to the number of attempts for each 
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)? I used ChatGPT and Claude to help with the fixes.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result). The AI suggested that the str(number) was not the correct implimitation and fixed the TypeError
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).AI did not fix the bug. 

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed? Retested the functionality of the bug several times to make sure that the fix did not break.
- Describe at least one test you ran (manual or using pytest)  I ran pytest
  and what it showed you about your code. It showed me that may code returned the desired output.
- Did AI help you design or understand any tests? How? Yes I would ask claude to explain what the test was doing. It is similar to how Jest test work in JavaScript.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app. Because it was like the game was starting over on its own.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit? Stremlit uses st.session_state to act as a dictionary.
- What change did you make that finally gave the game a stable secret number? Updated the st.session_state to keep the number from updating without the game reset.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects? Co-programming with AI and reading through the code for any issues that I may see.
- This could be a testing habit, a prompting strategy, or a way you used Git. I used git to update the changes and push them. Git is a way to reverse to a previous commit if something happened. 
- What is one thing you would do differently next time you work with AI on a coding task? I will create a file explaining what I expect the game to be. 
- In one or two sentences, describe how this project changed the way you think about AI generated code. I still think that the need for foundational skills will help with co-programming with A.I. There are alot of mistakes that the model still makes but that is why it is worth slowly iterating to build an app or website. 
