remove-quizzes ../token.yaml -v

# remove files in notebooks/output/
clean-output -v

# generate 5 notebooks with random parameters
generate-notebooks -n $1

# filter notebooks 
filter-notebook ../notebooks/output/unfiltered/ ../notebooks/output/filtered/ 

# send all quizzes to canvas
to-canvas ../notebooks/output/filtered/solution/ -i 51824 -v  