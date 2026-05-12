# Agent Instructions

## Documentation

Local HTML documentation is **not tracked in git** (too large). Before answering
questions about Blender features or the Python API, check if the docs are present:

```
blender_manual_html/        ← Blender manual (v5.1)
blender_python_reference_5_1/  ← Python API reference (v5.1)
```

If either directory is missing, warn the user:

> "Local documentation not found. Download the Blender manual and Python API
> reference and place them at the repo root as `blender_manual_html/` and
> `blender_python_reference_5_1/`. See `index.md` for the expected structure."

A navigation index for both doc sets is at `index.md`.

## MCP Server

The MCP server and addon live in `mcp/`. Install the addon into Blender by running:

```bash
blender --background --python install_mcp_addon.py
```

The MCP server has its own bundled RST docs at `mcp/mcp/blmcp/data/` — these are
used by the MCP tools and are always available regardless of the HTML docs above.

## Upstreams

| Remote | Source |
|--------|--------|
| `upstream-blender` | github.com/blender/blender |
| `upstream-mcp` | projects.blender.org/lab/blender_mcp |

To sync Blender source updates:
```bash
git fetch upstream-blender
git merge upstream-blender/main
```

To sync MCP updates:
```bash
git fetch upstream-mcp
git checkout upstream-mcp/main -- mcp/
git commit -m "Sync mcp/ from upstream"
```

## Binary Assets

Binary assets (`.blend`, `.png`, textures, compiled libs) are excluded from git.
The Blender build system fetches them via:

```bash
make update
```
