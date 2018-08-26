import os.path as osp
import sys

#0 Priority has the highest priority
def add_path(path,priority=0):
    if path not in sys.path:
        sys.path.insert(0, path)
# hello

this_dir = osp.dirname(__file__)

## Important to give this a priority of one since, both repo has a 'nets' directory and want to force to look for nets in lib_path
vgg_preprocess_path = '/home/paperspace/Hackathon/show-attend-and-tell'
add_path(vgg_preprocess_path)
