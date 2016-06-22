'''
Created on 2016-6-14

@author: LiuHao
'''
import os
import sys  

def Main(argv):
    ignoreFolders = ["*.svn", ".git", ".metadata", ".settings", 
                     ".svn", "Debug", "__pycache__", "build"];
    ignoreFiles = ["*.a", "*.al", "*.aps", "*.bz2", "*.git", "*.gz", "*.ilk", "*.la", "*.ldb",
                   "*.lo", "*.o", "*.obj", "*.opensdf", "*.pdb", "*.pyc", "*.pyo", "*.rej", "*.res", "*.sdf", 
                   "*.so.[0-9]*", "*.suo", "*.svn", "*.tlog", "*.user", "*.vcxproj.user", "*.zip", 
                   ".DS_Store", ".libs", ".project", ".pydevproject", "desktop.ini", "~*.doc", "~*.docx"];

    ignoreFolders.sort();  
    ignoreFiles.sort();      
    
    print("Folders (for Beyond Compare):");
    for i in ignoreFolders:
        print(i);
    
    print();
    print("Files (for Beyond Compare)  :");
    for i in ignoreFiles:
        print(i);

    print();
    print("Folders + Files (for Svn): ");
    
    for i in ignoreFolders + ignoreFiles:
        print(i, end=" ");
    
if __name__ == '__main__':
    sys.exit(Main(sys.argv));