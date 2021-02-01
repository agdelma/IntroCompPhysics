''' Make a zipped directory for Physics 256 Assignments.
'''

import os, shutil


def main():

    assign_num = 2
    solution_path = 'files'
    name = 'DelMaestro_A'

    # get the list of all files
    assign_files  = [f for f in os.listdir(solution_path) if os.path.isfile(os.path.join(solution_path,f)) ]

    # test if the assignment directory exists, if not, make it
    assign_dir = name + os.path.sep + 'A%02d' % assign_num
    if not os.path.exists(assign_dir):
        os.makedirs(assign_dir)

    # copy them to the assignment directory
    for afile in assign_files:
        source = solution_path + os.path.sep + afile
        dest = assign_dir + os.path.sep + afile
        shutil.copy(source,dest)

    # make the archive
    shutil.make_archive(name + '_A%02d' % assign_num, 'zip', '.', name)

if __name__ == '__main__':
    main()
