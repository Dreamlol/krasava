import os, tinify

tinify.key = "okwa-kKGX1yv_oikkB3Yp9FohyajHUcM"
a = os.listdir(os.getcwd())
path = os.getcwd()




for i in a:
    filename, file_extension = os.path.splitext(i)
    if file_extension == '.jpg':
        if not os.path.exists('new'):
            os.makedirs('new')


        source = tinify.from_file(i)
        resized = source.resize(method="scale", width=1280)
        os.chdir(path+"/new")
        resized.to_file(i)



        #source.to_file(i)
        os.chdir(path)


