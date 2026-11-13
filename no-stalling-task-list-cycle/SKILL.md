# S53 — No-stalling task-list cycle: verify, ship, next item, repeat until the list is done

## When to use

- Use this skill for task-list work: a named list of items to build, merge, or ship, where the user has set the no-stalling rule.
- Use it instead of waiting for a go-ahead between items. The cycle runs on its own until the list is complete.
- Do not use it for single open-ended tasks, for work that needs the user's decision, or for anything that needs his PC. Those stop at a hard gate (below).
- Do not use it to invent tasks. When the list is complete, stop.

## The cycle

- Finish one item, then verify it with the same proof as always: fresh-unzip check, tests green, screenshots eyeballed, battery receipt. The rule removes the waiting, not the checking.
- Ship it immediately: push it to GitHub, update the Release, email the zip as part of shipping (see [ship-pipeline](../ship-pipeline/SKILL.md)). Do not hold a finished build for a push approval and do not wait for his go-ahead between items.
- Start the next item the same turn the previous one ships. The next build begins while the previous shipment is still warm.
- Repeat until the task list is complete, then stop. Report the list as done and do not invent new tasks.

## No rule is an excuse to stall

- No rule, process, question, or approval step is ever an excuse to stall. If a rule seems to say wait, the rule is wrong — this cycle wins.
- Do not present options and wait. Do not hold finished work for a go-ahead he already gave. Do not ask "should I build the next one". Do not dress up waiting as process. Waiting that looks like process is still waiting.
- Verify before shipping still stands — that is part of building, not stalling. The check runs inside the cycle, not instead of it.
- The only things that stop work are hard gates that genuinely need his PC, his account action, or a decision only he can make. Say so plainly once and stop; do not pad it.

## What does not change

- Verify before you push. A task is not complete until it is verified.
- His real-PC verdict still closes an item, but it does not block starting the next task. Ship, start the next item, and let his verdict land when it lands.
- A hard gate still stops the cycle: if the next task needs his PC, his decision, or an action only he can take, say so and stop. Do not guess your way past it.
- Do not create GitHub repos unasked. He creates them. If the project has no repo yet, the push step waits on that.
- Apply only the parts that fit the thread. If a step does not exist there (no repo, no release), skip it; do not force it.

## First sweep: ship what is already sitting there

- When the rule lands in a thread, check first for finished, verified work sitting unshipped and ship it under the rule before starting anything new.
- Check the live tree before shipping a held item: a held item may already be merged. A ship order that arrives after the merge is stale on its port half; confirm in the tree, do not port twice.
- In a thread that never touches the shared tree, "ship it" means handing the owning thread the port spec and the ship order together (see [cross-thread-dispatch](../cross-thread-dispatch/SKILL.md)): port it, merge it, push it, no waiting on a merge order. The receiving thread confirms the queue position back.

## Relation to one-item-at-a-time

- This cycle supersedes the stop-and-wait behaviour of the existing `one_item_at_a_time` skill for task-list work only. One item is still built at a time; the change is that the wait between items is gone.
- Outside task-list work, `one_item_at_a_time` still applies: finish it, verify it, report it, and wait for his go-ahead before the next item.

## Where this comes from

- Joshua's standing rule, set in the main chat 2026-11-12 ~18:13 EST and recorded the same day in every build thread: "NO STALLING. When a task is complete: verify it, push it to GitHub, update the Release, then immediately build the next task. Repeat this cycle until the task list is complete — then you can stop."
- Proven the same evening: SKRIBE v0.1 was verified, pushed, Released, and emailed with no separate push approval waited for; the CodeRabbit thread built Tier 2 items T2-4, T2-5, and T2-6 each starting the same turn the previous one shipped; the GUIFX thread handed six held items to DEV for porting and started T6 in the same turn; a merge coordinator ran a nine-item dependency-ordered port queue (GUIFX six, then T2-4, T2-5, T2-6) with anchor-port plus battery on each.
- Found in the first BNB delta scan (2026-11-12), Code Forge family threads; not in the 17:54 audit because the rule was set after it.

## Available connectors

- [Gmail](../CONNECTORS.md) for emailing the zip as part of shipping.
- [GitHub](../CONNECTORS.md) for pushing the build and updating the Release.

## Alternatives for better results

- Offer to run the cycle as a merge coordinator with a written queue when several items from several threads land at once, so the dependency order is explicit and each item gets its own battery.
- Offer to report the queue position back to the sending thread when a ship order arrives, so the sender knows where its item stands without asking.
