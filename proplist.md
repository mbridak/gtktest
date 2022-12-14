<!-- markdownlint-disable no-inline-html -->
<!-- markdownlint-disable no-multiple-blanks -->
<!-- markdownlint-disable no-trailing-spaces -->
# Gtk Class List

If class derived from Gtk.Widget, properties from Gtk.Widget are omitted.

---

<details><summary>Gtk.ATContext</summary>

Object GtkATContext
    
    Signals from GtkATContext:
      state-change ()
    
    Properties from GtkATContext:
      accessible-role -> GtkAccessibleRole: accessible-role
      accessible -> GtkAccessible: accessible
      display -> GdkDisplay: display
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.AboutDialog</summary>

Object GtkAboutDialog
    
    Signals from GtkAboutDialog:
      activate-link (gchararray) -> gboolean
    
    Properties from GtkAboutDialog:
      program-name -> gchararray: program-name
      version -> gchararray: version
      copyright -> gchararray: copyright
      comments -> gchararray: comments
      website -> gchararray: website
      website-label -> gchararray: website-label
      license -> gchararray: license
      system-information -> gchararray: system-information
      authors -> GStrv: authors
      documenters -> GStrv: documenters
      translator-credits -> gchararray: translator-credits
      artists -> GStrv: artists
      logo -> GdkPaintable: logo
      logo-icon-name -> gchararray: logo-icon-name
      wrap-license -> gboolean: wrap-license
      license-type -> GtkLicense: license-type
    
    Signals from GtkWindow:
      activate-focus ()
      activate-default ()
      keys-changed ()
      enable-debugging (gboolean) -> gboolean
      close-request () -> gboolean
    
    Properties from GtkWindow:
      title -> gchararray: title
      resizable -> gboolean: resizable
      modal -> gboolean: modal
      default-width -> gint: default-width
      default-height -> gint: default-height
      destroy-with-parent -> gboolean: destroy-with-parent
      hide-on-close -> gboolean: hide-on-close
      icon-name -> gchararray: icon-name
      display -> GdkDisplay: display
      decorated -> gboolean: decorated
      deletable -> gboolean: deletable
      transient-for -> GtkWindow: transient-for
      application -> GtkApplication: application
      default-widget -> GtkWidget: default-widget
      focus-widget -> GtkWidget: focus-widget
      child -> GtkWidget: child
      titlebar -> GtkWidget: titlebar
      handle-menubar-accel -> gboolean: handle-menubar-accel
      is-active -> gboolean: is-active
      startup-id -> gchararray: startup-id
      mnemonics-visible -> gboolean: mnemonics-visible
      focus-visible -> gboolean: focus-visible
      maximized -> gboolean: maximized
      fullscreened -> gboolean: fullscreened
    
    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
    
    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.Accessible</summary>

Interface GtkAccessible
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.ActionBar</summary>

Object GtkActionBar
    
    Properties from GtkActionBar:
      revealed -> gboolean: revealed
    
    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
    
    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.Actionable</summary>

Interface GtkActionable
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.ActivateAction</summary>

Object GtkActivateAction
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.Adjustment</summary>

Object GtkAdjustment
    
    Signals from GtkAdjustment:
      changed ()
      value-changed ()
    
    Properties from GtkAdjustment:
      value -> gdouble: value
      lower -> gdouble: lower
      upper -> gdouble: upper
      step-increment -> gdouble: step-increment
      page-increment -> gdouble: page-increment
      page-size -> gdouble: page-size
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.AlternativeTrigger</summary>

Object GtkAlternativeTrigger
    
    Properties from GtkAlternativeTrigger:
      first -> GtkShortcutTrigger: first
      second -> GtkShortcutTrigger: second
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.AnyFilter</summary>

Object GtkAnyFilter
    
    Signals from GListModel:
      items-changed (guint, guint, guint)
    
    Properties from GtkMultiFilter:
      item-type -> GType: item-type
      n-items -> guint: n-items
    
    Signals from GListModel:
      items-changed (guint, guint, guint)
    
    Signals from GtkFilter:
      changed (GtkFilterChange)
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.AppChooser</summary>

Interface GtkAppChooser
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.AppChooserButton</summary>

Object GtkAppChooserButton
    
    Signals from GtkAppChooserButton:
      changed ()
      custom-item-activated (gchararray)
      activate ()
    
    Properties from GtkAppChooserButton:
      show-dialog-item -> gboolean: show-dialog-item
      show-default-item -> gboolean: show-default-item
      heading -> gchararray: heading
      modal -> gboolean: modal
    
    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
    
    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.AppChooserDialog</summary>

Object GtkAppChooserDialog
    
    Properties from GtkAppChooserDialog:
      gfile -> GFile: gfile
      heading -> gchararray: heading
    
    Signals from GtkDialog:
      response (gint)
      close ()
    
    Properties from GtkDialog:
      use-header-bar -> gint: use-header-bar
    
    Signals from GtkWindow:
      activate-focus ()
      activate-default ()
      keys-changed ()
      enable-debugging (gboolean) -> gboolean
      close-request () -> gboolean
    
    Properties from GtkWindow:
      title -> gchararray: title
      resizable -> gboolean: resizable
      modal -> gboolean: modal
      default-width -> gint: default-width
      default-height -> gint: default-height
      destroy-with-parent -> gboolean: destroy-with-parent
      hide-on-close -> gboolean: hide-on-close
      icon-name -> gchararray: icon-name
      display -> GdkDisplay: display
      decorated -> gboolean: decorated
      deletable -> gboolean: deletable
      transient-for -> GtkWindow: transient-for
      application -> GtkApplication: application
      default-widget -> GtkWidget: default-widget
      focus-widget -> GtkWidget: focus-widget
      child -> GtkWidget: child
      titlebar -> GtkWidget: titlebar
      handle-menubar-accel -> gboolean: handle-menubar-accel
      is-active -> gboolean: is-active
      startup-id -> gchararray: startup-id
      mnemonics-visible -> gboolean: mnemonics-visible
      focus-visible -> gboolean: focus-visible
      maximized -> gboolean: maximized
      fullscreened -> gboolean: fullscreened
    
    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
    
    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.AppChooserWidget</summary>

Object GtkAppChooserWidget
    
    Signals from GtkAppChooserWidget:
      application-selected (GAppInfo)
      application-activated (GAppInfo)
    
    Properties from GtkAppChooserWidget:
      show-default -> gboolean: show-default
      show-recommended -> gboolean: show-recommended
      show-fallback -> gboolean: show-fallback
      show-other -> gboolean: show-other
      show-all -> gboolean: show-all
      default-text -> gchararray: default-text
    
    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
    
    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.Application</summary>

Object GtkApplication
    
    Signals from GtkApplication:
      window-added (GtkWindow)
      window-removed (GtkWindow)
      query-end ()
    
    Properties from GtkApplication:
      register-session -> gboolean: register-session
      screensaver-active -> gboolean: screensaver-active
      menubar -> GMenuModel: menubar
      active-window -> GtkWindow: active-window
    
    Signals from GActionGroup:
      action-added (gchararray)
      action-removed (gchararray)
      action-enabled-changed (gchararray, gboolean)
      action-state-changed (gchararray, GVariant)
    
    Signals from GApplication:
      activate ()
      startup ()
      shutdown ()
      open (gpointer, gint, gchararray)
      command-line (GApplicationCommandLine) -> gint
      handle-local-options (GVariantDict) -> gint
      name-lost () -> gboolean
    
    Properties from GApplication:
      application-id -> gchararray: Application identifier
        The unique identifier for the application
      flags -> GApplicationFlags: Application flags
        Flags specifying the behaviour of the application
      resource-base-path -> gchararray: Resource base path
        The base resource path for the application
      is-registered -> gboolean: Is registered
        If g_application_register() has been called
      is-remote -> gboolean: Is remote
        If this application instance is remote
      inactivity-timeout -> guint: Inactivity timeout
        Time (ms) to stay alive after becoming idle
      action-group -> GActionGroup: Action group
        The group of actions that the application exports
      is-busy -> gboolean: Is busy
        If this application is currently marked busy
    
    Signals from GActionGroup:
      action-added (gchararray)
      action-removed (gchararray)
      action-enabled-changed (gchararray, gboolean)
      action-state-changed (gchararray, GVariant)
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.ApplicationWindow</summary>

Object GtkApplicationWindow
    
    Properties from GtkApplicationWindow:
      show-menubar -> gboolean: show-menubar
    
    Signals from GActionGroup:
      action-added (gchararray)
      action-removed (gchararray)
      action-enabled-changed (gchararray, gboolean)
      action-state-changed (gchararray, GVariant)
    
    Signals from GtkWindow:
      activate-focus ()
      activate-default ()
      keys-changed ()
      enable-debugging (gboolean) -> gboolean
      close-request () -> gboolean
    
    Properties from GtkWindow:
      title -> gchararray: title
      resizable -> gboolean: resizable
      modal -> gboolean: modal
      default-width -> gint: default-width
      default-height -> gint: default-height
      destroy-with-parent -> gboolean: destroy-with-parent
      hide-on-close -> gboolean: hide-on-close
      icon-name -> gchararray: icon-name
      display -> GdkDisplay: display
      decorated -> gboolean: decorated
      deletable -> gboolean: deletable
      transient-for -> GtkWindow: transient-for
      application -> GtkApplication: application
      default-widget -> GtkWidget: default-widget
      focus-widget -> GtkWidget: focus-widget
      child -> GtkWidget: child
      titlebar -> GtkWidget: titlebar
      handle-menubar-accel -> gboolean: handle-menubar-accel
      is-active -> gboolean: is-active
      startup-id -> gchararray: startup-id
      mnemonics-visible -> gboolean: mnemonics-visible
      focus-visible -> gboolean: focus-visible
      maximized -> gboolean: maximized
      fullscreened -> gboolean: fullscreened
    
    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
    
    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.AspectFrame</summary>

Object GtkAspectFrame
    
    Properties from GtkAspectFrame:
      xalign -> gfloat: xalign
      yalign -> gfloat: yalign
      ratio -> gfloat: ratio
      obey-child -> gboolean: obey-child
      child -> GtkWidget: child
    
    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
    
    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.Assistant</summary>

Object GtkAssistant
    
    Signals from GtkAssistant:
      close ()
      cancel ()
      prepare (GtkWidget)
      apply ()
      escape ()
    
    Properties from GtkAssistant:
      use-header-bar -> gint: use-header-bar
      pages -> GListModel: pages
    
    Signals from GtkWindow:
      activate-focus ()
      activate-default ()
      keys-changed ()
      enable-debugging (gboolean) -> gboolean
      close-request () -> gboolean
    
    Properties from GtkWindow:
      title -> gchararray: title
      resizable -> gboolean: resizable
      modal -> gboolean: modal
      default-width -> gint: default-width
      default-height -> gint: default-height
      destroy-with-parent -> gboolean: destroy-with-parent
      hide-on-close -> gboolean: hide-on-close
      icon-name -> gchararray: icon-name
      display -> GdkDisplay: display
      decorated -> gboolean: decorated
      deletable -> gboolean: deletable
      transient-for -> GtkWindow: transient-for
      application -> GtkApplication: application
      default-widget -> GtkWidget: default-widget
      focus-widget -> GtkWidget: focus-widget
      child -> GtkWidget: child
      titlebar -> GtkWidget: titlebar
      handle-menubar-accel -> gboolean: handle-menubar-accel
      is-active -> gboolean: is-active
      startup-id -> gchararray: startup-id
      mnemonics-visible -> gboolean: mnemonics-visible
      focus-visible -> gboolean: focus-visible
      maximized -> gboolean: maximized
      fullscreened -> gboolean: fullscreened
    
    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
    
    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.AssistantPage</summary>

Object GtkAssistantPage
    
    Properties from GtkAssistantPage:
      child -> GtkWidget: child
      page-type -> GtkAssistantPageType: page-type
      title -> gchararray: title
      complete -> gboolean: complete
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.BinLayout</summary>

Object GtkBinLayout
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.BookmarkList</summary>

Object GtkBookmarkList
    
    Properties from GtkBookmarkList:
      filename -> gchararray: filename
      attributes -> gchararray: attributes
      io-priority -> gint: io-priority
      item-type -> GType: item-type
      loading -> gboolean: loading
      n-items -> guint: n-items
    
    Signals from GListModel:
      items-changed (guint, guint, guint)
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.BoolFilter</summary>

Object GtkBoolFilter
    
    Properties from GtkBoolFilter:
      expression -> GtkExpression: expression
      invert -> gboolean: invert
    
    Signals from GtkFilter:
      changed (GtkFilterChange)
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.Box</summary>

Object GtkBox
    
    Properties from GtkBox:
      spacing -> gint: spacing
      homogeneous -> gboolean: homogeneous
      baseline-position -> GtkBaselinePosition: baseline-position
    
    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
    
    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.BoxLayout</summary>

Object GtkBoxLayout
    
    Properties from GtkBoxLayout:
      homogeneous -> gboolean: homogeneous
      spacing -> gint: spacing
      baseline-position -> GtkBaselinePosition: baseline-position
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.Buildable</summary>

Interface GtkBuildable
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.Builder</summary>

Object GtkBuilder
    
    Properties from GtkBuilder:
      current-object -> GObject: current-object
      scope -> GtkBuilderScope: scope
      translation-domain -> gchararray: translation-domain
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.BuilderCScope</summary>

Object GtkBuilderCScope
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.BuilderListItemFactory</summary>

Object GtkBuilderListItemFactory
    
    Properties from GtkBuilderListItemFactory:
      bytes -> GBytes: bytes
      resource -> gchararray: resource
      scope -> GtkBuilderScope: scope
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.BuilderScope</summary>

Interface GtkBuilderScope
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.Button</summary>

Object GtkButton
    
    Signals from GtkButton:
      activate ()
      clicked ()
    
    Properties from GtkButton:
      label -> gchararray: label
      has-frame -> gboolean: has-frame
      use-underline -> gboolean: use-underline
      icon-name -> gchararray: icon-name
      child -> GtkWidget: child
    
    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
    
    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.CClosureExpression</summary>


    :Constructors:
    
    ::
    
        CClosureExpression(**properties)
        new(value_type:GType, marshal:GObject.ClosureMarshal=None, params:list, callback_func:GObject.Callback, user_data=None) -> Gtk.CClosureExpression
    

---


</details>

<details><summary>Gtk.Calendar</summary>

Object GtkCalendar
    
    Signals from GtkCalendar:
      day-selected ()
      prev-month ()
      next-month ()
      prev-year ()
      next-year ()
    
    Properties from GtkCalendar:
      year -> gint: year
      month -> gint: month
      day -> gint: day
      show-heading -> gboolean: show-heading
      show-day-names -> gboolean: show-day-names
      show-week-numbers -> gboolean: show-week-numbers
    
    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
    
    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.CallbackAction</summary>

Object GtkCallbackAction
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.CellArea</summary>

Object GtkCellArea
    
    Signals from GtkCellArea:
      apply-attributes (GtkTreeModel, GtkTreeIter, gboolean, gboolean)
      add-editable (GtkCellRenderer, GtkCellEditable, GdkRectangle, gchararray)
      remove-editable (GtkCellRenderer, GtkCellEditable)
      focus-changed (GtkCellRenderer, gchararray)
    
    Properties from GtkCellArea:
      focus-cell -> GtkCellRenderer: focus-cell
      edited-cell -> GtkCellRenderer: edited-cell
      edit-widget -> GtkCellEditable: edit-widget
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.CellAreaBox</summary>

Object GtkCellAreaBox
    
    Properties from GtkCellAreaBox:
      spacing -> gint: spacing
    
    Signals from GtkCellArea:
      apply-attributes (GtkTreeModel, GtkTreeIter, gboolean, gboolean)
      add-editable (GtkCellRenderer, GtkCellEditable, GdkRectangle, gchararray)
      remove-editable (GtkCellRenderer, GtkCellEditable)
      focus-changed (GtkCellRenderer, gchararray)
    
    Properties from GtkCellArea:
      focus-cell -> GtkCellRenderer: focus-cell
      edited-cell -> GtkCellRenderer: edited-cell
      edit-widget -> GtkCellEditable: edit-widget
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.CellAreaContext</summary>

Object GtkCellAreaContext
    
    Properties from GtkCellAreaContext:
      area -> GtkCellArea: area
      minimum-width -> gint: minimum-width
      natural-width -> gint: natural-width
      minimum-height -> gint: minimum-height
      natural-height -> gint: natural-height
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.CellEditable</summary>

Interface GtkCellEditable
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.CellLayout</summary>

Interface GtkCellLayout
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.CellRenderer</summary>

Object GtkCellRenderer
    
    Signals from GtkCellRenderer:
      editing-canceled ()
      editing-started (GtkCellEditable, gchararray)
    
    Properties from GtkCellRenderer:
      mode -> GtkCellRendererMode: mode
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      xalign -> gfloat: xalign
      yalign -> gfloat: yalign
      xpad -> guint: xpad
      ypad -> guint: ypad
      width -> gint: width
      height -> gint: height
      is-expander -> gboolean: is-expander
      is-expanded -> gboolean: is-expanded
      cell-background -> gchararray: cell-background
      cell-background-rgba -> GdkRGBA: cell-background-rgba
      cell-background-set -> gboolean: cell-background-set
      editing -> gboolean: editing
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.CellRendererAccel</summary>

Object GtkCellRendererAccel
    
    Signals from GtkCellRendererAccel:
      accel-edited (gchararray, guint, GdkModifierType, guint)
      accel-cleared (gchararray)
    
    Properties from GtkCellRendererAccel:
      accel-key -> guint: accel-key
      accel-mods -> GdkModifierType: accel-mods
      keycode -> guint: keycode
      accel-mode -> GtkCellRendererAccelMode: accel-mode
    
    Signals from GtkCellRendererText:
      edited (gchararray, gchararray)
    
    Properties from GtkCellRendererText:
      text -> gchararray: text
      markup -> gchararray: markup
      attributes -> PangoAttrList: attributes
      single-paragraph-mode -> gboolean: single-paragraph-mode
      width-chars -> gint: width-chars
      max-width-chars -> gint: max-width-chars
      wrap-width -> gint: wrap-width
      alignment -> PangoAlignment: alignment
      placeholder-text -> gchararray: placeholder-text
      background -> gchararray: background
      foreground -> gchararray: foreground
      background-rgba -> GdkRGBA: background-rgba
      foreground-rgba -> GdkRGBA: foreground-rgba
      font -> gchararray: font
      font-desc -> PangoFontDescription: font-desc
      family -> gchararray: family
      style -> PangoStyle: style
      variant -> PangoVariant: variant
      weight -> gint: weight
      stretch -> PangoStretch: stretch
      size -> gint: size
      size-points -> gdouble: size-points
      scale -> gdouble: scale
      editable -> gboolean: editable
      strikethrough -> gboolean: strikethrough
      underline -> PangoUnderline: underline
      rise -> gint: rise
      language -> gchararray: language
      ellipsize -> PangoEllipsizeMode: ellipsize
      wrap-mode -> PangoWrapMode: wrap-mode
      background-set -> gboolean: background-set
      foreground-set -> gboolean: foreground-set
      family-set -> gboolean: family-set
      style-set -> gboolean: style-set
      variant-set -> gboolean: variant-set
      weight-set -> gboolean: weight-set
      stretch-set -> gboolean: stretch-set
      size-set -> gboolean: size-set
      scale-set -> gboolean: scale-set
      editable-set -> gboolean: editable-set
      strikethrough-set -> gboolean: strikethrough-set
      underline-set -> gboolean: underline-set
      rise-set -> gboolean: rise-set
      language-set -> gboolean: language-set
      ellipsize-set -> gboolean: ellipsize-set
      align-set -> gboolean: align-set
    
    Signals from GtkCellRenderer:
      editing-canceled ()
      editing-started (GtkCellEditable, gchararray)
    
    Properties from GtkCellRenderer:
      mode -> GtkCellRendererMode: mode
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      xalign -> gfloat: xalign
      yalign -> gfloat: yalign
      xpad -> guint: xpad
      ypad -> guint: ypad
      width -> gint: width
      height -> gint: height
      is-expander -> gboolean: is-expander
      is-expanded -> gboolean: is-expanded
      cell-background -> gchararray: cell-background
      cell-background-rgba -> GdkRGBA: cell-background-rgba
      cell-background-set -> gboolean: cell-background-set
      editing -> gboolean: editing
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.CellRendererCombo</summary>

Object GtkCellRendererCombo
    
    Signals from GtkCellRendererCombo:
      changed (gchararray, GtkTreeIter)
    
    Properties from GtkCellRendererCombo:
      model -> GtkTreeModel: model
      text-column -> gint: text-column
      has-entry -> gboolean: has-entry
    
    Signals from GtkCellRendererText:
      edited (gchararray, gchararray)
    
    Properties from GtkCellRendererText:
      text -> gchararray: text
      markup -> gchararray: markup
      attributes -> PangoAttrList: attributes
      single-paragraph-mode -> gboolean: single-paragraph-mode
      width-chars -> gint: width-chars
      max-width-chars -> gint: max-width-chars
      wrap-width -> gint: wrap-width
      alignment -> PangoAlignment: alignment
      placeholder-text -> gchararray: placeholder-text
      background -> gchararray: background
      foreground -> gchararray: foreground
      background-rgba -> GdkRGBA: background-rgba
      foreground-rgba -> GdkRGBA: foreground-rgba
      font -> gchararray: font
      font-desc -> PangoFontDescription: font-desc
      family -> gchararray: family
      style -> PangoStyle: style
      variant -> PangoVariant: variant
      weight -> gint: weight
      stretch -> PangoStretch: stretch
      size -> gint: size
      size-points -> gdouble: size-points
      scale -> gdouble: scale
      editable -> gboolean: editable
      strikethrough -> gboolean: strikethrough
      underline -> PangoUnderline: underline
      rise -> gint: rise
      language -> gchararray: language
      ellipsize -> PangoEllipsizeMode: ellipsize
      wrap-mode -> PangoWrapMode: wrap-mode
      background-set -> gboolean: background-set
      foreground-set -> gboolean: foreground-set
      family-set -> gboolean: family-set
      style-set -> gboolean: style-set
      variant-set -> gboolean: variant-set
      weight-set -> gboolean: weight-set
      stretch-set -> gboolean: stretch-set
      size-set -> gboolean: size-set
      scale-set -> gboolean: scale-set
      editable-set -> gboolean: editable-set
      strikethrough-set -> gboolean: strikethrough-set
      underline-set -> gboolean: underline-set
      rise-set -> gboolean: rise-set
      language-set -> gboolean: language-set
      ellipsize-set -> gboolean: ellipsize-set
      align-set -> gboolean: align-set
    
    Signals from GtkCellRenderer:
      editing-canceled ()
      editing-started (GtkCellEditable, gchararray)
    
    Properties from GtkCellRenderer:
      mode -> GtkCellRendererMode: mode
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      xalign -> gfloat: xalign
      yalign -> gfloat: yalign
      xpad -> guint: xpad
      ypad -> guint: ypad
      width -> gint: width
      height -> gint: height
      is-expander -> gboolean: is-expander
      is-expanded -> gboolean: is-expanded
      cell-background -> gchararray: cell-background
      cell-background-rgba -> GdkRGBA: cell-background-rgba
      cell-background-set -> gboolean: cell-background-set
      editing -> gboolean: editing
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.CellRendererPixbuf</summary>

Object GtkCellRendererPixbuf
    
    Properties from GtkCellRendererPixbuf:
      pixbuf -> GdkPixbuf: pixbuf
      pixbuf-expander-open -> GdkPixbuf: pixbuf-expander-open
      pixbuf-expander-closed -> GdkPixbuf: pixbuf-expander-closed
      texture -> GdkTexture: texture
      icon-size -> GtkIconSize: icon-size
      icon-name -> gchararray: icon-name
      gicon -> GIcon: gicon
    
    Signals from GtkCellRenderer:
      editing-canceled ()
      editing-started (GtkCellEditable, gchararray)
    
    Properties from GtkCellRenderer:
      mode -> GtkCellRendererMode: mode
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      xalign -> gfloat: xalign
      yalign -> gfloat: yalign
      xpad -> guint: xpad
      ypad -> guint: ypad
      width -> gint: width
      height -> gint: height
      is-expander -> gboolean: is-expander
      is-expanded -> gboolean: is-expanded
      cell-background -> gchararray: cell-background
      cell-background-rgba -> GdkRGBA: cell-background-rgba
      cell-background-set -> gboolean: cell-background-set
      editing -> gboolean: editing
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.CellRendererProgress</summary>

Object GtkCellRendererProgress
    
    Properties from GtkCellRendererProgress:
      value -> gint: value
      text -> gchararray: text
      pulse -> gint: pulse
      text-xalign -> gfloat: text-xalign
      text-yalign -> gfloat: text-yalign
      inverted -> gboolean: inverted
    
    Signals from GtkCellRenderer:
      editing-canceled ()
      editing-started (GtkCellEditable, gchararray)
    
    Properties from GtkCellRenderer:
      mode -> GtkCellRendererMode: mode
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      xalign -> gfloat: xalign
      yalign -> gfloat: yalign
      xpad -> guint: xpad
      ypad -> guint: ypad
      width -> gint: width
      height -> gint: height
      is-expander -> gboolean: is-expander
      is-expanded -> gboolean: is-expanded
      cell-background -> gchararray: cell-background
      cell-background-rgba -> GdkRGBA: cell-background-rgba
      cell-background-set -> gboolean: cell-background-set
      editing -> gboolean: editing
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.CellRendererSpin</summary>

Object GtkCellRendererSpin
    
    Properties from GtkCellRendererSpin:
      adjustment -> GtkAdjustment: adjustment
      climb-rate -> gdouble: climb-rate
      digits -> guint: digits
    
    Signals from GtkCellRendererText:
      edited (gchararray, gchararray)
    
    Properties from GtkCellRendererText:
      text -> gchararray: text
      markup -> gchararray: markup
      attributes -> PangoAttrList: attributes
      single-paragraph-mode -> gboolean: single-paragraph-mode
      width-chars -> gint: width-chars
      max-width-chars -> gint: max-width-chars
      wrap-width -> gint: wrap-width
      alignment -> PangoAlignment: alignment
      placeholder-text -> gchararray: placeholder-text
      background -> gchararray: background
      foreground -> gchararray: foreground
      background-rgba -> GdkRGBA: background-rgba
      foreground-rgba -> GdkRGBA: foreground-rgba
      font -> gchararray: font
      font-desc -> PangoFontDescription: font-desc
      family -> gchararray: family
      style -> PangoStyle: style
      variant -> PangoVariant: variant
      weight -> gint: weight
      stretch -> PangoStretch: stretch
      size -> gint: size
      size-points -> gdouble: size-points
      scale -> gdouble: scale
      editable -> gboolean: editable
      strikethrough -> gboolean: strikethrough
      underline -> PangoUnderline: underline
      rise -> gint: rise
      language -> gchararray: language
      ellipsize -> PangoEllipsizeMode: ellipsize
      wrap-mode -> PangoWrapMode: wrap-mode
      background-set -> gboolean: background-set
      foreground-set -> gboolean: foreground-set
      family-set -> gboolean: family-set
      style-set -> gboolean: style-set
      variant-set -> gboolean: variant-set
      weight-set -> gboolean: weight-set
      stretch-set -> gboolean: stretch-set
      size-set -> gboolean: size-set
      scale-set -> gboolean: scale-set
      editable-set -> gboolean: editable-set
      strikethrough-set -> gboolean: strikethrough-set
      underline-set -> gboolean: underline-set
      rise-set -> gboolean: rise-set
      language-set -> gboolean: language-set
      ellipsize-set -> gboolean: ellipsize-set
      align-set -> gboolean: align-set
    
    Signals from GtkCellRenderer:
      editing-canceled ()
      editing-started (GtkCellEditable, gchararray)
    
    Properties from GtkCellRenderer:
      mode -> GtkCellRendererMode: mode
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      xalign -> gfloat: xalign
      yalign -> gfloat: yalign
      xpad -> guint: xpad
      ypad -> guint: ypad
      width -> gint: width
      height -> gint: height
      is-expander -> gboolean: is-expander
      is-expanded -> gboolean: is-expanded
      cell-background -> gchararray: cell-background
      cell-background-rgba -> GdkRGBA: cell-background-rgba
      cell-background-set -> gboolean: cell-background-set
      editing -> gboolean: editing
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.CellRendererSpinner</summary>

Object GtkCellRendererSpinner
    
    Properties from GtkCellRendererSpinner:
      active -> gboolean: active
      pulse -> guint: pulse
      size -> GtkIconSize: size
    
    Signals from GtkCellRenderer:
      editing-canceled ()
      editing-started (GtkCellEditable, gchararray)
    
    Properties from GtkCellRenderer:
      mode -> GtkCellRendererMode: mode
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      xalign -> gfloat: xalign
      yalign -> gfloat: yalign
      xpad -> guint: xpad
      ypad -> guint: ypad
      width -> gint: width
      height -> gint: height
      is-expander -> gboolean: is-expander
      is-expanded -> gboolean: is-expanded
      cell-background -> gchararray: cell-background
      cell-background-rgba -> GdkRGBA: cell-background-rgba
      cell-background-set -> gboolean: cell-background-set
      editing -> gboolean: editing
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.CellRendererText</summary>

Object GtkCellRendererText
    
    Signals from GtkCellRendererText:
      edited (gchararray, gchararray)
    
    Properties from GtkCellRendererText:
      text -> gchararray: text
      markup -> gchararray: markup
      attributes -> PangoAttrList: attributes
      single-paragraph-mode -> gboolean: single-paragraph-mode
      width-chars -> gint: width-chars
      max-width-chars -> gint: max-width-chars
      wrap-width -> gint: wrap-width
      alignment -> PangoAlignment: alignment
      placeholder-text -> gchararray: placeholder-text
      background -> gchararray: background
      foreground -> gchararray: foreground
      background-rgba -> GdkRGBA: background-rgba
      foreground-rgba -> GdkRGBA: foreground-rgba
      font -> gchararray: font
      font-desc -> PangoFontDescription: font-desc
      family -> gchararray: family
      style -> PangoStyle: style
      variant -> PangoVariant: variant
      weight -> gint: weight
      stretch -> PangoStretch: stretch
      size -> gint: size
      size-points -> gdouble: size-points
      scale -> gdouble: scale
      editable -> gboolean: editable
      strikethrough -> gboolean: strikethrough
      underline -> PangoUnderline: underline
      rise -> gint: rise
      language -> gchararray: language
      ellipsize -> PangoEllipsizeMode: ellipsize
      wrap-mode -> PangoWrapMode: wrap-mode
      background-set -> gboolean: background-set
      foreground-set -> gboolean: foreground-set
      family-set -> gboolean: family-set
      style-set -> gboolean: style-set
      variant-set -> gboolean: variant-set
      weight-set -> gboolean: weight-set
      stretch-set -> gboolean: stretch-set
      size-set -> gboolean: size-set
      scale-set -> gboolean: scale-set
      editable-set -> gboolean: editable-set
      strikethrough-set -> gboolean: strikethrough-set
      underline-set -> gboolean: underline-set
      rise-set -> gboolean: rise-set
      language-set -> gboolean: language-set
      ellipsize-set -> gboolean: ellipsize-set
      align-set -> gboolean: align-set
    
    Signals from GtkCellRenderer:
      editing-canceled ()
      editing-started (GtkCellEditable, gchararray)
    
    Properties from GtkCellRenderer:
      mode -> GtkCellRendererMode: mode
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      xalign -> gfloat: xalign
      yalign -> gfloat: yalign
      xpad -> guint: xpad
      ypad -> guint: ypad
      width -> gint: width
      height -> gint: height
      is-expander -> gboolean: is-expander
      is-expanded -> gboolean: is-expanded
      cell-background -> gchararray: cell-background
      cell-background-rgba -> GdkRGBA: cell-background-rgba
      cell-background-set -> gboolean: cell-background-set
      editing -> gboolean: editing
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.CellRendererToggle</summary>

Object GtkCellRendererToggle
    
    Signals from GtkCellRendererToggle:
      toggled (gchararray)
    
    Properties from GtkCellRendererToggle:
      activatable -> gboolean: activatable
      active -> gboolean: active
      radio -> gboolean: radio
      inconsistent -> gboolean: inconsistent
    
    Signals from GtkCellRenderer:
      editing-canceled ()
      editing-started (GtkCellEditable, gchararray)
    
    Properties from GtkCellRenderer:
      mode -> GtkCellRendererMode: mode
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      xalign -> gfloat: xalign
      yalign -> gfloat: yalign
      xpad -> guint: xpad
      ypad -> guint: ypad
      width -> gint: width
      height -> gint: height
      is-expander -> gboolean: is-expander
      is-expanded -> gboolean: is-expanded
      cell-background -> gchararray: cell-background
      cell-background-rgba -> GdkRGBA: cell-background-rgba
      cell-background-set -> gboolean: cell-background-set
      editing -> gboolean: editing
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.CellView</summary>

Object GtkCellView
    
    Properties from GtkCellView:
      model -> GtkTreeModel: model
      cell-area -> GtkCellArea: cell-area
      cell-area-context -> GtkCellAreaContext: cell-area-context
      draw-sensitive -> gboolean: draw-sensitive
      fit-model -> gboolean: fit-model
    
    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
    
    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.CenterBox</summary>

Object GtkCenterBox
    
    Properties from GtkCenterBox:
      baseline-position -> GtkBaselinePosition: baseline-position
    
    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
    
    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.CenterLayout</summary>

Object GtkCenterLayout
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.CheckButton</summary>

Object GtkCheckButton
    
    Signals from GtkCheckButton:
      activate ()
      toggled ()
    
    Properties from GtkCheckButton:
      active -> gboolean: active
      group -> GtkCheckButton: group
      label -> gchararray: label
      inconsistent -> gboolean: inconsistent
      use-underline -> gboolean: use-underline
      child -> GtkWidget: child
    
    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
    
    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.ClosureExpression</summary>


    :Constructors:
    
    ::
    
        ClosureExpression(**properties)
        new(value_type:GType, closure:GObject.Closure, params:list=None) -> Gtk.ClosureExpression
    

---


</details>

<details><summary>Gtk.ColorButton</summary>

Object GtkColorButton
    
    Signals from GtkColorButton:
      activate ()
      color-set ()
    
    Properties from GtkColorButton:
      title -> gchararray: title
      show-editor -> gboolean: show-editor
      modal -> gboolean: modal
    
    Signals from GtkColorChooser:
      color-activated (GdkRGBA)
    
    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
    
    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.ColorChooser</summary>

Interface GtkColorChooser
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.ColorChooserDialog</summary>

Object GtkColorChooserDialog
    
    Properties from GtkColorChooserDialog:
      show-editor -> gboolean: show-editor
    
    Signals from GtkColorChooser:
      color-activated (GdkRGBA)
    
    Signals from GtkDialog:
      response (gint)
      close ()
    
    Properties from GtkDialog:
      use-header-bar -> gint: use-header-bar
    
    Signals from GtkWindow:
      activate-focus ()
      activate-default ()
      keys-changed ()
      enable-debugging (gboolean) -> gboolean
      close-request () -> gboolean
    
    Properties from GtkWindow:
      title -> gchararray: title
      resizable -> gboolean: resizable
      modal -> gboolean: modal
      default-width -> gint: default-width
      default-height -> gint: default-height
      destroy-with-parent -> gboolean: destroy-with-parent
      hide-on-close -> gboolean: hide-on-close
      icon-name -> gchararray: icon-name
      display -> GdkDisplay: display
      decorated -> gboolean: decorated
      deletable -> gboolean: deletable
      transient-for -> GtkWindow: transient-for
      application -> GtkApplication: application
      default-widget -> GtkWidget: default-widget
      focus-widget -> GtkWidget: focus-widget
      child -> GtkWidget: child
      titlebar -> GtkWidget: titlebar
      handle-menubar-accel -> gboolean: handle-menubar-accel
      is-active -> gboolean: is-active
      startup-id -> gchararray: startup-id
      mnemonics-visible -> gboolean: mnemonics-visible
      focus-visible -> gboolean: focus-visible
      maximized -> gboolean: maximized
      fullscreened -> gboolean: fullscreened
    
    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
    
    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.ColorChooserWidget</summary>

Object GtkColorChooserWidget
    
    Properties from GtkColorChooserWidget:
      show-editor -> gboolean: show-editor
    
    Signals from GtkColorChooser:
      color-activated (GdkRGBA)
    
    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
    
    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.ColumnView</summary>

Object GtkColumnView
    
    Signals from GtkColumnView:
      activate (guint)
    
    Properties from GtkColumnView:
      columns -> GListModel: columns
      model -> GtkSelectionModel: model
      show-row-separators -> gboolean: show-row-separators
      show-column-separators -> gboolean: show-column-separators
      sorter -> GtkSorter: sorter
      single-click-activate -> gboolean: single-click-activate
      reorderable -> gboolean: reorderable
      enable-rubberband -> gboolean: enable-rubberband
    
    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
    
    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.ColumnViewColumn</summary>

Object GtkColumnViewColumn
    
    Properties from GtkColumnViewColumn:
      column-view -> GtkColumnView: column-view
      factory -> GtkListItemFactory: factory
      title -> gchararray: title
      sorter -> GtkSorter: sorter
      visible -> gboolean: visible
      header-menu -> GMenuModel: header-menu
      resizable -> gboolean: resizable
      expand -> gboolean: expand
      fixed-width -> gint: fixed-width
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.ComboBox</summary>

Object GtkComboBox
    
    Signals from GtkComboBox:
      changed ()
      activate ()
      move-active (GtkScrollType)
      popup ()
      popdown () -> gboolean
      format-entry-text (gchararray) -> gchararray
    
    Properties from GtkComboBox:
      model -> GtkTreeModel: model
      active -> gint: active
      has-frame -> gboolean: has-frame
      popup-shown -> gboolean: popup-shown
      button-sensitivity -> GtkSensitivityType: button-sensitivity
      has-entry -> gboolean: has-entry
      entry-text-column -> gint: entry-text-column
      popup-fixed-width -> gboolean: popup-fixed-width
      id-column -> gint: id-column
      active-id -> gchararray: active-id
      child -> GtkWidget: child
    
    Signals from GtkCellEditable:
      editing-done ()
      remove-widget ()
    
    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
    
    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.ComboBoxText</summary>

Object GtkComboBoxText
    
    Signals from GtkCellEditable:
      editing-done ()
      remove-widget ()
    
    Signals from GtkComboBox:
      changed ()
      activate ()
      move-active (GtkScrollType)
      popup ()
      popdown () -> gboolean
      format-entry-text (gchararray) -> gchararray
    
    Properties from GtkComboBox:
      model -> GtkTreeModel: model
      active -> gint: active
      has-frame -> gboolean: has-frame
      popup-shown -> gboolean: popup-shown
      button-sensitivity -> GtkSensitivityType: button-sensitivity
      has-entry -> gboolean: has-entry
      entry-text-column -> gint: entry-text-column
      popup-fixed-width -> gboolean: popup-fixed-width
      id-column -> gint: id-column
      active-id -> gchararray: active-id
      child -> GtkWidget: child
    
    Signals from GtkCellEditable:
      editing-done ()
      remove-widget ()
    
    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
    
    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.ConstantExpression</summary>


    :Constructors:
    
    ::
    
        ConstantExpression(**properties)
        new_for_value(value:GObject.Value) -> Gtk.ConstantExpression
    

---


</details>

<details><summary>Gtk.Constraint</summary>

Object GtkConstraint
    
    Properties from GtkConstraint:
      target -> GtkConstraintTarget: target
      target-attribute -> GtkConstraintAttribute: target-attribute
      relation -> GtkConstraintRelation: relation
      source -> GtkConstraintTarget: source
      source-attribute -> GtkConstraintAttribute: source-attribute
      multiplier -> gdouble: multiplier
      constant -> gdouble: constant
      strength -> gint: strength
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.ConstraintGuide</summary>

Object GtkConstraintGuide
    
    Properties from GtkConstraintGuide:
      min-width -> gint: min-width
      min-height -> gint: min-height
      nat-width -> gint: nat-width
      nat-height -> gint: nat-height
      max-width -> gint: max-width
      max-height -> gint: max-height
      strength -> GtkConstraintStrength: strength
      name -> gchararray: name
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.ConstraintLayout</summary>

Object GtkConstraintLayout
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.ConstraintLayoutChild</summary>

Object GtkConstraintLayoutChild
    
    Properties from GtkLayoutChild:
      layout-manager -> GtkLayoutManager: layout-manager
      child-widget -> GtkWidget: child-widget
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.ConstraintTarget</summary>

Interface GtkConstraintTarget
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.CssProvider</summary>

Object GtkCssProvider
    
    Signals from GtkCssProvider:
      parsing-error (GtkCssSection, GError)
    
    Signals from GtkStyleProvider:
      gtk-private-changed ()
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.CustomFilter</summary>

Object GtkCustomFilter
    
    Signals from GtkFilter:
      changed (GtkFilterChange)
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.CustomLayout</summary>

Object GtkCustomLayout
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.CustomSorter</summary>

Object GtkCustomSorter
    
    Signals from GtkSorter:
      changed (GtkSorterChange)
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.Dialog</summary>

Object GtkDialog
    
    Signals from GtkDialog:
      response (gint)
      close ()
    
    Properties from GtkDialog:
      use-header-bar -> gint: use-header-bar
    
    Signals from GtkWindow:
      activate-focus ()
      activate-default ()
      keys-changed ()
      enable-debugging (gboolean) -> gboolean
      close-request () -> gboolean
    
    Properties from GtkWindow:
      title -> gchararray: title
      resizable -> gboolean: resizable
      modal -> gboolean: modal
      default-width -> gint: default-width
      default-height -> gint: default-height
      destroy-with-parent -> gboolean: destroy-with-parent
      hide-on-close -> gboolean: hide-on-close
      icon-name -> gchararray: icon-name
      display -> GdkDisplay: display
      decorated -> gboolean: decorated
      deletable -> gboolean: deletable
      transient-for -> GtkWindow: transient-for
      application -> GtkApplication: application
      default-widget -> GtkWidget: default-widget
      focus-widget -> GtkWidget: focus-widget
      child -> GtkWidget: child
      titlebar -> GtkWidget: titlebar
      handle-menubar-accel -> gboolean: handle-menubar-accel
      is-active -> gboolean: is-active
      startup-id -> gchararray: startup-id
      mnemonics-visible -> gboolean: mnemonics-visible
      focus-visible -> gboolean: focus-visible
      maximized -> gboolean: maximized
      fullscreened -> gboolean: fullscreened
    
    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
    
    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.DirectoryList</summary>

Object GtkDirectoryList
    
    Properties from GtkDirectoryList:
      attributes -> gchararray: attributes
      error -> GError: error
      file -> GFile: file
      io-priority -> gint: io-priority
      item-type -> GType: item-type
      loading -> gboolean: loading
      monitored -> gboolean: monitored
      n-items -> guint: n-items
    
    Signals from GListModel:
      items-changed (guint, guint, guint)
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.DragIcon</summary>

Object GtkDragIcon
    
    Properties from GtkDragIcon:
      child -> GtkWidget: child
    
    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
    
    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.DragSource</summary>

Object GtkDragSource
    
    Signals from GtkDragSource:
      prepare (gdouble, gdouble) -> GdkContentProvider
      drag-begin (GdkDrag)
      drag-end (GdkDrag, gboolean)
      drag-cancel (GdkDrag, GdkDragCancelReason) -> gboolean
    
    Properties from GtkDragSource:
      content -> GdkContentProvider: content
      actions -> GdkDragAction: actions
    
    Properties from GtkGestureSingle:
      touch-only -> gboolean: touch-only
      exclusive -> gboolean: exclusive
      button -> guint: button
    
    Signals from GtkGesture:
      update (GdkEventSequence)
      cancel (GdkEventSequence)
      begin (GdkEventSequence)
      end (GdkEventSequence)
      sequence-state-changed (GdkEventSequence, GtkEventSequenceState)
    
    Properties from GtkGesture:
      n-points -> guint: n-points
    
    Properties from GtkEventController:
      widget -> GtkWidget: widget
      propagation-phase -> GtkPropagationPhase: propagation-phase
      propagation-limit -> GtkPropagationLimit: propagation-limit
      name -> gchararray: name
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.DrawingArea</summary>

Object GtkDrawingArea
    
    Signals from GtkDrawingArea:
      resize (gint, gint)
    
    Properties from GtkDrawingArea:
      content-width -> gint: content-width
      content-height -> gint: content-height
    
    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
    
    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.DropControllerMotion</summary>

Object GtkDropControllerMotion
    
    Signals from GtkDropControllerMotion:
      enter (gdouble, gdouble)
      leave ()
      motion (gdouble, gdouble)
    
    Properties from GtkDropControllerMotion:
      contains-pointer -> gboolean: contains-pointer
      drop -> GdkDrop: drop
      is-pointer -> gboolean: is-pointer
    
    Properties from GtkEventController:
      widget -> GtkWidget: widget
      propagation-phase -> GtkPropagationPhase: propagation-phase
      propagation-limit -> GtkPropagationLimit: propagation-limit
      name -> gchararray: name
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.DropDown</summary>

Object GtkDropDown
    
    Signals from GtkDropDown:
      activate ()
    
    Properties from GtkDropDown:
      factory -> GtkListItemFactory: factory
      list-factory -> GtkListItemFactory: list-factory
      model -> GListModel: model
      selected -> guint: selected
      selected-item -> GObject: selected-item
      enable-search -> gboolean: enable-search
      expression -> GtkExpression: expression
      show-arrow -> gboolean: show-arrow
    
    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
    
    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.DropTarget</summary>

Object GtkDropTarget
    
    Signals from GtkDropTarget:
      drop (GValue, gdouble, gdouble) -> gboolean
      enter (gdouble, gdouble) -> GdkDragAction
      leave ()
      motion (gdouble, gdouble) -> GdkDragAction
      accept (GdkDrop) -> gboolean
    
    Properties from GtkDropTarget:
      actions -> GdkDragAction: actions
      current-drop -> GdkDrop: current-drop
      drop -> GdkDrop: drop
      formats -> GdkContentFormats: formats
      preload -> gboolean: preload
      value -> GValue: value
    
    Properties from GtkEventController:
      widget -> GtkWidget: widget
      propagation-phase -> GtkPropagationPhase: propagation-phase
      propagation-limit -> GtkPropagationLimit: propagation-limit
      name -> gchararray: name
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.DropTargetAsync</summary>

Object GtkDropTargetAsync
    
    Signals from GtkDropTargetAsync:
      drop (GdkDrop, gdouble, gdouble) -> gboolean
      accept (GdkDrop) -> gboolean
      drag-enter (GdkDrop, gdouble, gdouble) -> GdkDragAction
      drag-motion (GdkDrop, gdouble, gdouble) -> GdkDragAction
      drag-leave (GdkDrop)
    
    Properties from GtkDropTargetAsync:
      actions -> GdkDragAction: actions
      formats -> GdkContentFormats: formats
    
    Properties from GtkEventController:
      widget -> GtkWidget: widget
      propagation-phase -> GtkPropagationPhase: propagation-phase
      propagation-limit -> GtkPropagationLimit: propagation-limit
      name -> gchararray: name
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.Editable</summary>

Interface GtkEditable
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.EditableLabel</summary>

Object GtkEditableLabel
    
    Properties from GtkEditableLabel:
      editing -> gboolean: editing
    
    Signals from GtkEditable:
      changed ()
      insert-text (gchararray, gint, gpointer)
      delete-text (gint, gint)
    
    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
    
    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.EmojiChooser</summary>

Object GtkEmojiChooser
    
    Signals from GtkEmojiChooser:
      emoji-picked (gchararray)
    
    Signals from GtkPopover:
      closed ()
      activate-default ()
    
    Properties from GtkPopover:
      pointing-to -> GdkRectangle: pointing-to
      position -> GtkPositionType: position
      autohide -> gboolean: autohide
      default-widget -> GtkWidget: default-widget
      has-arrow -> gboolean: has-arrow
      mnemonics-visible -> gboolean: mnemonics-visible
      child -> GtkWidget: child
      cascade-popdown -> gboolean: cascade-popdown
    
    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
    
    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.Entry</summary>

Object GtkEntry
    
    Signals from GtkEntry:
      activate ()
      icon-press (GtkEntryIconPosition)
      icon-release (GtkEntryIconPosition)
    
    Properties from GtkEntry:
      buffer -> GtkEntryBuffer: buffer
      max-length -> gint: max-length
      visibility -> gboolean: visibility
      has-frame -> gboolean: has-frame
      invisible-char -> guint: invisible-char
      activates-default -> gboolean: activates-default
      scroll-offset -> gint: scroll-offset
      truncate-multiline -> gboolean: truncate-multiline
      overwrite-mode -> gboolean: overwrite-mode
      text-length -> guint: text-length
      invisible-char-set -> gboolean: invisible-char-set
      progress-fraction -> gdouble: progress-fraction
      progress-pulse-step -> gdouble: progress-pulse-step
      primary-icon-paintable -> GdkPaintable: primary-icon-paintable
      secondary-icon-paintable -> GdkPaintable: secondary-icon-paintable
      primary-icon-name -> gchararray: primary-icon-name
      secondary-icon-name -> gchararray: secondary-icon-name
      primary-icon-gicon -> GIcon: primary-icon-gicon
      secondary-icon-gicon -> GIcon: secondary-icon-gicon
      primary-icon-storage-type -> GtkImageType: primary-icon-storage-type
      secondary-icon-storage-type -> GtkImageType: secondary-icon-storage-type
      primary-icon-activatable -> gboolean: primary-icon-activatable
      secondary-icon-activatable -> gboolean: secondary-icon-activatable
      primary-icon-sensitive -> gboolean: primary-icon-sensitive
      secondary-icon-sensitive -> gboolean: secondary-icon-sensitive
      primary-icon-tooltip-text -> gchararray: primary-icon-tooltip-text
      secondary-icon-tooltip-text -> gchararray: secondary-icon-tooltip-text
      primary-icon-tooltip-markup -> gchararray: primary-icon-tooltip-markup
      secondary-icon-tooltip-markup -> gchararray: secondary-icon-tooltip-markup
      im-module -> gchararray: im-module
      placeholder-text -> gchararray: placeholder-text
      completion -> GtkEntryCompletion: completion
      input-purpose -> GtkInputPurpose: input-purpose
      input-hints -> GtkInputHints: input-hints
      attributes -> PangoAttrList: attributes
      tabs -> PangoTabArray: tabs
      extra-menu -> GMenuModel: extra-menu
      show-emoji-icon -> gboolean: show-emoji-icon
      enable-emoji-completion -> gboolean: enable-emoji-completion
    
    Signals from GtkEditable:
      changed ()
      insert-text (gchararray, gint, gpointer)
      delete-text (gint, gint)
    
    Signals from GtkCellEditable:
      editing-done ()
      remove-widget ()
    
    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
    
    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.EntryBuffer</summary>

Object GtkEntryBuffer
    
    Signals from GtkEntryBuffer:
      inserted-text (guint, gchararray, guint)
      deleted-text (guint, guint)
    
    Properties from GtkEntryBuffer:
      text -> gchararray: text
      length -> guint: length
      max-length -> gint: max-length
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.EntryCompletion</summary>

Object GtkEntryCompletion
    
    Signals from GtkEntryCompletion:
      insert-prefix (gchararray) -> gboolean
      match-selected (GtkTreeModel, GtkTreeIter) -> gboolean
      cursor-on-match (GtkTreeModel, GtkTreeIter) -> gboolean
      no-matches ()
    
    Properties from GtkEntryCompletion:
      model -> GtkTreeModel: model
      minimum-key-length -> gint: minimum-key-length
      text-column -> gint: text-column
      inline-completion -> gboolean: inline-completion
      popup-completion -> gboolean: popup-completion
      popup-set-width -> gboolean: popup-set-width
      popup-single-match -> gboolean: popup-single-match
      inline-selection -> gboolean: inline-selection
      cell-area -> GtkCellArea: cell-area
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.EventController</summary>

Object GtkEventController
    
    Properties from GtkEventController:
      widget -> GtkWidget: widget
      propagation-phase -> GtkPropagationPhase: propagation-phase
      propagation-limit -> GtkPropagationLimit: propagation-limit
      name -> gchararray: name
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.EventControllerFocus</summary>

Object GtkEventControllerFocus
    
    Signals from GtkEventControllerFocus:
      enter ()
      leave ()
    
    Properties from GtkEventControllerFocus:
      is-focus -> gboolean: is-focus
      contains-focus -> gboolean: contains-focus
    
    Properties from GtkEventController:
      widget -> GtkWidget: widget
      propagation-phase -> GtkPropagationPhase: propagation-phase
      propagation-limit -> GtkPropagationLimit: propagation-limit
      name -> gchararray: name
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.EventControllerKey</summary>

Object GtkEventControllerKey
    
    Signals from GtkEventControllerKey:
      modifiers (GdkModifierType) -> gboolean
      key-pressed (guint, guint, GdkModifierType) -> gboolean
      key-released (guint, guint, GdkModifierType)
      im-update ()
    
    Properties from GtkEventController:
      widget -> GtkWidget: widget
      propagation-phase -> GtkPropagationPhase: propagation-phase
      propagation-limit -> GtkPropagationLimit: propagation-limit
      name -> gchararray: name
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.EventControllerLegacy</summary>

Object GtkEventControllerLegacy
    
    Signals from GtkEventControllerLegacy:
      event (GdkEvent) -> gboolean
    
    Properties from GtkEventController:
      widget -> GtkWidget: widget
      propagation-phase -> GtkPropagationPhase: propagation-phase
      propagation-limit -> GtkPropagationLimit: propagation-limit
      name -> gchararray: name
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.EventControllerMotion</summary>

Object GtkEventControllerMotion
    
    Signals from GtkEventControllerMotion:
      enter (gdouble, gdouble)
      leave ()
      motion (gdouble, gdouble)
    
    Properties from GtkEventControllerMotion:
      is-pointer -> gboolean: is-pointer
      contains-pointer -> gboolean: contains-pointer
    
    Properties from GtkEventController:
      widget -> GtkWidget: widget
      propagation-phase -> GtkPropagationPhase: propagation-phase
      propagation-limit -> GtkPropagationLimit: propagation-limit
      name -> gchararray: name
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.EventControllerScroll</summary>

Object GtkEventControllerScroll
    
    Signals from GtkEventControllerScroll:
      scroll-begin ()
      scroll (gdouble, gdouble) -> gboolean
      scroll-end ()
      decelerate (gdouble, gdouble)
    
    Properties from GtkEventControllerScroll:
      flags -> GtkEventControllerScrollFlags: flags
    
    Properties from GtkEventController:
      widget -> GtkWidget: widget
      propagation-phase -> GtkPropagationPhase: propagation-phase
      propagation-limit -> GtkPropagationLimit: propagation-limit
      name -> gchararray: name
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.EveryFilter</summary>

Object GtkEveryFilter
    
    Signals from GListModel:
      items-changed (guint, guint, guint)
    
    Properties from GtkMultiFilter:
      item-type -> GType: item-type
      n-items -> guint: n-items
    
    Signals from GListModel:
      items-changed (guint, guint, guint)
    
    Signals from GtkFilter:
      changed (GtkFilterChange)
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.Expander</summary>

Object GtkExpander
    
    Signals from GtkExpander:
      activate ()
    
    Properties from GtkExpander:
      expanded -> gboolean: expanded
      label -> gchararray: label
      use-underline -> gboolean: use-underline
      use-markup -> gboolean: use-markup
      label-widget -> GtkWidget: label-widget
      resize-toplevel -> gboolean: resize-toplevel
      child -> GtkWidget: child
    
    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
    
    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.Expression</summary>


    :Constructors:
    
    ::
    
        Expression(**properties)
    

---


</details>

<details><summary>Gtk.FileChooser</summary>

Interface GtkFileChooser
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.FileChooserDialog</summary>

Object GtkFileChooserDialog
    
    Signals from GtkDialog:
      response (gint)
      close ()
    
    Properties from GtkDialog:
      use-header-bar -> gint: use-header-bar
    
    Signals from GtkWindow:
      activate-focus ()
      activate-default ()
      keys-changed ()
      enable-debugging (gboolean) -> gboolean
      close-request () -> gboolean
    
    Properties from GtkWindow:
      title -> gchararray: title
      resizable -> gboolean: resizable
      modal -> gboolean: modal
      default-width -> gint: default-width
      default-height -> gint: default-height
      destroy-with-parent -> gboolean: destroy-with-parent
      hide-on-close -> gboolean: hide-on-close
      icon-name -> gchararray: icon-name
      display -> GdkDisplay: display
      decorated -> gboolean: decorated
      deletable -> gboolean: deletable
      transient-for -> GtkWindow: transient-for
      application -> GtkApplication: application
      default-widget -> GtkWidget: default-widget
      focus-widget -> GtkWidget: focus-widget
      child -> GtkWidget: child
      titlebar -> GtkWidget: titlebar
      handle-menubar-accel -> gboolean: handle-menubar-accel
      is-active -> gboolean: is-active
      startup-id -> gchararray: startup-id
      mnemonics-visible -> gboolean: mnemonics-visible
      focus-visible -> gboolean: focus-visible
      maximized -> gboolean: maximized
      fullscreened -> gboolean: fullscreened
    
    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
    
    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.FileChooserNative</summary>

Object GtkFileChooserNative
    
    Properties from GtkFileChooserNative:
      accept-label -> gchararray: accept-label
      cancel-label -> gchararray: cancel-label
    
    Signals from GtkNativeDialog:
      response (gint)
    
    Properties from GtkNativeDialog:
      title -> gchararray: title
      visible -> gboolean: visible
      modal -> gboolean: modal
      transient-for -> GtkWindow: transient-for
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.FileChooserWidget</summary>

Object GtkFileChooserWidget
    
    Signals from GtkFileChooserWidget:
      location-popup (gchararray)
      location-popup-on-paste ()
      location-toggle-popup ()
      up-folder ()
      down-folder ()
      home-folder ()
      desktop-folder ()
      quick-bookmark (gint)
      show-hidden ()
      search-shortcut ()
      recent-shortcut ()
      places-shortcut ()
    
    Properties from GtkFileChooserWidget:
      search-mode -> gboolean: search-mode
      subtitle -> gchararray: subtitle
    
    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
    
    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.FileFilter</summary>

Object GtkFileFilter
    
    Properties from GtkFileFilter:
      name -> gchararray: name
    
    Signals from GtkFilter:
      changed (GtkFilterChange)
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.Filter</summary>

Object GtkFilter
    
    Signals from GtkFilter:
      changed (GtkFilterChange)
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.FilterListModel</summary>

Object GtkFilterListModel
    
    Properties from GtkFilterListModel:
      filter -> GtkFilter: filter
      incremental -> gboolean: incremental
      item-type -> GType: item-type
      model -> GListModel: model
      n-items -> guint: n-items
      pending -> guint: pending
    
    Signals from GListModel:
      items-changed (guint, guint, guint)
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.Fixed</summary>

Object GtkFixed
    
    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
    
    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.FixedLayout</summary>

Object GtkFixedLayout
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.FixedLayoutChild</summary>

Object GtkFixedLayoutChild
    
    Properties from GtkFixedLayoutChild:
      transform -> GskTransform: transform
    
    Properties from GtkLayoutChild:
      layout-manager -> GtkLayoutManager: layout-manager
      child-widget -> GtkWidget: child-widget
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.FlattenListModel</summary>

Object GtkFlattenListModel
    
    Properties from GtkFlattenListModel:
      item-type -> GType: item-type
      model -> GListModel: model
      n-items -> guint: n-items
    
    Signals from GListModel:
      items-changed (guint, guint, guint)
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.FlowBox</summary>

Object GtkFlowBox
    
    Signals from GtkFlowBox:
      child-activated (GtkFlowBoxChild)
      selected-children-changed ()
      activate-cursor-child ()
      toggle-cursor-child ()
      move-cursor (GtkMovementStep, gint, gboolean, gboolean) -> gboolean
      select-all ()
      unselect-all ()
    
    Properties from GtkFlowBox:
      homogeneous -> gboolean: homogeneous
      column-spacing -> guint: column-spacing
      row-spacing -> guint: row-spacing
      min-children-per-line -> guint: min-children-per-line
      max-children-per-line -> guint: max-children-per-line
      selection-mode -> GtkSelectionMode: selection-mode
      activate-on-single-click -> gboolean: activate-on-single-click
      accept-unpaired-release -> gboolean: accept-unpaired-release
    
    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
    
    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.FlowBoxChild</summary>

Object GtkFlowBoxChild
    
    Signals from GtkFlowBoxChild:
      activate ()
    
    Properties from GtkFlowBoxChild:
      child -> GtkWidget: child
    
    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
    
    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.FontButton</summary>

Object GtkFontButton
    
    Signals from GtkFontButton:
      activate ()
      font-set ()
    
    Properties from GtkFontButton:
      title -> gchararray: title
      modal -> gboolean: modal
      use-font -> gboolean: use-font
      use-size -> gboolean: use-size
    
    Signals from GtkFontChooser:
      font-activated (gchararray)
    
    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
    
    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.FontChooser</summary>

Interface GtkFontChooser
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.FontChooserDialog</summary>

Object GtkFontChooserDialog
    
    Signals from GtkFontChooser:
      font-activated (gchararray)
    
    Signals from GtkDialog:
      response (gint)
      close ()
    
    Properties from GtkDialog:
      use-header-bar -> gint: use-header-bar
    
    Signals from GtkWindow:
      activate-focus ()
      activate-default ()
      keys-changed ()
      enable-debugging (gboolean) -> gboolean
      close-request () -> gboolean
    
    Properties from GtkWindow:
      title -> gchararray: title
      resizable -> gboolean: resizable
      modal -> gboolean: modal
      default-width -> gint: default-width
      default-height -> gint: default-height
      destroy-with-parent -> gboolean: destroy-with-parent
      hide-on-close -> gboolean: hide-on-close
      icon-name -> gchararray: icon-name
      display -> GdkDisplay: display
      decorated -> gboolean: decorated
      deletable -> gboolean: deletable
      transient-for -> GtkWindow: transient-for
      application -> GtkApplication: application
      default-widget -> GtkWidget: default-widget
      focus-widget -> GtkWidget: focus-widget
      child -> GtkWidget: child
      titlebar -> GtkWidget: titlebar
      handle-menubar-accel -> gboolean: handle-menubar-accel
      is-active -> gboolean: is-active
      startup-id -> gchararray: startup-id
      mnemonics-visible -> gboolean: mnemonics-visible
      focus-visible -> gboolean: focus-visible
      maximized -> gboolean: maximized
      fullscreened -> gboolean: fullscreened
    
    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
    
    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.FontChooserWidget</summary>

Object GtkFontChooserWidget
    
    Properties from GtkFontChooserWidget:
      tweak-action -> GAction: tweak-action
    
    Signals from GtkFontChooser:
      font-activated (gchararray)
    
    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
    
    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.Frame</summary>

Object GtkFrame
    
    Properties from GtkFrame:
      label -> gchararray: label
      label-xalign -> gfloat: label-xalign
      label-widget -> GtkWidget: label-widget
      child -> GtkWidget: child
    
    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
    
    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.GLArea</summary>

Object GtkGLArea
    
    Signals from GtkGLArea:
      render (GdkGLContext) -> gboolean
      resize (gint, gint)
      create-context () -> GdkGLContext
    
    Properties from GtkGLArea:
      context -> GdkGLContext: context
      has-depth-buffer -> gboolean: has-depth-buffer
      has-stencil-buffer -> gboolean: has-stencil-buffer
      use-es -> gboolean: use-es
      auto-render -> gboolean: auto-render
    
    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
    
    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.Gesture</summary>

Object GtkGesture
    
    Signals from GtkGesture:
      update (GdkEventSequence)
      cancel (GdkEventSequence)
      begin (GdkEventSequence)
      end (GdkEventSequence)
      sequence-state-changed (GdkEventSequence, GtkEventSequenceState)
    
    Properties from GtkGesture:
      n-points -> guint: n-points
    
    Properties from GtkEventController:
      widget -> GtkWidget: widget
      propagation-phase -> GtkPropagationPhase: propagation-phase
      propagation-limit -> GtkPropagationLimit: propagation-limit
      name -> gchararray: name
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.GestureClick</summary>

Object GtkGestureClick
    
    Signals from GtkGestureClick:
      pressed (gint, gdouble, gdouble)
      released (gint, gdouble, gdouble)
      stopped ()
      unpaired-release (gdouble, gdouble, guint, GdkEventSequence)
    
    Properties from GtkGestureSingle:
      touch-only -> gboolean: touch-only
      exclusive -> gboolean: exclusive
      button -> guint: button
    
    Signals from GtkGesture:
      update (GdkEventSequence)
      cancel (GdkEventSequence)
      begin (GdkEventSequence)
      end (GdkEventSequence)
      sequence-state-changed (GdkEventSequence, GtkEventSequenceState)
    
    Properties from GtkGesture:
      n-points -> guint: n-points
    
    Properties from GtkEventController:
      widget -> GtkWidget: widget
      propagation-phase -> GtkPropagationPhase: propagation-phase
      propagation-limit -> GtkPropagationLimit: propagation-limit
      name -> gchararray: name
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.GestureDrag</summary>

Object GtkGestureDrag
    
    Signals from GtkGestureDrag:
      drag-begin (gdouble, gdouble)
      drag-end (gdouble, gdouble)
      drag-update (gdouble, gdouble)
    
    Properties from GtkGestureSingle:
      touch-only -> gboolean: touch-only
      exclusive -> gboolean: exclusive
      button -> guint: button
    
    Signals from GtkGesture:
      update (GdkEventSequence)
      cancel (GdkEventSequence)
      begin (GdkEventSequence)
      end (GdkEventSequence)
      sequence-state-changed (GdkEventSequence, GtkEventSequenceState)
    
    Properties from GtkGesture:
      n-points -> guint: n-points
    
    Properties from GtkEventController:
      widget -> GtkWidget: widget
      propagation-phase -> GtkPropagationPhase: propagation-phase
      propagation-limit -> GtkPropagationLimit: propagation-limit
      name -> gchararray: name
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.GestureLongPress</summary>

Object GtkGestureLongPress
    
    Signals from GtkGestureLongPress:
      cancelled ()
      pressed (gdouble, gdouble)
    
    Properties from GtkGestureLongPress:
      delay-factor -> gdouble: delay-factor
    
    Properties from GtkGestureSingle:
      touch-only -> gboolean: touch-only
      exclusive -> gboolean: exclusive
      button -> guint: button
    
    Signals from GtkGesture:
      update (GdkEventSequence)
      cancel (GdkEventSequence)
      begin (GdkEventSequence)
      end (GdkEventSequence)
      sequence-state-changed (GdkEventSequence, GtkEventSequenceState)
    
    Properties from GtkGesture:
      n-points -> guint: n-points
    
    Properties from GtkEventController:
      widget -> GtkWidget: widget
      propagation-phase -> GtkPropagationPhase: propagation-phase
      propagation-limit -> GtkPropagationLimit: propagation-limit
      name -> gchararray: name
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.GesturePan</summary>

Object GtkGesturePan
    
    Signals from GtkGesturePan:
      pan (GtkPanDirection, gdouble)
    
    Properties from GtkGesturePan:
      orientation -> GtkOrientation: orientation
    
    Signals from GtkGestureDrag:
      drag-begin (gdouble, gdouble)
      drag-end (gdouble, gdouble)
      drag-update (gdouble, gdouble)
    
    Properties from GtkGestureSingle:
      touch-only -> gboolean: touch-only
      exclusive -> gboolean: exclusive
      button -> guint: button
    
    Signals from GtkGesture:
      update (GdkEventSequence)
      cancel (GdkEventSequence)
      begin (GdkEventSequence)
      end (GdkEventSequence)
      sequence-state-changed (GdkEventSequence, GtkEventSequenceState)
    
    Properties from GtkGesture:
      n-points -> guint: n-points
    
    Properties from GtkEventController:
      widget -> GtkWidget: widget
      propagation-phase -> GtkPropagationPhase: propagation-phase
      propagation-limit -> GtkPropagationLimit: propagation-limit
      name -> gchararray: name
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.GestureRotate</summary>

Object GtkGestureRotate
    
    Signals from GtkGestureRotate:
      angle-changed (gdouble, gdouble)
    
    Signals from GtkGesture:
      update (GdkEventSequence)
      cancel (GdkEventSequence)
      begin (GdkEventSequence)
      end (GdkEventSequence)
      sequence-state-changed (GdkEventSequence, GtkEventSequenceState)
    
    Properties from GtkGesture:
      n-points -> guint: n-points
    
    Properties from GtkEventController:
      widget -> GtkWidget: widget
      propagation-phase -> GtkPropagationPhase: propagation-phase
      propagation-limit -> GtkPropagationLimit: propagation-limit
      name -> gchararray: name
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.GestureSingle</summary>

Object GtkGestureSingle
    
    Properties from GtkGestureSingle:
      touch-only -> gboolean: touch-only
      exclusive -> gboolean: exclusive
      button -> guint: button
    
    Signals from GtkGesture:
      update (GdkEventSequence)
      cancel (GdkEventSequence)
      begin (GdkEventSequence)
      end (GdkEventSequence)
      sequence-state-changed (GdkEventSequence, GtkEventSequenceState)
    
    Properties from GtkGesture:
      n-points -> guint: n-points
    
    Properties from GtkEventController:
      widget -> GtkWidget: widget
      propagation-phase -> GtkPropagationPhase: propagation-phase
      propagation-limit -> GtkPropagationLimit: propagation-limit
      name -> gchararray: name
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.GestureStylus</summary>

Object GtkGestureStylus
    
    Signals from GtkGestureStylus:
      motion (gdouble, gdouble)
      proximity (gdouble, gdouble)
      down (gdouble, gdouble)
      up (gdouble, gdouble)
    
    Properties from GtkGestureSingle:
      touch-only -> gboolean: touch-only
      exclusive -> gboolean: exclusive
      button -> guint: button
    
    Signals from GtkGesture:
      update (GdkEventSequence)
      cancel (GdkEventSequence)
      begin (GdkEventSequence)
      end (GdkEventSequence)
      sequence-state-changed (GdkEventSequence, GtkEventSequenceState)
    
    Properties from GtkGesture:
      n-points -> guint: n-points
    
    Properties from GtkEventController:
      widget -> GtkWidget: widget
      propagation-phase -> GtkPropagationPhase: propagation-phase
      propagation-limit -> GtkPropagationLimit: propagation-limit
      name -> gchararray: name
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.GestureSwipe</summary>

Object GtkGestureSwipe
    
    Signals from GtkGestureSwipe:
      swipe (gdouble, gdouble)
    
    Properties from GtkGestureSingle:
      touch-only -> gboolean: touch-only
      exclusive -> gboolean: exclusive
      button -> guint: button
    
    Signals from GtkGesture:
      update (GdkEventSequence)
      cancel (GdkEventSequence)
      begin (GdkEventSequence)
      end (GdkEventSequence)
      sequence-state-changed (GdkEventSequence, GtkEventSequenceState)
    
    Properties from GtkGesture:
      n-points -> guint: n-points
    
    Properties from GtkEventController:
      widget -> GtkWidget: widget
      propagation-phase -> GtkPropagationPhase: propagation-phase
      propagation-limit -> GtkPropagationLimit: propagation-limit
      name -> gchararray: name
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.GestureZoom</summary>

Object GtkGestureZoom
    
    Signals from GtkGestureZoom:
      scale-changed (gdouble)
    
    Signals from GtkGesture:
      update (GdkEventSequence)
      cancel (GdkEventSequence)
      begin (GdkEventSequence)
      end (GdkEventSequence)
      sequence-state-changed (GdkEventSequence, GtkEventSequenceState)
    
    Properties from GtkGesture:
      n-points -> guint: n-points
    
    Properties from GtkEventController:
      widget -> GtkWidget: widget
      propagation-phase -> GtkPropagationPhase: propagation-phase
      propagation-limit -> GtkPropagationLimit: propagation-limit
      name -> gchararray: name
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.Grid</summary>

Object GtkGrid
    
    Properties from GtkGrid:
      row-spacing -> gint: row-spacing
      column-spacing -> gint: column-spacing
      row-homogeneous -> gboolean: row-homogeneous
      column-homogeneous -> gboolean: column-homogeneous
      baseline-row -> gint: baseline-row
    
    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
    
    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.GridLayout</summary>

Object GtkGridLayout
    
    Properties from GtkGridLayout:
      row-spacing -> gint: row-spacing
      column-spacing -> gint: column-spacing
      row-homogeneous -> gboolean: row-homogeneous
      column-homogeneous -> gboolean: column-homogeneous
      baseline-row -> gint: baseline-row
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.GridLayoutChild</summary>

Object GtkGridLayoutChild
    
    Properties from GtkGridLayoutChild:
      column -> gint: column
      row -> gint: row
      column-span -> gint: column-span
      row-span -> gint: row-span
    
    Properties from GtkLayoutChild:
      layout-manager -> GtkLayoutManager: layout-manager
      child-widget -> GtkWidget: child-widget
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.GridView</summary>

Object GtkGridView
    
    Signals from GtkGridView:
      activate (guint)
    
    Properties from GtkGridView:
      factory -> GtkListItemFactory: factory
      max-columns -> guint: max-columns
      min-columns -> guint: min-columns
      model -> GtkSelectionModel: model
      single-click-activate -> gboolean: single-click-activate
      enable-rubberband -> gboolean: enable-rubberband
    
    Properties from GtkListBase:
      orientation -> GtkOrientation: orientation
    
    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
    
    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.HeaderBar</summary>

Object GtkHeaderBar
    
    Properties from GtkHeaderBar:
      title-widget -> GtkWidget: title-widget
      show-title-buttons -> gboolean: show-title-buttons
      decoration-layout -> gchararray: decoration-layout
    
    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
    
    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.IMContext</summary>

Object GtkIMContext
    
    Signals from GtkIMContext:
      preedit-start ()
      preedit-end ()
      preedit-changed ()
      commit (gchararray)
      retrieve-surrounding () -> gboolean
      delete-surrounding (gint, gint) -> gboolean
    
    Properties from GtkIMContext:
      input-purpose -> GtkInputPurpose: input-purpose
      input-hints -> GtkInputHints: input-hints
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.IMContextSimple</summary>

Object GtkIMContextSimple
    
    Signals from GtkIMContext:
      preedit-start ()
      preedit-end ()
      preedit-changed ()
      commit (gchararray)
      retrieve-surrounding () -> gboolean
      delete-surrounding (gint, gint) -> gboolean
    
    Properties from GtkIMContext:
      input-purpose -> GtkInputPurpose: input-purpose
      input-hints -> GtkInputHints: input-hints
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.IMMulticontext</summary>

Object GtkIMMulticontext
    
    Signals from GtkIMContext:
      preedit-start ()
      preedit-end ()
      preedit-changed ()
      commit (gchararray)
      retrieve-surrounding () -> gboolean
      delete-surrounding (gint, gint) -> gboolean
    
    Properties from GtkIMContext:
      input-purpose -> GtkInputPurpose: input-purpose
      input-hints -> GtkInputHints: input-hints
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.IconPaintable</summary>

Object GtkIconPaintable
    
    Properties from GtkIconPaintable:
      file -> GFile: file
      icon-name -> gchararray: icon-name
      is-symbolic -> gboolean: is-symbolic
    
    Signals from GdkPaintable:
      invalidate-contents ()
      invalidate-size ()
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.IconTheme</summary>

Object GtkIconTheme
    
    Signals from GtkIconTheme:
      changed ()
    
    Properties from GtkIconTheme:
      display -> GdkDisplay: display
      icon-names -> GStrv: icon-names
      search-path -> GStrv: search-path
      resource-path -> GStrv: resource-path
      theme-name -> gchararray: theme-name
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.IconView</summary>

Object GtkIconView
    
    Signals from GtkIconView:
      move-cursor (GtkMovementStep, gint, gboolean, gboolean) -> gboolean
      select-all ()
      unselect-all ()
      item-activated (GtkTreePath)
      selection-changed ()
      select-cursor-item ()
      toggle-cursor-item ()
      activate-cursor-item () -> gboolean
    
    Properties from GtkIconView:
      pixbuf-column -> gint: pixbuf-column
      text-column -> gint: text-column
      markup-column -> gint: markup-column
      selection-mode -> GtkSelectionMode: selection-mode
      item-orientation -> GtkOrientation: item-orientation
      model -> GtkTreeModel: model
      columns -> gint: columns
      item-width -> gint: item-width
      spacing -> gint: spacing
      row-spacing -> gint: row-spacing
      column-spacing -> gint: column-spacing
      margin -> gint: margin
      reorderable -> gboolean: reorderable
      tooltip-column -> gint: tooltip-column
      item-padding -> gint: item-padding
      cell-area -> GtkCellArea: cell-area
      activate-on-single-click -> gboolean: activate-on-single-click
    
    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
    
    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.Image</summary>

Object GtkImage
    
    Properties from GtkImage:
      paintable -> GdkPaintable: paintable
      file -> gchararray: file
      icon-size -> GtkIconSize: icon-size
      pixel-size -> gint: pixel-size
      icon-name -> gchararray: icon-name
      storage-type -> GtkImageType: storage-type
      gicon -> GIcon: gicon
      resource -> gchararray: resource
      use-fallback -> gboolean: use-fallback
    
    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
    
    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.InfoBar</summary>

Object GtkInfoBar
    
    Signals from GtkInfoBar:
      response (gint)
      close ()
    
    Properties from GtkInfoBar:
      message-type -> GtkMessageType: message-type
      show-close-button -> gboolean: show-close-button
      revealed -> gboolean: revealed
    
    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
    
    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.Inscription</summary>

Object GtkInscription
    
    Properties from GtkInscription:
      attributes -> PangoAttrList: attributes
      markup -> gchararray: markup
      min-chars -> guint: min-chars
      min-lines -> guint: min-lines
      nat-chars -> guint: nat-chars
      nat-lines -> guint: nat-lines
      text -> gchararray: text
      text-overflow -> GtkInscriptionOverflow: text-overflow
      wrap-mode -> PangoWrapMode: wrap-mode
      xalign -> gfloat: xalign
      yalign -> gfloat: yalign
    
    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
    
    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.KeyvalTrigger</summary>

Object GtkKeyvalTrigger
    
    Properties from GtkKeyvalTrigger:
      keyval -> guint: keyval
      modifiers -> GdkModifierType: modifiers
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.Label</summary>

Object GtkLabel
    
    Signals from GtkLabel:
      activate-link (gchararray) -> gboolean
      move-cursor (GtkMovementStep, gint, gboolean)
      copy-clipboard ()
      activate-current-link ()
    
    Properties from GtkLabel:
      label -> gchararray: label
      attributes -> PangoAttrList: attributes
      use-markup -> gboolean: use-markup
      use-underline -> gboolean: use-underline
      justify -> GtkJustification: justify
      wrap -> gboolean: wrap
      wrap-mode -> PangoWrapMode: wrap-mode
      natural-wrap-mode -> GtkNaturalWrapMode: natural-wrap-mode
      selectable -> gboolean: selectable
      mnemonic-keyval -> guint: mnemonic-keyval
      mnemonic-widget -> GtkWidget: mnemonic-widget
      ellipsize -> PangoEllipsizeMode: ellipsize
      width-chars -> gint: width-chars
      single-line-mode -> gboolean: single-line-mode
      max-width-chars -> gint: max-width-chars
      lines -> gint: lines
      xalign -> gfloat: xalign
      yalign -> gfloat: yalign
      extra-menu -> GMenuModel: extra-menu
      tabs -> PangoTabArray: tabs
    
    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
    
    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.LayoutChild</summary>

Object GtkLayoutChild
    
    Properties from GtkLayoutChild:
      layout-manager -> GtkLayoutManager: layout-manager
      child-widget -> GtkWidget: child-widget
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.LayoutManager</summary>

Object GtkLayoutManager
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.LevelBar</summary>

Object GtkLevelBar
    
    Signals from GtkLevelBar:
      offset-changed (gchararray)
    
    Properties from GtkLevelBar:
      value -> gdouble: value
      min-value -> gdouble: min-value
      max-value -> gdouble: max-value
      mode -> GtkLevelBarMode: mode
      inverted -> gboolean: inverted
    
    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
    
    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.LinkButton</summary>

Object GtkLinkButton
    
    Signals from GtkLinkButton:
      activate-link () -> gboolean
    
    Properties from GtkLinkButton:
      uri -> gchararray: uri
      visited -> gboolean: visited
    
    Signals from GtkButton:
      activate ()
      clicked ()
    
    Properties from GtkButton:
      label -> gchararray: label
      has-frame -> gboolean: has-frame
      use-underline -> gboolean: use-underline
      icon-name -> gchararray: icon-name
      child -> GtkWidget: child
    
    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
    
    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.ListBase</summary>

Object GtkListBase
    
    Properties from GtkListBase:
      orientation -> GtkOrientation: orientation
    
    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
    
    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.ListBox</summary>

Object GtkListBox
    
    Signals from GtkListBox:
      move-cursor (GtkMovementStep, gint, gboolean, gboolean)
      select-all ()
      unselect-all ()
      row-selected (GtkListBoxRow)
      selected-rows-changed ()
      row-activated (GtkListBoxRow)
      activate-cursor-row ()
      toggle-cursor-row ()
    
    Properties from GtkListBox:
      selection-mode -> GtkSelectionMode: selection-mode
      activate-on-single-click -> gboolean: activate-on-single-click
      accept-unpaired-release -> gboolean: accept-unpaired-release
      show-separators -> gboolean: show-separators
    
    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
    
    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.ListBoxRow</summary>

Object GtkListBoxRow
    
    Signals from GtkListBoxRow:
      activate ()
    
    Properties from GtkListBoxRow:
      activatable -> gboolean: activatable
      selectable -> gboolean: selectable
      child -> GtkWidget: child
    
    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
    
    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.ListItem</summary>

Object GtkListItem
    
    Properties from GtkListItem:
      activatable -> gboolean: activatable
      child -> GtkWidget: child
      item -> GObject: item
      position -> guint: position
      selectable -> gboolean: selectable
      selected -> gboolean: selected
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.ListItemFactory</summary>

Object GtkListItemFactory
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.ListStore</summary>

Object GtkListStore
    
    Signals from GtkTreeModel:
      row-changed (GtkTreePath, GtkTreeIter)
      row-inserted (GtkTreePath, GtkTreeIter)
      row-has-child-toggled (GtkTreePath, GtkTreeIter)
      row-deleted (GtkTreePath)
      rows-reordered (GtkTreePath, GtkTreeIter, gpointer)
    
    Signals from GtkTreeSortable:
      sort-column-changed ()
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.ListView</summary>

Object GtkListView
    
    Signals from GtkListView:
      activate (guint)
    
    Properties from GtkListView:
      factory -> GtkListItemFactory: factory
      model -> GtkSelectionModel: model
      show-separators -> gboolean: show-separators
      single-click-activate -> gboolean: single-click-activate
      enable-rubberband -> gboolean: enable-rubberband
    
    Properties from GtkListBase:
      orientation -> GtkOrientation: orientation
    
    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
    
    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.LockButton</summary>

Object GtkLockButton
    
    Properties from GtkLockButton:
      permission -> GPermission: permission
      text-lock -> gchararray: text-lock
      text-unlock -> gchararray: text-unlock
      tooltip-lock -> gchararray: tooltip-lock
      tooltip-unlock -> gchararray: tooltip-unlock
      tooltip-not-authorized -> gchararray: tooltip-not-authorized
    
    Signals from GtkButton:
      activate ()
      clicked ()
    
    Properties from GtkButton:
      label -> gchararray: label
      has-frame -> gboolean: has-frame
      use-underline -> gboolean: use-underline
      icon-name -> gchararray: icon-name
      child -> GtkWidget: child
    
    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
    
    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.MapListModel</summary>

Object GtkMapListModel
    
    Properties from GtkMapListModel:
      has-map -> gboolean: has-map
      item-type -> GType: item-type
      model -> GListModel: model
      n-items -> guint: n-items
    
    Signals from GListModel:
      items-changed (guint, guint, guint)
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.MediaControls</summary>

Object GtkMediaControls
    
    Properties from GtkMediaControls:
      media-stream -> GtkMediaStream: media-stream
    
    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
    
    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.MediaFile</summary>

Object GtkMediaFile
    
    Properties from GtkMediaFile:
      file -> GFile: file
      input-stream -> GInputStream: input-stream
    
    Signals from GdkPaintable:
      invalidate-contents ()
      invalidate-size ()
    
    Properties from GtkMediaStream:
      prepared -> gboolean: prepared
      error -> GError: error
      has-audio -> gboolean: has-audio
      has-video -> gboolean: has-video
      playing -> gboolean: playing
      ended -> gboolean: ended
      timestamp -> gint64: timestamp
      duration -> gint64: duration
      seekable -> gboolean: seekable
      seeking -> gboolean: seeking
      loop -> gboolean: loop
      muted -> gboolean: muted
      volume -> gdouble: volume
    
    Signals from GdkPaintable:
      invalidate-contents ()
      invalidate-size ()
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.MediaStream</summary>

Object GtkMediaStream
    
    Properties from GtkMediaStream:
      prepared -> gboolean: prepared
      error -> GError: error
      has-audio -> gboolean: has-audio
      has-video -> gboolean: has-video
      playing -> gboolean: playing
      ended -> gboolean: ended
      timestamp -> gint64: timestamp
      duration -> gint64: duration
      seekable -> gboolean: seekable
      seeking -> gboolean: seeking
      loop -> gboolean: loop
      muted -> gboolean: muted
      volume -> gdouble: volume
    
    Signals from GdkPaintable:
      invalidate-contents ()
      invalidate-size ()
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.MenuButton</summary>

Object GtkMenuButton
    
    Signals from GtkMenuButton:
      activate ()
    
    Properties from GtkMenuButton:
      menu-model -> GMenuModel: menu-model
      direction -> GtkArrowType: direction
      popover -> GtkPopover: popover
      icon-name -> gchararray: icon-name
      always-show-arrow -> gboolean: always-show-arrow
      label -> gchararray: label
      use-underline -> gboolean: use-underline
      has-frame -> gboolean: has-frame
      primary -> gboolean: primary
      child -> GtkWidget: child
    
    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
    
    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.MessageDialog</summary>

Object GtkMessageDialog
    
    Properties from GtkMessageDialog:
      message-type -> GtkMessageType: message-type
      buttons -> GtkButtonsType: buttons
      text -> gchararray: text
      use-markup -> gboolean: use-markup
      secondary-text -> gchararray: secondary-text
      secondary-use-markup -> gboolean: secondary-use-markup
      message-area -> GtkWidget: message-area
    
    Signals from GtkDialog:
      response (gint)
      close ()
    
    Properties from GtkDialog:
      use-header-bar -> gint: use-header-bar
    
    Signals from GtkWindow:
      activate-focus ()
      activate-default ()
      keys-changed ()
      enable-debugging (gboolean) -> gboolean
      close-request () -> gboolean
    
    Properties from GtkWindow:
      title -> gchararray: title
      resizable -> gboolean: resizable
      modal -> gboolean: modal
      default-width -> gint: default-width
      default-height -> gint: default-height
      destroy-with-parent -> gboolean: destroy-with-parent
      hide-on-close -> gboolean: hide-on-close
      icon-name -> gchararray: icon-name
      display -> GdkDisplay: display
      decorated -> gboolean: decorated
      deletable -> gboolean: deletable
      transient-for -> GtkWindow: transient-for
      application -> GtkApplication: application
      default-widget -> GtkWidget: default-widget
      focus-widget -> GtkWidget: focus-widget
      child -> GtkWidget: child
      titlebar -> GtkWidget: titlebar
      handle-menubar-accel -> gboolean: handle-menubar-accel
      is-active -> gboolean: is-active
      startup-id -> gchararray: startup-id
      mnemonics-visible -> gboolean: mnemonics-visible
      focus-visible -> gboolean: focus-visible
      maximized -> gboolean: maximized
      fullscreened -> gboolean: fullscreened
    
    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
    
    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.MnemonicAction</summary>

Object GtkMnemonicAction
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.MnemonicTrigger</summary>

Object GtkMnemonicTrigger
    
    Properties from GtkMnemonicTrigger:
      keyval -> guint: keyval
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.MountOperation</summary>

Object GtkMountOperation
    
    Properties from GtkMountOperation:
      parent -> GtkWindow: parent
      is-showing -> gboolean: is-showing
      display -> GdkDisplay: display
    
    Signals from GMountOperation:
      ask-password (gchararray, gchararray, gchararray, GAskPasswordFlags)
      ask-question (gchararray, GStrv)
      reply (GMountOperationResult)
      aborted ()
      show-processes (gchararray, GArray, GStrv)
      show-unmount-progress (gchararray, gint64, gint64)
    
    Properties from GMountOperation:
      username -> gchararray: Username
        The user name
      password -> gchararray: Password
        The password
      anonymous -> gboolean: Anonymous
        Whether to use an anonymous user
      domain -> gchararray: Domain
        The domain of the mount operation
      password-save -> GPasswordSave: Password save
        How passwords should be saved
      choice -> gint: Choice
        The users choice
      is-tcrypt-hidden-volume -> gboolean: TCRYPT Hidden Volume
        Whether to unlock a TCRYPT hidden volume. See https://www.veracrypt.fr/en/Hidden%20Volume.html.
      is-tcrypt-system-volume -> gboolean: TCRYPT System Volume
        Whether to unlock a TCRYPT system volume. Only supported for unlocking Windows system volumes. See https://www.veracrypt.fr/en/System%20Encryption.html.
      pim -> guint: PIM
        The VeraCrypt PIM value
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.MultiFilter</summary>

Object GtkMultiFilter
    
    Properties from GtkMultiFilter:
      item-type -> GType: item-type
      n-items -> guint: n-items
    
    Signals from GListModel:
      items-changed (guint, guint, guint)
    
    Signals from GtkFilter:
      changed (GtkFilterChange)
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.MultiSelection</summary>

Object GtkMultiSelection
    
    Properties from GtkMultiSelection:
      item-type -> GType: item-type
      model -> GListModel: model
      n-items -> guint: n-items
    
    Signals from GListModel:
      items-changed (guint, guint, guint)
    
    Signals from GtkSelectionModel:
      selection-changed (guint, guint)
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.MultiSorter</summary>

Object GtkMultiSorter
    
    Properties from GtkMultiSorter:
      item-type -> GType: item-type
      n-items -> guint: n-items
    
    Signals from GListModel:
      items-changed (guint, guint, guint)
    
    Signals from GtkSorter:
      changed (GtkSorterChange)
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.NamedAction</summary>

Object GtkNamedAction
    
    Properties from GtkNamedAction:
      action-name -> gchararray: action-name
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.Native</summary>

Interface GtkNative
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.NativeDialog</summary>

Object GtkNativeDialog
    
    Signals from GtkNativeDialog:
      response (gint)
    
    Properties from GtkNativeDialog:
      title -> gchararray: title
      visible -> gboolean: visible
      modal -> gboolean: modal
      transient-for -> GtkWindow: transient-for
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.NeverTrigger</summary>

Object GtkNeverTrigger
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.NoSelection</summary>

Object GtkNoSelection
    
    Properties from GtkNoSelection:
      item-type -> GType: item-type
      model -> GListModel: model
      n-items -> guint: n-items
    
    Signals from GListModel:
      items-changed (guint, guint, guint)
    
    Signals from GtkSelectionModel:
      selection-changed (guint, guint)
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.Notebook</summary>

Object GtkNotebook
    
    Signals from GtkNotebook:
      switch-page (GtkWidget, guint)
      focus-tab (GtkNotebookTab) -> gboolean
      select-page (gboolean) -> gboolean
      change-current-page (gint) -> gboolean
      move-focus-out (GtkDirectionType)
      reorder-tab (GtkDirectionType, gboolean) -> gboolean
      page-reordered (GtkWidget, guint)
      page-removed (GtkWidget, guint)
      page-added (GtkWidget, guint)
      create-window (GtkWidget) -> GtkNotebook
    
    Properties from GtkNotebook:
      tab-pos -> GtkPositionType: tab-pos
      show-tabs -> gboolean: show-tabs
      show-border -> gboolean: show-border
      scrollable -> gboolean: scrollable
      page -> gint: page
      enable-popup -> gboolean: enable-popup
      group-name -> gchararray: group-name
      pages -> GListModel: pages
    
    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
    
    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.NotebookPage</summary>

Object GtkNotebookPage
    
    Properties from GtkNotebookPage:
      tab-label -> gchararray: tab-label
      menu-label -> gchararray: menu-label
      position -> gint: position
      tab-expand -> gboolean: tab-expand
      tab-fill -> gboolean: tab-fill
      reorderable -> gboolean: reorderable
      detachable -> gboolean: detachable
      child -> GtkWidget: child
      tab -> GtkWidget: tab
      menu -> GtkWidget: menu
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.NothingAction</summary>

Object GtkNothingAction
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.NumericSorter</summary>

Object GtkNumericSorter
    
    Properties from GtkNumericSorter:
      expression -> GtkExpression: expression
      sort-order -> GtkSortType: sort-order
    
    Signals from GtkSorter:
      changed (GtkSorterChange)
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.ObjectExpression</summary>


    :Constructors:
    
    ::
    
        ObjectExpression(**properties)
        new(object:GObject.Object) -> Gtk.ObjectExpression
    

---


</details>

<details><summary>Gtk.Orientable</summary>

Interface GtkOrientable
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.Overlay</summary>

Object GtkOverlay
    
    Signals from GtkOverlay:
      get-child-position (GtkWidget, GdkRectangle) -> gboolean
    
    Properties from GtkOverlay:
      child -> GtkWidget: child
    
    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
    
    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.OverlayLayout</summary>

Object GtkOverlayLayout
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.OverlayLayoutChild</summary>

Object GtkOverlayLayoutChild
    
    Properties from GtkOverlayLayoutChild:
      measure -> gboolean: measure
      clip-overlay -> gboolean: clip-overlay
    
    Properties from GtkLayoutChild:
      layout-manager -> GtkLayoutManager: layout-manager
      child-widget -> GtkWidget: child-widget
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.PadController</summary>

Object GtkPadController
    
    Properties from GtkPadController:
      action-group -> GActionGroup: action-group
      pad -> GdkDevice: pad
    
    Properties from GtkEventController:
      widget -> GtkWidget: widget
      propagation-phase -> GtkPropagationPhase: propagation-phase
      propagation-limit -> GtkPropagationLimit: propagation-limit
      name -> gchararray: name
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.PageSetup</summary>

Object GtkPageSetup
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.PageSetupUnixDialog</summary>

Object GtkPageSetupUnixDialog
    
    Signals from GtkDialog:
      response (gint)
      close ()
    
    Properties from GtkDialog:
      use-header-bar -> gint: use-header-bar
    
    Signals from GtkWindow:
      activate-focus ()
      activate-default ()
      keys-changed ()
      enable-debugging (gboolean) -> gboolean
      close-request () -> gboolean
    
    Properties from GtkWindow:
      title -> gchararray: title
      resizable -> gboolean: resizable
      modal -> gboolean: modal
      default-width -> gint: default-width
      default-height -> gint: default-height
      destroy-with-parent -> gboolean: destroy-with-parent
      hide-on-close -> gboolean: hide-on-close
      icon-name -> gchararray: icon-name
      display -> GdkDisplay: display
      decorated -> gboolean: decorated
      deletable -> gboolean: deletable
      transient-for -> GtkWindow: transient-for
      application -> GtkApplication: application
      default-widget -> GtkWidget: default-widget
      focus-widget -> GtkWidget: focus-widget
      child -> GtkWidget: child
      titlebar -> GtkWidget: titlebar
      handle-menubar-accel -> gboolean: handle-menubar-accel
      is-active -> gboolean: is-active
      startup-id -> gchararray: startup-id
      mnemonics-visible -> gboolean: mnemonics-visible
      focus-visible -> gboolean: focus-visible
      maximized -> gboolean: maximized
      fullscreened -> gboolean: fullscreened
    
    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
    
    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.Paned</summary>

Object GtkPaned
    
    Signals from GtkPaned:
      cycle-child-focus (gboolean) -> gboolean
      toggle-handle-focus () -> gboolean
      move-handle (GtkScrollType) -> gboolean
      cycle-handle-focus (gboolean) -> gboolean
      accept-position () -> gboolean
      cancel-position () -> gboolean
    
    Properties from GtkPaned:
      position -> gint: position
      position-set -> gboolean: position-set
      min-position -> gint: min-position
      max-position -> gint: max-position
      wide-handle -> gboolean: wide-handle
      resize-start-child -> gboolean: resize-start-child
      resize-end-child -> gboolean: resize-end-child
      shrink-start-child -> gboolean: shrink-start-child
      shrink-end-child -> gboolean: shrink-end-child
      start-child -> GtkWidget: start-child
      end-child -> GtkWidget: end-child
    
    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
    
    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.ParamSpecExpression</summary>


    :Constructors:
    
    ::
    
        ParamSpecExpression(**properties)
    

---


</details>

<details><summary>Gtk.PasswordEntry</summary>

Object GtkPasswordEntry
    
    Signals from GtkPasswordEntry:
      activate ()
    
    Properties from GtkPasswordEntry:
      placeholder-text -> gchararray: placeholder-text
      activates-default -> gboolean: activates-default
      show-peek-icon -> gboolean: show-peek-icon
      extra-menu -> GMenuModel: extra-menu
    
    Signals from GtkEditable:
      changed ()
      insert-text (gchararray, gint, gpointer)
      delete-text (gint, gint)
    
    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
    
    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.PasswordEntryBuffer</summary>

Object GtkPasswordEntryBuffer
    
    Signals from GtkEntryBuffer:
      inserted-text (guint, gchararray, guint)
      deleted-text (guint, guint)
    
    Properties from GtkEntryBuffer:
      text -> gchararray: text
      length -> guint: length
      max-length -> gint: max-length
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.Picture</summary>

Object GtkPicture
    
    Properties from GtkPicture:
      paintable -> GdkPaintable: paintable
      file -> GFile: file
      alternative-text -> gchararray: alternative-text
      keep-aspect-ratio -> gboolean: keep-aspect-ratio
      can-shrink -> gboolean: can-shrink
      content-fit -> GtkContentFit: content-fit
    
    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
    
    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.Popover</summary>

Object GtkPopover
    
    Signals from GtkPopover:
      closed ()
      activate-default ()
    
    Properties from GtkPopover:
      pointing-to -> GdkRectangle: pointing-to
      position -> GtkPositionType: position
      autohide -> gboolean: autohide
      default-widget -> GtkWidget: default-widget
      has-arrow -> gboolean: has-arrow
      mnemonics-visible -> gboolean: mnemonics-visible
      child -> GtkWidget: child
      cascade-popdown -> gboolean: cascade-popdown
    
    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
    
    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.PopoverMenu</summary>

Object GtkPopoverMenu
    
    Properties from GtkPopoverMenu:
      visible-submenu -> gchararray: visible-submenu
      menu-model -> GMenuModel: menu-model
    
    Signals from GtkPopover:
      closed ()
      activate-default ()
    
    Properties from GtkPopover:
      pointing-to -> GdkRectangle: pointing-to
      position -> GtkPositionType: position
      autohide -> gboolean: autohide
      default-widget -> GtkWidget: default-widget
      has-arrow -> gboolean: has-arrow
      mnemonics-visible -> gboolean: mnemonics-visible
      child -> GtkWidget: child
      cascade-popdown -> gboolean: cascade-popdown
    
    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
    
    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.PopoverMenuBar</summary>

Object GtkPopoverMenuBar
    
    Properties from GtkPopoverMenuBar:
      menu-model -> GMenuModel: menu-model
    
    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
    
    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.PrintContext</summary>

Object GtkPrintContext
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.PrintJob</summary>

Object GtkPrintJob
    
    Signals from GtkPrintJob:
      status-changed ()
    
    Properties from GtkPrintJob:
      title -> gchararray: title
      printer -> GtkPrinter: printer
      page-setup -> GtkPageSetup: page-setup
      settings -> GtkPrintSettings: settings
      track-print-status -> gboolean: track-print-status
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.PrintOperation</summary>

Object GtkPrintOperation
    
    Signals from GtkPrintOperation:
      status-changed ()
      done (GtkPrintOperationResult)
      begin-print (GtkPrintContext)
      paginate (GtkPrintContext) -> gboolean
      request-page-setup (GtkPrintContext, gint, GtkPageSetup)
      draw-page (GtkPrintContext, gint)
      end-print (GtkPrintContext)
      create-custom-widget () -> GObject
      update-custom-widget (GtkWidget, GtkPageSetup, GtkPrintSettings)
      custom-widget-apply (GtkWidget)
      preview (GtkPrintOperationPreview, GtkPrintContext, GtkWindow) -> gboolean
    
    Properties from GtkPrintOperation:
      default-page-setup -> GtkPageSetup: default-page-setup
      print-settings -> GtkPrintSettings: print-settings
      job-name -> gchararray: job-name
      n-pages -> gint: n-pages
      current-page -> gint: current-page
      use-full-page -> gboolean: use-full-page
      track-print-status -> gboolean: track-print-status
      unit -> GtkUnit: unit
      show-progress -> gboolean: show-progress
      allow-async -> gboolean: allow-async
      export-filename -> gchararray: export-filename
      status -> GtkPrintStatus: status
      status-string -> gchararray: status-string
      custom-tab-label -> gchararray: custom-tab-label
      embed-page-setup -> gboolean: embed-page-setup
      has-selection -> gboolean: has-selection
      support-selection -> gboolean: support-selection
      n-pages-to-print -> gint: n-pages-to-print
    
    Signals from GtkPrintOperationPreview:
      ready (GtkPrintContext)
      got-page-size (GtkPrintContext, GtkPageSetup)
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.PrintOperationPreview</summary>

Interface GtkPrintOperationPreview
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.PrintSettings</summary>

Object GtkPrintSettings
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.PrintUnixDialog</summary>

Object GtkPrintUnixDialog
    
    Properties from GtkPrintUnixDialog:
      page-setup -> GtkPageSetup: page-setup
      current-page -> gint: current-page
      print-settings -> GtkPrintSettings: print-settings
      selected-printer -> GtkPrinter: selected-printer
      manual-capabilities -> GtkPrintCapabilities: manual-capabilities
      support-selection -> gboolean: support-selection
      has-selection -> gboolean: has-selection
      embed-page-setup -> gboolean: embed-page-setup
    
    Signals from GtkDialog:
      response (gint)
      close ()
    
    Properties from GtkDialog:
      use-header-bar -> gint: use-header-bar
    
    Signals from GtkWindow:
      activate-focus ()
      activate-default ()
      keys-changed ()
      enable-debugging (gboolean) -> gboolean
      close-request () -> gboolean
    
    Properties from GtkWindow:
      title -> gchararray: title
      resizable -> gboolean: resizable
      modal -> gboolean: modal
      default-width -> gint: default-width
      default-height -> gint: default-height
      destroy-with-parent -> gboolean: destroy-with-parent
      hide-on-close -> gboolean: hide-on-close
      icon-name -> gchararray: icon-name
      display -> GdkDisplay: display
      decorated -> gboolean: decorated
      deletable -> gboolean: deletable
      transient-for -> GtkWindow: transient-for
      application -> GtkApplication: application
      default-widget -> GtkWidget: default-widget
      focus-widget -> GtkWidget: focus-widget
      child -> GtkWidget: child
      titlebar -> GtkWidget: titlebar
      handle-menubar-accel -> gboolean: handle-menubar-accel
      is-active -> gboolean: is-active
      startup-id -> gchararray: startup-id
      mnemonics-visible -> gboolean: mnemonics-visible
      focus-visible -> gboolean: focus-visible
      maximized -> gboolean: maximized
      fullscreened -> gboolean: fullscreened
    
    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
    
    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.Printer</summary>

Object GtkPrinter
    
    Signals from GtkPrinter:
      details-acquired (gboolean)
    
    Properties from GtkPrinter:
      name -> gchararray: name
      backend -> GtkPrintBackend: backend
      is-virtual -> gboolean: is-virtual
      state-message -> gchararray: state-message
      location -> gchararray: location
      icon-name -> gchararray: icon-name
      job-count -> gint: job-count
      accepts-pdf -> gboolean: accepts-pdf
      accepts-ps -> gboolean: accepts-ps
      paused -> gboolean: paused
      accepting-jobs -> gboolean: accepting-jobs
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.ProgressBar</summary>

Object GtkProgressBar
    
    Properties from GtkProgressBar:
      fraction -> gdouble: fraction
      pulse-step -> gdouble: pulse-step
      inverted -> gboolean: inverted
      text -> gchararray: text
      show-text -> gboolean: show-text
      ellipsize -> PangoEllipsizeMode: ellipsize
    
    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
    
    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.PropertyExpression</summary>


    :Constructors:
    
    ::
    
        PropertyExpression(**properties)
        new(this_type:GType, expression:Gtk.Expression=None, property_name:str) -> Gtk.PropertyExpression
        new_for_pspec(expression:Gtk.Expression=None, pspec:GObject.ParamSpec) -> Gtk.PropertyExpression
    

---


</details>

<details><summary>Gtk.Range</summary>

Object GtkRange
    
    Signals from GtkRange:
      value-changed ()
      adjust-bounds (gdouble)
      move-slider (GtkScrollType)
      change-value (GtkScrollType, gdouble) -> gboolean
    
    Properties from GtkRange:
      adjustment -> GtkAdjustment: adjustment
      inverted -> gboolean: inverted
      show-fill-level -> gboolean: show-fill-level
      restrict-to-fill-level -> gboolean: restrict-to-fill-level
      fill-level -> gdouble: fill-level
      round-digits -> gint: round-digits
    
    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
    
    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.RecentManager</summary>

Object GtkRecentManager
    
    Signals from GtkRecentManager:
      changed ()
    
    Properties from GtkRecentManager:
      filename -> gchararray: filename
      size -> gint: size
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.Revealer</summary>

Object GtkRevealer
    
    Properties from GtkRevealer:
      transition-type -> GtkRevealerTransitionType: transition-type
      transition-duration -> guint: transition-duration
      reveal-child -> gboolean: reveal-child
      child-revealed -> gboolean: child-revealed
      child -> GtkWidget: child
    
    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
    
    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.Root</summary>

Interface GtkRoot
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.Scale</summary>

Object GtkScale
    
    Properties from GtkScale:
      digits -> gint: digits
      draw-value -> gboolean: draw-value
      has-origin -> gboolean: has-origin
      value-pos -> GtkPositionType: value-pos
    
    Signals from GtkRange:
      value-changed ()
      adjust-bounds (gdouble)
      move-slider (GtkScrollType)
      change-value (GtkScrollType, gdouble) -> gboolean
    
    Properties from GtkRange:
      adjustment -> GtkAdjustment: adjustment
      inverted -> gboolean: inverted
      show-fill-level -> gboolean: show-fill-level
      restrict-to-fill-level -> gboolean: restrict-to-fill-level
      fill-level -> gdouble: fill-level
      round-digits -> gint: round-digits
    
    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
    
    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.ScaleButton</summary>

Object GtkScaleButton
    
    Signals from GtkScaleButton:
      value-changed (gdouble)
      popup ()
      popdown ()
    
    Properties from GtkScaleButton:
      value -> gdouble: value
      adjustment -> GtkAdjustment: adjustment
      icons -> GStrv: icons
    
    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
    
    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.Scrollable</summary>

Interface GtkScrollable
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.Scrollbar</summary>

Object GtkScrollbar
    
    Properties from GtkScrollbar:
      adjustment -> GtkAdjustment: adjustment
    
    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
    
    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.ScrolledWindow</summary>

Object GtkScrolledWindow
    
    Signals from GtkScrolledWindow:
      move-focus-out (GtkDirectionType)
      scroll-child (GtkScrollType, gboolean) -> gboolean
      edge-overshot (GtkPositionType)
      edge-reached (GtkPositionType)
    
    Properties from GtkScrolledWindow:
      hadjustment -> GtkAdjustment: hadjustment
      vadjustment -> GtkAdjustment: vadjustment
      hscrollbar-policy -> GtkPolicyType: hscrollbar-policy
      vscrollbar-policy -> GtkPolicyType: vscrollbar-policy
      window-placement -> GtkCornerType: window-placement
      has-frame -> gboolean: has-frame
      min-content-width -> gint: min-content-width
      min-content-height -> gint: min-content-height
      kinetic-scrolling -> gboolean: kinetic-scrolling
      overlay-scrolling -> gboolean: overlay-scrolling
      max-content-width -> gint: max-content-width
      max-content-height -> gint: max-content-height
      propagate-natural-width -> gboolean: propagate-natural-width
      propagate-natural-height -> gboolean: propagate-natural-height
      child -> GtkWidget: child
    
    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
    
    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.SearchBar</summary>

Object GtkSearchBar
    
    Properties from GtkSearchBar:
      search-mode-enabled -> gboolean: search-mode-enabled
      show-close-button -> gboolean: show-close-button
      child -> GtkWidget: child
      key-capture-widget -> GtkWidget: key-capture-widget
    
    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
    
    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.SearchEntry</summary>

Object GtkSearchEntry
    
    Signals from GtkSearchEntry:
      activate ()
      search-changed ()
      next-match ()
      previous-match ()
      stop-search ()
      search-started ()
    
    Properties from GtkSearchEntry:
      placeholder-text -> gchararray: placeholder-text
      activates-default -> gboolean: activates-default
      search-delay -> guint: search-delay
    
    Signals from GtkEditable:
      changed ()
      insert-text (gchararray, gint, gpointer)
      delete-text (gint, gint)
    
    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
    
    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.SelectionFilterModel</summary>

Object GtkSelectionFilterModel
    
    Properties from GtkSelectionFilterModel:
      item-type -> GType: item-type
      model -> GtkSelectionModel: model
      n-items -> guint: n-items
    
    Signals from GListModel:
      items-changed (guint, guint, guint)
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.SelectionModel</summary>

Interface GtkSelectionModel
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.Separator</summary>

Object GtkSeparator
    
    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
    
    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.Settings</summary>

Object GtkSettings
    
    Properties from GtkSettings:
      gtk-double-click-time -> gint: gtk-double-click-time
      gtk-double-click-distance -> gint: gtk-double-click-distance
      gtk-cursor-blink -> gboolean: gtk-cursor-blink
      gtk-cursor-blink-time -> gint: gtk-cursor-blink-time
      gtk-cursor-blink-timeout -> gint: gtk-cursor-blink-timeout
      gtk-split-cursor -> gboolean: gtk-split-cursor
      gtk-cursor-aspect-ratio -> gdouble: gtk-cursor-aspect-ratio
      gtk-theme-name -> gchararray: gtk-theme-name
      gtk-icon-theme-name -> gchararray: gtk-icon-theme-name
      gtk-dnd-drag-threshold -> gint: gtk-dnd-drag-threshold
      gtk-font-name -> gchararray: gtk-font-name
      gtk-xft-antialias -> gint: gtk-xft-antialias
      gtk-xft-hinting -> gint: gtk-xft-hinting
      gtk-xft-hintstyle -> gchararray: gtk-xft-hintstyle
      gtk-xft-rgba -> gchararray: gtk-xft-rgba
      gtk-xft-dpi -> gint: gtk-xft-dpi
      gtk-hint-font-metrics -> gboolean: gtk-hint-font-metrics
      gtk-cursor-theme-name -> gchararray: gtk-cursor-theme-name
      gtk-cursor-theme-size -> gint: gtk-cursor-theme-size
      gtk-alternative-button-order -> gboolean: gtk-alternative-button-order
      gtk-alternative-sort-arrows -> gboolean: gtk-alternative-sort-arrows
      gtk-enable-animations -> gboolean: gtk-enable-animations
      gtk-error-bell -> gboolean: gtk-error-bell
      gtk-print-backends -> gchararray: gtk-print-backends
      gtk-print-preview-command -> gchararray: gtk-print-preview-command
      gtk-enable-accels -> gboolean: gtk-enable-accels
      gtk-im-module -> gchararray: gtk-im-module
      gtk-recent-files-max-age -> gint: gtk-recent-files-max-age
      gtk-fontconfig-timestamp -> guint: gtk-fontconfig-timestamp
      gtk-sound-theme-name -> gchararray: gtk-sound-theme-name
      gtk-enable-input-feedback-sounds -> gboolean: gtk-enable-input-feedback-sounds
      gtk-enable-event-sounds -> gboolean: gtk-enable-event-sounds
      gtk-primary-button-warps-slider -> gboolean: gtk-primary-button-warps-slider
      gtk-application-prefer-dark-theme -> gboolean: gtk-application-prefer-dark-theme
      gtk-entry-select-on-focus -> gboolean: gtk-entry-select-on-focus
      gtk-entry-password-hint-timeout -> guint: gtk-entry-password-hint-timeout
      gtk-label-select-on-focus -> gboolean: gtk-label-select-on-focus
      gtk-shell-shows-app-menu -> gboolean: gtk-shell-shows-app-menu
      gtk-shell-shows-menubar -> gboolean: gtk-shell-shows-menubar
      gtk-shell-shows-desktop -> gboolean: gtk-shell-shows-desktop
      gtk-decoration-layout -> gchararray: gtk-decoration-layout
      gtk-titlebar-double-click -> gchararray: gtk-titlebar-double-click
      gtk-titlebar-middle-click -> gchararray: gtk-titlebar-middle-click
      gtk-titlebar-right-click -> gchararray: gtk-titlebar-right-click
      gtk-dialogs-use-header -> gboolean: gtk-dialogs-use-header
      gtk-enable-primary-paste -> gboolean: gtk-enable-primary-paste
      gtk-recent-files-enabled -> gboolean: gtk-recent-files-enabled
      gtk-long-press-time -> guint: gtk-long-press-time
      gtk-keynav-use-caret -> gboolean: gtk-keynav-use-caret
      gtk-overlay-scrolling -> gboolean: gtk-overlay-scrolling
    
    Signals from GtkStyleProvider:
      gtk-private-changed ()
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.Shortcut</summary>

Object GtkShortcut
    
    Properties from GtkShortcut:
      action -> GtkShortcutAction: action
      arguments -> GVariant: arguments
      trigger -> GtkShortcutTrigger: trigger
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.ShortcutAction</summary>

Object GtkShortcutAction
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.ShortcutController</summary>

Object GtkShortcutController
    
    Properties from GtkShortcutController:
      item-type -> GType: item-type
      mnemonic-modifiers -> GdkModifierType: mnemonic-modifiers
      model -> GListModel: model
      n-items -> guint: n-items
      scope -> GtkShortcutScope: scope
    
    Signals from GListModel:
      items-changed (guint, guint, guint)
    
    Properties from GtkEventController:
      widget -> GtkWidget: widget
      propagation-phase -> GtkPropagationPhase: propagation-phase
      propagation-limit -> GtkPropagationLimit: propagation-limit
      name -> gchararray: name
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.ShortcutLabel</summary>

Object GtkShortcutLabel
    
    Properties from GtkShortcutLabel:
      accelerator -> gchararray: accelerator
      disabled-text -> gchararray: disabled-text
    
    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
    
    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.ShortcutManager</summary>

Interface GtkShortcutManager
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.ShortcutTrigger</summary>

Object GtkShortcutTrigger
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.ShortcutsGroup</summary>

Object GtkShortcutsGroup
    
    Properties from GtkShortcutsGroup:
      title -> gchararray: title
      view -> gchararray: view
      accel-size-group -> GtkSizeGroup: accel-size-group
      title-size-group -> GtkSizeGroup: title-size-group
      height -> guint: height
    
    Properties from GtkBox:
      spacing -> gint: spacing
      homogeneous -> gboolean: homogeneous
      baseline-position -> GtkBaselinePosition: baseline-position
    
    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
    
    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.ShortcutsSection</summary>

Object GtkShortcutsSection
    
    Signals from GtkShortcutsSection:
      change-current-page (gint) -> gboolean
    
    Properties from GtkShortcutsSection:
      title -> gchararray: title
      section-name -> gchararray: section-name
      view-name -> gchararray: view-name
      max-height -> guint: max-height
    
    Properties from GtkBox:
      spacing -> gint: spacing
      homogeneous -> gboolean: homogeneous
      baseline-position -> GtkBaselinePosition: baseline-position
    
    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
    
    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.ShortcutsShortcut</summary>

Object GtkShortcutsShortcut
    
    Properties from GtkShortcutsShortcut:
      accelerator -> gchararray: accelerator
      icon -> GIcon: icon
      icon-set -> gboolean: icon-set
      title -> gchararray: title
      subtitle -> gchararray: subtitle
      subtitle-set -> gboolean: subtitle-set
      accel-size-group -> GtkSizeGroup: accel-size-group
      title-size-group -> GtkSizeGroup: title-size-group
      direction -> GtkTextDirection: direction
      shortcut-type -> GtkShortcutType: shortcut-type
      action-name -> gchararray: action-name
    
    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
    
    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.ShortcutsWindow</summary>

Object GtkShortcutsWindow
    
    Signals from GtkShortcutsWindow:
      close ()
      search ()
    
    Properties from GtkShortcutsWindow:
      section-name -> gchararray: section-name
      view-name -> gchararray: view-name
    
    Signals from GtkWindow:
      activate-focus ()
      activate-default ()
      keys-changed ()
      enable-debugging (gboolean) -> gboolean
      close-request () -> gboolean
    
    Properties from GtkWindow:
      title -> gchararray: title
      resizable -> gboolean: resizable
      modal -> gboolean: modal
      default-width -> gint: default-width
      default-height -> gint: default-height
      destroy-with-parent -> gboolean: destroy-with-parent
      hide-on-close -> gboolean: hide-on-close
      icon-name -> gchararray: icon-name
      display -> GdkDisplay: display
      decorated -> gboolean: decorated
      deletable -> gboolean: deletable
      transient-for -> GtkWindow: transient-for
      application -> GtkApplication: application
      default-widget -> GtkWidget: default-widget
      focus-widget -> GtkWidget: focus-widget
      child -> GtkWidget: child
      titlebar -> GtkWidget: titlebar
      handle-menubar-accel -> gboolean: handle-menubar-accel
      is-active -> gboolean: is-active
      startup-id -> gchararray: startup-id
      mnemonics-visible -> gboolean: mnemonics-visible
      focus-visible -> gboolean: focus-visible
      maximized -> gboolean: maximized
      fullscreened -> gboolean: fullscreened
    
    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
    
    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.SignalAction</summary>

Object GtkSignalAction
    
    Properties from GtkSignalAction:
      signal-name -> gchararray: signal-name
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.SignalListItemFactory</summary>

Object GtkSignalListItemFactory
    
    Signals from GtkSignalListItemFactory:
      setup (GObject)
      bind (GObject)
      unbind (GObject)
      teardown (GObject)
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.SingleSelection</summary>

Object GtkSingleSelection
    
    Properties from GtkSingleSelection:
      autoselect -> gboolean: autoselect
      can-unselect -> gboolean: can-unselect
      item-type -> GType: item-type
      model -> GListModel: model
      n-items -> guint: n-items
      selected -> guint: selected
      selected-item -> GObject: selected-item
    
    Signals from GListModel:
      items-changed (guint, guint, guint)
    
    Signals from GtkSelectionModel:
      selection-changed (guint, guint)
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.SizeGroup</summary>

Object GtkSizeGroup
    
    Properties from GtkSizeGroup:
      mode -> GtkSizeGroupMode: mode
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.SliceListModel</summary>

Object GtkSliceListModel
    
    Properties from GtkSliceListModel:
      item-type -> GType: item-type
      model -> GListModel: model
      n-items -> guint: n-items
      offset -> guint: offset
      size -> guint: size
    
    Signals from GListModel:
      items-changed (guint, guint, guint)
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.Snapshot</summary>

Object GtkSnapshot
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.SortListModel</summary>

Object GtkSortListModel
    
    Properties from GtkSortListModel:
      incremental -> gboolean: incremental
      item-type -> GType: item-type
      model -> GListModel: model
      n-items -> guint: n-items
      pending -> guint: pending
      sorter -> GtkSorter: sorter
    
    Signals from GListModel:
      items-changed (guint, guint, guint)
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.Sorter</summary>

Object GtkSorter
    
    Signals from GtkSorter:
      changed (GtkSorterChange)
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.SpinButton</summary>

Object GtkSpinButton
    
    Signals from GtkSpinButton:
      value-changed ()
      change-value (GtkScrollType)
      input (gpointer) -> gint
      output () -> gboolean
      wrapped ()
    
    Properties from GtkSpinButton:
      adjustment -> GtkAdjustment: adjustment
      climb-rate -> gdouble: climb-rate
      digits -> guint: digits
      snap-to-ticks -> gboolean: snap-to-ticks
      numeric -> gboolean: numeric
      wrap -> gboolean: wrap
      update-policy -> GtkSpinButtonUpdatePolicy: update-policy
      value -> gdouble: value
    
    Signals from GtkEditable:
      changed ()
      insert-text (gchararray, gint, gpointer)
      delete-text (gint, gint)
    
    Signals from GtkCellEditable:
      editing-done ()
      remove-widget ()
    
    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
    
    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.Spinner</summary>

Object GtkSpinner
    
    Properties from GtkSpinner:
      spinning -> gboolean: spinning
    
    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
    
    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.Stack</summary>

Object GtkStack
    
    Properties from GtkStack:
      hhomogeneous -> gboolean: hhomogeneous
      vhomogeneous -> gboolean: vhomogeneous
      visible-child -> GtkWidget: visible-child
      visible-child-name -> gchararray: visible-child-name
      transition-duration -> guint: transition-duration
      transition-type -> GtkStackTransitionType: transition-type
      transition-running -> gboolean: transition-running
      interpolate-size -> gboolean: interpolate-size
      pages -> GtkSelectionModel: pages
    
    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
    
    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.StackPage</summary>

Object GtkStackPage
    
    Properties from GtkStackPage:
      child -> GtkWidget: child
      name -> gchararray: name
      title -> gchararray: title
      icon-name -> gchararray: icon-name
      needs-attention -> gboolean: needs-attention
      visible -> gboolean: visible
      use-underline -> gboolean: use-underline
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.StackSidebar</summary>

Object GtkStackSidebar
    
    Properties from GtkStackSidebar:
      stack -> GtkStack: stack
    
    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
    
    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.StackSwitcher</summary>

Object GtkStackSwitcher
    
    Properties from GtkStackSwitcher:
      stack -> GtkStack: stack
    
    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
    
    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.Statusbar</summary>

Object GtkStatusbar
    
    Signals from GtkStatusbar:
      text-pushed (guint, gchararray)
      text-popped (guint, gchararray)
    
    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
    
    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.StringFilter</summary>

Object GtkStringFilter
    
    Properties from GtkStringFilter:
      expression -> GtkExpression: expression
      ignore-case -> gboolean: ignore-case
      match-mode -> GtkStringFilterMatchMode: match-mode
      search -> gchararray: search
    
    Signals from GtkFilter:
      changed (GtkFilterChange)
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.StringList</summary>

Object GtkStringList
    
    Signals from GListModel:
      items-changed (guint, guint, guint)
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.StringObject</summary>

Object GtkStringObject
    
    Properties from GtkStringObject:
      string -> gchararray: string
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.StringSorter</summary>

Object GtkStringSorter
    
    Properties from GtkStringSorter:
      expression -> GtkExpression: expression
      ignore-case -> gboolean: ignore-case
    
    Signals from GtkSorter:
      changed (GtkSorterChange)
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.StyleContext</summary>

Object GtkStyleContext
    
    Properties from GtkStyleContext:
      display -> GdkDisplay: display
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.StyleProvider</summary>

Interface GtkStyleProvider
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.Switch</summary>

Object GtkSwitch
    
    Signals from GtkSwitch:
      activate ()
      state-set (gboolean) -> gboolean
    
    Properties from GtkSwitch:
      active -> gboolean: active
      state -> gboolean: state
    
    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
    
    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.SymbolicPaintable</summary>

Interface GtkSymbolicPaintable
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.Text</summary>

Object GtkText
    
    Signals from GtkText:
      activate ()
      move-cursor (GtkMovementStep, gint, gboolean)
      preedit-changed (gchararray)
      copy-clipboard ()
      insert-at-cursor (gchararray)
      delete-from-cursor (GtkDeleteType, gint)
      backspace ()
      cut-clipboard ()
      paste-clipboard ()
      toggle-overwrite ()
      insert-emoji ()
    
    Properties from GtkText:
      buffer -> GtkEntryBuffer: buffer
      max-length -> gint: max-length
      visibility -> gboolean: visibility
      invisible-char -> guint: invisible-char
      invisible-char-set -> gboolean: invisible-char-set
      activates-default -> gboolean: activates-default
      scroll-offset -> gint: scroll-offset
      truncate-multiline -> gboolean: truncate-multiline
      overwrite-mode -> gboolean: overwrite-mode
      im-module -> gchararray: im-module
      placeholder-text -> gchararray: placeholder-text
      input-purpose -> GtkInputPurpose: input-purpose
      input-hints -> GtkInputHints: input-hints
      attributes -> PangoAttrList: attributes
      tabs -> PangoTabArray: tabs
      enable-emoji-completion -> gboolean: enable-emoji-completion
      propagate-text-width -> gboolean: propagate-text-width
      extra-menu -> GMenuModel: extra-menu
    
    Signals from GtkEditable:
      changed ()
      insert-text (gchararray, gint, gpointer)
      delete-text (gint, gint)
    
    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
    
    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.TextBuffer</summary>

Object GtkTextBuffer
    
    Signals from GtkTextBuffer:
      changed ()
      insert-text (GtkTextIter, gchararray, gint)
      insert-paintable (GtkTextIter, GdkPaintable)
      insert-child-anchor (GtkTextIter, GtkTextChildAnchor)
      delete-range (GtkTextIter, GtkTextIter)
      modified-changed ()
      mark-set (GtkTextIter, GtkTextMark)
      mark-deleted (GtkTextMark)
      apply-tag (GtkTextTag, GtkTextIter, GtkTextIter)
      remove-tag (GtkTextTag, GtkTextIter, GtkTextIter)
      begin-user-action ()
      end-user-action ()
      paste-done (GdkClipboard)
      redo ()
      undo ()
    
    Properties from GtkTextBuffer:
      tag-table -> GtkTextTagTable: tag-table
      text -> gchararray: text
      has-selection -> gboolean: has-selection
      cursor-position -> gint: cursor-position
      can-undo -> gboolean: can-undo
      can-redo -> gboolean: can-redo
      enable-undo -> gboolean: enable-undo
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.TextChildAnchor</summary>

Object GtkTextChildAnchor
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.TextMark</summary>

Object GtkTextMark
    
    Properties from GtkTextMark:
      name -> gchararray: name
      left-gravity -> gboolean: left-gravity
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.TextTag</summary>

Object GtkTextTag
    
    Properties from GtkTextTag:
      name -> gchararray: name
      background -> gchararray: background
      foreground -> gchararray: foreground
      background-rgba -> GdkRGBA: background-rgba
      foreground-rgba -> GdkRGBA: foreground-rgba
      font -> gchararray: font
      font-desc -> PangoFontDescription: font-desc
      family -> gchararray: family
      style -> PangoStyle: style
      variant -> PangoVariant: variant
      weight -> gint: weight
      stretch -> PangoStretch: stretch
      size -> gint: size
      size-points -> gdouble: size-points
      scale -> gdouble: scale
      pixels-above-lines -> gint: pixels-above-lines
      pixels-below-lines -> gint: pixels-below-lines
      pixels-inside-wrap -> gint: pixels-inside-wrap
      line-height -> gfloat: line-height
      editable -> gboolean: editable
      wrap-mode -> GtkWrapMode: wrap-mode
      justification -> GtkJustification: justification
      direction -> GtkTextDirection: direction
      left-margin -> gint: left-margin
      indent -> gint: indent
      strikethrough -> gboolean: strikethrough
      strikethrough-rgba -> GdkRGBA: strikethrough-rgba
      right-margin -> gint: right-margin
      underline -> PangoUnderline: underline
      underline-rgba -> GdkRGBA: underline-rgba
      overline -> PangoOverline: overline
      overline-rgba -> GdkRGBA: overline-rgba
      rise -> gint: rise
      background-full-height -> gboolean: background-full-height
      language -> gchararray: language
      tabs -> PangoTabArray: tabs
      invisible -> gboolean: invisible
      paragraph-background -> gchararray: paragraph-background
      paragraph-background-rgba -> GdkRGBA: paragraph-background-rgba
      fallback -> gboolean: fallback
      letter-spacing -> gint: letter-spacing
      font-features -> gchararray: font-features
      allow-breaks -> gboolean: allow-breaks
      show-spaces -> PangoShowFlags: show-spaces
      insert-hyphens -> gboolean: insert-hyphens
      text-transform -> PangoTextTransform: text-transform
      word -> gboolean: word
      sentence -> gboolean: sentence
      accumulative-margin -> gboolean: accumulative-margin
      background-set -> gboolean: background-set
      foreground-set -> gboolean: foreground-set
      family-set -> gboolean: family-set
      style-set -> gboolean: style-set
      variant-set -> gboolean: variant-set
      weight-set -> gboolean: weight-set
      stretch-set -> gboolean: stretch-set
      size-set -> gboolean: size-set
      scale-set -> gboolean: scale-set
      pixels-above-lines-set -> gboolean: pixels-above-lines-set
      pixels-below-lines-set -> gboolean: pixels-below-lines-set
      pixels-inside-wrap-set -> gboolean: pixels-inside-wrap-set
      line-height-set -> gboolean: line-height-set
      editable-set -> gboolean: editable-set
      wrap-mode-set -> gboolean: wrap-mode-set
      justification-set -> gboolean: justification-set
      left-margin-set -> gboolean: left-margin-set
      indent-set -> gboolean: indent-set
      strikethrough-set -> gboolean: strikethrough-set
      strikethrough-rgba-set -> gboolean: strikethrough-rgba-set
      right-margin-set -> gboolean: right-margin-set
      underline-set -> gboolean: underline-set
      underline-rgba-set -> gboolean: underline-rgba-set
      overline-set -> gboolean: overline-set
      overline-rgba-set -> gboolean: overline-rgba-set
      rise-set -> gboolean: rise-set
      background-full-height-set -> gboolean: background-full-height-set
      language-set -> gboolean: language-set
      tabs-set -> gboolean: tabs-set
      invisible-set -> gboolean: invisible-set
      paragraph-background-set -> gboolean: paragraph-background-set
      fallback-set -> gboolean: fallback-set
      letter-spacing-set -> gboolean: letter-spacing-set
      font-features-set -> gboolean: font-features-set
      allow-breaks-set -> gboolean: allow-breaks-set
      show-spaces-set -> gboolean: show-spaces-set
      insert-hyphens-set -> gboolean: insert-hyphens-set
      text-transform-set -> gboolean: text-transform-set
      sentence-set -> gboolean: sentence-set
      word-set -> gboolean: word-set
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.TextTagTable</summary>

Object GtkTextTagTable
    
    Signals from GtkTextTagTable:
      tag-changed (GtkTextTag, gboolean)
      tag-added (GtkTextTag)
      tag-removed (GtkTextTag)
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.TextView</summary>

Object GtkTextView
    
    Signals from GtkTextView:
      move-cursor (GtkMovementStep, gint, gboolean)
      select-all (gboolean)
      preedit-changed (gchararray)
      copy-clipboard ()
      insert-at-cursor (gchararray)
      delete-from-cursor (GtkDeleteType, gint)
      backspace ()
      cut-clipboard ()
      paste-clipboard ()
      toggle-overwrite ()
      insert-emoji ()
      move-viewport (GtkScrollStep, gint)
      set-anchor ()
      toggle-cursor-visible ()
      extend-selection (GtkTextExtendSelection, GtkTextIter, GtkTextIter, GtkTextIter) -> gboolean
    
    Properties from GtkTextView:
      pixels-above-lines -> gint: pixels-above-lines
      pixels-below-lines -> gint: pixels-below-lines
      pixels-inside-wrap -> gint: pixels-inside-wrap
      editable -> gboolean: editable
      wrap-mode -> GtkWrapMode: wrap-mode
      justification -> GtkJustification: justification
      left-margin -> gint: left-margin
      right-margin -> gint: right-margin
      top-margin -> gint: top-margin
      bottom-margin -> gint: bottom-margin
      indent -> gint: indent
      tabs -> PangoTabArray: tabs
      cursor-visible -> gboolean: cursor-visible
      buffer -> GtkTextBuffer: buffer
      overwrite -> gboolean: overwrite
      accepts-tab -> gboolean: accepts-tab
      im-module -> gchararray: im-module
      input-purpose -> GtkInputPurpose: input-purpose
      input-hints -> GtkInputHints: input-hints
      monospace -> gboolean: monospace
      extra-menu -> GMenuModel: extra-menu
    
    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
    
    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.ToggleButton</summary>

Object GtkToggleButton
    
    Signals from GtkToggleButton:
      toggled ()
    
    Properties from GtkToggleButton:
      active -> gboolean: active
      group -> GtkToggleButton: group
    
    Signals from GtkButton:
      activate ()
      clicked ()
    
    Properties from GtkButton:
      label -> gchararray: label
      has-frame -> gboolean: has-frame
      use-underline -> gboolean: use-underline
      icon-name -> gchararray: icon-name
      child -> GtkWidget: child
    
    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
    
    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.Tooltip</summary>

Object GtkTooltip
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.TreeDragDest</summary>

Interface GtkTreeDragDest
    
    

---


</details>

<details><summary>Gtk.TreeDragSource</summary>

Interface GtkTreeDragSource
    
    

---


</details>

<details><summary>Gtk.TreeExpander</summary>

Object GtkTreeExpander
    
    Properties from GtkTreeExpander:
      child -> GtkWidget: child
      item -> GObject: item
      list-row -> GtkTreeListRow: list-row
      indent-for-icon -> gboolean: indent-for-icon
    
    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
    
    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.TreeListModel</summary>

Object GtkTreeListModel
    
    Properties from GtkTreeListModel:
      autoexpand -> gboolean: autoexpand
      item-type -> GType: item-type
      model -> GListModel: model
      n-items -> guint: n-items
      passthrough -> gboolean: passthrough
    
    Signals from GListModel:
      items-changed (guint, guint, guint)
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.TreeListRow</summary>

Object GtkTreeListRow
    
    Properties from GtkTreeListRow:
      children -> GListModel: children
      depth -> guint: depth
      expandable -> gboolean: expandable
      expanded -> gboolean: expanded
      item -> GObject: item
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.TreeListRowSorter</summary>

Object GtkTreeListRowSorter
    
    Properties from GtkTreeListRowSorter:
      sorter -> GtkSorter: sorter
    
    Signals from GtkSorter:
      changed (GtkSorterChange)
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.TreeModel</summary>

Interface GtkTreeModel
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.TreeModelFilter</summary>

Object GtkTreeModelFilter
    
    Properties from GtkTreeModelFilter:
      child-model -> GtkTreeModel: child-model
      virtual-root -> GtkTreePath: virtual-root
    
    Signals from GtkTreeModel:
      row-changed (GtkTreePath, GtkTreeIter)
      row-inserted (GtkTreePath, GtkTreeIter)
      row-has-child-toggled (GtkTreePath, GtkTreeIter)
      row-deleted (GtkTreePath)
      rows-reordered (GtkTreePath, GtkTreeIter, gpointer)
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.TreeModelSort</summary>

Object GtkTreeModelSort
    
    Properties from GtkTreeModelSort:
      model -> GtkTreeModel: model
    
    Signals from GtkTreeModel:
      row-changed (GtkTreePath, GtkTreeIter)
      row-inserted (GtkTreePath, GtkTreeIter)
      row-has-child-toggled (GtkTreePath, GtkTreeIter)
      row-deleted (GtkTreePath)
      rows-reordered (GtkTreePath, GtkTreeIter, gpointer)
    
    Signals from GtkTreeSortable:
      sort-column-changed ()
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.TreeSelection</summary>

Object GtkTreeSelection
    
    Signals from GtkTreeSelection:
      changed ()
    
    Properties from GtkTreeSelection:
      mode -> GtkSelectionMode: mode
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.TreeSortable</summary>

Interface GtkTreeSortable
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.TreeStore</summary>

Object GtkTreeStore
    
    Signals from GtkTreeModel:
      row-changed (GtkTreePath, GtkTreeIter)
      row-inserted (GtkTreePath, GtkTreeIter)
      row-has-child-toggled (GtkTreePath, GtkTreeIter)
      row-deleted (GtkTreePath)
      rows-reordered (GtkTreePath, GtkTreeIter, gpointer)
    
    Signals from GtkTreeSortable:
      sort-column-changed ()
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.TreeView</summary>

Object GtkTreeView
    
    Signals from GtkTreeView:
      move-cursor (GtkMovementStep, gint, gboolean, gboolean) -> gboolean
      select-all () -> gboolean
      unselect-all () -> gboolean
      row-activated (GtkTreePath, GtkTreeViewColumn)
      toggle-cursor-row () -> gboolean
      test-expand-row (GtkTreeIter, GtkTreePath) -> gboolean
      test-collapse-row (GtkTreeIter, GtkTreePath) -> gboolean
      row-expanded (GtkTreeIter, GtkTreePath)
      row-collapsed (GtkTreeIter, GtkTreePath)
      columns-changed ()
      cursor-changed ()
      select-cursor-row (gboolean) -> gboolean
      expand-collapse-cursor-row (gboolean, gboolean, gboolean) -> gboolean
      select-cursor-parent () -> gboolean
      start-interactive-search () -> gboolean
    
    Properties from GtkTreeView:
      model -> GtkTreeModel: model
      headers-visible -> gboolean: headers-visible
      headers-clickable -> gboolean: headers-clickable
      expander-column -> GtkTreeViewColumn: expander-column
      reorderable -> gboolean: reorderable
      enable-search -> gboolean: enable-search
      search-column -> gint: search-column
      fixed-height-mode -> gboolean: fixed-height-mode
      hover-selection -> gboolean: hover-selection
      hover-expand -> gboolean: hover-expand
      show-expanders -> gboolean: show-expanders
      level-indentation -> gint: level-indentation
      rubber-banding -> gboolean: rubber-banding
      enable-grid-lines -> GtkTreeViewGridLines: enable-grid-lines
      enable-tree-lines -> gboolean: enable-tree-lines
      tooltip-column -> gint: tooltip-column
      activate-on-single-click -> gboolean: activate-on-single-click
    
    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
    
    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.TreeViewColumn</summary>

Object GtkTreeViewColumn
    
    Signals from GtkTreeViewColumn:
      clicked ()
    
    Properties from GtkTreeViewColumn:
      visible -> gboolean: visible
      resizable -> gboolean: resizable
      x-offset -> gint: x-offset
      width -> gint: width
      spacing -> gint: spacing
      sizing -> GtkTreeViewColumnSizing: sizing
      fixed-width -> gint: fixed-width
      min-width -> gint: min-width
      max-width -> gint: max-width
      title -> gchararray: title
      expand -> gboolean: expand
      clickable -> gboolean: clickable
      widget -> GtkWidget: widget
      alignment -> gfloat: alignment
      reorderable -> gboolean: reorderable
      sort-indicator -> gboolean: sort-indicator
      sort-order -> GtkSortType: sort-order
      sort-column-id -> gint: sort-column-id
      cell-area -> GtkCellArea: cell-area
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.Video</summary>

Object GtkVideo
    
    Properties from GtkVideo:
      autoplay -> gboolean: autoplay
      file -> GFile: file
      loop -> gboolean: loop
      media-stream -> GtkMediaStream: media-stream
    
    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
    
    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.Viewport</summary>

Object GtkViewport
    
    Properties from GtkViewport:
      scroll-to-focus -> gboolean: scroll-to-focus
      child -> GtkWidget: child
    
    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
    
    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.VolumeButton</summary>

Object GtkVolumeButton
    
    Properties from GtkVolumeButton:
      use-symbolic -> gboolean: use-symbolic
    
    Signals from GtkScaleButton:
      value-changed (gdouble)
      popup ()
      popdown ()
    
    Properties from GtkScaleButton:
      value -> gdouble: value
      adjustment -> GtkAdjustment: adjustment
      icons -> GStrv: icons
    
    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
    
    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.Widget</summary>

Object GtkWidget
    
    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
    
    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.WidgetPaintable</summary>

Object GtkWidgetPaintable
    
    Properties from GtkWidgetPaintable:
      widget -> GtkWidget: widget
    
    Signals from GdkPaintable:
      invalidate-contents ()
      invalidate-size ()
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.Window</summary>

Object GtkWindow
    
    Signals from GtkWindow:
      activate-focus ()
      activate-default ()
      keys-changed ()
      enable-debugging (gboolean) -> gboolean
      close-request () -> gboolean
    
    Properties from GtkWindow:
      title -> gchararray: title
      resizable -> gboolean: resizable
      modal -> gboolean: modal
      default-width -> gint: default-width
      default-height -> gint: default-height
      destroy-with-parent -> gboolean: destroy-with-parent
      hide-on-close -> gboolean: hide-on-close
      icon-name -> gchararray: icon-name
      display -> GdkDisplay: display
      decorated -> gboolean: decorated
      deletable -> gboolean: deletable
      transient-for -> GtkWindow: transient-for
      application -> GtkApplication: application
      default-widget -> GtkWidget: default-widget
      focus-widget -> GtkWidget: focus-widget
      child -> GtkWidget: child
      titlebar -> GtkWidget: titlebar
      handle-menubar-accel -> gboolean: handle-menubar-accel
      is-active -> gboolean: is-active
      startup-id -> gchararray: startup-id
      mnemonics-visible -> gboolean: mnemonics-visible
      focus-visible -> gboolean: focus-visible
      maximized -> gboolean: maximized
      fullscreened -> gboolean: fullscreened
    
    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
    
    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.WindowControls</summary>

Object GtkWindowControls
    
    Properties from GtkWindowControls:
      side -> GtkPackType: side
      decoration-layout -> gchararray: decoration-layout
      empty -> gboolean: empty
    
    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
    
    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.WindowGroup</summary>

Object GtkWindowGroup
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Gtk.WindowHandle</summary>

Object GtkWindowHandle
    
    Properties from GtkWindowHandle:
      child -> GtkWidget: child
    
    Signals from GtkWidget:
      destroy ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      state-flags-changed (GtkStateFlags)
      direction-changed (GtkTextDirection)
      mnemonic-activate (gboolean) -> gboolean
      move-focus (GtkDirectionType)
      keynav-failed (GtkDirectionType) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
    
    Properties from GtkWidget:
      name -> gchararray: name
      parent -> GtkWidget: parent
      root -> GtkRoot: root
      width-request -> gint: width-request
      height-request -> gint: height-request
      visible -> gboolean: visible
      sensitive -> gboolean: sensitive
      can-focus -> gboolean: can-focus
      has-focus -> gboolean: has-focus
      can-target -> gboolean: can-target
      focus-on-click -> gboolean: focus-on-click
      focusable -> gboolean: focusable
      has-default -> gboolean: has-default
      receives-default -> gboolean: receives-default
      cursor -> GdkCursor: cursor
      has-tooltip -> gboolean: has-tooltip
      tooltip-markup -> gchararray: tooltip-markup
      tooltip-text -> gchararray: tooltip-text
      opacity -> gdouble: opacity
      overflow -> GtkOverflow: overflow
      halign -> GtkAlign: halign
      valign -> GtkAlign: valign
      margin-start -> gint: margin-start
      margin-end -> gint: margin-end
      margin-top -> gint: margin-top
      margin-bottom -> gint: margin-bottom
      hexpand -> gboolean: hexpand
      vexpand -> gboolean: vexpand
      hexpand-set -> gboolean: hexpand-set
      vexpand-set -> gboolean: vexpand-set
      scale-factor -> gint: scale-factor
      css-name -> gchararray: css-name
      css-classes -> GStrv: css-classes
      layout-manager -> GtkLayoutManager: layout-manager
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>
