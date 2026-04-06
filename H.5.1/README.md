# Gym Workout Planner MVP

## What It Does
A beginner-friendly, single-page gym workout planner that removes the guesswork from going to the gym. Users fill out a quick setup, get a personalized 7-day workout schedule, see exactly what to do today, and log their strength and cardio sessions — all without any external libraries or accounts required.

## How to Use
1. Go to the **⚙️ Setup** tab and enter your name, goal, workout style, and which days you want to work out.
2. Click **Generate Weekly Plan** — you'll be taken straight to the **📅 Today & Weekly** tab.
3. Follow today's step-by-step workout (warm-up → strength → cardio → stretching).
4. Scroll down to see your full 7-day plan at a glance.
5. After your session, head to **📝 Log Workout** to record your sets, reps, weight, or cardio.
6. Toggle **🌙 Dark Mode** in the top-right corner anytime.

## Features Implemented
- **3 workout styles** — Full Body, Upper/Lower Split, and Push/Pull/Legs Split
- **Flexible scheduling** — choose 3 to 5 workout days per week
- **Today's plan** — step-by-step breakdown of warm-up, strength exercises, cardio finish, and stretching
- **7-day weekly view** — color-coded workout, light cardio, and rest days with today highlighted
- **Workout logging** — log strength (machine, sets, reps, weight) or cardio (type, duration, intensity)
- **Dark mode** — toggle with preference saved across sessions
- **Tab-based layout** — Today & Weekly, Log Workout, and Setup tabs on one page
- **Data persistence** — all settings, plans, and logs saved to localStorage
- **Graceful error handling** — inline field validation, toast notifications, corrupt data recovery, and future-date blocking

## Try It Yourself
https://thearn1981.github.io/CSC-113/H.5.1/

## What I Learned
There are several different AI's to use from knowing which one is better for what is just as important as the prompts that you feed to it. Using the same prompt on the 3 different AI platforms I used generated 3 different gym workout planners while each had some cool things that would be cool to see implemented into one. Some are just more detailed while neither really nailed what I was looking for. AI is very useful but it can take several iterations to get close to what you were invisioning and still may not be perfect. 

## Future Improvements
- Allow users to add custom exercises beyond the preset machine list
- Add a progress chart showing weight lifted or cardio duration over time
- Support multiple saved plans (e.g. a bulk plan vs. a cut plan)
- Add rest timer between sets
- Mobile app version with push notifications for workout reminders
