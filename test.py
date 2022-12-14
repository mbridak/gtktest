import gi

gi.require_version("Gtk", "4.0")
gi.require_version("GLib", "2.0")
from gi.repository import Gtk, GLib

widget = Gtk.Widget()
window = Gtk.ApplicationWindow()
box = Gtk.Box()
label = Gtk.Label()
entry = Gtk.Entry()
frame = Gtk.Frame()
infobar = Gtk.InfoBar()
button = Gtk.Button()
image = Gtk.Image()

items = {
    widget: "Gtk.Widget",
    window: "Gtk.ApplicationWindow",
    box: "Gtk.Box",
    label: "Gtk.Label",
    entry: "Gtk.Entry",
    frame: "Gtk.Frame",
    infobar: "Gtk.InfoBar",
    button: "Gtk.Button",
    image: "Gtk.Image",
}


with open("proplist.md", "w", encoding="utf-8") as f:
    print("# Property List\r\n", file=f)
    for item in items:
        proplist = dir(item)
        print(f"\r\n## {items.get(item)}\r\n", file=f)
        for propitem in proplist:
            print(f"* {propitem}", file=f)
