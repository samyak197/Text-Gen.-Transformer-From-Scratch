import kagglehub

# Download latest version
path = kagglehub.dataset_download("blessondensil294/friends-tv-series-screenplay-script")

print("Path to dataset files:", path)