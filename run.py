from PIL import Image

with Image.open("files/{your_file_name}.tif") as im:

    height = 1354
    width = 940

    resize_images = []

    for i in range(im.n_frames):
        try:
            im.seek(i)
            new_image = im.resize((width, height), Image.ANTIALIAS)
            resize_images.append(new_image)
        except EOFError:
            print("error")
            break

    first_image = resize_images[0]

    del resize_images[0]

    first_image.save("results/{your_file_name}.tif", save_all = True ,append_images = resize_images)


