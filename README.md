# cogrob-website
Repository for CogRob website made with Hugo. Cloned from [https://wowchemy.com/](wowchemy).
To test locally, run `` hugo server -D ``

### Requirements.

`hugo-extended` and `go` (>1.15) are required to compile. [https://github.com/klakegg/docker-hugo](hugodocker) is a good start for this. Use the `hugo-extended` image.


### General structure.
```
.
+-- config
|   +-- config.yaml
|   +-- menus.yaml : If any new page needs to be added, add it here
|   +-- params.yaml: Font and theme that can be edited in /themes/
+-- content : all contents of the website goes here. publications page needs to be edited
+-- static: Add an images folder, and all post images must be placed here (I think)
+-- themes/academictheme
|   +-- assets - to change the css
|   +-- data - to change the fonts
|   +-- layout - to change the html here
```