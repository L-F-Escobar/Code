ALL: Assign5.EXE 

CLEAN: 
 -@erase Assign5.EXE 
 -@erase Assign5.ILK 
 -@erase Assign5.PDB 
 -@erase Assign5.OBJ 
 -@erase Assign5.LST 

Assign5.ASM: 

Assign5.OBJ: Assign5.ASM 
 ml /c /coff /Zi Assign5.ASM 

Assign5.EXE: Assign5.OBJ 
 link /debug /subsystem:console /out:Assign5.EXE /entry:start Assign5.OBJ KERNEL32.LIB IO.OBJ

