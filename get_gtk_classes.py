"""Get GTK Classes"""

# pylint: disable=wrong-import-position
# pylint: disable=no-member
# pylint: disable=eval-used

import gi

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk

widget_dir = dir(Gtk.Widget)

with open("proplist.md", "w", encoding="utf-8") as f:
    print("<!-- markdownlint-disable no-inline-html -->", file=f)
    print("<!-- markdownlint-disable no-multiple-blanks -->", file=f)
    print("<!-- markdownlint-disable no-trailing-spaces -->", file=f)
    print("# Gtk Class List", file=f)
    print(
        "\r\nIf class derived from Gtk.Widget, properties from Gtk.Widget are omitted.\r\n\r\n---",
        file=f,
    )
    gtk_items = dir(Gtk)
    for item in gtk_items:
        gtk_item = eval(f"Gtk.{item}")
        if isinstance(eval(f"Gtk.{item}"), gi.types.GObjectMeta):
            if hasattr(gtk_item, "__gdoc__"):
                thedoc = repr(gtk_item.__gdoc__)
            else:
                thedoc = repr(gtk_item.__doc__)
            thedoc = thedoc.replace("'", "")
            thedoc = thedoc.replace("\\n", "\r\n    ")

            print(
                f"\r\n<details><summary>Gtk.{item}</summary>\r\n\r\n"
                f"{thedoc}\r\n\r\n---\r\n",
                file=f,
            )
            # proplist = dir(gtk_item)
            # derived_from_widget = "Gtk.Widget" in thedoc
            # for propitem in proplist:
            #     if propitem not in widget_dir or not derived_from_widget:
            #         print(f"- {propitem}", file=f)
            print("\r\n</details>", file=f)
