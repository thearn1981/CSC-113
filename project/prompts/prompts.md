# CHATGPT
# 🧠 Gym Workout Planner – Prompt Library

This file contains reusable prompts and expected response formats used to design and build the MVP.

---

## 📌 1. PRD Generation Prompt 

### Prompt
I'm a computer science student building an MVP for a Gym Workout Planner.
Help me create a PRD that includes:
- problem statement
- target user
- 3 must-have features for the MVP
- user interaction flow
- what to exclude from v1

Format as a markdown document I can use to generate code later.

---

### Expected Response Structure

- Clear problem definition
- Defined target user persona
- 3 focused MVP features
- Step-by-step user flow
- Explicit out-of-scope list
- Markdown formatting (headers, bullets, tables where helpful)

---

## 🏋️ 2. Workout Plan Generation Prompt

### Prompt
Generate a beginner-friendly weekly gym workout plan.

Constraints:
- 3 workout days per week
- Full-body workouts only
- Machine-based exercises only
- Include cardio in every workout
- Avoid consecutive intense days

Output format:
- Weekly table
- Daily breakdowns

---

### Expected Response Structure

- Weekly schedule table
- Each day labeled clearly
- Includes rest days
- Beginner-safe pacing

---

## 📋 3. Daily Workout Output Prompt

### Prompt
Generate a "Today's Workout" plan for a beginner gym user.

Requirements:
- Must follow this order:
  1. Warm-up
  2. Strength (machines only)
  3. Cardio finish
  4. Stretching

Keep it simple and easy to follow.

---

### Expected Response Structure

- Clean step-by-step format
- Bullet points for exercises
- Includes sets/reps or duration
- No extra explanation (UI-ready)

---

## 🧩 4. Feature-to-Code Prompt (Django)

### Prompt
Convert this feature into Django models and basic backend logic:

[PASTE FEATURE HERE]

Requirements:
- Keep it simple for MVP
- Use clear model relationships
- Include basic fields only

---

### Expected Response Structure

- Django models (models.py)
- Field definitions
- Foreign key relationships
- Minimal but functional

---

## 🔄 5. User Flow Prompt

### Prompt
Create a simple user interaction flow for a beginner workout planner app.

Include:
- onboarding
- daily usage
- logging workouts

---

### Expected Response Structure

- Numbered steps
- Logical progression
- Matches MVP features
- No unnecessary complexity

---

## 🚫 6. Scope Control Prompt

### Prompt
Given this MVP idea, list what should NOT be included in version 1.

Focus on:
- avoiding complexity
- keeping development fast
- beginner-friendly experience

---

### Expected Response Structure

- Bullet list
- Clear exclusions
- Focus on simplicity

---

## 💡 Notes

- All prompts are designed for **MVP-first development**
- Keep outputs:
  - simple
  - structured
  - code-ready
- Avoid overengineering early versions

---

## 🚀 Future Prompts (To Add Later)

- Progress tracking logic
- Personalized workout generation
- UI/UX improvements
- Mobile optimization


---
 
## Prompts for CLAUDE AI
 
```
I need you to create a single-page web application based on this PRD:
 
Requirements:
- Single HTML file with embedded CSS and JavaScript
- No external dependencies or libraries needed
- Works when opened directly in a browser
- Include clear comments explaining major sections
 
Please generate the complete code.
```
 
*(PRD attached: Gym Workout Planner – MVP PRD, Beginner + Cardio Focused)*
 
---
 
## Response
 
Generated a complete single-file HTML web application (`gym-planner.html`) based on the PRD. Here's a summary of what was built:
 
**On first load**, a setup screen collects the user's goal (General Fitness / Weight Loss / Endurance) and preferred workout days per week (2, 3, or 4). This generates the weekly plan and is remembered across sessions via `localStorage`.
 
**4 Tabs:**
- **Today** — the core "What Do I Do Today?" dashboard. Tap any day pill at the top to preview that day's plan. Workout days show all 4 phases (Warm-Up → Strength → Cardio → Stretch). Rest/light days show a clean rest banner.
- **Weekly Plan** — a 7-card grid showing the full week at a glance, clickable to jump to that day.
- **Log Workout** — toggle between Strength and Cardio forms, fill in details, and save. Entries persist to localStorage.
- **History** — a table of all logged entries, newest first.
**Design choices:** Industrial-dark aesthetic with amber accents, Barlow Condensed headings for a gym-board feel, and a subtle grid texture background. Color-coded phases (amber = strength, ember-red = cardio, green = rest/stretch) make the structure immediately scannable.
 
**Technical implementation highlights:**
- Zero external dependencies — fonts loaded via Google Fonts CDN only
- `localStorage` used for full state persistence (setup choices, log entries, selected day)
- Weekly plan generator follows PRD rules: no consecutive workout days, spread across the week
- 3 workout rotations cycle through different machine exercises for variety
- Goal selection (general / weight loss / endurance) affects cardio finish duration and type
---