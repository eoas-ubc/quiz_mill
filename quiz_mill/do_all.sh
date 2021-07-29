remove ..

# remove files in notebooks/output/
clean

# generate 5 notebooks with random parameters
generate ../notebooks -n $1

# filter notebooks 
filter ../notebooks/output

# send all quizzes to canvas
send ../notebooks/output/filtered/solution/ -c 51824