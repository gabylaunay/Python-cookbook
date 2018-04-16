#!/bin/bash

notebook_dir="$(pwd)/notebooks"
content_dir="$(pwd)/content"

# Clean old generated jupyter notebooks
echo "=== Cleaning ==="
for file in "$content_dir/*"; do
    [[ -d $file ]] && rm -rf $file
done

# Generate new pages from jupyter notebooks
cd $notebook_dir
for file in *.ipynb; do
    basename=${file%.*}
    echo " "
    echo "=== Exporting $basename ==="
    # Get page metadata
    page_name=$(jq -r ".metadata.hugo_page_name" "$basename.ipynb")
    if [[ $page_name = 'null' ]] ; then
        page_name=$basename
    fi
    page_description=$(jq -r ".metadata.hugo_description" "$basename.ipynb")
    if [[ $page_description = 'null' ]] ; then
        page_description=""
    fi
    page_weight=$(jq -r ".metadata.hugo_weight" "$basename.ipynb")
    if [[ $page_weight = 'null' ]] ; then
        page_weight="0"
    fi
    # Exporting to markdown
    jupyter nbconvert --to markdown "$file"
    #     Addind header
    sed -i "1i+++" "${basename}.md"
    sed -i "2ititle = \"$page_name\"" "${basename}.md"
    sed -i "3iweight = $page_weight" "${basename}.md"
    sed -i "4idescription = \"$page_description\"" "${basename}.md"
    sed -i "5i+++" "${basename}.md"
    sed -i "6i{{% notice tip %}}" "${basename}.md"
    sed -i "7iYou can get the python script detailled in this page here: [script.py](files/script.py)." "${basename}.md"
    sed -i "8i "
    sed -i "9iAnd an archive containing the script and the data here: [archive.tar.gz](files/archive.tar.gz), [archive.zip](files/archive.zip)." "${basename}.md"
    sed -i "10i{{% /notice %}}" "${basename}.md"
    # Exporting to python script
    jupyter nbconvert --to python "$file" --template=strip_markdown.tpl
    sed -i '/^# In\[.*$/{N;N;d}' "${basename}.py"
    sed -i '/^##.*$/{N;d}' "${basename}.py"
    sed -i "1i#!/bin/env python3" "${basename}.py"
    mv -f "${basename}.py" "script.py"
    # Make archives
    tar -czf "archive.tar.gz" "script.py" "data"
    zip -r "archive.zip" "script.py" "data"
    # Move to content folder
    mkdir -p "$content_dir/$basename"
    mkdir -p "$content_dir/$basename/files"
    mv -f "${basename}.md" "$content_dir/$basename/_index.md"
    rm -rf "$content_dir/$basename/${basename}_files"
    mv -f "${basename}_files" "$content_dir/$basename/"
    mv -f "script.py" "$content_dir/$basename/files/"
    mv -f "archive.tar.gz" "$content_dir/$basename/files/"
    mv -f "archive.zip" "$content_dir/$basename/files/"
done
