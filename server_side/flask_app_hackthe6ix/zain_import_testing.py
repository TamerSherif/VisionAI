import _init_paths
import os

from main import func_to_call

path_to_image = '/home/paperspace/Hackathon/show-attend-and-tell/test/images/1.jpg'
print(os.path.isfile(path_to_image))
func_to_call(path_to_image)