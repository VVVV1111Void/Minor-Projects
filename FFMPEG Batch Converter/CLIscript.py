# The main script for the file
import innerlib
SUPPORTED = [
    'mp3', 'mp4', 'opus', 'ogg', 'webm'
]


def ask():
    try:
        print('\n Type or paste in the folder you are trying to convert.')
        target_dir = str(input("\n Enter the path of your file: "))

        if innerlib.verify_dir(target_dir):  # Just to be sure
            ext = str( # Source type
                input("\n Enter source file extension, eg. 'mp3'(no .): "))
            tar = str( # Target type
                input("\n Enter target file extension, eg. 'mp3'(no .): "))
            if innerlib.verify_ext(ext, SUPPORTED):
                if innerlib.verify_ext(tar, SUPPORTED):
                    innerlib.convert_dir(target_dir, tar, ext)
                    print('\n Conversion success!')
                    return 0
                else:
                    raise Exception(
                        '\n Unable to verify extensions.')
            else:
                raise Exception(
                    '\n Unable to verify extensions.')
        else:
            raise Exception('\n Unable to find directory')

    except Exception as e:
        print(e)
        print('\n Would you like to try again? (Y or N)')
        user_input = str(input("")).lower()
        if user_input[0] == 'y':
            ask()
        else:
            return 1


if __name__ == "__main__":
    print('\n Hello!')
    print('Press Ctrl C to cancel anytime!')
    ask()
