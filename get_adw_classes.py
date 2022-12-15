"""Get GTK Classes"""

# pylint: disable=wrong-import-position
# pylint: disable=no-member
# pylint: disable=eval-used

import gi

gi.require_version("Adw", "1")
from gi.repository import Adw

# widget_dir = dir(Adw.Widget)

with open("adw_proplist.md", "w", encoding="utf-8") as f:
    print("<!-- markdownlint-disable no-inline-html -->", file=f)
    print("<!-- markdownlint-disable no-multiple-blanks -->", file=f)
    print("<!-- markdownlint-disable no-trailing-spaces -->", file=f)
    print("# Adw Class Signals and Properties List", file=f)
    adw_items = dir(Adw)
    for item in adw_items:
        adw_item = eval(f"Adw.{item}")
        if isinstance(eval(f"Adw.{item}"), gi.types.GObjectMeta):
            if hasattr(adw_item, "__gdoc__"):
                thedoc = repr(adw_item.__gdoc__)
            else:
                thedoc = repr(adw_item.__doc__)
            thedoc = thedoc.replace("'", "")
            thedoc = thedoc.replace("\\n", "\r\n    ")

            print(
                f"\r\n<details><summary>Adw.{item}</summary>\r\n\r\n"
                f"{thedoc}\r\n\r\n---\r\n",
                file=f,
            )
            print("\r\n</details>", file=f)
