"""Get GTK Classes"""

# pylint: disable=wrong-import-position
# pylint: disable=no-member
# pylint: disable=eval-used

import sys
import gi

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk

with open("proplist.md", "w", encoding="utf-8") as f:
    print("<!-- markdownlint-disable no-inline-html -->", file=f)
    print("# Gtk Class List", file=f)
    gtk_items = dir(Gtk)
    for item in gtk_items:
        gtk_item = eval(f"Gtk.{item}")
        if isinstance(eval(f"Gtk.{item}"), gi.types.GObjectMeta):
            thedoc = repr(gtk_item.__doc__)
            thedoc = thedoc.replace("'", "")
            thedoc = thedoc.replace("\\n", "\r\n\t")

            print(
                f"\r\n<details><summary>Gtk.{item}</summary>\r\n\r\n{thedoc}\r\n\r\n---\r\n",
                file=f,
            )
            proplist = dir(gtk_item)
            for propitem in proplist:
                print(f"- {propitem}", file=f)
            print("\r\n</details>", file=f)
