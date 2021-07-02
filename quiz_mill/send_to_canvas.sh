files=`ls notebooks/output/filtered/solution/*md`
for file in $files
do
    md2canvas $file -f token.txt -c 51824 -u https://canvas.ubc.ca -s
done