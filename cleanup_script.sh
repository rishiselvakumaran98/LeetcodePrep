# For each subdirectory in the current directory
for dir in $(find . -mindepth 1 -maxdepth 1 -type d); do
    # remove java files
    rm -rf "$dir/*.java"
done


# for dir in $(find ./* -mindepth 1 -maxdepth 1 -type d); do
#     # Remove Java folder
#     rm -rf "$dir/Java"
#     # Copy .py files from Python folder to current directory
#     cp "$dir/Python"/*.py .
#     # Remove Python folder
#     rm -rf "$dir/Python"
# done

