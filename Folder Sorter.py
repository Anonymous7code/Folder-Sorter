import os
import sys
import shutil

def sort_dir(dir, func=shutil.copy):

    #to check if the directory exists
    if not os.path.isdir(dir):
        return 1
    # root --> current directory
    # dirs --> sub directory in root dir.
    # files --> files in root
    for root, dirs, files in os.walk(dir):
        for file in files:
            #to get name and extension while looping thorough files
            name, extn = os.path.splitext(file)
            extn = extn[1:]
            # to check if the output dir exists if not then create one
            if not os.path.exists(os.path.join('out', extn)):
                os.makedirs(os.path.join('out', extn))

            # to check for duplicate file in output folder
            if os.path.exists(os.path.join("out",extn,file)):
                count =1
                for newFile in os.listdir(os.path.join('out',extn,'')):
                    if name == '_'.join(newFile.split('.')[0].split('_')[:-1]):
                        count +=1

                outFile = name + '_' +str(count) + "." + extn

            else:
                outFile = file

            print('File : ',os.path.join(root,file),'-->', os.path.join('out',extn,outFile))

            func(os.path.join(root,file),os.path.join('out',extn, outFile))

    return 0

def main():

    funDict = {
        'm' :shutil.move,
        'c' : shutil.copy,
    }

    flag = shutil.copy
    if len(sys.argv) == 3
        if sys.argv[2].lower()[0] in funDict:
            flag = funDict[sys.argv[2].lower()[0]]

        else:
            print('Unsupported 3rd argument .Use \'m\'ove or \'c\'opy')
            return 1

    elif len(sys.argv) == 1 or len(sys.argv) > 3:
        print('Wrong amount of arguments. only 2 supported : [path function]')
        return 1

    return sort_dir(sys.argv[1],flag)


if __name__ == '__main__':
    main()

