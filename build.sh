#!/bin/bash

set -euxo pipefail

rm -rf themes/book/
git clone https://github.com/getzola/book.git themes/book/

rm -rf public/
zola build

# Make checkboxes editable, just in case the user wants to keep their own checklist.
find public/ -name "*.html" -type f -exec sed -i 's/input disabled=""/input/g' {} +
