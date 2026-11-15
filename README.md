# Illustrious Tag Converter

Offline prototype for converting Traditional Chinese / English descriptions into **candidate Danbooru-style tags** for Illustrious image generation.

## Run

Requires Python 3.10+ and Tkinter (included with most Windows Python installations).

```powershell
python app.py
```

No API key or external packages required.

## Example

Input: `黑色長髮的女孩，穿著和服，微笑，看著鏡頭`

Output: `1girl, long_hair, black_hair, kimono, smile, looking_at_viewer`

## Tests

```powershell
python -m unittest discover -s tests
```

## Limitations

- Small rule-based vocabulary, not an LLM.
- Candidate tags are **not validated** against Danbooru.
- Negation, complex relationships, and unrecognized terms may be missed.
- No guarantee that every candidate tag is effective for a given Illustrious checkpoint.

## Planned

Danbooru tag validation, LM Studio local LLM support, unknown-term reporting, ComfyUI export.
