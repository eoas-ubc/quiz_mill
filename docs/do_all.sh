python ../quiz_mill/remove_quizzes.py
echo "Removed Two Layers quizzes from Canvas"

# remove files in notebooks/output/
find ../notebooks/output/ -type f -exec rm {} \;
echo "Removed previous output notebooks"

# generate 5 notebooks with random parameters
python ../quiz_mill/generate_notebooks.py -n $1
echo "Generated notebooks with random parameters"

# filter notebooks 
filter-notebook ../notebooks/output/unfiltered/ ../notebooks/output/filtered/ 
echo "Generated notebooks have been filtered"

# send all quizzes to canvas
sh ../quiz_mill/send_to_canvas.sh   
echo "Quizzes sent to canvas"