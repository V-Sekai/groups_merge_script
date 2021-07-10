import os

os.system("git stash")
print("Checkout remotes")

os.system("git remote rm reduz")
os.system("git remote add reduz https://github.com/reduz/godot")
os.system("git fetch reduz")
#
os.system("git remote rm GiantBlargg")
os.system("git remote add GiantBlargg https://github.com/GiantBlargg/godot")
os.system("git fetch GiantBlargg")
#
os.system("git remote rm SaracenOne")
os.system("git remote add SaracenOne https://github.com/SaracenOne/godot")
os.system("git fetch SaracenOne")
#
os.system("git remote rm lyuma")
os.system("git remote add lyuma https://github.com/lyuma/godot")
os.system("git fetch lyuma")
#
os.system("git remote rm godot-fire")
os.system("git remote add godot-fire https://github.com/godot-extended-libraries/godot-fire")
os.system("git fetch godot-fire")
#
os.system("git remote rm fire")
os.system("git remote add fire https://github.com/fire/godot")
os.system("git fetch firee")
#
os.system("git remote rm v-sekai-godot")
os.system("git remote add v-sekai-godot git@github.com:V-Sekai/godot.git")
os.system("git fetch v-sekai-godot")
#
os.system("git remote rm TwistedTwigleg")
os.system("git remote add TwistedTwigleg https://github.com/TwistedTwigleg/godot.git")
os.system("git fetch TwistedTwigleg")
#
os.system("git remote rm JFonS")
os.system("git remote add JFonS https://github.com/JFonS/godot.git")
os.system("git fetch JFonS")
#
os.system("git remote rm Xrayez")
os.system("git remote add Xrayez https://github.com/Xrayez/godot.git")
os.system("git fetch Xrayez")
#
os.system("git remote rm YeldhamDev")
os.system("git remote add YeldhamDev https://github.com/YeldhamDev/godot.git")
os.system("git fetch YeldhamDev")
#
os.system("git remote rm BastiaanOlij")
os.system("git remote add BastiaanOlij https://github.com/BastiaanOlij/godot.git")
os.system("git fetch BastiaanOlij")
#
os.system("git remote rm floppyhammer")
os.system("git remote add floppyhammer https://github.com/floppyhammer/godot.git")
os.system("git fetch floppyhammer")
#
os.system("git remote rm bruvzg")
os.system("git remote add bruvzg https://github.com/bruvzg/godot.git")
os.system("git fetch bruvzg")
#
os.system("git remote rm tokage")
os.system("git remote add tokage https://github.com/TokageItLab/godot.git")
os.system("git fetch tokage")

os.system("git remote rm godotengine")
os.system("git remote add godotengine https://github.com/godotengine/godot")
os.system("git remote set-url --push godotengine https://example.com/")
os.system("git fetch godotengine")

print("Work")
os.system("git stash")
ORIGINAL_BRANCH="merge-script-4.x"
MERGE_REMOTE="v-sekai-godot"
MERGE_BRANCH="groups-4.x"
os.system(f"git checkout {ORIGINAL_BRANCH} --force")
os.system(f"git branch -D {MERGE_BRANCH}")
os.system(f"python3 ./thirdparty/git-assembler -av --recreate")
os.system(f"git checkout {MERGE_BRANCH} -f")
import datetime
d = datetime.now()
MERGE_DATE=str(d).replace('+00:00', 'Z')
MERGE_TAG=f"groups-4.x.{MERGE_DATE}"
os.system(f"git tag -a {MERGE_TAG} -m \"Commited at {MERGE_DATE}.\"")
os.system(f"git push {MERGE_REMOTE} {MERGE_TAG}")
os.system(f"git push {MERGE_REMOTE} {MERGE_BRANCH} -f")
os.system(f"git checkout {ORIGINAL_BRANCH} --force")
os.system(f"git branch -D {MERGE_BRANCH}")