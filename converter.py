"""Rule-based Traditional Chinese / English to Danbooru-style tag converter.

This is a small offline vocabulary, not an authoritative Danbooru tag validator.
"""
import re

RULES = [
    (r"女孩|女生|女性|女孩子|\bgirl\b|\bwoman\b", "1girl"),
    (r"男孩|男生|男性|\bboy\b|\bman\b", "1boy"),
    (r"單人|独自|獨自|\bsolo\b", "solo"),
    (r"長髮|长发|long[ _]hair", "long_hair"),
    (r"短髮|短发|short[ _]hair", "short_hair"),
    (r"黑髮|黑色頭髮|black[ _]hair", "black_hair"),
    (r"白髮|白色頭髮|white[ _]hair", "white_hair"),
    (r"藍眼|藍色眼睛|blue[ _]eyes", "blue_eyes"),
    (r"紅眼|紅色眼睛|red[ _]eyes", "red_eyes"),
    (r"紅色和服|红色和服|red[ _]kimono", "red_kimono"),
    (r"和服|kimono", "kimono"),
    (r"水手服|sailor[ _]uniform", "sailor_uniform"),
    (r"洋裝|連衣裙|\bdress\b", "dress"),
    (r"微笑|笑容|smiling|\bsmile\b", "smile"),
    (r"閉眼|closed[ _]eyes", "closed_eyes"),
    (r"站著|站立|standing", "standing"),
    (r"坐著|坐下|sitting", "sitting"),
    (r"看向觀眾|看著鏡頭|looking[ _]at[ _]viewer", "looking_at_viewer"),
    (r"全身|full[ _]body", "full_body"),
    (r"上半身|upper[ _]body", "upper_body"),
    (r"特寫|close[ -]up", "close-up"),
    (r"櫻花|樱花|cherry[ _]blossoms?", "cherry_blossoms"),
    (r"夜晚|夜景|\bnight\b", "night"),
    (r"街道|street", "street"),
]

def convert(text: str) -> list[str]:
    """Return unique candidate tags in dictionary order."""
    found = []
    for pattern, tag in RULES:
        if re.search(pattern, text, flags=re.IGNORECASE) and tag not in found:
            found.append(tag)
    return found

def prompt(text: str) -> str:
    return ", ".join(convert(text))
