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
\usepackage{textcomp}
\usepackage{amsmath}

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
    
    # Create a temporary LaTeX file to compile
    temp_texfile="temp_$(basename "$texfile")"
    
    # Write the modified LaTeX code into the temporary file
    echo "$latex_code" > "$temp_texfile"
    
    # Compile the temporary LaTeX file to generate the PDF
    pdflatex "$temp_texfile"
    
    # Optional: clean up auxiliary files (.aux, .log, etc.)
    rm -f "${temp_texfile%.*}".{aux,log,toc,out}
    
    # Remove the temporary LaTeX file
    rm -f "$temp_texfile"
done

echo "PDF generation completed!"

