# S88 - Lean core, add-ons: the base stays small, extras live as add-ons

The base program stays lean and does its core job well. Everything
extra lives as an add-on, exactly like Blender: a good base program,
with add-ons on top for the rest. When something already planned or
already built belongs in an add-on, it is separated out of the base
instead of being left to bloat it.

## When to use

- Use this skill when a program is growing past its core job, or
  when a new feature is proposed that serves a narrower use than
  the base.
- Use it when the task list for the base holds items that are
  really add-on work: separate them out instead of building them
  into the base.
- Do NOT use it to strip the base of what it needs to do its own
  job: the core stays whole. The line is between the job the
  program exists to do and the extras that extend it.

## Keep the base lean

- The base does its core job, and does it well. That is the whole
  test for what belongs in it.
- Anything that serves a narrower use, a specific workflow, or a
  single kind of content is an add-on candidate, not base work.
- Bloat is measured in the task list as well as in the code: a
  base plan that keeps growing past its core job is bloating
  before a line is written. The plan shrinks when add-on work is
  separated out of it.

## Separate add-on material out of the base

- When something already planned or already built should be
  considered an add-on, separate it as such: out of the base
  plan, out of the base build, and into the add-on side.
- Separation is a job in itself, not a note: the plan, the task
  list, and the code all change, and the base plan's count drops
  by what moved out.
- Do not leave separated material half in the base: a half-moved
  feature is worse than a bloated one, because neither side owns
  it.

## The add-on suite is a separate program

- The tool that creates add-on packs is its own program, not a
  mode of the base. It authors, packs, and tests add-on packs
  that plug into the base.
- The base stays the base: it loads add-on packs, it does not
  become the add-on authoring tool.
- The two programs are built in their own threads, with their own
  task lists, so neither one's work bleeds into the other's.

## Where this comes from

- REBLEND DEV thread (2a82689c, 2026-11-16 17:00 EST): "Add
  scooter brushes for imported objects too that would dope,
  ididmt realize that bkender had add ons So im thinking we
  shoukd make reblend as really good as possible and then we can
  create a development suite program for my personal ise that
  will create add on packs for it".
- REBLEND DEV thread (2a82689c, 2026-11-16 17:08 EST): "If there
  is anything your ve already got planned or buikt that should
  he considered an add on please seperste as such so we dont
  over bloat replenish as a good base program does thisbmake
  sense? Exactly like blender feel me?" The plan went from 43
  tasks to 40 when the add-on material was separated out. The
  same turn ordered a new chat for the REBLEND ADDON DEV SUITE.
- Found in the seventh BNB delta scan (2026-11-17). One
  in-window instance, Joshua-ordered, with the add-on suite
  already building in its own thread.
