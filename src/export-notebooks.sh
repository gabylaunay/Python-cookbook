#!/bin/bash

notebook_dir="$(pwd)/notebooks"
content_dir="$(pwd)/content"

cd $notebook_dir
for file in *.ipynb; do
    basename=${file%.*}
    echo "=== Exporting $basename ==="
    # exporting to markdown
    jupyter nbconvert --to markdown "$file"
    # Get page name from metadata
    page_name=$(jq -r ".metadata.hugo_page_name" "$basename.ipynb")
    if [[ $page_name = 'null' ]] ; then
        page_name=$basename
    fi
    # adding hugo header
    sed -i "1i+++" "${basename}.md"
    sed -i "1ititle = \"$page_name\"" "${basename}.md"
    sed -i "1iweight = 1" "${basename}.md"
    sed -i "1i+++" "${basename}.md"
    # Move to content folder
    mkdir -p "$content_dir/$basename"
    mv -f "${basename}.md" "$content_dir/$basename/_index.md"
    rm -rf "$content_dir/$basename/${basename}_files"
    mv -f "${basename}_files" "$content_dir/$basename/"
done
