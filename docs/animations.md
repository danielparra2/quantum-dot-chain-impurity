# Animations and analogies

All clips come from the thesis defense material or from COMSOL. They were
re-encoded to keep the repository light: max width 360–800 px, 12–15 fps,
reduced palette, looping.

## Scientific animations

| File | What it shows | Source | Size |
|---|---|---|---|
| `figures/animations/field_battery_devil.gif` | A battery applies an electric field; the electron is dragged across the chain and the induced dipole flips. | Defense animation (`image7.gif`) | 472 KB |
| `figures/animations/field_quantified.gif` | Same process with the numerical plateau `p₁ = −15.00` displayed. | Defense animation (`image96.gif`) | 519 KB |
| `figures/animations/wavefunction_localization.gif` | Probability density following the impurity along the uniform chain. | COMSOL export (`probando.gif`) | 128 KB |
| `figures/animations/wavefunction_r50.gif` | Wavefunction at `R₅ = 50 nm`: the enlarged fifth dot takes the electron. | COMSOL export (`hh.gif`) | 142 KB |

## Cartoon analogies

These are the analogies used in the defense. They are included for context;
the scientific content is in the figures and notebooks.

| File | Analogy | Size |
|---|---|---|
| `figures/animations/donor_acceptor_battle.gif` | The fifth dot as a donor or an acceptor: who keeps the electron? | 1.7 MB |
| `figures/animations/magician.gif` | The magnifying-glass analogy for localization. | 435 KB |
| `figures/analogies/tasmanian_devil.jpg` | Dimensionality: from bulk to a zero-dimensional dot. | 321 KB |
| `figures/analogies/dimensionality.jpg` | Blocks in 3D, 2D, 1D and 0D. | 160 KB |
| `figures/animations/quantum_cat.gif` | Easter egg: a cat-shaped eigenmode. | 3.1 MB |

## How the clips were produced

1. Export the frames from COMSOL (or take the original defense clip).
2. Re-encode with `ffmpeg` or Pillow: reduce fps, resize, quantize the palette.
3. Keep the loop short (2–5 s) and the file below ~3 MB for the README.

The raw COMSOL clips are kept in the working folder and are not part of the
repository. The raw `.mph` models are not included either; the exported `.txt`
files are the reproducible data.

## Third-party material

Some cartoon stills (Tasmanian devil, magnifying glass, Homer) are third-party
imagery used as analogies in the defense. They are **not** covered by the CC BY
license of the original figures. If you reuse this repository, replace them or
remove them.
