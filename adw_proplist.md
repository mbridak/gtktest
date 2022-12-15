<!-- markdownlint-disable no-inline-html -->
<!-- markdownlint-disable no-multiple-blanks -->
<!-- markdownlint-disable no-trailing-spaces -->
# Adw Class Signals and Properties List

<details><summary>Adw.AboutWindow</summary>

Object AdwAboutWindow
    
    Signals from AdwAboutWindow:
      activate-link (gchararray) -> gboolean
    
    Properties from AdwAboutWindow:
      application-icon -> gchararray: application-icon
      application-name -> gchararray: application-name
      developer-name -> gchararray: developer-name
      version -> gchararray: version
      release-notes-version -> gchararray: release-notes-version
      release-notes -> gchararray: release-notes
      comments -> gchararray: comments
      website -> gchararray: website
      support-url -> gchararray: support-url
      issue-url -> gchararray: issue-url
      debug-info -> gchararray: debug-info
      debug-info-filename -> gchararray: debug-info-filename
      developers -> GStrv: developers
      designers -> GStrv: designers
      artists -> GStrv: artists
      documenters -> GStrv: documenters
      translator-credits -> gchararray: translator-credits
      copyright -> gchararray: copyright
      license-type -> GtkLicense: license-type
      license -> gchararray: license
    
    Properties from AdwWindow:
      content -> GtkWidget: content
    
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

<details><summary>Adw.ActionRow</summary>

Object AdwActionRow
    
    Signals from AdwActionRow:
      activated ()
    
    Properties from AdwActionRow:
      subtitle -> gchararray: subtitle
      icon-name -> gchararray: icon-name
      activatable-widget -> GtkWidget: activatable-widget
      title-lines -> gint: title-lines
      subtitle-lines -> gint: subtitle-lines
    
    Properties from AdwPreferencesRow:
      title -> gchararray: title
      use-underline -> gboolean: use-underline
      title-selectable -> gboolean: title-selectable
      use-markup -> gboolean: use-markup
    
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

<details><summary>Adw.Animation</summary>

Object AdwAnimation
    
    Signals from AdwAnimation:
      done ()
    
    Properties from AdwAnimation:
      widget -> GtkWidget: widget
      target -> AdwAnimationTarget: target
      value -> gdouble: value
      state -> AdwAnimationState: state
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Adw.AnimationTarget</summary>

Object AdwAnimationTarget
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Adw.Application</summary>

Object AdwApplication
    
    Properties from AdwApplication:
      style-manager -> AdwStyleManager: style-manager
    
    Signals from GActionGroup:
      action-added (gchararray)
      action-removed (gchararray)
      action-enabled-changed (gchararray, gboolean)
      action-state-changed (gchararray, GVariant)
    
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

<details><summary>Adw.ApplicationWindow</summary>

Object AdwApplicationWindow
    
    Properties from AdwApplicationWindow:
      content -> GtkWidget: content
    
    Signals from GActionGroup:
      action-added (gchararray)
      action-removed (gchararray)
      action-enabled-changed (gchararray, gboolean)
      action-state-changed (gchararray, GVariant)
    
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

<details><summary>Adw.Avatar</summary>

Object AdwAvatar
    
    Properties from AdwAvatar:
      icon-name -> gchararray: icon-name
      text -> gchararray: text
      show-initials -> gboolean: show-initials
      custom-image -> GdkPaintable: custom-image
      size -> gint: size
    
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

<details><summary>Adw.Bin</summary>

Object AdwBin
    
    Properties from AdwBin:
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

<details><summary>Adw.ButtonContent</summary>

Object AdwButtonContent
    
    Properties from AdwButtonContent:
      icon-name -> gchararray: icon-name
      label -> gchararray: label
      use-underline -> gboolean: use-underline
    
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

<details><summary>Adw.CallbackAnimationTarget</summary>

Object AdwCallbackAnimationTarget
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Adw.Carousel</summary>

Object AdwCarousel
    
    Signals from AdwCarousel:
      page-changed (guint)
    
    Properties from AdwCarousel:
      n-pages -> guint: n-pages
      position -> gdouble: position
      interactive -> gboolean: interactive
      spacing -> guint: spacing
      scroll-params -> AdwSpringParams: scroll-params
      allow-mouse-drag -> gboolean: allow-mouse-drag
      allow-scroll-wheel -> gboolean: allow-scroll-wheel
      allow-long-swipes -> gboolean: allow-long-swipes
      reveal-duration -> guint: reveal-duration
    
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

<details><summary>Adw.CarouselIndicatorDots</summary>

Object AdwCarouselIndicatorDots
    
    Properties from AdwCarouselIndicatorDots:
      carousel -> AdwCarousel: carousel
    
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

<details><summary>Adw.CarouselIndicatorLines</summary>

Object AdwCarouselIndicatorLines
    
    Properties from AdwCarouselIndicatorLines:
      carousel -> AdwCarousel: carousel
    
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

<details><summary>Adw.Clamp</summary>

Object AdwClamp
    
    Properties from AdwClamp:
      child -> GtkWidget: child
      maximum-size -> gint: maximum-size
      tightening-threshold -> gint: tightening-threshold
    
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

<details><summary>Adw.ClampLayout</summary>

Object AdwClampLayout
    
    Properties from AdwClampLayout:
      maximum-size -> gint: maximum-size
      tightening-threshold -> gint: tightening-threshold
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Adw.ClampScrollable</summary>

Object AdwClampScrollable
    
    Properties from AdwClampScrollable:
      child -> GtkWidget: child
      maximum-size -> gint: maximum-size
      tightening-threshold -> gint: tightening-threshold
    
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

<details><summary>Adw.ComboRow</summary>

Object AdwComboRow
    
    Properties from AdwComboRow:
      selected -> guint: selected
      selected-item -> GObject: selected-item
      model -> GListModel: model
      factory -> GtkListItemFactory: factory
      list-factory -> GtkListItemFactory: list-factory
      expression -> GtkExpression: Expression
        Expression to determine strings to search for
      use-subtitle -> gboolean: use-subtitle
    
    Signals from AdwActionRow:
      activated ()
    
    Properties from AdwActionRow:
      subtitle -> gchararray: subtitle
      icon-name -> gchararray: icon-name
      activatable-widget -> GtkWidget: activatable-widget
      title-lines -> gint: title-lines
      subtitle-lines -> gint: subtitle-lines
    
    Properties from AdwPreferencesRow:
      title -> gchararray: title
      use-underline -> gboolean: use-underline
      title-selectable -> gboolean: title-selectable
      use-markup -> gboolean: use-markup
    
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

<details><summary>Adw.EntryRow</summary>

Object AdwEntryRow
    
    Signals from AdwEntryRow:
      apply ()
      entry-activated ()
    
    Properties from AdwEntryRow:
      show-apply-button -> gboolean: show-apply-button
      input-hints -> GtkInputHints: input-hints
      input-purpose -> GtkInputPurpose: input-purpose
      attributes -> PangoAttrList: attributes
      enable-emoji-completion -> gboolean: enable-emoji-completion
      activates-default -> gboolean: activates-default
    
    Signals from GtkEditable:
      changed ()
      insert-text (gchararray, gint, gpointer)
      delete-text (gint, gint)
    
    Properties from AdwPreferencesRow:
      title -> gchararray: title
      use-underline -> gboolean: use-underline
      title-selectable -> gboolean: title-selectable
      use-markup -> gboolean: use-markup
    
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

<details><summary>Adw.EnumListItem</summary>

Object AdwEnumListItem
    
    Properties from AdwEnumListItem:
      value -> gint: value
      name -> gchararray: name
      nick -> gchararray: nick
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Adw.EnumListModel</summary>

Object AdwEnumListModel
    
    Properties from AdwEnumListModel:
      enum-type -> GType: enum-type
    
    Signals from GListModel:
      items-changed (guint, guint, guint)
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Adw.ExpanderRow</summary>

Object AdwExpanderRow
    
    Properties from AdwExpanderRow:
      subtitle -> gchararray: subtitle
      icon-name -> gchararray: icon-name
      expanded -> gboolean: expanded
      enable-expansion -> gboolean: enable-expansion
      show-enable-switch -> gboolean: show-enable-switch
    
    Properties from AdwPreferencesRow:
      title -> gchararray: title
      use-underline -> gboolean: use-underline
      title-selectable -> gboolean: title-selectable
      use-markup -> gboolean: use-markup
    
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

<details><summary>Adw.Flap</summary>

Object AdwFlap
    
    Properties from AdwFlap:
      content -> GtkWidget: content
      flap -> GtkWidget: flap
      separator -> GtkWidget: separator
      flap-position -> GtkPackType: flap-position
      reveal-flap -> gboolean: reveal-flap
      reveal-params -> AdwSpringParams: reveal-params
      reveal-progress -> gdouble: reveal-progress
      fold-policy -> AdwFlapFoldPolicy: fold-policy
      fold-threshold-policy -> AdwFoldThresholdPolicy: fold-threshold-policy
      fold-duration -> guint: fold-duration
      folded -> gboolean: folded
      locked -> gboolean: locked
      transition-type -> AdwFlapTransitionType: transition-type
      modal -> gboolean: modal
      swipe-to-open -> gboolean: swipe-to-open
      swipe-to-close -> gboolean: swipe-to-close
    
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

<details><summary>Adw.HeaderBar</summary>

Object AdwHeaderBar
    
    Properties from AdwHeaderBar:
      title-widget -> GtkWidget: title-widget
      show-start-title-buttons -> gboolean: show-start-title-buttons
      show-end-title-buttons -> gboolean: show-end-title-buttons
      decoration-layout -> gchararray: decoration-layout
      centering-policy -> AdwCenteringPolicy: centering-policy
    
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

<details><summary>Adw.Leaflet</summary>

Object AdwLeaflet
    
    Properties from AdwLeaflet:
      can-unfold -> gboolean: can-unfold
      folded -> gboolean: folded
      fold-threshold-policy -> AdwFoldThresholdPolicy: fold-threshold-policy
      homogeneous -> gboolean: homogeneous
      visible-child -> GtkWidget: visible-child
      visible-child-name -> gchararray: visible-child-name
      transition-type -> AdwLeafletTransitionType: transition-type
      mode-transition-duration -> guint: mode-transition-duration
      child-transition-params -> AdwSpringParams: child-transition-params
      child-transition-running -> gboolean: child-transition-running
      can-navigate-back -> gboolean: can-navigate-back
      can-navigate-forward -> gboolean: can-navigate-forward
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

<details><summary>Adw.LeafletPage</summary>

Object AdwLeafletPage
    
    Properties from AdwLeafletPage:
      child -> GtkWidget: child
      name -> gchararray: name
      navigatable -> gboolean: navigatable
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Adw.MessageDialog</summary>

Object AdwMessageDialog
    
    Signals from AdwMessageDialog:
      response (gchararray)
    
    Properties from AdwMessageDialog:
      heading -> gchararray: heading
      heading-use-markup -> gboolean: heading-use-markup
      body -> gchararray: body
      body-use-markup -> gboolean: body-use-markup
      extra-child -> GtkWidget: extra-child
      default-response -> gchararray: default-response
      close-response -> gchararray: close-response
    
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

<details><summary>Adw.PasswordEntryRow</summary>

Object AdwPasswordEntryRow
    
    Signals from GtkEditable:
      changed ()
      insert-text (gchararray, gint, gpointer)
      delete-text (gint, gint)
    
    Signals from AdwEntryRow:
      apply ()
      entry-activated ()
    
    Properties from AdwEntryRow:
      show-apply-button -> gboolean: show-apply-button
      input-hints -> GtkInputHints: input-hints
      input-purpose -> GtkInputPurpose: input-purpose
      attributes -> PangoAttrList: attributes
      enable-emoji-completion -> gboolean: enable-emoji-completion
      activates-default -> gboolean: activates-default
    
    Signals from GtkEditable:
      changed ()
      insert-text (gchararray, gint, gpointer)
      delete-text (gint, gint)
    
    Properties from AdwPreferencesRow:
      title -> gchararray: title
      use-underline -> gboolean: use-underline
      title-selectable -> gboolean: title-selectable
      use-markup -> gboolean: use-markup
    
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

<details><summary>Adw.PreferencesGroup</summary>

Object AdwPreferencesGroup
    
    Properties from AdwPreferencesGroup:
      title -> gchararray: title
      description -> gchararray: description
      header-suffix -> GtkWidget: header-suffix
    
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

<details><summary>Adw.PreferencesPage</summary>

Object AdwPreferencesPage
    
    Properties from AdwPreferencesPage:
      icon-name -> gchararray: icon-name
      title -> gchararray: title
      name -> gchararray: name
      use-underline -> gboolean: use-underline
    
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

<details><summary>Adw.PreferencesRow</summary>

Object AdwPreferencesRow
    
    Properties from AdwPreferencesRow:
      title -> gchararray: title
      use-underline -> gboolean: use-underline
      title-selectable -> gboolean: title-selectable
      use-markup -> gboolean: use-markup
    
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

<details><summary>Adw.PreferencesWindow</summary>

Object AdwPreferencesWindow
    
    Properties from AdwPreferencesWindow:
      visible-page -> GtkWidget: visible-page
      visible-page-name -> gchararray: visible-page-name
      search-enabled -> gboolean: search-enabled
      can-navigate-back -> gboolean: can-navigate-back
    
    Properties from AdwWindow:
      content -> GtkWidget: content
    
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

<details><summary>Adw.PropertyAnimationTarget</summary>

Object AdwPropertyAnimationTarget
    
    Properties from AdwPropertyAnimationTarget:
      object -> GObject: object
      pspec -> GParam: pspec
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Adw.SplitButton</summary>

Object AdwSplitButton
    
    Signals from AdwSplitButton:
      activate ()
      clicked ()
    
    Properties from AdwSplitButton:
      label -> gchararray: label
      use-underline -> gboolean: use-underline
      icon-name -> gchararray: icon-name
      child -> GtkWidget: child
      menu-model -> GMenuModel: menu-model
      popover -> GtkPopover: popover
      direction -> GtkArrowType: direction
      dropdown-tooltip -> gchararray: dropdown-tooltip
    
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

<details><summary>Adw.SpringAnimation</summary>

Object AdwSpringAnimation
    
    Properties from AdwSpringAnimation:
      value-from -> gdouble: value-from
      value-to -> gdouble: value-to
      spring-params -> AdwSpringParams: spring-params
      initial-velocity -> gdouble: initial-velocity
      epsilon -> gdouble: epsilon
      clamp -> gboolean: clamp
      estimated-duration -> guint: estimated-duration
      velocity -> gdouble: velocity
    
    Signals from AdwAnimation:
      done ()
    
    Properties from AdwAnimation:
      widget -> GtkWidget: widget
      target -> AdwAnimationTarget: target
      value -> gdouble: value
      state -> AdwAnimationState: state
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Adw.Squeezer</summary>

Object AdwSqueezer
    
    Properties from AdwSqueezer:
      visible-child -> GtkWidget: visible-child
      homogeneous -> gboolean: homogeneous
      switch-threshold-policy -> AdwFoldThresholdPolicy: switch-threshold-policy
      allow-none -> gboolean: allow-none
      transition-duration -> guint: transition-duration
      transition-type -> AdwSqueezerTransitionType: transition-type
      transition-running -> gboolean: transition-running
      interpolate-size -> gboolean: interpolate-size
      xalign -> gfloat: xalign
      yalign -> gfloat: yalign
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

<details><summary>Adw.SqueezerPage</summary>

Object AdwSqueezerPage
    
    Properties from AdwSqueezerPage:
      child -> GtkWidget: child
      enabled -> gboolean: enabled
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Adw.StatusPage</summary>

Object AdwStatusPage
    
    Properties from AdwStatusPage:
      icon-name -> gchararray: icon-name
      paintable -> GdkPaintable: paintable
      title -> gchararray: title
      description -> gchararray: description
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

<details><summary>Adw.StyleManager</summary>

Object AdwStyleManager
    
    Properties from AdwStyleManager:
      display -> GdkDisplay: display
      color-scheme -> AdwColorScheme: color-scheme
      system-supports-color-schemes -> gboolean: system-supports-color-schemes
      dark -> gboolean: dark
      high-contrast -> gboolean: high-contrast
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Adw.SwipeTracker</summary>

Object AdwSwipeTracker
    
    Signals from AdwSwipeTracker:
      prepare (AdwNavigationDirection)
      begin-swipe ()
      update-swipe (gdouble)
      end-swipe (gdouble, gdouble)
    
    Properties from AdwSwipeTracker:
      swipeable -> AdwSwipeable: swipeable
      enabled -> gboolean: enabled
      reversed -> gboolean: reversed
      allow-mouse-drag -> gboolean: allow-mouse-drag
      allow-long-swipes -> gboolean: allow-long-swipes
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Adw.Swipeable</summary>

Interface AdwSwipeable
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Adw.TabBar</summary>

Object AdwTabBar
    
    Signals from AdwTabBar:
      extra-drag-drop (AdwTabPage, GValue) -> gboolean
    
    Properties from AdwTabBar:
      view -> AdwTabView: view
      start-action-widget -> GtkWidget: start-action-widget
      end-action-widget -> GtkWidget: end-action-widget
      autohide -> gboolean: autohide
      tabs-revealed -> gboolean: tabs-revealed
      expand-tabs -> gboolean: expand-tabs
      inverted -> gboolean: inverted
      is-overflowing -> gboolean: is-overflowing
    
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

<details><summary>Adw.TabPage</summary>

Object AdwTabPage
    
    Properties from AdwTabPage:
      child -> GtkWidget: child
      parent -> AdwTabPage: parent
      selected -> gboolean: selected
      pinned -> gboolean: pinned
      title -> gchararray: title
      tooltip -> gchararray: tooltip
      icon -> GIcon: icon
      loading -> gboolean: loading
      indicator-icon -> GIcon: indicator-icon
      indicator-tooltip -> gchararray: indicator-tooltip
      indicator-activatable -> gboolean: indicator-activatable
      needs-attention -> gboolean: needs-attention
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Adw.TabView</summary>

Object AdwTabView
    
    Signals from AdwTabView:
      page-attached (AdwTabPage, gint)
      page-detached (AdwTabPage, gint)
      page-reordered (AdwTabPage, gint)
      close-page (AdwTabPage) -> gboolean
      setup-menu (AdwTabPage)
      create-window () -> AdwTabView
      indicator-activated (AdwTabPage)
    
    Properties from AdwTabView:
      n-pages -> gint: n-pages
      n-pinned-pages -> gint: n-pinned-pages
      is-transferring-page -> gboolean: is-transferring-page
      selected-page -> AdwTabPage: selected-page
      default-icon -> GIcon: default-icon
      menu-model -> GMenuModel: menu-model
      shortcuts -> AdwTabViewShortcuts: shortcuts
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

<details><summary>Adw.TimedAnimation</summary>

Object AdwTimedAnimation
    
    Properties from AdwTimedAnimation:
      value-from -> gdouble: value-from
      value-to -> gdouble: value-to
      duration -> guint: duration
      easing -> AdwEasing: easing
      repeat-count -> guint: repeat-count
      reverse -> gboolean: reverse
      alternate -> gboolean: alternate
    
    Signals from AdwAnimation:
      done ()
    
    Properties from AdwAnimation:
      widget -> GtkWidget: widget
      target -> AdwAnimationTarget: target
      value -> gdouble: value
      state -> AdwAnimationState: state
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Adw.Toast</summary>

Object AdwToast
    
    Signals from AdwToast:
      dismissed ()
      button-clicked ()
    
    Properties from AdwToast:
      title -> gchararray: title
      button-label -> gchararray: button-label
      action-name -> gchararray: action-name
      action-target -> GVariant: action-target
      priority -> AdwToastPriority: priority
      timeout -> guint: timeout
      custom-title -> GtkWidget: custom-title
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Adw.ToastOverlay</summary>

Object AdwToastOverlay
    
    Properties from AdwToastOverlay:
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

<details><summary>Adw.ViewStack</summary>

Object AdwViewStack
    
    Properties from AdwViewStack:
      hhomogeneous -> gboolean: hhomogeneous
      vhomogeneous -> gboolean: vhomogeneous
      visible-child -> GtkWidget: visible-child
      visible-child-name -> gchararray: visible-child-name
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

<details><summary>Adw.ViewStackPage</summary>

Object AdwViewStackPage
    
    Properties from AdwViewStackPage:
      child -> GtkWidget: child
      name -> gchararray: name
      title -> gchararray: title
      use-underline -> gboolean: use-underline
      icon-name -> gchararray: icon-name
      needs-attention -> gboolean: needs-attention
      badge-number -> guint: badge-number
      visible -> gboolean: visible
    
    Signals from GObject:
      notify (GParam)
    
    

---


</details>

<details><summary>Adw.ViewSwitcher</summary>

Object AdwViewSwitcher
    
    Properties from AdwViewSwitcher:
      policy -> AdwViewSwitcherPolicy: policy
      stack -> AdwViewStack: stack
    
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

<details><summary>Adw.ViewSwitcherBar</summary>

Object AdwViewSwitcherBar
    
    Properties from AdwViewSwitcherBar:
      stack -> AdwViewStack: stack
      reveal -> gboolean: reveal
    
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

<details><summary>Adw.ViewSwitcherTitle</summary>

Object AdwViewSwitcherTitle
    
    Properties from AdwViewSwitcherTitle:
      stack -> AdwViewStack: stack
      title -> gchararray: title
      subtitle -> gchararray: subtitle
      view-switcher-enabled -> gboolean: view-switcher-enabled
      title-visible -> gboolean: title-visible
    
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

<details><summary>Adw.Window</summary>

Object AdwWindow
    
    Properties from AdwWindow:
      content -> GtkWidget: content
    
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

<details><summary>Adw.WindowTitle</summary>

Object AdwWindowTitle
    
    Properties from AdwWindowTitle:
      title -> gchararray: title
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
