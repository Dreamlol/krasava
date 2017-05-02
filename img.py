import tinify

tinify.key = "okwa-kKGX1yv_oikkB3Yp9FohyajHUcM"

source = tinify.from_file("sahara.jpg")
source.to_file("new.jpg")

