from model import main
import os
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
os.environ['SDL_VIDEO_CENTERED'] = '1'



if __name__ == "__main__":
    main()