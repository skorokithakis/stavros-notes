#!/bin/bash

set -euxo pipefail

rm -rf themes/book/
git clone https://github.com/getzola/book.git themes/book/

sed -i '5i if (window.innerWidth < 900) { $menu.classList.toggle("menu-hidden"); $page.classList.toggle("page-without-menu"); }\n' themes/book/static/book.js

rm -rf public/
zola build

# Make checkboxes editable, just in case the user wants to keep their own checklist.
find public/ -name "*.html" -type f -exec sed -i 's/input disabled=""/input/g' {} +
