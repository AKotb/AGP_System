# Pythono3 code to rename multiple
# files in a directory or folder

# importing os module
import os


# Function to rename multiple files
def main():
    for filename in enumerate(os.listdir("D:/NARSS/Contractual Project/Data_05-07-2020/Phase 20200622/Output/surveyjpg")):
        old_name = 'D:/NARSS/Contractual Project/Data_05-07-2020/Phase 20200622/Output/surveyjpg/' + filename[1]

        new_name = old_name.replace('admin_','')
        print new_name

        # rename() function will
        # rename all the files
        os.rename(old_name, new_name)

    # Driver Code


if __name__ == '__main__':
    # Calling main() function
    main()