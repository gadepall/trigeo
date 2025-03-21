#!/bin/bash

# Define the LaTeX template (content of the LaTeX document)
LATEX_TEMPLATE=$(cat <<'EOF'
% Code by GVV Sharma
% December 16, 2019
% Released under GNU GPL

\documentclass{standalone}
\usepackage{tikz}
\usepackage{tkz-euclide} % Loads TikZ and tkz-base
\usetikzlibrary{calc, math}
\usepackage{graphicx} % Needed for \resizebox

\begin{document}

% Resize and include the diagram from the specified file
\resizebox{\columnwidth}{!}{\input{FILE_PATH}}

\end{document}
EOF
)

# Find all .tex files in subdirectories and process them
find . -type f -name "*.tex" | while read texfile; do
    echo "Processing $texfile..."
    
    # Replace the placeholder with the actual file path in the LaTeX template
    latex_code="${LATEX_TEMPLATE//FILE_PATH/$texfile}"
    
    # Extract the directory of the .tex file
    tex_dir=$(dirname "$texfile")
    
    # Create a temporary LaTeX file to compile in the same directory as the .tex file
    temp_texfile="$tex_dir/temp_$(basename "$texfile")"
    
    # Write the modified LaTeX code into the temporary file
    echo "$latex_code" > "$temp_texfile"
    
    # Compile the temporary LaTeX file and output the .pdf to the same directory
    pdflatex -output-directory="$tex_dir" "$temp_texfile"
    
    # If a PDF was created with the 'temp_' prefix, remove the prefix
    temp_pdf="$tex_dir/temp_$(basename "$texfile" .tex).pdf"
    if [[ -f "$temp_pdf" ]]; then
        # Remove 'temp_' prefix from the PDF filename
        new_pdf="$tex_dir/$(basename "$texfile" .tex).pdf"
        mv "$temp_pdf" "$new_pdf"
        echo "Renamed PDF: $temp_pdf -> $new_pdf"
    fi
    
    # Optional: clean up auxiliary files (.aux, .log, etc.) in the directory
    rm -f "$tex_dir"/{temp_*.aux,temp_*.log,temp_*.toc,temp_*.out}
    
    # Remove the temporary LaTeX file
    rm -f "$temp_texfile"
done

echo "PDF generation completed!"

