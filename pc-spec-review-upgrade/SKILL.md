# S51 — PC spec review and compatible upgrade shortlist

**Status: Tier 3, weak. The lowest-priority skill in this repo. The spec-to-bottleneck analysis is the only new bit here. Product search and comparison already live in the system shopping skill, so use that for the shopping half and keep this skill to the analysis.**

## When to use

- Use this skill when the user hands over a PC spec file and asks what is slow, what can be upgraded, and what parts to buy.

- Use it for one named machine at a time, with its exact model on record.

## Read the spec and record the machine

- Read the spec file and record the machine: make, exact model, CPU, RAM amount and channel layout, storage type and size, and any expansion slots listed.

- Keep the exact model on record. The upgrade path depends on the exact model, not the product line.

## Name the real bottlenecks

- Name the parts that actually slow the machine down, from the spec, not from a guess.

- Call out a spinning hard drive as a bottleneck when the machine still boots and loads from one.

- Call out single-channel RAM when the machine has one stick instead of a matched pair.

- Rank the bottlenecks by how much each one holds the machine back.

## Check the exact model's upgrade path

- Check what the exact model can actually take before naming any part.

- Look for an empty M.2 2280 socket and say whether the machine has one.

- Say what speed a faster drive will actually run at on that machine. A Gen4 drive in a Gen3 slot runs at Gen3 speed, so the user should not pay for speed the machine cannot use.

- Check RAM the same way: slots, maximum supported, and whether a second stick would give dual channel.

## Find the cheapest compatible parts

- Search across stores for the cheapest part that fits the machine.

- Give a compatibility verdict per item: fits, fits with a caveat, or does not fit, with the reason in each case.

- Name the cheapest compatible option per upgrade, and say what the user gives up by picking the cheapest one.

- Do not recommend a part whose compatibility you could not verify.

## Where this comes from

- Distilled from the "Linux Mint PC specifications" thread (d81cbb00) in the 2026-11-12 audit: a spec review of an HP All-in-One 22-df0xxx (Ryzen 3 3250U, 8 GB single-stick, 1 TB HDD) that named the bottlenecks and shortlisted the cheapest compatible NVMe upgrade for its empty M.2 2280 socket.

## Alternatives for better results

- Use the system shopping skill for the product search and comparison half of the job, and keep this skill to the spec-to-bottleneck analysis.

- Offer to re-run the review after the user installs an upgrade, since the bottleneck ranking changes once the slowest part is gone.
