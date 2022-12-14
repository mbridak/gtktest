"""Get GTK Classes"""

# pylint: disable=wrong-import-position
# pylint: disable=no-member
# pylint: disable=eval-used

import gi

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk

with open("proplist.md", "w", encoding="utf-8") as f:
    print("# Gtk Class List\r\n", file=f)
    gtk_items = dir(Gtk)
    for item in gtk_items:
        gtk_item = eval(f"Gtk.{item}")
        if isinstance(eval(f"Gtk.{item}"), gi.types.GObjectMeta):
            print(f"\r\n<details><summary>Gtk.{item}</summary><hr>\r\n", file=f)
            proplist = dir(gtk_item)
            for propitem in proplist:
                print(f"* {propitem}", file=f)
            print("</details>", file=f)
