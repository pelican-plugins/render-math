Render Math Plugin for Pelican
==============================

[![Build Status](https://img.shields.io/github/actions/workflow/status/pelican-plugins/render-math/main.yml?branch=main)](https://github.com/pelican-plugins/render-math/actions)
[![PyPI Version](https://img.shields.io/pypi/v/pelican-render-math)](https://pypi.org/project/pelican-render-math/)
[![Downloads](https://img.shields.io/pypi/dm/pelican-render-math)](https://pypi.org/project/pelican-render-math/)
![License](https://img.shields.io/pypi/l/pelican-render-math?color=blue)

This plugin gives [Pelican][] the ability to render mathematics inside post
content. It accomplishes this by using the [MathJax][] JavaScript engine.

The plugin also makes [Typogrify][] and recognized math play nicely together by
ensuring [Typogrify][] does not alter math content.

Both Markdown and reStructuredText are supported.

Requirements
------------

* [Pelican][] version *4.5* or above is required.
* [Typogrify][] version *2.0.7* or higher is needed for Typogrify to behave
  properly with this plugin. If this version is not available, Typogrify will be
  disabled for the entire site.
* [BeautifulSoup][] 4+ is required to correct summaries. If BeautifulSoup is not
  installed, summary processing will be ignored, even if specified in user
  settings.

Installation
------------

This plugin can be installed via:

    python -m pip install pelican-render-math

As long as you have not explicitly added a `PLUGINS` setting to your Pelican settings file, then the newly-installed plugin should be automatically detected and enabled. Otherwise, you must add `render_math` to your existing `PLUGINS` list. For more information, please see the [How to Use Plugins](https://docs.getpelican.com/en/latest/plugins.html#how-to-use-plugins) documentation.

Once the plugin has been installed according to those instructions, your site
should be capable of rendering math using the MathJax JavaScript engine.
No alterations to the template are needed — just use and enjoy!

However, if you wish, you can set the `auto_insert` setting to `False` which
will disable the MathJax script from being automatically inserted into the
content. You would only want to do this if you have control over the template
and want to insert the script manually.

### Typogrify

In the past, using [Typogrify][] would alter math content, resulting in math
that could not be rendered by [MathJax][]. The only option was to ensure that
[Typogrify][] was disabled in the settings.

The problem has been rectified in this plugin, but it requires at a minimum
[Typogrify][] version 2.0.7 or higher. If this version is not present, the
plugin will disable Typogrify for the entire site.

### BeautifulSoup

Pelican creates summaries by truncating the post content to a specified user
length. The truncation process is oblivious to any math and can therefore
destroy the math output in the summary.

To restore math, [BeautifulSoup][] is used. If it is not installed, no summary
processing will happen.

Usage
-----

### Templates

No template alteration is needed for this plugin to work. Just install the
plugin and start writing your math.

### Settings

Certain MathJax rendering options can be set. These options are in a dictionary
variable called `MATH_JAX` in the Pelican settings file.

The dictionary can be set with the following keys:

 * `align`: [string] controls how displayed math will be aligned. Can be set to
   either `'left'`, `'right'` or `'center'`. **Default Value**: `'center'`.
 * `auto_insert`: [boolean] will insert the MathJax script into content that it
   is detected to have math in it. Setting it to false is not recommended.
   **Default Value**: `True`
 * `indent`: [string] if `align` not set to `'center'`, then this controls the
   indent level. **Default Value**: `'0em'`.
 * `show_menu`: [boolean] controls whether the MathJax contextual menu is
   shown.  **Default Value**: `True`
 * `process_escapes`: [boolean] controls whether MathJax processes escape
   sequences.  **Default Value**: `True`
 * `MathJax_font`: [string] will force MathJax to use the chosen font. Current
   choices for the font is `sanserif`, `typewriter` or `fraktur`. If this is
   not set, it will use the default font settings. **Default Value**: `default`
 * `latex_preview`: [string] controls the preview message users are shown while
   MathJax is rendering LaTex. If set to `'Tex'`, then the TeX code is used as
   the preview (which will be visible until it is processed by MathJax).
   **Default Value**: `'Tex'`
 * `color`: [string] controls the color of the MathJax rendered font. **Default
   Value**: `'inherit'`
 * `linebreak_automatic`: [boolean] If set, MathJax will try to *intelligently*
   break up displayed math (Note: It will not work for inline math). This is
   very useful for a responsive site. It is turned off by default due to it
   potentially being CPU expensive. **Default Value**: `False`
 * `tex_extensions`: [list] a list of [latex
   extensions](https://docs.mathjax.org/en/latest/input/tex/extensions.html)
   accepted by MathJax. **Default Value**: `[]` (empty list)
 * `responsive`: [boolean] tries to make displayed math render responsively. It
   does by determining if the width is less than `responsive_break` (see below)
   and if so, sets `align` to `left`, `indent` to `0em` and
   `linebreak_automatic` to `True`.  **Default Value**: `False` (defaults to
   `False` for backward compatibility)
 * `responsive_break`: [integer] a number (in pixels) representing the width
   breakpoint that is used when setting `responsive_align` to `True`. **Default
   Value**: 768
 * `process_summary`: [boolean] ensures math will render in summaries and fixes
   math in that were cut off. Requires [BeautifulSoup][] be installed. **Default
   Value**: `True`
 * `message_style`: [string] This value controls the verbosity of the messages
   in the lower left-hand corner. Set it to `None` to eliminate all messages.
   **Default Value**: normal

#### Settings Examples

Make math render in blue and display math aligned to the left:

    MATH_JAX = {'color':'blue','align':left}

Use the [color](https://docs.mathjax.org/en/latest/input/tex/extensions/color.html)
and [mhchem](https://docs.mathjax.org/en/latest/input/tex/extensions/mhchem.html)
extensions:

    MATH_JAX = {'tex_extensions': ['color.js','mhchem.js']}

#### Resulting HTML

Inline math is wrapped in `span` tags, while displayed math is wrapped in
`div` tags.  These tags will have a class attribute that is set to `math` which
can be used by template designers to alter the display of the math.

Markdown
--------

This plugin implements a custom extension for Markdown resulting in math being
a "first class citizen" for Pelican.

### Inline Math

Math between `$`..`$`, for example, `$`x^2`$`, will be rendered inline with
respect to the current HTML block. Note: To use inline math, there must *not*
be any whitespace before the ending `$`. So for example:

 * **Relevant inline math**: `$e=mc^2$`
 * **Will not render as inline math**: `$40 vs $50`

### Displayed Math

Math between `$$`..`$$` will be rendered "block style", for example,
`$$`x^2`$$`, will be rendered centered in a new paragraph.

#### Other Latex Display Math Commands

The other LaTeX commands which usually invoke display math mode from text mode
are supported, and are automatically treated like `$$`-style displayed math in
that they are rendered "block" style on their own lines.  For example,
`\begin{equation}` x^2 `\end{equation}`, will be rendered in its own block with
a right justified equation number at the top of the block. This equation number
can be referenced in the document.  To do this, use a `label` inside of the
equation format and then refer to that label using `ref`. For example:
`\begin{equation}` `\label{eq}` X^2 `\end{equation}`.  Now refer to that
equation number by `$`\ref{eq}`$`.

reStructuredText
----------------

If there is math detected in reStructuredText content, the plugin will
automatically set the
[math_output](https://docutils.sourceforge.io/docs/user/config.html#math-output)
configuration setting to `mathjax`.

### Inline Math

Inline math needs to use the [math
role](https://docutils.sourceforge.io/docs/ref/rst/roles.html#math):

```
The area of a circle is :math:`A_\text{c} = (\pi/4) d^2`.
```

### Displayed Math

Displayed math uses the [math block](https://docutils.sourceforge.io/docs/ref/rst/directives.html#math):

```rst
.. math::

   α_t(i) = P(O_1, O_2, … O_t, q_t = S_i λ)
```

Enabling Additional Features
----------------------------

In order for `\frac`, equation numbering, and other features to work, the MathJAX JavaScript file must be added to the HTML file, either via your theme's template configuration (if supported) or by editing the relevant template file directly. The current MathJAX CDN is hosted at `http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML`, and the code to add it to the HTML is provided below.

```html
<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
```
As long as this script is loaded in either the head or body of the HTML output, the complex expressions are also converted.

Contributing
------------

Contributions are welcome and much appreciated. Every little bit helps. You can contribute by improving the documentation, adding missing features, and fixing bugs. You can also help out by reviewing and commenting on [existing issues][].

To start contributing to this plugin, review the [Contributing to Pelican][] documentation, beginning with the **Contributing Code** section.


[BeautifulSoup]: https://www.crummy.com/software/BeautifulSoup/
[MathJax]: https://www.mathjax.org/
[Pelican]: https://github.com/getpelican/pelican
[Typogrify]: https://github.com/mintchaos/typogrify
[existing issues]: https://github.com/pelican-plugins/render-math/issues
[Contributing to Pelican]: https://docs.getpelican.com/en/latest/contribute.html

License
-------

This project is licensed under the AGPL-3.0 license.
