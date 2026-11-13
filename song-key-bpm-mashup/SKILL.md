# S41 — Song key and BPM lookup with mashup compatibility

> Twin tool: [song-key-bpm-lookup (T17)](https://github.com/BROKE-N-BORED/BNB-TOOLS/tree/main/song-key-bpm-lookup) — key/BPM lookup plus mashup-compatibility math.

## When to use

- Use it when the user wants to know whether a list of songs can be mashed up or mixed together.

- Use it when a set needs a key and tempo plan before anyone opens a DAW.

- Do not use it to pick the songs; the user brings the list.

## Look up key and BPM for every song

- Take the song list as title plus artist; never guess which version or recording the user means.

- Look up the key and BPM for every song on the list and record them in a table.

- When sources disagree on a song's key or BPM, record the disagreement instead of picking one silently.

## Find the key family

- Group the songs by key family: songs in the same key, and songs in relative major/minor pairs, belong together.

- Name which songs share a family and which stand alone.

- A song outside the family is not a failure; it is a candidate for a shift or its own section.

## Pick a BPM anchor with minimal stretches

- Pick a BPM anchor — the tempo the mashup will run at — that keeps every song's stretch as small as possible.

- Prefer the tempo most songs already sit near; a big stretch on every track is a bad anchor.

- Record the stretch each song needs to reach the anchor.

## Work out the semitone shift for outliers

- For a song outside the key family, work out the semitone shift that would bring it into key.

- If the shift is small, name it as part of the plan; if it is large, flag the song as its own section or a key change instead.

- Show the shift math in the verdict so the user can check it.

## Report the verdict

- Report the key/BPM table, the key-family grouping, the BPM anchor with each song's stretch, and the shift math for outliers.

- Give a plain compatibility verdict: which songs mash cleanly, which need a shift, and which belong in their own section.

- Example shape from the proven run: a 146 BPM anchor with one song shifted +4 semitones into B minor.

## Standing rules

- Never claim more than was checked; a looked-up key is only as good as its source, and disagreements get recorded.

- Measure, do not eyeball; the verdict comes from the table, not from a feeling that two songs go together.

- Hard $0: use only free lookup sources.

## Where this comes from

- Proven in the Key and BPM for songs thread (Tomorrow, Alive, Plush): 146 BPM anchor, Plush +4 semitones to B minor — recorded in the BNB audit as S41.
