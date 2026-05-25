# Turtle Generative Art

Generative art with turtle graphics. Runnable scripts live in `paper/`; each one produces an `.svg` file saved in the `Drawings` folder, a sibling of this project's root.

## Folder structure

This repository (`Code`) should sit inside a parent folder alongside `Drawings`:

```
Turtle Graphics/          (parent folder)
├── Code/                 (this repository)
└── Drawings/             (SVG output — create it if missing)
```

Scripts write to `../Drawings/` relative to the `Code` root.

## Setup (one-time)

From the `Code` root:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

On Windows, activate the venv with `.venv\Scripts\activate`.

## Running a script

1. Activate the virtual environment (`source .venv/bin/activate`).
2. From the `Code` root, run the script as a module:

```bash
python -m paper.<module_name>
```

`<module_name>` is the filename in `paper/` without the `.py` extension.

### Available scripts

| Command | Output in `Drawings/` |
|---------|------------------------|
| `python -m paper.basic` | `basic_paper.svg` |
| `python -m paper.circles_and_triangles` | `circles_and_triangles.svg` |
| `python -m paper.attractor` | `lorenz_attractor.svg` |
| `python -m paper.henon_attractor` | `henon.svg` |
| `python -m paper.l_system_algae` | `algae_l_system.svg` |
| `python -m paper.penrose_kite` | `penrose_kite_9.svg` |
| `python -m paper.random_plane_filling` | `random_plane_filling.svg` (+ `random_plane_filling.txt` with stats) |
| `python -m paper.strange_dodecahedron` | `strange_dodecahedron.svg` |

Example:

```bash
python -m paper.basic
```

After it runs, the console prints a message like `Saved: …` and the `.svg` file appears in `Drawings/`.
