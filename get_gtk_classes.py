"""Get GTK Classes"""

# pylint: disable=wrong-import-position
# pylint: disable=no-member
# pylint: disable=eval-used

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
            print(f"\r\n<details><summary>Gtk.{item}</summary>\r\n\r\n---\r\n", file=f)
            proplist = dir(gtk_item)
            for propitem in proplist:
                print(f"- {propitem}", file=f)
            print("\r\n</details>", file=f)
