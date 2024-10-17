from PIL import Image
import numpy as np
import os
import time
import multiprocessing

start = time.time()
def anlx_dsg(anlx_dir, dsg_dir):
    anilox_list = []
    design_list = []
    # with Image.open(repl_dsg_nr) as img1:
    #     img1.load()
    start = time.time()
    try:
        for droot, ddirs, dfiles in os.walk(dsg_dir):
            for dfile in dfiles:
                dpath = os.path.join(droot, dfile)
                with Image.open(dpath) as img1:
                    img1.load()
                for aroot, adirs, afiles in os.walk(anlx_dir):
                    for file in afiles:
                        path = os.path.join(aroot, file)
                        #print("Opening image: {}".format(path))
                        #try:
                        with Image.open(path) as img2:
                            img2.load()
                        # with Image.open(repl_dsg_nr) as design:
                        #     design.load()
                        new_width = img2.size[0]
                        new_height = img1.size[1]
                        new_size = (new_width, new_height)
                        img_new = Image.new('L', new_size)
                        #h = int((new_width - img1.size[0]) / 2)
                        img_new.paste(img1, (870, 0))
                        img2_new = img2.resize(img_new.size)

                        img_new.convert('L')
                        img2_new.convert('L')

                        dsg_array = np.array(img_new, dtype=np.uint8)
                        threshold = 250
                        dsg_array[dsg_array >= threshold] = 255
                        dsg_array[dsg_array < threshold] = 0
                        # dsg_array[dsg_array != 0] = 255
                        anlx_array = np.array(img2_new, dtype=np.uint8)
                        # anlx_array[anlx_array != 0] = 255

                        diff_array = anlx_array + dsg_array
                        diff_array[diff_array != 0] = 255
                        diff_array_sum = diff_array.sum()
                        #print(diff_array_sum)

                        x, y = diff_array.shape
                        sum_white = x * y * 255


                        if sum_white == diff_array_sum:
                            # if np.array_equal(sum_white_fill, diff_array_sum):
                            print(f'Дизайн: {dfile}, Анилокс: {file}, Нет пересечения')
                            anilox_list.append(file)
                            design_list.append(dfile)
                        else:
                            print(f'Дизайн: {dfile}, Анилокс: {file}, Есть пересечение')


                        #diff = Image.fromarray(diff_array)
                        #diff.show()

                        diff2_array = dsg_array - anlx_array
                        diff2_array[diff2_array != 0] = 255  # для получения визульного контроля пересечения
                        diff2 = Image.fromarray(diff2_array)
                        #diff2.show()
    except OSError:
        print('Файл не является изображением')
    return anilox_list, design_list

#aniloxes = anlx_dsg('C:\\Users\\kerzhid\\PycharmProjects\\Anilox_check\\Anilox_checkout\\Anilox_140', 'replicated_image1.png')
aniloxes = anlx_dsg('Anilox_140_1', 'Design2')
for i in aniloxes:
    print(i)
#print(aniloxes)
end = time.time()
print(end - start)

# if __name__ == '__main__':
#     with multiprocessing.Pool(processes=4) as pool:
#         #filenames = [f'./file {number}.txt' for number in range(1, 4)]
#         start_proc = time.time()
#         pool.map(anlx_dsg, "Anilox140", 'Designs')
#         #print(anlx_dsg)
#         end_proc = time.time()
#         print('время выполнения мульти:', end_proc - start_proc)