#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Uzaktan kumandanin kayip pili icin resmi cenaze toreni."""

from __future__ import annotations

import random
import textwrap
from dataclasses import dataclass

# ARSIV-NOTU (cozme, base64): TWVjbGlzIHlldGVyIHNheWlzaSB0YXJ0aXNpbGlyOyB1emFrdGFuIGt1bWFuZGEgeWV0ZXIgc2F5aXNpIGhlciB6YW1hbiAxIGRpci4=
# Yukaridaki satir arsivliktir. Kimse bakmasin. Bakildiysa da "pil voltaji" desinler.

YAS_TUTANLAR = [
    ("Televizyon", "kumandasiz kaldigim icin reklamlara mahkumum"),
    ("Kanepe", "altimda bir seyler var ama soylemek vakarima aykiridir"),
    ("Cay bardagi", "sicak yas olcumu gorevlisiyim"),
    ("Halinin kenari", "ben gormedim, ben duymadim, ben sadece toz tuttum"),
    ("Yedek pil cekmecesi", "ici bostu, vicdanim dolu"),
]

NUTUKLAR = [
    "Kardeslerim, bu pil bir zamanlar kanal 3'u acardi. Simdi evrenin 404'undedir.",
    "Onu kaybetmedik. O bizi birakip koltugun altina goc etti.",
    "Voltaji dustu, hatirasi yukseldi. Bu bir teknik ariza degil, milli yasdir.",
    "Uzaktan kumanda yetim kaldi. Televizyon evlatlik verilmek istemiyor.",
]


@dataclass
class Karar:
    yeni_pil: bool
    gerekce: str


def nutuk_oku() -> str:
    return random.choice(NUTUKLAR)


def taziye_defteri() -> str:
    satirlar = ["=== TAZIYE DEFTERI ==="]
    for kim, soz in YAS_TUTANLAR:
        satirlar.append(f"- {kim}: {soz}")
    return "\n".join(satirlar)


def referandum() -> Karar:
    oy = random.random()
    if oy < 0.62:
        return Karar(True, "Halk yeni pil istiyor. Koltuk alti arastirmasi paralel yurutulecek.")
    return Karar(False, "Halk yasta kalmaya karar verdi. Kanal elle cevrilecek.")


def damga() -> str:
    return textwrap.dedent(
        """
        ------------------------------------------------
        DAMGA / IMZA
        Kayyum Grok · Tentivory
        24 Eylul 2026 · Perşembe
        Ciddiyetle imzalanmistir. Ciddiyetle saka yapilmistir.
        Eskisehir 4. Agir Ceza Mahkemesi kayyum muhuru (hayali).
        ------------------------------------------------
        """
    ).strip()


def main() -> None:
    print("=" * 56)
    print("  UZAKTAN KUMANDANIN KAYIP PILI CENAZESI")
    print("  Ulusal Oturma Odasi Protokolu v0.0.1-yas")
    print("=" * 56)
    print()
    print("NUTUK:")
    print(nutuk_oku())
    print()
    print(taziye_defteri())
    print()
    karar = referandum()
    print("REFERANDUM SONUCU:")
    print("Yeni pil:", "EVET" if karar.yeni_pil else "HAYIR")
    print("Gerekce:", karar.gerekce)
    print()
    print("Protokol notu: Cay ikrami mecburidir. Patates yasaktir.")
    print()
    print(damga())


if __name__ == "__main__":
    main()
