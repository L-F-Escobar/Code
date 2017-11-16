ALL: Assign3.EXE 

CLEAN: 
 -@erase Assign3.EXE 
 -@erase Assign3.ILK 
 -@erase Assign3.PDB 
 -@erase Assign3.OBJ 
 -@erase Assign3.LST 

Assign3.ASM: 

Assign3.OBJ: Assign3.ASM 
 ml /c /coff /Zi Assign3.ASM 

Assign3.EXE: Assign3.OBJ 
 link /debug /subsystem:console /out:Assign3.EXE /entry:start Assign3.OBJ KERNEL32.LIB IO.OBJ