#!/bin/bash
# Recursively remove 'temp_' from filenames in all subdirectories
find . -type f -name "temp_*" | while read file; do
    # Remove 'temp_' prefix from the filename
    new_name=$(echo "$file" | sed 's|/temp_||')
    
    # Rename the file
    mv "$file" "$new_name"
    echo "Renamed: $file -> $new_name"
done

echo "Renaming completed!"
