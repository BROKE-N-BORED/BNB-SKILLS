# S85 - Pick it up and it works: the app sets itself up, finds its own files, and needs no manual steps

The user picks the app up and it works. Services start under the hood,
models and files are found on their own, and the best settings for the
machine are set dynamically. No start buttons, no refresh buttons, no
hunting for files, no manual setup steps. This is his design code, not
a nice-to-have: every project must be usable by anyone without
disturbing the performance or the purpose of the program.

## When to use

- Use this skill for every app, from the first version. Self-setup
  is the design, not a feature to add later.
- Use it when a build adds a button, a step, or a setting the user
  has to touch before the app does its job: that is the thing this
  skill removes.
- Do NOT use it to hide a real choice the user has to make: when
  two genuinely different behaviours exist and only he can pick,
  the choice stays visible. The skill removes busywork, not
  decisions.

## Services start under the hood

- The app starts the services it needs on its own, in code, when it
  launches. There is no Start button and no Refresh button for a
  service the app can start itself.
- A service that is already running is detected and used, not
  started twice: "address already in use" means the service is up,
  not that something is broken.
- If another app on the same machine already manages the same
  service without buttons, the new app must do the same. The
  comparison app is the proof the code can do it.
- A start or refresh button added because the connection code is
  broken is a bandaid, not a feature: fix the code and remove the
  button (see [no-bandaids](../no-bandaids/SKILL.md)).

## The app finds its own models and files

- The app scans the PC for models itself and lists what it finds.
  The user never has to hunt for a model file or tell the app
  where his models live.
- An app that opens on an empty folder and makes him search for a
  model is broken by design. Auto-discovery comes first, before
  any manual path option.
- The same rule covers files: the app looks in the places the
  files live and shows what it found, instead of asking him to
  browse to them.

## Settings are set dynamically, and still settings do not appear

- The best settings for the machine are set dynamically, in code,
  from what the machine actually is: its RAM, its cores, what is
  installed. The user does not set them by hand.
- A setting that does not change does not appear. If the right
  value is always the same on his machine, there is no control
  for it at all.
- A settings screen full of controls he should never have to touch
  is a design failure, not a feature. Simplify it down to the
  choices that are genuinely his.

## Every project is usable by anyone

- Every project must be gamified so that anyone can access and use
  it without disturbing the integrity of the performance and what
  the program is designed to do. "Gamified" here means pick-it-up
  usability: clear, rewarding, and obvious at first touch, not a
  game layered on top.
- The test is the toy test (see
  [ui-design-source-library](../ui-design-source-library/SKILL.md)):
  a child could pick it up and use it. If a first-time user has to
  read a manual before the app does its job, the design has failed
  this skill.

## A model that works in one program must work in all of them

- If a model runs fine in one of his programs, it must run fine in
  all of them. A model that tests fast in one app and will not work
  in another is a defect in the second app's code, not in the
  model and not in the service it runs on.
- Do not blame the service: when the same service works perfectly
  everywhere else, the fault is in the app's code. Find the
  difference between the app that works and the app that does not,
  and fix it in the app that does not.

## Deduce, do not ask

- The app works out what is in the folder it is given: it infers
  what the data is and what it is good for, instead of making him
  declare it. He opens a folder; the app deduces what is in it and
  what should be done with it.
- The app is never designed around his personal data in particular.
  It is designed around the kinds of data it will meet, and it
  recognizes them when it sees them.
- When the app cannot tell what something is, it says so in plain
  words and asks about that one thing - it does not make him
  describe everything up front because it could not be bothered
  to look.

## Look it up yourself

- If the program can derive what it needs from data it already
  has, it must do so, and never hand the user a box to type it in
  or a role to assign by hand. The Hugging Face repo for a known
  model, and what the model is good at and not good at, are data
  the program can look up; the user must never be asked to type
  them in or assign them.
- STELLA v0.30.0 is the worked example: one-tap Hugging Face
  pull. The root cause it fixed was that picking a model from
  Ollama stored the Ollama name as the base, and the download
  button hit a wall instead of looking up the model's Hugging
  Face home, even though the lookup already existed in Stella.
  v0.31.0 simplified the profile window the same way: name, what
  it can do, good and not good at in plain words, one
  training-file button.
- Unresolved tension, recorded 2026-11-18 ~19:00 EST: Joshua
  repeated the order ("I shouldn't have to do anything") and was
  still given a manual repo name to type
  (`ibm-granite/granite-4.1-3b-base`). The rule stands; the
  instance is not yet fixed.

## Where this comes from

- OLLAMA SYSTEM TEST thread (662fb3aa, 2026-11-15 11:57-12:08
  EST): Joshua, third time: "This is also bullshit I shouldn't
  have to do anything to start ollama I dont have to do this
  shitnto use code forge at all dude why are you doing this?
  Ollma can be connected using code under the hood jive built
  plenty of ahit that works using ollama wothiut having to do
  this bulkshir thisnis the 3rd time ive told you this sht for
  OST" - and "It failed also thee is no refresh button,
  WHYBARENT YOUBKISTEN8NG TO ME I SHOUOD NOTNHAVE TO MANUALLY
  START OR REFEESH OLLAMA AT ALL!!! I DONT HAVE TO DO THAT FOR
  DUO OR CODEFORGE THEY JUST FUCKING WORK BECAUEBTHATS HOWBYOU
  WORTE THE CODE WHYBZRWNT YOU DOING THAT FOR OST?????" He had
  to touch the terminal himself because OST did not manage
  Ollama itself.
- OLLAMA SYSTEM TEST thread (662fb3aa, 2026-11-15 12:53 EST),
  from his design code: "I dontnhave to do that shit in code
  forge, it should all be set for whats best dynamically for
  you sytem and whats best I shouldn't have to do a bunch if
  manual shit imthat is part of my design code and you know
  this stop making shitndiffuclt and confusing and nmunnecessary
  or make it difficult to use, every project must be gamified so
  that anyone can access and use it without disturbing the
  integrity of the performance and what the program is designed
  to do it must do".
- FYRN thread (75f1a546, 2026-11-15 16:12 EST): "Whybthr fuck do
  inhale to search fo a fucking model when all the other ones
  automatically scanned my oc for models dude why the fuck arw
  you making ot difficult and making me have to tell yku shit
  you jnow isnt going to fucking work Your really starting to
  miss me off". FYRN opened an empty folder and made him hunt;
  the fix was auto-discovery first.
- CODE FORGE DEV thread (94792a18, 2026-11-15 14:02 EST), sixth
  time: "Also it foe not make sense to me how I can run a test
  for thisbmodel and it runs fast as fuck nonossoes but it wont
  work in code forge thata huge fucking problem that needs to be
  addressed for the 6th time If thr mofepsbwork fine in other
  programs they need to work fine in code forge or its all a
  fucjing wast". Same thread 15:44: "My ollama works everywhere
  perfectly eoth every model no handfuls or issues so its
  something yku coded thats doing it dude".
- DATAPACKR thread (6c8ad11f, 2026-11-15 13:36-13:37 EST):
  "This isn't built rihht I just opened it on my pc and it s
  not designed correctly at all, its not supposed to be designed
  around my personal data packs from ai or anything in
  particular its supposed to be abke tondeduce what's in the
  souce folder I have and know what in them and whatbthye are
  good for etc etc does this make sense I shouldn't have to
  manually tell you what I want it tondo like that it ahould be
  abke to deduce what data is present and what should be
  packaged etc etc right? Figure out a waybtonmakenthisnwaybmorenusernfriendlybakdneasier
  to do please".
- Found in the seventh BNB delta scan (2026-11-17). Five
  in-window instances across four threads, two of them repeat
  complaints (third and sixth time).
- STELLA thread (2026-11-18 ~15:00-17:00 EST), his order twice in
  one day, for the "look it up yourself" rule: "This shit shoukd
  pull from huggingface automatically, I dont know what this
  is"; "I shouldn't need to do that dude... it shoukd be able to
  get the accurate weights and know what the model is good at
  and what it isnt good at". HF pull must be automatic, no typing
  repo names, no hand-assigned roles, child-easy.
