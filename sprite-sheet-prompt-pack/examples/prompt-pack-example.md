# Prompt pack example — <character>

Replace the bracketed details with the real character design. Paste the
lock block unchanged before every prompt. Keep the same model and seed
for every generation.

## Character-lock block

```
<Character name>, <species / type>, <height and build>, <primary colors>,
<clothing and gear in detail>, <distinctive features>, <art style>,
<fixed proportions and silhouette notes>
```

## Model and seed

- Model: <model name>
- Seed: <seed number>

## Per-action prompts (the reliable route)

### Idle

```
<lock block>

Standing idle, facing forward, arms relaxed at sides, full body,
pixel-art sprite sheet frame, plain background.
```

### Walk

```
<lock block>

Mid-stride walking pose, one foot forward, arms swinging, full body,
pixel-art sprite sheet frame, plain background.
```

### Attack

```
<lock block>

Attack pose, <weapon / action> extended, dynamic stance, full body,
pixel-art sprite sheet frame, plain background.
```

<!-- Add one block per action the game needs. -->

## Master one-shot prompt (hit-or-miss)

```
<lock block>

Full sprite sheet showing every action — idle, walk, attack, <...>
— in a grid, same character in every cell, pixel art, plain background.
```

Flag to the user: the one-shot is hit-or-miss. Per-action strips above
are the reliable route.
