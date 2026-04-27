---
title: Habits of high-functioning teams
date: 2024-09-12
summary: Notes on psychological safety, hygiene, redistribution of experience, and communicating generously.
slug: habits-of-high-functioning-teams
---

## High psychological safety

A few behaviors I've come to associate with healthy teams:

- **Regular retrospectives**, with several real items in the "what is not going well" column. If that column is empty, it's a sign that difficult topics are being kept rather than aired.
- Individuals don't spend a lot of time stuck or blocked. They ask for help.
- Individuals dissociate their value to the team from their personal output. The framing is "here's what *we* delivered," not "here's what *I* delivered." Safe teams can have conversations about what value means, and how it's not just lines of code.
- People take more PTO and sick time. I think this is a symptom of the belief that the rest of the team will continue making good decisions in their absence.

One small idea I keep returning to: a *feedback week*. Once a quarter, everyone — including the team lead and PM — is randomly assigned to collect feedback on someone else's behalf.

## Good hygiene practices

> As the complexity of a system increases, the accuracy of any single agent's own model of that system decreases rapidly.
> — Woods's Theorem

Good development hygiene means taking a bit of extra time to record present-day context. In practice that looks like:

- Descriptive commit messages. At minimum, every message contains a verb. Some teams require an issue number on every commit. Pick the level of cognitive investment that fits.
- Intention-revealing class and method names that follow the conventions of your language and framework.
- Unit tests with helpful descriptions, using realistic variable names and data — not `foo` and `bar`.
- Keeping back-and-forth about a feature inside the tracking issue, rather than in Slack DMs where your future teammate, six months from now, will never find it.

Hygiene is empathy in disguise. Cleaner artifacts let teammates absorb context faster and spend less energy spelunking. It also pays to empathize with your future self.

## Active redistribution of experience points

I like the framing that every new piece of work is an *enemy* that, when delivered, spreads domain context and confidence around your team.

If your team has plenty of senior engineers — Great Knights and Paladins, in JRPG terms — you should resist the temptation to always send them after the difficult stories. On healthy teams, part of the senior role is *context redistribution*: making sure a less experienced engineer can take a swing at the hard problem and earn some XP. The whole team's productivity and morale rise when everyone feels at least somewhat equipped to tackle whatever comes through the door — knowing they can always ask a Falcon Knight to adjutant in if needed.

## Communicating generously

> Be conservative in what you send, be liberal in what you accept.

Robustness as an interpersonal principle. The corollary is the *principle of charity*: assume the best interpretation of what someone has said. High-performing teams seem to do this almost reflexively.

The teaching analogue I keep coming back to: *assume that every student you interact with has limited information, but infinite intelligence*. That places the onus on the mentor to make sure their explanations make sense — which, given the inherent asymmetry between teacher and learner, is a fair way to distribute the emotional labor. Translated to a team setting: assume your peer is competent, intelligent, and reasonable, and that they're asking because they're missing context they've already tried to find on their own.
