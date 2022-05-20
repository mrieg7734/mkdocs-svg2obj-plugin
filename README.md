# mkdocs-svg2obj-plugin

This plugin converts SVGs embedded in markdown like:
```
![caption](path/to/image.svg)
```
into HTML objects and a caption:
```
<object data="../path/to/image.svg" height="auto" type="image/svg+xml" width="100%"></object>
<p><center>caption</center></p>
```
This makes the text inside the svg images searchable.
  
## Usage
  
Install the plugin using pip:
  
`pip install git+https://github.com/mrieg7734/mkdocs-svg2obj-plugin.git`
  
Activate the plugin in `mkdocs.yml`:
```yaml
plugins:
  - search
  - svg2obj
```
  
> **Note:** If you have no `plugins` entry in your config file yet, you'll likely also want to add the `search` plugin. MkDocs enables it by default if there is no `plugins` entry set, but now you have to enable it explicitly.

More information about plugins in the [MkDocs documentation][mkdocs-plugins].
  
## Credits
This is my first MkDocs plugin. It is based on the following similar plugins:
- https://github.com/stuebersystems/mkdocs-img2fig-plugin
- https://gitlab.com/craig0990/mkdocs-plugin-inline-svg
