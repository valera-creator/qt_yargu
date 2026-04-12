from PySide6.QtCore import QFile, QIODevice, QTextStream, QFileInfo

file = QFile("in.txt")
if not file.open(QIODevice.ReadOnly | QIODevice.Text):
    exit()
input_file = QTextStream(file)
while not input_file.atEnd():
    line = input_file.readLine()
    print(line)

info1 = QFileInfo("in.txt")
print(info1.isSymLink())
print(info1.absoluteFilePath())
print(info1.size())
